"""Join redundant solid-wall segments and compact classic map records."""
import math
import struct
from collections import defaultdict, deque


def optimize(lumps, texture_widths):
    raw = dict(lumps)
    vertices = list(struct.iter_unpack('<2h', raw['VERTEXES']))
    sides = list(struct.iter_unpack('<hh8s8s8sH', raw['SIDEDEFS']))
    lines = [list(v) for v in struct.iter_unpack('<7H', raw['LINEDEFS'])]
    original = len(lines)
    links = defaultdict(set)
    for i, line in enumerate(lines):
        links[line[0]].add(i)
        links[line[1]].add(i)

    def aligned(first, second, advance):
        if first == 65535 or second == 65535:
            return first == second
        a, b = sides[first], sides[second]
        # Preserve sector membership, vertical alignment and every texture.
        if a[1:] != b[1:]:
            return False
        for texture in a[2:5]:
            texture = texture.rstrip(b'\0').decode('ascii')
            if texture == '-':
                continue
            width = texture_widths.get(texture)
            if width is None or (a[0] + advance - b[0]) % width:
                return False
        return True

    queue = deque(links)
    merged = 0
    while queue:
        v = queue.popleft()
        if len(links[v]) != 2:
            continue
        i, j = sorted(links[v])
        a, b = lines[i], lines[j]
        if a[0] == v and b[1] == v:
            i, j, a, b = j, i, b, a
        if a[1] != v or b[0] != v:
            continue
        # Every action/tag, junction and two-sided lighting boundary stays
        # intact. Only solid axis-aligned walls are joined without UV rounding.
        if a[2:5] != b[2:5] or a[3] or a[4] or a[6] != 65535 or b[6] != 65535:
            continue
        p, q, r = vertices[a[0]], vertices[v], vertices[b[1]]
        horizontal = p[1] == q[1] == r[1] and (q[0]-p[0])*(r[0]-q[0]) > 0
        vertical = p[0] == q[0] == r[0] and (q[1]-p[1])*(r[1]-q[1]) > 0
        if not (horizontal or vertical):
            continue
        na = round(math.dist(p, q))
        if not aligned(a[5], b[5], na):
            continue
        end = b[1]
        a[1], a[6] = end, b[6]
        lines[j] = None
        links[v].clear()
        links[end].remove(j)
        links[end].add(i)
        queue.extend((a[0], end))
        merged += 1

    remap = {}
    kept = []
    for i, line in enumerate(lines):
        if line is not None:
            remap[i] = len(kept)
            kept.append(line)
    used_vertices = sorted({v for line in kept for v in line[:2]})
    used_sides = sorted({s for line in kept for s in line[5:] if s != 65535})
    vm = {old: new for new, old in enumerate(used_vertices)}
    sm = {old: new for new, old in enumerate(used_sides)}
    for line in kept:
        line[:2] = [vm[v] for v in line[:2]]
        line[5:] = [sm[s] if s != 65535 else s for s in line[5:]]
    raw['VERTEXES'] = b''.join(struct.pack('<2h', *vertices[v]) for v in used_vertices)
    raw['SIDEDEFS'] = b''.join(struct.pack('<hh8s8s8sH', *sides[s]) for s in used_sides)
    raw['LINEDEFS'] = b''.join(struct.pack('<7H', *line) for line in kept)
    # ZDBSP regenerates these from the simplified, authoritative map geometry.
    for key in ('SEGS', 'SSECTORS', 'NODES', 'BLOCKMAP'):
        raw[key] = b''
    return list(raw.items()), remap, dict(
        linedefs_before=original, linedefs_after=len(kept), merged_collinear=merged,
        unused_vertices_removed=len(vertices)-len(used_vertices),
        unused_sidedefs_removed=len(sides)-len(used_sides))

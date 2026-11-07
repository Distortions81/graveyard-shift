"""Authored classic-sector light pools and cast-shadow wedges for Map 1.

Brushes split only flat outdoor floor polygons. They never add overlaid walls,
change walk heights, alter actor behavior, or change tags/actions. Indoor fixtures use the
existing ceiling sectors. Coordinates are in the map's 64-unit design grid.
"""
from dataclasses import replace
import math
from fractions import Fraction


def _area(poly):
    return sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(poly,poly[1:]+poly[:1]))


def _clip(poly,a,b,inside):
    # Exact intersections keep neighboring lighting pieces on shared edges.
    if not poly:return []
    def distance(p):return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
    result=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        dp,dq=distance(p),distance(q)
        pin=dp<=0 if inside else dp>=0
        qin=dq<=0 if inside else dq>=0
        if pin:result.append(p)
        if pin!=qin:
            t=dp/(dp-dq)
            result.append(tuple(p[i]+t*(q[i]-p[i]) for i in [0,1]))
    clean=[]
    for point in result:
        if not clean or point!=clean[-1]:clean.append(point)
    if len(clean)>1 and clean[0]==clean[-1]:clean.pop()
    return clean if len(clean)>=3 and abs(_area(clean))>1e-7 else []


def _partition(poly,brush):
    """Disjoint convex remainder pieces plus the convex intersection."""
    remaining=poly;outside=[]
    for a,b in zip(brush,brush[1:]+brush[:1]):
        piece=_clip(remaining,a,b,False)
        if piece:outside.append(piece)
        remaining=_clip(remaining,a,b,True)
        if not remaining:break
    return outside,remaining


def apply_map1(l):
    # Stock decorations sit between the kiosks and facade, leaving the
    # established outer walking lanes clear. No wall-texture fixtures.
    sources=[(-.5,7,35),(-.5,18.5,35),(15.5,8.5,35),(16.5,19.5,35),
             (-16.5,20.5,2028),(-9,30.5,2028)]
    for x,y,kind in sources:l.thing(x,y,kind)
    brushes=[]
    def brush(points,light,shadow=False):
        p=[tuple(Fraction(v) for v in point) for point in points]
        if _area(p)>0:p.reverse()
        brushes.append((p,light,shadow,(min(x for x,y in p),min(y for x,y in p),max(x for x,y in p),max(y for x,y in p))))
    def hull(points):
        def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
        points=sorted(set(points));lower=[];upper=[]
        for p in points:
            while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
            lower.append(p)
        for p in reversed(points):
            while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
            upper.append(p)
        return lower[:-1]+upper[:-1]
    # Moonlight comes from the northeast. All architectural shadows trail
    # southwest; the little decorative lamps light back into those shadows.
    for x,y,w,h in [(0,5,2,2),(13,5,2,2),(0,16,2,2),(14,16,2,2),(-14,23,3,3)]:
        footprint=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
        for dx,dy,light in [(-3.5,-2,144),(-3,-2,128)]:
            brush(hull(footprint+[(a+dx,b+dy) for a,b in footprint]),light,True)
    brush([(4,21),(14,21),(11,19),(1,19)],144,True)
    for x,y,kind in sources:
        for radius,light in [(1.25,192 if kind==35 else 208),(.625,224)]:
            points=[(round((x+radius*math.cos(-i*math.pi/4))*8)/8,
                     round((y+radius*math.sin(-i*math.pi/4))*8)/8) for i in range(8)]
            brush(points,light)
    touched=_paint(l,brushes)
    l.lighting_summary=dict(sprite_lights=6,light_brushes=len(brushes),floor_cells_split=touched,
                            moonlight_direction='northeast to southwest',
                            method='classic sector lighting; small sprite-light pools and architectural moon shadows')


def _paint(l,brushes,covered=False):
    touched=0
    for (x,y),style in list(l.cells.items()):
        if (x,y) in l.carved or style.floor!=0 or (not covered and style.roof!='F_SKY1') or style.door or style.tag or style.special:continue
        pieces=[([tuple(Fraction(v) for v in p) for p in [(x,y),(x,y+1),(x+1,y+1),(x+1,y)]],style.light)]
        for polygon,light,shadow,box in brushes:
            if shadow and style.roof!='F_SKY1':continue
            if box[2]<=x or box[0]>=x+1 or box[3]<=y or box[1]>=y+1:continue
            next_pieces=[]
            for piece,old in pieces:
                outside,inside=_partition(piece,polygon)
                next_pieces.extend((p,old) for p in outside)
                if inside:next_pieces.append((inside,min(old,light) if shadow else max(old,light)))
            pieces=next_pieces
        if all(light==style.light for poly,light in pieces):continue
        l.carved.add((x,y));touched+=1
        l.extra_polygons.extend(([tuple(float(v) for v in p) for p in poly],replace(style,light=light)) for poly,light in pieces)
    return touched


def apply_map2(l):
    # Small stock sprite lights, placed away from the established route and
    # shooting lanes. Covered rooms receive local light, never moon shadows.
    sources=[(1,8.5,35),(18.5,8,35),(1,22.5,35),(18.5,22.5,35),
             (-15,31.5,2028),(-1,32.5,2028),
             (21.75,3.5,2028),(44.25,3.5,2028),(34.5,20,2028),
             (-15,9,35),(-14.5,22.5,35),(9,34.5,35),(28.25,37.5,35)]
    for x,y,kind in sources:l.thing(x,y,kind)
    brushes=[]
    def brush(points,light,shadow=False):
        p=[tuple(Fraction(v) for v in point) for point in points]
        if _area(p)>0:p.reverse()
        brushes.append((p,light,shadow,(min(x for x,y in p),min(y for x,y in p),max(x for x,y in p),max(y for x,y in p))))
    def hull(points):
        def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
        points=sorted(set(points));lower=[];upper=[]
        for p in points:
            while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
            lower.append(p)
        for p in reversed(points):
            while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
            upper.append(p)
        return lower[:-1]+upper[:-1]
    for x,y,w,h in [(1,5,4,2),(14,5,4,2),(1,18,4,2),(14,18,4,2),
                     (8,11,4,6),(-15,29,2,2),(-5,27,2,2)]:
        footprint=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
        for dx,dy,light in [(-3.5,-2,144),(-3,-2,128)]:
            brush(hull(footprint+[(a+dx,b+dy) for a,b in footprint]),light,True)
    brush([(8,28),(20,28),(17,26),(5,26)],144,True)
    for x,y,kind in sources:
        sector=l.cells[math.floor(x),math.floor(y)]
        covered=sector.roof!='F_SKY1'
        for radius,light in [(1 if covered else 1.25,192 if kind==35 else 208),(.5 if covered else .625,224)]:
            points=[(round((x+radius*math.cos(-i*math.pi/4))*8)/8,
                     round((y+radius*math.sin(-i*math.pi/4))*8)/8) for i in range(8)]
            brush(points,light)
    touched=_paint(l,brushes,covered=True)
    l.lighting_summary=dict(sprite_lights=len(sources),light_brushes=len(brushes),floor_cells_split=touched,
                            moonlight_direction='northeast to southwest',
                            method='classic sector lighting; small sprite-light pools, ceiling fixtures and outdoor moon shadows')

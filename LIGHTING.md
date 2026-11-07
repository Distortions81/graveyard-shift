# Lighting and framed surfaces

Map 1 uses four stock DOOM candelabra sprites and two tech-lamp sprites. Their
small octagonal floor pools use classic sector lighting, with a brighter core
close to each prop. The sprites come from the player's shareware IWAD; no base-game
sprite graphics are copied into this mapset.

The broad shadows come from moonlight arriving from the northeast, with the
booths and generator casting southwest-facing shadows. Dark cores and softer
outer strips separate these from the little local lights. The balcony has a
wider moon-shadow band. Local sprite lights illuminate back into those shadows.

Light polygons keep the existing floor heights and textures. Exact rational
intersections avoid cracks between lighting sectors. There are no wall-lantern
or floodlight graphics, raised light patches or inset wall overlays. Standing
props are placed off the main route, checked using ordinary collision and pickups.
The indoor ceiling fixtures remain separate from the high outdoor skies.

## Reference study

I inspected the actual sector and linedef data in the shareware **E1M1: Hangar**
and Espi's **Suspended in Dusk, MAP01**, plus John Bishop's
[DOOM editing guide](https://jbsharx.uk/doom2/dmstrtd.html).
[Espi's original package is on the idgames mirror](https://dukeworld.com/idgames/levels/doom2/s-u/sid.zip).

In Suspended in Dusk MAP01, 132 two-sided linedefs separate sectors with the
same floor/ceiling heights and flats but different lighting; 99 of those
boundaries differ by 16 light units. Hangar has 12 such lighting-only boundaries,
with stronger contrasts around its brighter areas. These observations informed
the use of modest local pools and architectural shadows from one broad light direction.
The reference WADs stay outside this repository; its geometry and art are original.

## Texture-aware architecture

Framed textures need deliberate edges. Map 1's outdoor wall height is 384 units
(three 128-unit repeats); the staff corridor is 128 units high. The control
booth's floor and ceiling are 128 and 256, giving its framed panels a complete
128-unit bay. Its final rise is another ordinary 16-unit step. The balcony follows
that floor level. Existing wall textures use offsets and pegging appropriate to
the local bay; the signs stay on their original wall planes.

This is a constraint for visible frames, sign panels and decorative trim, not a
requirement to size every surface to a full texture. Seamless wood, brick, paving,
and small bespoke props can use other dimensions where those cuts read naturally.

## Checks

The rebuilt map passes GD-DOOM route tests on skills 1, 3 and 4, secret-door,
texture-alignment, animation and sky checks. Fixed-camera checks include the
plaza, service yard, control booth, balcony and carousel in Chocolate Doom.
The original recorded demos remain paired with their historical WAD versions.

# E1M2 — Midway Massacre

A larger second shift through the midway: rigged games, a shooting gallery,
bumper cars and prize redemption. Built with the same classic DOOM formats as
Map 1. The same lyric-led metal park theme currently plays on both maps.

## Scale and pacing

| Measure | Map 1 | Map 2 |
| --- | ---: | ---: |
| Reachable 64-unit grid cells, doors open | 1,219 | 1,842 |
| Relative floor area | 100% | 151.1% |
| HMP enemies | 36 | 54 |
| Easy / UV enemies | 20 / 52 | 34 / 60 |
| Secrets | 3 | 3 |

This measures the reachable design-grid footprint with doors open and normal
step/headroom limits. Curved props use an approximate grid classification; it
is not an exact polygon-area survey. The first-visit target remains 6–9 minutes,
subject to human playtesting. Numeric-assisted recordings are not human timing estimates.

## Route

1. Collect the visible shotgun, armor and shells on the promenade.
2. Open a gallery entrance; shooting the bullseye opens an optional prize cache.
3. Cross the operator court, collect the blue skill token and recovery kit, and return to the midway.
4. Open blue admission, collect the chaingun, and cross the Collision Department using cars as cover.
5. Climb the ordinary 16-unit steps to the red token on the control deck.
6. Enter prize redemption through either red gate. Clear the counters and exit
   toward the future ghost-train map. The front gate also opens a return loop.

The finale is a larger room with flanking aisles, counters and displays rather
than a large closet ambush. The arena entrance offers a chaingun, with a bullet box farther along the west
aisle. Optional secrets offer a backpack, armor and supplies.

## Detail and lessons from Map 1

- Outdoor skies use a consistent 384-unit plane. The shooting gallery uses a
  complete 128-unit wall height, and the arena uses a complete 256-unit height.
  Low ceilings belong to covered rooms.
- Signs use existing wall faces and normal texture offsets; no inset sign overlays.
- Framed panels, siding and door lettering align across wall segments. Prize booths
  use full 128-unit modules and complete PRIZES labels, with skull dolls in the windows.
  The shorter redemption counters use plain wood rather than cropped booth artwork.
- Eight candelabra and five tech-lamp sprites produce small local pools of light.
  Booths, the quota monument and service crates cast consistent southwest-facing
  moon shadows outdoors. Covered rooms get local fixtures and pools without moon shadows.
- The raised display no longer obscures the Next Shift sign. Redemption text is
  split into three readable lines. The builder carries authored offsets onto wall
  pieces introduced by lighting subdivisions, preserving complete sign lettering.
- Rounded cars have rubber rings, colored bodies and seat backs. Broad lanes
  leave maneuvering room; floor lamps do not block circulation.
- Gallery ducks, electrical ceiling grids, quota notices and prize-policy signs
  establish a separate attraction identity. Ghost trains, funhouses, roller
  coasters and the Ferris wheel remain reserved for Maps 3–4.
- An early combat attempt revealed gallery/service enemies joining the opener.
  Doors now isolate these encounters until the player opens their entrances.

## Validation

GD-DOOM progression tests walk the actual route on skills 1, 3 and 4 with collision,
steps, pickups, use traces and no monsters. Both gates reject the player without
the correct token, and the final switch activates. The WAD audit reports no
unknown actions or invalid thing flags. Five fixed-camera render checks also
pass in Chocolate Doom. The latest pass also refines Map 1’s opening encounter and security supplies.

`playtests/map02/attempt-02-midway` records a completed HMP run of the earlier layout: **54/54 kills,
3/3 secrets**, 88 health and 184 armor. It includes a return through both token
loops and a cleared-map bumper-car tour. All enemies were defeated at 3:15.49;
the run exits at 4:26.89 including exploration, stalled waypoints and the tour.
Normal GD-DOOM demo playback reproduces its final state exactly. The complete
rendered demo also passed in Chocolate Doom, independently reporting 54/54 kills
and 3/3 secrets. Verification results are retained beside the recording.

The current polish pass is separately verified by route/lock checks on all three
skills and fresh renderer checks. The earlier demo keeps its matching pinned WAD;
its 54/54 result does not substitute for human combat testing of the latest revision.
Sign-audit previews 08–12 and lighting previews 13–14 show the updated artwork;
monsters are hidden in these inspection captures so they do not obscure the text.

The failed first attempt, before the encounter-door revision, is preserved in
`playtests/map02-early-layout/` with its matching earlier WAD. Do not substitute
the current WAD when replaying that attempt.

## Second refinement pass

Two gallery hitscanners now guard redemption; a gallery-entry medikit and an
operator-court kit provide recovery before the arena. The main-route chaingun
and bullet box add a weapon choice without requiring secrets. The gallery
secret now rewards a backpack. Enemy totals and all key locks stay the same.

Four ceiling lamps punctuate the arena’s dark electrical grid. Car bodies use
more restrained sector lighting. The prize hall has timber side aisles and a
patterned carpet runner, plus counter fixtures. Its dedicated exit poster points
toward the ghost train. See [current recorded checks](playtests/refinement-pass/README.md).

## Play

```bash
GD_DOOM_BIN=/path/to/gddoom ./play.sh --iwad /path/to/DOOM1.WAD -map E1M2 -skill=3
./playtests/watch.sh attempt-02-midway --iwad /path/to/DOOM1.WAD
```

Map 1 also leads into Map 2 through its normal exit. The current Map 2 exit
continues into the IWAD’s E1M3 until the third map is built.

# Both-map refinement pass

These HMP pistol-start recordings use the WAD pinned in this directory, matching
`wad-sha256.txt`. Numeric controls issue ordinary movement, turning, weapon,
attack and use commands; there are no injected keys, health changes or teleports.
Turning uses mouse-like acceleration, and the routes include running.

| Recording | Result | Secrets | Health / armor | Demo duration |
| --- | --- | --- | --- | --- |
| `refined-map01` | Exit reached, 36/36 kills | 3/3 | 100 / 184 | 2:42.80 |
| `refined-map02` | Exit reached, 54/54 kills | 0/3 | 83 / 29 | 2:56.11 |

Map 2 deliberately skips secret rewards to check the main-route supply budget.
Its player takes the chaingun and bullet box in the arena, switches back to the
shotgun late in the finale, then inspects the cleared prize hall before exiting.
Map 1 includes the secret route and a cleared carousel inspection. These are
assisted runs, not estimates of a new human player's completion time. Some
waypoints stall against cover; the later commands navigate around it.

## Changes informed by the attempts

The old Map 1 approach died in the security room after yard enemies joined the
opening. Yard guards now wait for sight of the player, and the pinky and shotgun
guard use the generator as cover. A medikit replaces the office stimpack.
The exterior security sign identifies the shotgun room, and two ceiling lights
pick out the starter kit and staff route. Ticket kiosks use complete 128-unit faces.

Early Map 2 attempts took excessive damage in the gallery. Two hitscanners now
guard redemption instead, and recovery supplies sit at the gallery entrance and
blue-token court. A main-route chaingun and bullet box give the bumper arena a
weapon change; the gallery secret instead provides a backpack. The return-lane
medikit gives a recovery opportunity before redemption. Enemy totals remain
20/36/52 on Map 1 and 34/54/60 on Map 2 (Easy/HMP/UV).

The gallery and prize hall have stronger local lighting contrast. Four arena
ceiling lamps sit within a dark electrical grid, and the car bodies have more
restrained brightness. A patterned carpet runner separates redemption's center
from the wooden side aisles. The dedicated exit sign points to the ghost train.

## Verification

- Ordinary collision, stairs, pickups, key rejection and exit activation pass
  on skills 1, 3 and 4 in both maps; Map 1's secret, animation, alignment and sky
  checks also pass. See `route-checks.txt`.
- The saved demos reproduce their recorded final state through GD-DOOM's normal
  demo player. See `replay-verification.txt`.
- Eleven fixed-camera checks pass in Chocolate Doom, including the balcony and
  arena views that exposed excess visible planes in the first lighting draft.
  See `classic-cameras-map01.txt` and `classic-cameras-map02.txt`.
- `classic-demo-map01.txt` and `classic-demo-map02.txt` retain the full rendered
  Chocolate Doom timedemo results. The private combined IWAD used by this check
  is outside the repository.

Every command and state checkpoint is retained. Named checkpoints and the final
state also retain renderer PNGs; `screenshot` values are relative to the attempt
folder. The older demos elsewhere keep their original matching WADs.

The final optimization uses single-level sprite pools and single moon-shadow
boundaries. The solid-wall cleanup preserves texture phase and leaves triggers
and floor-light boundaries intact. Against the previous committed revision,
Map 1 has 25.8% fewer linedefs and Map 2 has 23.3% fewer. The WAD is 21.1% smaller.

## Watch in modern mode

```bash
GD_DOOM_BIN=/path/to/gddoom ./playtests/watch.sh refined-map01 --iwad /path/to/DOOM1.WAD
GD_DOOM_BIN=/path/to/gddoom ./playtests/watch.sh refined-map02 --iwad /path/to/DOOM1.WAD
```

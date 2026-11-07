# Map 2 combat playtest

`attempt-02-midway/session.lmp` completes E1M2 on Hurt Me Plenty: 54/54 kills,
3/3 secrets, 4:26.89 including a cleared-map tour. Final health 88, armor 184.
All enemies were dead at tic 6842 (3:15.49). Numeric aiming and waypoint assistance
produce standard v1.9 demo inputs; no cheats, actor removal or inventory injection.

From the mapset root:

```bash
./playtests/watch.sh attempt-02-midway --iwad /path/to/DOOM1.WAD
```

Use the pinned `graveyard-shift-playtest.wad`, not another revision. Normal demo
playback was independently checked against the recorder’s final position,
inventory and exit status. Chocolate Doom also rendered the complete demo and
reported 54/54 kills and 3/3 secrets; results are in `verification/`. Checkpoints 101–102 show the cleared bumper arena.
The earlier failed layout is preserved separately under `../map02-early-layout/`.


This recording predates the sprite-light, moon-shadow, framed-panel and sign polish
pass. Its pinned WAD preserves that earlier layout. Current preview images and the
main WAD show the updated map; do not substitute that WAD when replaying the demo.

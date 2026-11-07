#!/usr/bin/env bash
set -euo pipefail
mapset_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
iwad="${IWAD:-$mapset_dir/DOOM1.WAD}"
if [[ "${1:-}" == --iwad ]]; then
  [[ $# -ge 2 ]] || { echo 'Usage: play.sh --iwad /path/to/DOOM1.WAD [GD-DOOM options]' >&2; exit 2; }
  iwad="$2"
  shift 2
fi
[[ -f "$iwad" ]] || { echo 'Supply your own IWAD with --iwad /path/to/DOOM1.WAD or IWAD=/path/to/DOOM1.WAD.' >&2; exit 2; }
exec "${GD_DOOM_BIN:-gddoom}" -wad "$iwad" -file "$mapset_dir/graveyard-shift.wad" \
  -map E1M1 -render=true -sourceport-mode=true "$@"

#!/usr/bin/env bash
set -euo pipefail
playtest_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
attempt_name=attempt-07-detailed
if [[ $# -gt 0 && "$1" != -* ]]; then attempt_name="$1"; shift; fi
recording_dir="$playtest_dir"
case "$attempt_name" in
  attempt-07-detailed) recording_dir="$playtest_dir/detailed-showcase" ;;
  refined-map01|refined-map02) recording_dir="$playtest_dir/refinement-pass" ;;
  attempt-02-midway) recording_dir="$playtest_dir/map02" ;;
  attempt-03-classic|attempt-04-classic-clear) ;;
  *) echo 'Choose refined-map01, refined-map02, attempt-02-midway, attempt-07-detailed, attempt-03-classic or attempt-04-classic-clear.' >&2; exit 2 ;;
esac
iwad="${IWAD:-$playtest_dir/../DOOM1.WAD}"
if [[ "${1:-}" == --iwad ]]; then
  [[ $# -ge 2 ]] || { echo 'Usage: watch.sh [attempt] --iwad /path/to/DOOM1.WAD [GD-DOOM options]' >&2; exit 2; }
  iwad="$2"; shift 2
fi
[[ -f "$iwad" ]] || { echo 'Supply your own IWAD with --iwad /path/to/DOOM1.WAD or IWAD=/path/to/DOOM1.WAD.' >&2; exit 2; }
exec "${GD_DOOM_BIN:-gddoom}" -config= -wad "$iwad" \
  -file "$recording_dir/graveyard-shift-playtest.wad" \
  -demo "$recording_dir/$attempt_name/session.lmp" -render=true -sourceport-mode=true \
  -width=1920 -height=1080 -detail-level=0 "$@"

#!/usr/bin/env bash
set -u
ROOT=$PWD
EVIDENCE=/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/approved-core-checks
export TMPDIR="$ROOT/.validation-core/tmp"
export FM_HERDR_LAB_STATE_DIR="$ROOT/.validation-core/herdr-state"
# Select the explicitly approved executable for this process only.
export PATH="/usr/local/bin:$PATH"
[ "$(type -P herdr)" = /usr/local/bin/herdr ] || exit 2
/usr/local/bin/herdr --version
LAB=$(bash bin/fm-herdr-lab.sh name start-repair)
printf '%s\n' "$LAB" > "$ROOT/.validation-core/lab-name"
printf 'fresh_lab=%s\n' "$LAB"
printf 'command: PATH=/usr/local/bin:<unchanged> TMPDIR=<worktree> FM_HERDR_LAB_STATE_DIR=<worktree> bash bin/fm-herdr-lab.sh prepare <fresh_lab>\n'
bash bin/fm-herdr-lab.sh prepare "$LAB"
rc=$?
printf 'prepare_exit_code=%s\n' "$rc"
if [ "$rc" -eq 0 ]; then
  cp "$FM_HERDR_LAB_STATE_DIR/$LAB.fleet-state.json" "$EVIDENCE/default-baseline-before.json"
  printf 'default_baseline=verified_by_guard\n'
else
  printf 'STOP: guard refusal; no provision, runtime relocation, fallback binary or control attempted\n'
fi
exit "$rc"

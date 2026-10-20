#!/usr/bin/env bash
set -eu
ROOT=$PWD
EVIDENCE=/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/setup-continuation
export PATH=/usr/local/bin:$PATH
[ "$(type -P herdr)" = /usr/local/bin/herdr ] || exit 1
export FM_HERDR_LAB_STATE_DIR="$ROOT/.validation-continuation/herdr-state"
export TMPDIR="$ROOT/.validation-continuation/tmp"
HELPER="$ROOT/bin/fm-herdr-lab.sh"
SESSION=$(bash "$HELPER" name start-repair-current)
printf '%s\n' "$SESSION" > "$EVIDENCE/session-name.txt"
LAB="$ROOT/.validation-continuation/lab-home"
bash "$ROOT/bin/fm-lab-home.sh" create "$LAB" > "$EVIDENCE/lab-home-create.log"
cleanup() {
  status=$?
  trap - EXIT
  if [ -f "$FM_HERDR_LAB_STATE_DIR/$SESSION.fleet-state.json" ]; then
    cp "$FM_HERDR_LAB_STATE_DIR/$SESSION.fleet-state.json" "$EVIDENCE/default-baseline-before.json"
    bash "$HELPER" teardown "$SESSION" > "$EVIDENCE/lab-cleanup.log" 2>&1 || status=1
  fi
  printf 'driver_exit=%s\n' "$status" >> "$EVIDENCE/lab-cleanup.log"
  exit "$status"
}
trap cleanup EXIT
printf 'selected executable: /usr/local/bin/herdr\n'
/usr/local/bin/herdr --version
printf 'fresh lab: %s\n' "$SESSION"
# Fresh provision performs preparation internally. Never pre-create a tripwire.
bash "$HELPER" provision "$SESSION"
printf 'provision succeeded\n'
bash "$HELPER" run "$SESSION" status --json > "$EVIDENCE/lab-status.json"
printf '%s\n' "$SESSION" > "$ROOT/.validation-continuation/ready"
while [ ! -e "$ROOT/.validation-continuation/finish" ]; do sleep 1; done

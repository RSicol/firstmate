#!/usr/bin/env bash
set -u
ROOT=$PWD
EVIDENCE=/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/approved-core-checks
export TMPDIR="$ROOT/.validation-core/tmp"
export FM_HERDR_LAB_STATE_DIR="$ROOT/.validation-core/herdr-state"
export PATH="/usr/local/bin:$PATH"
[ "$(type -P herdr)" = /usr/local/bin/herdr ] || exit 2
IFS= read -r LAB < "$ROOT/.validation-core/lab-name"
printf 'cleanup_command: bash bin/fm-herdr-lab.sh teardown %s\n' "$LAB"
bash bin/fm-herdr-lab.sh teardown "$LAB"
rc=$?
printf 'teardown_exit_code=%s\n' "$rc"
[ "$rc" -eq 0 ] || exit "$rc"
# Read only guard-required session metadata, never panes, chats or agents.
bash bin/fm-herdr-lab.sh run "$LAB" session list --json | jq -ec --arg name "$LAB" '
  if ([.sessions[]? | select(.name == $name)] | length) != 0 then error("owned lab remains") else
  [.sessions[]? | select(.default == true)]
  | if length == 1 and .[0].name == "default" and .[0].running == true
    then .[0] | {name, default, running, socket_path}
    else error("default tripwire is invalid") end
  end' > "$EVIDENCE/default-baseline-after.json"
rc=$?
printf 'cleanup_metadata_exit_code=%s\n' "$rc"
[ "$rc" -eq 0 ] || exit "$rc"
cmp -s "$EVIDENCE/default-baseline-before.json" "$EVIDENCE/default-baseline-after.json"
rc=$?
printf 'unchanged_default_compare_exit_code=%s\n' "$rc"
[ "$rc" -eq 0 ] || exit "$rc"
[ ! -e "$FM_HERDR_LAB_STATE_DIR/$LAB.fleet-state.json" ] || exit 1
printf 'owned_lab_absent=true; prepared_tripwire_removed=true; default_unchanged=true\n'

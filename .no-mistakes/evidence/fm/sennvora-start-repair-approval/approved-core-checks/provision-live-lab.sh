#!/usr/bin/env bash
set -u
ROOT=$PWD
export TMPDIR="$ROOT/.validation-core/tmp"
export FM_HERDR_LAB_STATE_DIR="$ROOT/.validation-core/herdr-state"
export PATH="/usr/local/bin:$PATH"
[ "$(type -P herdr)" = /usr/local/bin/herdr ] || exit 2
IFS= read -r LAB < "$ROOT/.validation-core/lab-name"
printf 'command: bash bin/fm-herdr-lab.sh provision %s\n' "$LAB"
bash bin/fm-herdr-lab.sh provision "$LAB"
rc=$?
printf 'provision_exit_code=%s\n' "$rc"
[ "$rc" -eq 0 ] || { printf 'STOP: guard/tool refusal; no alternate binary, runtime or control\n'; exit "$rc"; }
bash bin/fm-herdr-lab.sh run "$LAB" workspace list --json

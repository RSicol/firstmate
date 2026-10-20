#!/usr/bin/env bash
set -eu
ROOT=$PWD
D=$(mktemp -d "$ROOT/.validation/tmp/live-boundaries.XXXXXX")
trap 'rm -rf "$D"' EXIT
bin/fm-lab-home.sh create "$D/lab" >/dev/null
mkdir -p "$D/user" "$D/config/herdr" "$D/data" "$D/cache" "$D/runtime" "$D/tmp" "$D/lab-state"
chmod 700 "$D/runtime"
printf 'herdr\n' > "$D/lab/config/backend"
CLEAN=(env -i PATH="$PATH" HOME="$D/user" XDG_CONFIG_HOME="$D/config" XDG_DATA_HOME="$D/data" XDG_CACHE_HOME="$D/cache" XDG_STATE_HOME="$D/state" XDG_RUNTIME_DIR="$D/runtime" TMPDIR="$D/tmp" HERDR_CONFIG_PATH="$D/config/herdr/config.toml" FM_HERDR_LAB_STATE_DIR="$D/lab-state")
SESSION=$("${CLEAN[@]}" "$ROOT/bin/fm-herdr-lab.sh" name prestart-proof)
printf 'Isolated Herdr prepare (real herdr; no default session is created):\n'
set +e
"${CLEAN[@]}" "$ROOT/bin/fm-herdr-lab.sh" prepare "$SESSION"
rc=$?
set -e
printf 'prepare exit=%s\n' "$rc"
if [ "$rc" -eq 0 ]; then
  printf 'Preparation succeeded, but no server is provisioned without verified in-worktree runtime isolation.\n'
  "${CLEAN[@]}" "$ROOT/bin/fm-herdr-lab.sh" teardown "$SESSION"
fi
CONTROL=("${CLEAN[@]}" FM_HOME="$D/lab" NO_MISTAKES_GATE=1 "$ROOT/bin/fm-control.sh" synthetic-prestart cancel-prestart)
check_refusal() {
  local name=$1 expected=$2 out rc
  shift 2
  printf '\nScenario: %s\n' "$name"
  set +e
  out=$("${CONTROL[@]}" "$@" 2>&1)
  rc=$?
  set -e
  printf '%s\nexit=%s\n' "$out" "$rc"
  [ "$rc" -ne 0 ]
  case "$out" in *"$expected"*) ;; *) exit 1 ;; esac
  [ ! -e "$D/lab/state/synthetic-prestart.meta" ]
}
check_refusal 'Cancellation without an explicit pane is refused' 'cancel-prestart requires --pane'
check_refusal 'A malformed freshness proof is refused' '--if-match requires the exact fingerprint' --pane w1:p2 --if-match invalid-proof
check_refusal 'An unbound caller cannot inspect or cancel a prestart' 'could not prove an abandoned held prestart owned by this coordinator; no input sent' --pane w1:p2
printf '\nNo worker record created; disposable home removed on exit. No server, agent, or fetch was started.\n'

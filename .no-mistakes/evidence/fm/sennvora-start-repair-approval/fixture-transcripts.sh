#!/usr/bin/env bash
set -u
printf 'Synthetic authentication only; Treehouse, gh and terminal transports below are fixtures.\nNo live fetch, credential-store lookup, worker, or real cancellation is claimed.\n\n'
. tests/fm-spawn-github-prefetch.test.sh >/dev/null || exit 1
for DEST_SHELL in bash fish; do
  printf '\n=== %s: matching effective configuration roots ===\n' "$DEST_SHELL"
  make_case transcript-success
  CALLER_XDG=
  DEST_XDG="$HOME_DIR/user-home/.config"
  OUT=$(run_case); RC=$?
  printf '%s\nspawn exit=%s; destination exit=%s\n' "$OUT" "$RC" "$(< "$CASE_DIR/probe-status")"
  [ "$RC" = 0 ] || exit 1
  [ "$(< "$CASE_DIR/destination-cwd")" = "$WT_DIR" ] || exit 1
  printf 'Destination entered the task worktree in the original shell.\n'
  printf 'Git credential plumbing artifact: '; head -n 1 "$CASE_DIR/credential-ok"
  printf 'Selected helper invocation: '; head -n 1 "$CASE_DIR/helper-calls"

  printf '\n=== %s: HOME fallback store mismatch ===\n' "$DEST_SHELL"
  make_case transcript-root-refusal
  CALLER_XDG=
  DEST_XDG=
  OUT=$(run_case); RC=$?
  printf '%s\nspawn exit=%s; destination exit=%s\n' "$OUT" "$RC" "$(< "$CASE_DIR/probe-status")"
  printf 'Destination diagnostic: '; head -n 1 "$CASE_DIR/probe-output"
  [ "$RC" != 0 ] && [ ! -e "$CASE_DIR/treehouse-calls" ] && [ ! -e "$CASE_DIR/helper-calls" ] || exit 1
  [ "$(< "$CASE_DIR/destination-cwd")" = "$PROJ_DIR" ] || exit 1
  printf 'Neither Treehouse nor any helper was invoked; destination directory unchanged.\n'
done

. tests/fm-control-prestart.test.sh >/dev/null || exit 1
make_case transcript-proof
printf '\n=== synthetic prestart: inspection sends no input ===\n'
OUT=$(run_control) || exit 1
printf '%s\n' "$OUT"
PROOF=$(printf '%s' "$OUT" | jq -er .proof) || exit 1
[ ! -e "$D/keys" ] || exit 1
printf '\n=== synthetic prestart: changed process identity invalidates proof ===\n'
printf 'changed\n' > "$D/fault"
OUT=$(run_control --if-match "$PROOF"); RC=$?
printf '%s\nexit=%s\n' "$OUT" "$RC"
[ "$RC" != 0 ] && [ ! -e "$D/keys" ] || exit 1
rm "$D/fault"
printf '\n=== synthetic prestart: matching proof cancels once and verifies stop ===\n'
OUT=$(run_control --if-match "$PROOF"); RC=$?
printf '%s\nexit=%s\n' "$OUT" "$RC"
[ "$RC" = 0 ] && [ ! -e "$H/state/orphan.meta" ] || exit 1
printf 'Recorded fixture key delivery: '; head -n 1 "$D/keys"
printf '\nAll transcript fixtures are removed on exit.\n'

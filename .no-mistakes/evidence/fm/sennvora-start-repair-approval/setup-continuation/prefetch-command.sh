#!/usr/bin/env bash
set -eu
# Execute the existing two command-building functions without starting a worker.
# Acceptance evidence comes from native Git fetch and the acquired terminal cwd.
source <(awk '/^shell_quote\(\)/,/^}/; /^spawn_treehouse_get_command\(\)/,/^}/' bin/fm-spawn.sh)
spawn_treehouse_get_command "$1"

# Test revalidation after the scoped lint annotation

provider_class: openai-ok
sphaere: business:sennvora
native_task: sennvora-start-repair-approval
run: 01M55HGHVS6C46RYFFX5EXDFRX
phase: test
tested_head: b972ef1f313fed67c6595afa0b50a2c5fa0b4c3d
verdict: go
source_changes_by_this_test_turn: none

## Current execution

The current commit adds only the explanation and command-local SC2016 annotation; it does not change the deferred guard string or its execution.
Four existing targeted executable regressions were rerun sequentially at this exact head, with disposable HOME/configuration/temp paths inside the worktree.
The approved genuine Fish 4.9.3 directory was prefixed only for the individual test processes; Fish destination execution uses --no-config.

- `timeout 300 bash tests/fm-spawn-github-prefetch.test.sh`: exit 0.
- `timeout 300 bash tests/fm-control-prestart.test.sh`: exit 0.
- `timeout 300 bash tests/fm-control.test.sh`: exit 0.
- `timeout 300 bash tests/fm-spawn-worktree-settle.test.sh`: exit 0.

The prefetch regression executes the emitted command in real Bash and Fish with real Git credential plumbing and explicit terminal, Treehouse and gh fixtures.
It verifies helper identity, equivalent effective configuration roots, HOME fallback, parent-shell directory transition, mismatching/indeterminate root rejection, unsupported authentication refusal, prompt suppression and non-disclosure of synthetic overrides.
The prestart regression executes the control interface with explicit Herdr/process/backlog fixtures and real jq.
It verifies no-input inspection, matching cancellation, HTTPS-only operation, stale/foreign/ambiguous/unsafe identity rejection, producer-lock protection, unlanded-work preservation and no escalation after an unverified stop.
These are deterministic regression passes, not additional live Treehouse/authentication/Herdr acceptance claims.
The existing jq 1.8.2 counterevidence in `../jq-label-counterevidence.log` remains unchanged: matching synthetic metadata returned true/0 and foreign-label metadata false/1.
No jq parser defect was claimed or fixed.

## Same-run live evidence retained, not repeated

The latest captain decision explicitly forbids repeating the two already successful live actions merely for this comment change.
No new acquisition, lab, cancellation, external authentication experiment or operational-prestart action was performed in this invocation.
Both live passes below belong to this same run and are carried forward from `../final-core-checks/`, whose report records the earlier tested head 44973119034e1b6cf3414a741c641bdee1b42918.

1. Exactly one real native Treehouse-owned GitHub fetch completed with exit 0 in the own disposable Website copy, using the selected existing native helper before acquisition.
   The original destination shell PID survived, its directory entered the own Treehouse pool, and the acquired Git common directory and fetched head matched the own copy.
   Evidence: `../final-core-checks/acquisition-result.json`, `../final-core-checks/native-fetch-events.json`, `../final-core-checks/preconditions.json` and the executed `acquisition.py` driver.
2. A fresh own waiting HTTPS prestart in the guarded non-default Herdr lab was inspected without input and cancelled once with the newly returned fingerprint.
   The actual product reported `prestart stopped: sennvora-start-repair-approval; endpoint preserved; project unchanged`.
   The original shell remained, the fetch processes stopped, the project stayed clean with unchanged head, and no task metadata was adopted.
   Evidence: `../final-core-checks/cancel-result.log`, `../final-core-checks/waiting-prestart-result.json`, `../final-core-checks/prestart-postconditions.json` and the executed `waiting-prestart.py` driver.

The earlier lab teardown evidence confirms the owned lab absent, its tripwire removed and the default baseline unchanged and still running.
The supplied Website seed also remained clean with unchanged head and origin.
The earlier failed setup iterations remain historical failures and are not relabelled.

## Continuity and limits

A source-continuity review, not a substitute runtime test, compared the earlier live-tested head with the current head.
`bin/fm-prestart-control-lib.sh` and `bin/backends/herdr.sh` have no differences between those heads.
The prefetch command-generating function differs only by the two new comments, and the prestart dispatch/cancellation path is unchanged.
Other upstream/rebase changes exist between those heads; the entire intervening history is not described as comment-only.
Fresh execution of the four targeted regressions supplies current-head evidence separately from the retained live evidence.

No complete repository suite, linter, formatter, type checker or static analysis was run in this Test phase.
No source/test/memory/skill files, global configuration, credentials, daemon, production Website or pipeline controls were changed.
All scratch created by this invocation was removed; evidence remains only in the allowed run evidence directory.
This change exposes CLI/process behavior, not a changed rendered UI, so no screenshot or desktop interaction was needed.

This Test result does not prove cancellation of the original operational prestart; Firstmate still owns that separate fresh-identity operation.
Publication, PR, CI, merge, deployment and WeKnora delivery remain with the outer workflow owner; no new reusable knowledge beyond the existing handoff was introduced.
The next Website step remains a separately authorized existing-code build/start capability check for Hostinger without Horizons; it was not started here.

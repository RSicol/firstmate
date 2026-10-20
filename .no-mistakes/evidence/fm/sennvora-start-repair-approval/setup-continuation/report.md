# Test setup correction and bounded continuation

provider_class: openai-ok
sphaere: business:sennvora
native_task: sennvora-start-repair-approval
run: 01M55HGHVS6C46RYFFX5EXDFRX
phase: test
tested_head: 44973119034e1b6cf3414a741c641bdee1b42918
verdict: inconclusive
tracked_source_changes: none

## Outcome

The reported empty-response decoder failure was reproduced and corrected in the temporary Test driver only.
The corrected adapter accepts successful `pane run` without parsing a JSON body, while response-producing operations still require valid JSON and command failures still raise.
The driver now propagates exceptions as a nonzero process exit rather than concealing failure with exit 0.
No shared source, tests, jq binding, JSON schema or pipeline configuration was changed.

The supplied Website seed and selected absolute native gh entry were available and matched the provided identities.
The descriptor was explicitly supplied only to the individual command-building subprocess, not assumed inherited from the daemon and not installed globally.
`preconditions.json` records all four descriptor checks true, no unsupported authentication override, no conflicting existing descriptor, and the selected executable matching the outer-provided resolved identity.
No credential files, tokens, account lists or credential outputs were inspected.
The effective-root guard successfully generated its command; the resulting actual expected-root value stayed private in scratch and was not archived.

An own disposable ordinary Website input copy was cloned locally from the supplied seed with `--local --no-hardlinks --template=` and no external bootstrap fetch.
Only the own copy's origin was set to the authorized existing private repository.
The supplied seed was clean, at the expected input head and unchanged after copying; it was never a test CWD, acquisition target or pool.

## One real corrected lab iteration

Exactly one new named non-default lab was provisioned through the existing guarded helper and `/usr/local/bin/herdr` 0.9.5.
Session: `fm-lab-start-repair-cur-1564957-25718`.
Its own workspace/tab/pane identities came from its new creation responses, not previous sessions or historical targets.
The marked FM_HOME, synthetic project and pool were inside this worktree.
HOME, XDG and the Herdr profile were not relocated or changed.
The running default was retained as the helper's required tripwire baseline.

The real `pane run` returned 0 with empty stdout, and the corrected JSON handling proceeded successfully.
A real native Treehouse process, `git fetch origin` and the HTTPS transport were observed waiting on the owned loopback endpoint; see `waiting-process-info.json`.
TLS verification was not disabled and no external authentication experiment was substituted.
The read-only `fm-control.sh ... cancel-prestart --pane <fresh-own-pane>` command was submitted from the own coordinator.
No matching `--if-match` cancellation was sent.

### Additional temporary-driver error, not an established product defect

The remaining old driver treated any nonempty inspection stderr as a refusal before the command had finished.
The gate's informational `gate agent lifecycle permitted only against lab home ...` line therefore caused premature driver failure and cleanup.
A later `cancel-prestart did not establish its required result` line is preserved in `inspection-errors.log`, but must NOT be presented as proof that an intact live inspection independently failed.
The driver had already stopped and was closing its loopback socket before that log finished changing.
File modification times measured relative to snapshot creation were:

- `fresh-snapshot.json`: 0 ms.
- `waiting-prestart-result.json`: 62.363 ms.
- `waiting-console.log`: 152 ms.
- `inspection-errors.log`: 348 ms.
- `lab-cleanup.log`: 1276 ms.

The actual inspection result is consequently inconclusive; the incomplete snapshot was empty.
The archived executed driver and its logs retain this failure unchanged.
After cleanup, the temporary driver was corrected to record the inspection command's actual exit status and wait for that status before accepting or rejecting its JSON result.
This second correction was verified OFFLINE ONLY, without another lab iteration or another inspection/cancellation attempt.
`waiting-prestart.corrected-offline.py` is the revised driver; `waiting-prestart.py` is the version actually used live.

The combined driver exited 1, as required for a driver exception.
Because it stopped at this error, the prepared real GitHub acquisition driver was NOT executed.
`acquisition.py` is archived as unexecuted preparation, not successful acquisition evidence.
There were zero real GitHub Acquire/Fetch calls and zero `--if-match` calls in this continuation.
No real Website/CCM process or original operator prestart was touched.

## Focused verification

`python3 .validation-continuation/response-check.py`: exit 0.
It executes the actual temporary driver's response-handling sections with local command responses, without live Herdr or authentication actions.
It reproduces both the original empty-body JSON exception and the premature-stderr failure, then verifies:

- Successful empty command responses are accepted without JSON decoding.
- Valid metadata responses are decoded; malformed metadata remains an error.
- A failed submitted command remains an error.
- Informational stderr does not defeat a completed successful inspection.
- Nonzero inspection exit and malformed inspection JSON still fail.

These are Test-driver contract checks, NOT passing live cancellation or acquisition evidence.

Four existing focused product regression suites also passed again, separately from live acceptance:

- `timeout 300 bash tests/fm-spawn-github-prefetch.test.sh`: exit 0, 171 seconds.
- `timeout 300 bash tests/fm-control-prestart.test.sh`: exit 0, 30 seconds.
- `timeout 300 bash tests/fm-control.test.sh`: exit 0, 87 seconds.
- `timeout 300 bash tests/fm-spawn-worktree-settle.test.sh`: exit 0, 13 seconds.

The approved genuine Fish 4.9.3 was a PATH prefix for each individual test process only; its executable tests use `--no-config` and did not skip Fish.
The daemon, global PATH and shell configuration were unchanged.
These deterministic regressions retain their existing fixture boundaries and are not recast as additional live business/authentication scenarios.
No complete repository suite, linter, formatter, static-analysis tool, installation or compiler was run.

The existing real jq 1.8.2 counterevidence remains unchanged at `../jq-label-counterevidence.log`: matching metadata true/0; foreign label false/1.
No jq parser defect was reproduced or fixed.

## Cleanup, remaining boundary and handoff

The guarded teardown succeeded.
Fresh guard-mediated session metadata confirmed the exact owned lab absent, its tripwire removed and the default baseline identical and still running; see `cleanup-confirmation.json` and the before/after baseline records.
All transient copies, pools, generated expected-root command, fixtures and scratch are removed after evidence archival.
The outside supplied seed remains untouched.
Final worktree status and head are in `final-worktree.log`.

Both positive live core acceptances remain incomplete.
A further live iteration or acquisition continuation requires the outer executor's decision; none is started or silently approved here.
There is no demonstrated product defect requiring a source change, no waived test and no claim of end-to-end success.
No pipeline controls, extra worker/model, commits, push, PR, CI, daemon/session-default restart, global configuration change, credential copy or production change were performed.
There was no rendered UI change; screenshots were not applicable.

The reusable result is the narrow Test-driver response contract: command acceptance may have no JSON body; informational stderr is not an exit status; incomplete scenarios must exit nonzero.
WeKnora ingestion and any user-skill maintenance are handed back to the existing SennVora workflow owner, because this Test phase may not write those services/configurations outside its worktree/evidence boundary.
No external knowledge store or user skill was modified.
The next Website step remains a separately authorized existing-code build/start capability check for Hostinger without Horizons; it was not started and no Hostinger runtime acceptance is claimed.

Report path:
`/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/setup-continuation/report.md`

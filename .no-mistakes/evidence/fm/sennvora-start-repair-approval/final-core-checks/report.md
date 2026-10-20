# Bounded live Test acceptance

provider_class: openai-ok
sphaere: business:sennvora
native_task: sennvora-start-repair-approval
run: 01M55HGHVS6C46RYFFX5EXDFRX
phase: test
tested_head: 44973119034e1b6cf3414a741c641bdee1b42918
verdict: go
tracked_source_changes: none

## Scope and outcome

Both previously incomplete, explicitly approved positive live core checks completed successfully in this Test continuation.
The four existing targeted deterministic suites passed separately, including genuine Bash/Fish execution and adversarial authentication and prestart identity cases.
No fixture result is represented as a live acquisition or cancellation.
The latest recorded decision limits live work to the two positive core paths, not nine additional live business/authentication cases.
No product defect or source correction was needed.

The temporary driver reuses the prior corrected response contract: successful `pane run` may have an empty response, metadata operations require JSON, and inspection waits for the command's recorded exit status rather than treating informational stderr as failure.
The preserved earlier failed iterations remain failed/inconclusive historical evidence; this report does not relabel them.

## Live scenario 1: selected native helper reaches Treehouse acquisition

The supplied helper descriptor was explicitly provided to the individual command-building subprocess through the existing two-entry Git configuration interface.
`preconditions.json` confirms the descriptor shape, selected executable identity, lack of conflicting Git/authentication overrides and supplied seed identity using booleans only.
The selected existing entry was the outer-supplied absolute gh executable, not a substitute helper or new login.
HOME, XDG_CONFIG_HOME and GH_CONFIG_DIR were not changed to force a match.
The actual effective-root metadata remained private in disposable scratch and was not archived.

The supplied ordinary Website seed was read-only input to a local `git clone --local --no-hardlinks --template=` inside the worktree.
Only that new copy's origin was set to the authorized existing private Website repository.
There was no external bootstrap fetch or separate authentication/API experiment.

Exactly one real Treehouse-owned `git fetch origin` completed with exit 0 through the selected native gh helper.
The command emitted by the existing `spawn_treehouse_get_command` function was sourced in the original lab destination shell, not evaluated in a replacement controller shell.
The destination entered the isolated TREEHOUSE_ROOT pool; its shell PID was unchanged, its acquired Git common directory belonged to the own input copy, and its head matched the fetched default head.
No coding, Website or CCM worker was launched.

Evidence:

- `acquisition-result.json`: actual native acquisition, selected-helper observation, shell identity and isolated worktree assertions, recorded while the live native trace was available.
- `native-fetch-events.json`: non-secret native Git trace events showing the single fetch start and exit 0; raw trace, environments and credential output are excluded. Helper child events belonged to descendant trace sessions and are not included in this root-fetch-only extract.
- `acquisition.py`, `prefetch-command.sh` and `prepare-input.py`: the executed temporary test drivers.
- `supplied-seed-after.json`: the supplied seed remained clean with unchanged origin and head after the complete live turn.

## Live scenario 2: fresh own waiting HTTPS prestart is inspected and cancelled once

Exactly one fresh named non-default Herdr lab was provisioned through `bin/fm-herdr-lab.sh` and the existing `/usr/local/bin/herdr` 0.9.5.
Session: `fm-lab-start-repair-fin-2211127-5361`.
All workspace, tab and pane identities came from this iteration's creation responses.
No historical identifier, foreign pane, default-session pane, personal window, viewer or focus action was used.
The required running default was used only as the helper's metadata tripwire.

A real native Treehouse/Git HTTPS fetch waited against the test-owned loopback listener while it withheld the TLS handshake.
TLS verification was not disabled and no mock replaced Herdr, Treehouse, Git or the control product.
The synthetic project, held backlog row and marked FM_HOME were private disposable fixtures inside the worktree.

From that lab's own actual coordinator, `fm-control.sh sennvora-start-repair-approval cancel-prestart --pane <fresh-own-pane>` exited 0 and returned a fresh snapshot with `input_sent: false`.
The same native foreground process identities were still running after inspection.
Exactly one subsequent control call supplied the freshly returned `--if-match` fingerprint and exited 0.
The product reported: `prestart stopped: sennvora-start-repair-approval; endpoint preserved; project unchanged`.
The original terminal shell remained, the fetch processes were gone, the project head and cleanliness were unchanged, and no task metadata was adopted.
There was no raw cancellation route, extra key, endpoint closure, identity weakening or retry after refusal.

Evidence:

- `waiting-process-info.json`, `fresh-snapshot.json`, `process-info-after-inspection.json`: native waiting tree, fresh identity and no-input observation.
- `cancel-result.log`, `stopped-process-info.json`, `preserved-pane.json`: actual control output and preserved shell endpoint.
- `prestart-postconditions.json`, `waiting-prestart-result.json`: successful exit statuses and persisted postconditions.
- `control-from-actor.sh`, `cancel-from-actor.sh`, `waiting-prestart.py`: the executed temporary test drivers.

## Targeted deterministic regressions, not additional live scenarios

Executed sequentially with the approved existing Fish 4.9.3 directory prefixed only for each individual test process and TMPDIR inside disposable worktree scratch:

- `timeout 300 bash tests/fm-spawn-github-prefetch.test.sh`: exit 0.
- `timeout 300 bash tests/fm-control-prestart.test.sh`: exit 0.
- `timeout 300 bash tests/fm-control.test.sh`: exit 0.
- `timeout 300 bash tests/fm-spawn-worktree-settle.test.sh`: exit 0.

These preserve matching/equivalent effective-root success, mismatching/indeterminate root and existing override rejection, helper selection, prompt/disclosure prevention and parent-shell directory transitions in actual Bash and genuine Fish.
Prestart fixture cases cover stale, foreign, ambiguous, unsafe, active-producer, existing-record and dirty-project refusals, plus a failed-stop postcondition without escalation.
No Fish acceptance was skipped.
Full logs and `regression-results.json` are retained alongside this report.
No complete repository suite, linter, formatter, static analysis, installation or compiler was run.

The existing `../jq-label-counterevidence.log` remains unchanged: real jq 1.8.2 returned true/0 for matching synthetic tab metadata and false/1 for a foreign label.
This continuation did not reproduce or fix a jq parser defect and did not rename the jq binding or JSON field.

## Cleanup, remaining ownership and knowledge handoff

Guarded teardown completed in the same evidence turn.
`cleanup-confirmation.json` confirms the exact owned lab absent, its tripwire removed, and the default baseline identical and still running.
`default-baseline-before.json` and `default-baseline-after.json` preserve the guard-required metadata only.
All transient local copies, pools, raw trace, actual expected-root command, marked lab home and temporary test drivers are removed from the worktree after archiving non-secret evidence.
The final worktree is clean at the preserved target head.
No source, memory file, user skill, pipeline configuration, daemon, login, account, credential store, global Git/shell/PATH or production Website state was modified.
No pipeline controls, commits, push, PR, CI, merge or deployment phase was performed.
This is a CLI/process-control change; no rendered UI was changed and no desktop screenshot or viewer was needed or authorized.

This proves the two approved disposable live core paths, not cancellation of the original operational prestart.
That original prestart was neither inspected nor controlled here; any operational action still belongs to Firstmate and requires its own fresh identity proof.
No new external authentication/business cases were added.

The reusable handoff is the validated Test-driver response boundary and the successful bounded live evidence above.
WeKnora ingestion and any reusable user-skill maintenance are returned to the existing SennVora workflow owner; this Test phase does not have authority to write external services or user-level skills.
Use only provider_class=openai-ok and sphaere=business:sennvora, with this redacted report rather than raw transcripts, credentials or environment values.

The next Website step remains a separately authorized existing-code build/start capability check for Hostinger without Horizons, before content/privacy/public presence and the later portal.
It was not started here and no Hostinger runtime acceptance is claimed.

Absolute report path:
`/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/final-core-checks/report.md`

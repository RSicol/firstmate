# Current Test-phase evidence

provider_class: openai-ok
sphaere: business:sennvora
native_task: sennvora-start-repair-approval
run: 01M55HGHVS6C46RYFFX5EXDFRX
phase: test
tested_head: 44973119034e1b6cf3414a741c641bdee1b42918
base: 11990a20882556811418d10c266860416b5faf6f
verdict: inconclusive
source_changes: none

## Result

All four targeted executable-interface regression suites passed again in this invocation.
Real CLI argument rejection also passed without backend input.
A fresh guarded Herdr lab was actually provisioned using the required existing `/usr/local/bin/herdr` 0.9.5 and the unchanged caller runtime context.
The native helper successfully created its own coordinator workspace and target tab and accepted one command to start the controlled local HTTPS Treehouse prestart.
However, the temporary Python driver then incorrectly attempted to parse the successful, empty `pane run` response as JSON.
Its `Expecting value: line 1 column 1 (char 0)` exception triggered cleanup before any native process identity snapshot or matching cancellation was obtained.
This is a Test-driver setup failure, not an observed product defect or a Herdr permission/guard refusal.
The driver command itself returned 0 despite recording this exception; that exit is NOT treated as a passing scenario.

The real private-GitHub acquisition was not attempted.
The current phase did not inherit the required task-local two-entry native helper descriptor: `preconditions.json` records only boolean shape checks, all descriptor checks false.
The worktree has no supplied `projects/`, `data/` or `.no-mistakes/` Website seed.
No replacement helper/account selection, credential-file/configuration-store inspection, extra external bootstrap fetch or operation in an active Website/CCM copy was performed to manufacture that missing setup.
A continuation needs the existing selected non-secret helper descriptor and an authorized local Website seed accessible within the boundary, not a new login or copied credentials.

Neither approved positive core acceptance is claimed passed.
The approval itself is acknowledged; the old explanation that the caller lacks the required default baseline is disproved here.
No additional lab/acquisition attempt was made after cleanup of this one-shot attempt.
The outer executor owns the continuation decision; this phase does not approve or waive its missing acceptance evidence.

## Scenarios and targeted regressions

- Successful helper handoff and the original-shell directory transition: deterministic PASS in genuine Bash and Fish; real acquisition UNTESTED.
- Equivalent effective XDG/HOME roots versus mismatching, missing or relative roots, token/host/config overrides, arbitrary helpers and missing authentication: deterministic PASS in genuine Bash and Fish; fixtures are not live Treehouse/GitHub acceptance.
- Fresh inspection with no input and exactly one matching cancellation preserving endpoint/project, plus foreign, ambiguous, stale, unsafe, HTTP, active-producer and unconfirmed-stop rejection: deterministic PASS; real positive cancellation UNTESTED after the driver error.
- Missing pane and malformed fingerprint through the actual `fm-control.sh` executable: LIVE PASS, both exit 1 with the intended error and no backend operation.

Exact baseline commands, each invoked with a 300-second limit and `TMPDIR="$PWD/.validation-current/tmp"`:

- `timeout 300 bash tests/fm-spawn-github-prefetch.test.sh`: exit 0, 46.3 seconds; `fm-spawn-github-prefetch.log`.
- `timeout 300 bash tests/fm-control-prestart.test.sh`: exit 0, 27.4 seconds; `fm-control-prestart.log`.
- `timeout 300 bash tests/fm-control.test.sh`: exit 0, 39.1 seconds; `fm-control.log`.
- `timeout 300 bash tests/fm-spawn-worktree-settle.test.sh`: exit 0, 8.4 seconds; `fm-spawn-worktree-settle.log`.

The approved Fish directory was a PATH prefix for only these individual test processes; the suites invoke Fish with `--no-config`.
No complete suite, linter, formatter, compiler or static analyzer was run.
These regression outputs remain separate from actual live product evidence.

## Live lab, attempted action and teardown

Driver: `bash .validation-current/provision-check.sh`, archived as `provision-check.sh`.
Scenario driver: `python3 .validation-current/waiting-prestart.py`, archived as `waiting-prestart.py`.

Fresh helper-generated session: `fm-lab-start-repair-cur-64630-14040`.
Fresh marked FM_HOME: the worktree's `.validation-current/lab-home`, minted by `bin/fm-lab-home.sh create`.
Only this lab's new runtime objects used the existing user runtime; HOME, XDG settings, Herdr profile, global configuration and the default session were not changed.
A process-local `/usr/local/bin` prefix selected `/usr/local/bin/herdr`; the ambient alternative was not used.

Fresh provisioning called `bin/fm-herdr-lab.sh provision` directly, letting it perform its own internal prepare step.
It did not repeat the earlier erroneous separate-prepare-before-provision ordering.
Provisioning succeeded, including the guard-required running-default baseline.
All scenario Herdr commands went through `bin/fm-herdr-lab.sh run <fresh-session> ...` with explicit helper-owned session selection.
No viewer, attach, focus command, GUI or desktop input was used.

The driver used real tasks-axi to add and hold the same task id only inside its marked disposable lab, and created a minimal clean local project with a loopback HTTPS origin.
A local loopback socket was prepared to withhold the TLS handshake; TLS verification was never disabled and no external credential test was substituted.
The exact own create responses bound workspace `w1`, coordinator pane `w1:p1`, and target tab/pane `w1:t2`/`w1:p2`.
These are new lab-local identities, not historical operator targets or label-discovered fleet targets.

The actual native command accepted by Herdr was:

`bin/fm-herdr-lab.sh run fm-lab-start-repair-cur-64630-14040 pane run w1:p2 'env TREEHOUSE_ROOT=<own-lab>/pool GIT_TERMINAL_PROMPT=0 GIT_ASKPASS=/bin/false treehouse get'`

`pane run` returned 0 with no stdout; the subsequent JSON decode in the driver failed.
No process-info evidence was obtained, so even whether that command reached a qualifying waiting process tree is NOT claimed.
No `fm-control.sh --if-match` call was executed and no cancellation/endpoint-preservation postcondition was proved.
The created resources are setup evidence only, not a passing cancellation scenario.

The driver closed its own loopback listener and requested its combined cleanup.
Guarded `bin/fm-herdr-lab.sh teardown` returned 0 and removed the owned session.
A fresh helper-mediated session metadata read then verified that exact session absent and exactly one running default with metadata equal to the saved baseline.
`cleanup-confirmation.json` and `default-baseline-before.json` / `default-baseline-after.json` preserve these checks.
No default/fleet pane, chat, agent tree or original operator prestart was inspected or controlled.

A future executor-authorized continuation should treat successful `pane run` as a no-body operation, parsing JSON only for response-producing operations.
It must not change the product, relax guards, reuse deleted target ids or interpret this setup failure as a permission failure.
The actual failed driver is archived unchanged for reproducibility.

## Direct real-product rejection

Using the marked lab FM_HOME and no terminal fixture:

- `bash bin/fm-control.sh sennvora-start-repair-approval cancel-prestart`: exit 1, `error: cancel-prestart requires --pane`.
- `bash bin/fm-control.sh sennvora-start-repair-approval cancel-prestart --pane w1:p2 --if-match not-a-fingerprint`: exit 1, `error: --if-match requires the exact fingerprint from the read-only snapshot`.

The latter pane spelling was only invalid-command input after lab deletion; parsing rejected it before any backend targeting.
The gate diagnostic explicitly permitted the marked lab home; it was not a gate denial.
See `direct-cli-refusals.json`.

## Executables, counterevidence and remaining boundaries

- `/usr/local/bin/herdr`: 0.9.5, actually used for the live lab.
- `/home/sreazy/.local/bin/treehouse`: v3.1.4; native pane command submitted, no successful acquisition proved.
- `/usr/bin/bash`: 5.3.15.
- Approved absolute task-local Fish: 4.9.3, actually used with `--no-config` by the regression suite.
- `/usr/bin/git`: 2.55.0.
- `/usr/bin/jq`: 1.8.2.

The original `../jq-label-counterevidence.log` remains unchanged: matching metadata true/0; foreign-label metadata false/1 using real jq 1.8.2 and the unchanged expression.
No parser defect is claimed reproduced or fixed; no jq binding/schema or shared source was changed.

The only persistent new outputs are this evidence directory's files.
Temporary fixtures, scripts, native lab home/project/pool and test caches are removed from the worktree after archiving; final checks are recorded in `final-worktree.log`.
No pipeline controls, commits, push, PR, CI, extra worker/model run, actual CCM start, production change, installation, credential copy, login/store change or global configuration change was performed.
There is no rendered UI/layout change here; CLI responses are the applicable user surface, so screenshots were not applicable.
WeKnora handoff and any skill maintenance remain with the existing SennVora workflow owner, rather than making out-of-boundary service or user-skill writes inside this Test phase.
After repair acceptance, the next Website step is a separately authorized existing-code build/start capability check for Hostinger without Horizons; it was not started and no Hostinger runtime acceptance is claimed.

Absolute report path:
`/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/current-core-checks/report.md`

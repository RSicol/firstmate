# Approved core-check Test iteration

provider_class: openai-ok
sphaere: business:sennvora
native_task: sennvora-start-repair-approval
run: 01M55HGHVS6C46RYFFX5EXDFRX
phase: test
base: 11990a20882556811418d10c266860416b5faf6f
tested_head_sha: 44973119034e1b6cf3414a741c641bdee1b42918
verdict: inconclusive
source_changes: none

## Result

Both focused executable-interface regression suites passed unchanged.
The earlier missing-default explanation did NOT reproduce in the actual caller context with the approved `/usr/local/bin/herdr` 0.9.5: guarded preparation succeeded and captured the required running-default baseline.
The subsequent live lab provisioning stopped on a different guard refusal caused by this iteration's setup ordering.
No real acquisition, HTTPS waiting prestart, identity snapshot or matching cancellation was exercised.
Neither positive core path is claimed passed or approved.

## Exact refusal and root cause

Fresh helper-generated identity: `fm-lab-start-repair-3909255-1426`.

The temporary driver first called:

`bash bin/fm-herdr-lab.sh prepare fm-lab-start-repair-3909255-1426`

This returned 0 and created its own worktree-local tripwire.
It then called:

`bash bin/fm-herdr-lab.sh provision fm-lab-start-repair-3909255-1426`

This returned 1 with:

`fm-herdr-lab: tripwire already exists for 'fm-lab-start-repair-3909255-1426'; refusing ambiguous ownership`

This was a test-setup sequencing error, not an observed failure of the credential or cancellation changes.
For a fresh absent session, `fm_herdr_lab_provision` invokes `fm_herdr_lab_prepare` itself; the separate preceding preparation had already created the tripwire that this second preparation correctly refuses to overwrite.
The narrow setup correction for a future authorized attempt is to let fresh `provision` perform its own preparation, not weaken the ownership guard or accept an existing ambiguous tripwire.
No such retry was made: the current instructions require stopping on any guard/tool refusal and returning the evidence to the outer executor.
No alternate binary, relocated profile/runtime, raw lifecycle control, replacement session, second run or parallel validation was attempted.

The driver failed before the helper's server-start call.
No lab server, controlled HTTPS process or fetch was started, and no `fm-control.sh --if-match` input was sent.
The real GitHub/Treehouse check was not attempted after this refusal; approval is no longer its blocker, but live acceptance remains unproven.
The caller also did not inherit the two-entry task-local Git helper descriptor; only boolean shape checks were performed, with no credential/configuration-root values read or printed and no descriptor reconstructed.

## Focused deterministic verification

Temporary directory for both commands: `TMPDIR="$PWD/.validation-core/tmp"`.
Only individual test child processes received the approved Fish directory as a PATH prefix:

`/home/sreazy/sennvora/arbeitsbereich/secondmate-website/data/sennvora-start-repair-approval/fish-runtime/4.9.3/bin`

- `timeout 300 bash tests/fm-spawn-github-prefetch.test.sh`: exit 0, approximately 46.1 seconds; `fm-spawn-github-prefetch.log`.
  Real Bash and genuine Fish with `--no-config` exercised emitted commands, synthetic helper plumbing, parent-shell directory transition, effective-root equivalence/mismatch and unsupported-authentication refusal.
  Authentication, Treehouse and terminal fixtures are not live acquisition evidence.
- `timeout 120 bash tests/fm-control-prestart.test.sh`: exit 0, approximately 27.4 seconds; `fm-control-prestart.log`.
  Snapshot, matching cancellation, stale/foreign/unsafe rejection, project preservation and stop-verification cases used explicit Herdr/process fixtures, not live cancellation.

The other two previously passing focused suites and their evidence remain unchanged in the parent evidence directory; they were not redundantly rerun.
No complete test suite, linter, formatter, compiler or static analysis was run.

## Actual live commands, scope and cleanup

Temporary live drivers are archived beside this report.
They were executed from the exact target worktree using `timeout 30`, `timeout 80` and `timeout 30`, respectively:

1. `bash .validation-core/prepare-live-lab.sh`: exit 0; `live-lab-prepare.log`.
2. `bash .validation-core/provision-live-lab.sh`: exit 1; `live-lab-provision.log`.
3. Cleanup only, `bash .validation-core/cleanup-live-lab.sh`: exit 0; `live-lab-cleanup.log`.

These drivers selected `/usr/local/bin/herdr` with a process-local `/usr/local/bin` PATH prefix and checked that exact executable selection.
`HOME`, XDG settings, Herdr configuration/runtime location, global/daemon PATH and existing services/sessions were not changed.
`FM_HERDR_LAB_STATE_DIR` and `TMPDIR` kept the owned helper evidence under `.validation-core/` in the worktree.
All native Herdr commands went through `bin/fm-herdr-lab.sh` with the freshly generated explicit non-default identity.
No default/fleet panes, chats, agent trees or historical target IDs were inspected.

After refusal, guarded `teardown` returned 0 for the never-created lab, removed only its prepared tripwire and verified the default baseline.
A final helper-mediated session metadata query confirmed the fresh lab absent and exactly one running default.
`cmp` of `default-baseline-before.json` and `default-baseline-after.json` returned 0.
These are guard-required default metadata only, not control of that session.
The original operator prestart was neither inspected nor controlled and is not claimed stopped.
Temporary scripts, fixtures, caches and helper-state directories were removed from the worktree after archiving.
No dependencies were removed.
Final clean-source and target-HEAD checks are recorded in `final-worktree.log`.

## Executables

- Bash: `/usr/bin/bash`, GNU Bash 5.3.15.
- Git: `/usr/bin/git`, 2.55.0.
- jq: `/usr/bin/jq`, 1.8.2.
- Herdr used for all live helper commands: `/usr/local/bin/herdr`, 0.9.5; the different ambient PATH entry was not used.
- Approved Fish: absolute task-local path above plus `/fish`, 4.9.3; tests invoke it with `--no-config`.
- Treehouse: `/home/sreazy/.local/bin/treehouse`, v3.1.4; version/help inspection only, no acquisition.

## Preserved counterevidence and boundaries

The original `../jq-label-counterevidence.log` is retained byte-for-byte: real jq 1.8.2 returned `true`/0 for matching metadata and `false`/1 for a foreign label using the unchanged expression.
That earlier executable evidence disconfirms the repeated parser claim; this iteration did not rerun or claim to fix it.
No jq binding, Herdr JSON schema, credential guard, Fish compatibility, ownership predicate or strict rejection boundary was changed.

No pipeline controls, commits, push, PR, CI, actual CCM/agent start, external auth/API/fetch experiment, credential-file/keyring read, secret transfer, login/store change, installation, global configuration change, desktop operation or Website/production modification occurred.
The existing task, head, model route and budgets were preserved.

The outer executor owns the unresolved Test result and any next authorized iteration; this report does not answer its own ask-user finding or waive live acceptance.
WeKnora delivery and reusable skill maintenance remain with the existing SennVora workflow owner: this phase writes only the allowed local/evidence artifacts and does not mutate an external knowledge service or user skills.
After the existing repair is actually accepted, the next website step remains a separately authorized code/build/start-capability check for Hostinger without Horizons; nothing was started and no Hostinger runtime acceptance is claimed.

Absolute report path:
`/home/sreazy/sennvora/arbeitsbereich/secondmate-website/config/no-mistakes-start-repair/evidence/01M55HGHVS6C46RYFFX5EXDFRX/approved-core-checks/report.md`

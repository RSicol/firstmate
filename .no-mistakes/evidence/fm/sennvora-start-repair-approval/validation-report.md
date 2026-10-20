# Start-repair validation

provider_class: openai-ok
sphaere: business:sennvora
native_task: sennvora-start-repair-approval
phase: test
base: 11990a20882556811418d10c266860416b5faf6f
target: 44973119034e1b6cf3414a741c641bdee1b42918

## Result

No product failure was observed in the targeted checks.
Live end-to-end acceptance remains inconclusive: successful helper handoff and prestart cancellation were demonstrated with explicit fixtures, not with real Treehouse/GitHub authentication or a real Herdr fetch process tree.
Only the direct command-line refusal checks below are live-product results.
No source changes, pipeline controls, pushes, workers, production operations, credential reads, login changes or global configuration changes were performed.

## Named scenarios

- Selected helper reaches the destination before acquisition, and Treehouse's original-shell directory transition survives: PASS, fixture only, in Bash and the approved genuine Fish 4.9.3 with --no-config.
- Equivalent XDG/HOME effective roots are accepted: PASS, fixture only, including HOME fallback, XDG-to-HOME, HOME-to-XDG and equivalent XDG paths.
- Different or indeterminate configuration roots refuse before Treehouse/helper invocation: PASS, fixture only, including XDG and HOME mismatch combinations and missing/relative roots.
- Unsupported caller/destination authentication, arbitrary helpers and unavailable authentication cannot silently choose another account or prompt: PASS, fixture only; diagnostics and emitted commands did not disclose synthetic override values.
- Fresh prestart inspection sends no input; a matching fingerprint cancels once and verifies stop while preserving endpoint/project: PASS, fixture only.
- HTTP, foreign/ambiguous identity, unexpected processes, active producer/agent, stale proof, existing records, unlanded changes and unconfirmed stops fail closed: PASS, fixture only.
- The actual fm-control CLI refuses missing pane, malformed fingerprint and an unbound caller: PASS, LIVE, using a freshly minted disposable lab home and no terminal/agent fixtures.
- Real native-helper Treehouse acceptance: UNTESTED. The selected gh and Treehouse executables are present, but the latest recorded decision forbids fresh external authentication/API/fetch experiments, real credential-store inspection and actual CCM starts. Synthetic Git credential plumbing is the permitted workaround and passed; it does not establish real-fetch acceptance. Any real-account proof requires separate, narrowly scoped authority, not a new login or copied credentials.
- Real Herdr prestart cancellation: UNTESTED. A real guarded `fm-herdr-lab.sh prepare` was attempted with HOME, XDG directories, Herdr configuration, temporary files and lab-helper state confined to the worktree. It refused because its fleet tripwire requires exactly one running default session, which the isolated environment does not have. Provision was not attempted after refusal. Creating a default or weakening the helper is forbidden; using the host's Herdr runtime would require out-of-worktree runtime writes outside this phase's boundary. A compliant guarded lab environment or explicit lab-runtime write authority is needed. The operator's stalled prestart was not read, controlled or claimed stopped.

## Commands and evidence

All test temporary roots were selected with `TMPDIR="$PWD/.validation/tmp"`.
Fish was selected only for the individual child processes with `PATH="/home/sreazy/sennvora/arbeitsbereich/secondmate-website/data/sennvora-start-repair-approval/fish-runtime/4.9.3/bin:$PATH"`; no daemon or global PATH changed.

Baseline targeted commands:

- `timeout 300 bash tests/fm-spawn-github-prefetch.test.sh` — exit 0; `prefetch-regressions.log`.
- `timeout 120 bash tests/fm-control-prestart.test.sh` — exit 0; `prestart-regressions.log`.

Additional targeted protection checks:

- `timeout 180 bash tests/fm-spawn-worktree-settle.test.sh` — exit 0; `worktree-settle-regressions.log`.
- `timeout 240 bash tests/fm-control.test.sh` — exit 0; `control-regressions.log`.

Manual/evidence-producing checks:

- `bash .validation/live-boundaries.sh` — exit 0; real isolated lab preparation refused as described above, and all direct CLI refusal assertions passed. Driver archived as `live-boundaries.sh`; outputs in `live-boundaries.log`.
- `timeout 360 bash .validation/fixture-transcripts.sh` — exit 0; re-executes the two focused fixture suites, then captures successful Bash/Fish handoff, HOME-root mismatch rejection, a no-input snapshot, stale-identity refusal and one verified synthetic cancellation. Driver archived as `fixture-transcripts.sh`; outputs in `fixture-product-transcripts.log`. Its reported spawn and stop results are fixture results only.
- Executed the unchanged tab-identity jq expression with actual jq 1.8.2 against bounded matching and foreign-label JSON. Matching metadata returned true/0; foreign label returned false/1. `$label` parsed successfully. This retains disconfirming evidence for the declined parser finding; no jq binding or schema change was made. See `jq-label-counterevidence.log`.
- Read-only tool capability/version checks confirmed the approved Fish 4.9.3, jq 1.8.2, Herdr 0.8.2 and Treehouse v3.1.4. No missing executable was replaced, installed or searched for on the host.

No complete repository suite, linter, formatter or static analyzer was run.
There is no UI/layout change in this diff; the exercised user surface is CLI output, so visual screenshots were not applicable.
The temporary drivers, fixture repositories, lab home and remaining temporary registries were removed from the worktree after archiving their evidence.

## Remaining decision

The outer executor must decide whether the passing deterministic evidence plus real CLI refusal checks suffice under the recorded fixture-only acceptance boundary, or arrange a separately authorized compliant live lab.
This Test phase does not expand authority or answer that decision itself.
WeKnora delivery, publication and later website work remain with their existing workflow owners; no shared-service writes were made here.

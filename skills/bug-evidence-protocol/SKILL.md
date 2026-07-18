---
name: bug-evidence-protocol
description: Capture and classify minimal red-to-green evidence for a diagnosed bug and scoped fix, with command hashes, Git/environment identity, broader-check records, risk-based approval, route evidence, and optional cpat linkage. Use after diagnose establishes a credible reproducer or when a reported regression needs an auditable proof packet; do not use as an autonomous bug scanner.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Bug Evidence Protocol

Record proof without replacing the workflow that produces it:

- `diagnose` owns reproduction, hypotheses, and root cause;
- `test-driven-execution` owns the behavior-first red/green implementation loop;
- this skill captures and classifies evidence;
- `git-native-context-contract` may retain a recurrent lesson as a `cpat`.

Do not scan a repository for unsolicited bugs or claim a defect from inspection alone.

## Authority and approval

Invocation does not reduce authority already granted by the user. Reversible local tests and scoped code fixes may proceed when they are part of the requested task.

Stop for explicit approval before:

- production or device writes;
- destructive migrations or data mutation;
- dependency or configuration changes outside the approved scope;
- crossing security, privacy, financial, or protected-evidence boundaries;
- expanding files, behavior, or external effects materially beyond the request;
- changing production code during an audit-only or reproduce-only task.

## Evidence integrity

A confirmed bug requires a valid reachable path, a defensible expected behavior, and a focused command that fails for the predicted symptom. Syntax, fixture, dependency, permission, and unrelated setup failures are `INCONCLUSIVE`, not `REPRODUCED`.

Capture the exact targeted command before and after. Preserve argv rather than a shell string. The included capture helper records:

- SHA-256 command identity;
- cwd, runtime, Git root/head/dirty state;
- hashes of selected lockfiles when present;
- time, duration, exit code, and timeout;
- bounded redacted stdout and stderr.

Never capture a full environment dump. Inspect captured artifacts before publishing them; regex redaction is a safety net, not proof that output is public-safe.

```bash
python3 <skill>/scripts/capture_command.py --label targeted-before --output before.json -- <exact command>
python3 <skill>/scripts/capture_command.py --label targeted-after --output after.json -- <exact command>
python3 <skill>/scripts/capture_command.py --label broader-tests --output broader.json -- <relevant suite>
```

## Classification

Use only:

- `REPRODUCED`: the targeted before record fails for the confirmed symptom.
- `NOT_REPRODUCED`: the proposed reproducer passes before a fix.
- `NO_BUG_PROVEN`: investigation produced no credible failing case.
- `INCONCLUSIVE`: setup, environment, nondeterminism, command mismatch, or symptom ambiguity blocks a conclusion.
- `STILL_FAILING`: the same targeted command still fails after the attempted fix.
- `FIX_UNVERIFIED`: targeted evidence turns green but captured broader evidence is absent.
- `FIX_REGRESSION`: targeted evidence turns green but a captured relevant broader check fails.
- `FIX_PROVEN`: the same command hash turns red to green, symptom match is confirmed, and all captured relevant broader checks pass.

Do not accept a prose or CLI flag such as `full suite passed` as a substitute for captured check records.

```bash
python3 <skill>/scripts/classify_evidence.py \
  before.json after.json result.json \
  --symptom-match confirmed \
  --broader broader.json \
  --route-state unavailable \
  --route-detail "no routed executor used"
```

## Route evidence

Record exactly one state:

- `route accepted`: route controls were accepted, but effective runtime identity is not proven;
- `used and confirmed`: host metadata confirms the effective runtime or route;
- `unavailable`: routing failed, is absent, or was not relevant; include a reason.

Never promote `route accepted` to `used and confirmed` from agent prose.

## CPAT handoff

For a recurrent incident, CI/runtime defect, or device repair, create or update a `cpat` only after verification. Its `Verification` section should reference the stable evidence ID and summarize:

```text
symptom -> reproduction evidence -> root cause -> change -> scope -> red/green verification -> prevention
```

Keep raw bulky or protected output in its authoritative evidence store.

## Final report

Lead with the status and include evidence ID, targeted command identity, before/after exit codes, broader checks, Git SHAs, route state, limitations, residual risk, and `cpat_id` when present.

## Attribution

Adapted from `Kappaemme-git/codex-bug-reproducer`: minimal reproduction, honest evidence labels, same-command red-to-green proof, and structured reporting. ABVX changes replace unconditional two-gate consent with risk-based approval, remove autonomous bug hunting, require captured broader-check records, add Git/environment/command identity, preserve route states, and link recurrent lessons to `cpat`.

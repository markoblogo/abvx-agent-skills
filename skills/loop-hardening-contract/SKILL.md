---
name: loop-hardening-contract
description: Harden repeated delivery loops with evidence-based harness stripping, immutable runtime-path sprint packets, and broken-window revalidation without automatic revert. Use for Cardputer, browser, CI, runtime, or production work split into repeated sprints.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Loop Hardening Contract

Use this contract after `loop-readiness-review` when repeated delivery needs tighter execution evidence. It is a review and packet format, not a runner or scheduler.

## 1. Harness Stripping

Remove harness complexity only through an isolated, one-component experiment:

1. Record the component, its intended failure mode, and its operating cost.
2. Capture a representative baseline for completion, verification, cost, and failures.
3. Disable exactly one non-safety component between runs, never during a live run.
4. Repeat the same bounded case and classify `REMOVE`, `RESTORE`, `HARMFUL`, or `INCONCLUSIVE`.
5. Retain the evidence and human settlement decision.

Never strip sandboxing, budgets, stop conditions, human gates, root verification, or protected-data boundaries.

## 2. Runtime-Path Sprint Packet

Freeze this packet before execution:

- `sprint_id` and version;
- one concrete deliverable;
- 3–7 observable acceptance predicates;
- the actual runtime path to exercise;
- explicit out-of-scope items;
- owned files or write boundary;
- stop conditions and budget;
- verification commands, device/browser steps, and expected evidence.

The executor cannot accept its own result. A mid-run requirement change creates a new packet version with a reason and explicit human confirmation.

## 3. Broken-Window Revalidation

Before a new sprint, re-run the latest accepted result through its real runtime path:

- `STILL_GREEN`: the accepted predicates still pass;
- `REOPENED`: a previously accepted predicate now fails;
- `INCONCLUSIVE`: the required runtime or evidence is unavailable.

On `REOPENED`, stop new work, retain the evidence, reopen the result, and propose a bounded repair. Do not auto-revert. A revert may erase useful subsequent work or hide the causal change and therefore requires an inspected, human-approved settlement.

Compilation is not Cardputer device proof. Unit tests are not browser or production proof when the accepted claim names those runtime paths.

## Output

Return:

- sprint packet version;
- revalidation status and evidence;
- harness experiment and classification, if any;
- root verification result;
- settlement: `accept`, `revise`, `repair`, `restore`, or `inconclusive`;
- remaining risks.

## Guardrails

- Keep the contract opt-in and bounded; do not install Loopkit or add scheduling.
- Do not auto-revert, auto-commit, auto-merge, deploy, release, or publish.
- Do not use source inspection as runtime-path evidence.
- Root verifies integration; executor prose is evidence, not acceptance.
- Prefer a one-shot checklist when the work is not genuinely repeated.

## Pair With

- `loop-readiness-review` for readiness level, state, isolation, and human gates.
- `bounded-evaluation` for representative fixtures and comparison rubrics.
- `bug-evidence-protocol` for captured red-to-green command evidence.
- `git-native-context-contract` `cpat` records for recurring failure prevention.
- `bounded-orchestration-contract` when execution is delegated across disjoint file scopes.

## Provenance

Adapted from `Archive228/loopkit` sprint, broken-window, and harness-evolution ideas. The ABVX version removes the autonomous runner, transcript scraping, self-declared completion, automatic rollback, broad installation, and unpinned runtime dependencies.

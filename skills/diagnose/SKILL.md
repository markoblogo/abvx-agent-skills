---
name: diagnose
description: Debug coding failures through reproduction, ranked hypotheses, narrow fixes, and verification. Use when a bug, regression, flaky test, performance failure, or inconsistent behavior is broken, slow, throwing, or hard to reproduce and the task needs disciplined diagnosis instead of guessed fixes.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Diagnose

The core job is to build a reliable feedback loop. Without one, hypotheses are weak.

## Phase 1: Feedback Loop

Create the smallest useful pass/fail signal:

- failing test;
- CLI command with fixture;
- HTTP request against local server;
- browser script;
- replayed trace or payload;
- small harness around the relevant function;
- repeated flake trigger with counted failure rate.

If no loop can be built, state what was tried and ask for logs, traces, access, or permission to instrument.

## Phase 2: Reproduce

Confirm the loop matches the user's symptom, not a nearby failure. Capture exact error text, wrong output, timing, network failure, or UI state.

For nondeterministic issues, raise the reproduction rate with repetition, stress, seeded randomness, timing controls, and isolation.

## Phase 3: Hypothesize

Write 3-5 ranked hypotheses before editing. Each must include:

```text
Hypothesis:
Prediction:
Probe:
Result:
Status:
```

Test one variable at a time. Update rankings as evidence arrives.

## Phase 4: Instrument

- Prefer debugger, REPL, targeted logs, traces, or profiler over broad logging.
- Tag temporary instrumentation with a unique marker such as `[DEBUG-7b3c]`.
- Remove all temporary instrumentation before finalizing.
- For performance regressions, measure first and fix second.

## Phase 5: Fix And Regression Test

If a correct seam exists, turn the minimized repro into a failing regression check before the fix. If no correct seam exists, document that as an architecture gap.

Apply the smallest fix supported by evidence, then rerun:

- the regression check;
- the original feedback loop;
- relevant project checks.

## Final Report

Include root cause, winning hypothesis, files changed, verification, debug cleanup, and residual risk.

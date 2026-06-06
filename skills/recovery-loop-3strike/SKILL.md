---
name: recovery-loop-3strike
description: "Recover from failed execution or verification with a bounded three-step loop: retry, focused fix-spec, then honest handoff. Use when an agent is likely to spin on the same failure, when flaky environment issues blur the signal, or when you need a disciplined stop condition instead of endless optimistic retries."
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Recovery Loop 3-Strike

Bound retries so failure handling becomes diagnostic instead of repetitive.

## Use When

- a verification step fails and the cause is not yet clear;
- the task is long enough that repeated blind retries are likely;
- you need an explicit escalation path for autonomous or semi-autonomous work.

## Core Rules

- Failure one is for learning, not denial.
- Each retry must add new evidence or a narrower hypothesis.
- After two failed passes, stop improvising and write a focused fix plan.
- After the third failure, hand off honestly instead of pretending the loop is still productive.

## Workflow

1. First failure:
   - capture the exact failing signal;
   - state the most likely cause;
   - retry once with one concrete probe or adjustment.
2. Second failure:
   - write a compact fix spec for the same phase or task slice;
   - constrain the change to the verified failure mode;
   - execute the fix and re-run verification.
3. Third failure:
   - stop;
   - mark the task or phase blocked;
   - hand off with probe history, attempted fixes, and best next action.

## Required Failure Record

For each strike, preserve:

- failing command or acceptance criterion;
- observed output or symptom;
- hypothesis tested;
- action taken;
- result.

## Anti-Patterns

- Do not spend all three strikes on the same unmodified action.
- Do not escalate to a large rewrite unless the evidence points there.
- Do not hide a blocker behind optimistic language.

## Final Report

State which strike resolved the issue, or provide a clean blocked handoff with evidence.

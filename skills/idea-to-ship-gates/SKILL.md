---
name: idea-to-ship-gates
description: "Route an idea, vague feature request, or agent-built product change through delivery gates from intent to release. Use when work needs more discipline than a readiness check: clarify the spec, slice the work, protect architecture boundaries, gather proof, converge through review, and prepare release without turning the task into a heavyweight process."
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Idea To Ship Gates

Turn a vague idea into a shipped, reviewable slice. Use this as a router over existing skills, not as a replacement for implementation judgment.

## Core Principle

Readiness loops make a repo interpretable. Delivery loops make a change shippable.

The minimum useful delivery path is:

```text
intent -> spec -> slices -> proof -> review -> release
```

Advance only when the current gate has enough evidence for the next one.

## Gate Router

Start at the first missing gate:

1. **Intent gate**: clarify the user-visible outcome, non-goals, constraints, and risk level.
2. **Spec gate**: produce a small spec or PRD only when the idea is still ambiguous.
3. **Slice gate**: split work into thin end-to-end slices with acceptance criteria.
4. **Architecture gate**: check boundaries, data flow, ownership, and blast radius before broad edits.
5. **Execution gate**: implement the current slice with the narrowest useful verification loop.
6. **Proof gate**: collect commands, screenshots, artifacts, or review notes that show the slice works.
7. **Convergence gate**: review the diff, remove accidental scope, fix blockers, and repeat only on concrete findings.
8. **Release gate**: prepare changelog, version, deployment, or PR handoff only after proof survives review.

## Skill Routing

- Use `rapid-grilling` or `doc-grounded-grilling` for the intent gate.
- Use `spec-to-prd` when the spec is not yet durable enough.
- Use `plan-to-issues` for slice planning.
- Use `architecture-deepening-review` or `system-zoom-out` for architecture risk.
- Use `delivery-preflight-gate` before long or risky execution.
- Use `test-driven-execution`, `minimal-diff-builder`, or `phase-spec-execution` during implementation.
- Use `browser-verification`, `web-quality-audit`, or repo-specific checks for proof.
- Use `overengineering-review`, `delivery-baseline-audit`, and `recovery-loop-3strike` for convergence.
- Use `agent-learning-layer-triage` after repeated failures or reusable delivery lessons.

## Convergence Loop

Repeat this loop until the release gate passes or a blocker is honest:

1. State the current gate and acceptance criteria.
2. Do only the work needed for that gate.
3. Run the smallest proof command or inspection that can falsify success.
4. Classify the result:
   - `advance`: proof is sufficient for the next gate;
   - `repair`: one concrete blocker remains inside the current gate;
   - `reslice`: the slice is too large or crosses too many boundaries;
   - `handoff`: progress now needs user input, missing access, or a product decision.
5. Remove accidental scope before advancing.

## Guardrails

- Do not create process artifacts for tiny edits.
- Do not skip from idea to implementation when acceptance criteria are unclear.
- Do not turn release prep into proof; release notes are not verification.
- Do not keep looping on taste, preference, or ambiguous product calls without user input.
- Do not install external skill packs just because one pattern is useful; extract the smallest reusable gate.

## Final Report

Report the gates completed, evidence collected, gates intentionally skipped, and the next release or handoff action.

---
name: pipeline-readiness-gate
description: Choose and run a compact pre-implementation, post-implementation, or ship-readiness gate for agent work. Use when a task needs ordered review lenses, proof gates, or release confidence without adopting a heavy multi-agent pipeline runtime.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Pipeline Readiness Gate

Apply a small ordered gate instead of a large multi-agent runtime.

## Use When

- a plan needs review before implementation;
- an implementation needs validation before the next phase;
- a branch or artifact needs a ship gate;
- SET or another orchestrator provides a handoff bundle with recommended review lenses.

## Gate Modes

### Pre-Implementation

Use before code changes:

1. `doc-grounded-grilling` when requirements are unclear.
2. `assumption-excavation` on the plan/spec/bundle.
3. `architecture-deepening-review` for structural fit when architecture is affected.
4. Proceed only when critical assumptions and architecture risks are surfaced.

### Post-Implementation

Use after a phase:

1. Run the repo's narrow verification commands.
2. Use `minimal-diff-builder` or `overengineering-review` for scope drift.
3. Use `test-driven-execution` or test review when behavior changed.
4. Use `delivery-baseline-audit` against declared deliverables.

### Ship

Use before publication, PR merge, release, or public docs update:

1. Run `delivery-preflight-gate` push-gate mode when remote publication is in scope.
2. Run `confidence-fragility-review` on claims and release notes.
3. Run `authorized-security-router` first for security-sensitive surfaces.
4. Finish with `delivery-baseline-audit`.

## Output Shape

Include:

- selected gate mode;
- lenses used or skipped;
- verification commands;
- blockers;
- `PROCEED`, `REVISE`, or `HOLD` decision.

## Guardrails

- Do not invent a pipeline engine.
- Do not run every skill when one gate answers the question.
- Do not block implementation on low-risk advisory findings.
- Keep runtime state in the external harness, not in this skill.

## Provenance

Adapted from the `pre-implementation`, `post-implementation`, and `ship` pipeline ordering in `aself101/agents-and-pipelines`, narrowed for ABVX skill orchestration.

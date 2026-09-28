---
name: test-driven-execution
description: Execute feature work and bug fixes with a tracer-bullet red-green-refactor loop. Use when building behavior that should be guided by tests, when fixing regressions, or when the user wants TDD or test-first execution. Prefer public interfaces, vertical slices, and behavior-focused tests that survive refactors.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Test Driven Execution

Use tests as the feedback loop that shapes the implementation one vertical slice at a time.

## Core Rules

- Test behavior through public interfaces.
- Prefer integration-style tests over implementation-coupled tests.
- Work in vertical slices, not horizontal batches.
- One failing test -> one minimal implementation -> repeat.
- Refactor only while green.

## Workflow

1. Confirm the behavior to build or fix.
2. Inspect the repo, branch, and existing worktree changes; identify the highest useful seam to test. Isolate only when work overlaps or runs concurrently, and preserve pre-existing changes.
3. Write one failing test for one observable behavior.
4. Implement the minimum code to make it pass.
5. Repeat for the next behavior.
6. Refactor only after the slice is green.

## Evidence and handoff

- Use the narrowest check that proves the changed behavior, then run relevant broader checks. A green test proves only the behavior and environment it exercised.
- For visually material UI changes, compare the same important viewport and state before and after when feasible; do not require screenshots for non-visual changes.
- Report local tests, CI, deployment, and public release as separate gates. Do not claim a later gate from an earlier one.
- Completion means verified work and an honest handoff; commit, push, PR creation, and deployment still require task authorization.

For a diagnosed regression that needs durable proof, capture the exact same targeted command before and after with `bug-evidence-protocol`, then capture relevant broader checks. Do not infer `FIX_PROVEN` from a green targeted test alone.

## Anti-Pattern

Do not write all tests first and all code later. That produces test suites for imagined behavior instead of validated behavior.

## Good Tests

- name the user-visible behavior;
- survive internal refactors;
- avoid private methods and internal collaborator trivia;
- verify what the system does, not how it does it.

## Planning Questions

- Which behaviors matter most?
- Which seams already exist?
- What should not be tested at this layer?
- What prior art already exists in the repo?

## Final Report

Include the behaviors covered, the seams used, what remains untested, and any refactor opportunities exposed by the loop.

## Attribution

The scoped isolate/prove/ship and visual before/after evidence ideas were informed by [michaelshimeles/skills](https://github.com/michaelshimeles/skills); this skill retains ABVX's behavior-first testing and authorization boundaries.

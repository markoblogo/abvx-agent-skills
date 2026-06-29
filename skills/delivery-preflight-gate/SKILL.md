---
name: delivery-preflight-gate
description: Run a baseline preflight before long implementation, autonomous execution, or publishing a PR. Use when a task has multiple phases, mandatory commands, high risk of thrashing against an already-broken repo state, or should be checked in an isolated push gate before reaching the real remote. Deduplicate the minimum useful checks, surface red baseline conditions early, and require an explicit user decision before proceeding past known breakage.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Delivery Preflight Gate

Run the smallest useful baseline check before committing the agent to a long implementation loop or before letting a risky branch leave the local workspace.

## Use When

- the task is expected to take multiple implementation steps or phases;
- the repo already has build, test, typecheck, lint, or app-run expectations;
- a broken baseline would waste retries or mislead later verification;
- the user is about to ask for an autonomous or low-supervision run;
- a branch should pass a disposable push gate before opening or updating a PR.

For security-sensitive work, run `authorized-security-router` first when authorization, target boundary, or allowed action level is not already explicit.

## Core Rules

- Deduplicate checks. Do not run the same command under different names.
- Prefer the narrowest commands that still represent the real baseline.
- Verify before planning a large execution loop, not after failure number three.
- Distinguish `baseline already broken` from `task introduced a regression`.
- If the baseline is red, stop and present options instead of silently proceeding.
- For push-gate workflows, isolate review and repair work from the main working tree when the tooling supports it.

## Workflow

1. Identify the mandatory verification surface for this repo.
2. Select the minimum command set that represents that surface.
3. Run the commands once before starting the long task or before publishing the branch.
4. Classify the result:
   - `PREFLIGHT_GREEN`: baseline acceptable for execution.
   - `PREFLIGHT_RED`: baseline broken, flaky, or unverifiable.
   - `PUSH_GATE_GREEN`: branch is clean enough to push or open/update a PR.
   - `PUSH_GATE_RED`: branch needs a fix, explicit override, or smaller PR slice before publishing.
5. If red, report:
   - which commands failed;
   - whether the failure appears pre-existing or task-related;
   - whether it blocks the planned work or is exactly what phase 1 must fix.
6. Require an explicit proceed-or-fix decision before treating the task as safe for autonomous execution or remote publication.

## Optional Push Gate Mode

Use this mode when the risk is not only broken code, but publishing a noisy or unsafe PR branch.

1. Confirm the intended remote and target branch.
2. Create or use an isolated disposable worktree when available.
3. Re-run only the minimum repo checks that matter for the PR.
4. Run a focused review pass for accidental broad diffs, generated clutter, secrets, debug prints, and stale docs.
5. Apply only safe, reviewable auto-fixes; require approval for behavior changes or broad cleanup.
6. Push only after the branch is green, explicitly overridden, or deliberately narrowed.

This mode is compatible with tools such as `no-mistakes`, but does not require any specific gate implementation. Treat external tools as adapters around the same decision record.

## Output Shape

Produce a compact preflight record with:

- selected commands;
- pass/fail summary;
- blockers;
- proceed recommendation;
- push-gate decision when remote publication is in scope.

## Anti-Patterns

- Do not run a giant CI matrix when one local command answers the question.
- Do not hide a broken baseline inside a long plan.
- Do not call a repo "verified" if the necessary commands were skipped.
- Do not let auto-fixes from a push gate silently expand the PR scope.
- Do not replace human approval with a gate when the change touches secrets, auth, billing, destructive actions, or broad behavior.

## Final Report

State whether the execution loop started from green baseline, red baseline with explicit override, unverifiable baseline, or push-gate pass/fail before publication.

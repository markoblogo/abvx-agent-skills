---
name: delivery-preflight-gate
description: Run a baseline preflight before long implementation or autonomous execution. Use when a task has multiple phases, mandatory commands, or high risk of thrashing against an already-broken repo state. Deduplicate the minimum useful checks, surface red baseline conditions early, and require an explicit user decision before proceeding past known breakage.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Delivery Preflight Gate

Run the smallest useful baseline check before committing the agent to a long implementation loop.

## Use When

- the task is expected to take multiple implementation steps or phases;
- the repo already has build, test, typecheck, lint, or app-run expectations;
- a broken baseline would waste retries or mislead later verification;
- the user is about to ask for an autonomous or low-supervision run.

For security-sensitive work, run `authorized-security-router` first when authorization, target boundary, or allowed action level is not already explicit.

## Core Rules

- Deduplicate checks. Do not run the same command under different names.
- Prefer the narrowest commands that still represent the real baseline.
- Verify before planning a large execution loop, not after failure number three.
- Distinguish `baseline already broken` from `task introduced a regression`.
- If the baseline is red, stop and present options instead of silently proceeding.

## Workflow

1. Identify the mandatory verification surface for this repo.
2. Select the minimum command set that represents that surface.
3. Run the commands once before starting the long task.
4. Classify the result:
   - `PREFLIGHT_GREEN`: baseline acceptable for execution.
   - `PREFLIGHT_RED`: baseline broken, flaky, or unverifiable.
5. If red, report:
   - which commands failed;
   - whether the failure appears pre-existing or task-related;
   - whether it blocks the planned work or is exactly what phase 1 must fix.
6. Require an explicit proceed-or-fix decision before treating the task as safe for autonomous execution.

## Output Shape

Produce a compact preflight record with:

- selected commands;
- pass/fail summary;
- blockers;
- proceed recommendation.

## Anti-Patterns

- Do not run a giant CI matrix when one local command answers the question.
- Do not hide a broken baseline inside a long plan.
- Do not call a repo "verified" if the necessary commands were skipped.

## Final Report

State whether the execution loop started from green baseline, red baseline with explicit override, or unverifiable baseline.

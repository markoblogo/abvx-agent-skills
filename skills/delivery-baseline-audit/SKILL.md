---
name: delivery-baseline-audit
description: Audit claimed delivery against the starting baseline and the current working tree. Use when a task has declared deliverables, when a long run might say 'done' before shipping real changes, or when final verification must check the actual artifact set rather than only the transcript or commits.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Delivery Baseline Audit

Verify that the promised deliverables actually exist relative to where the work started.

## Use When

- the task names files, features, screens, commands, or other concrete deliverables;
- the implementation ran through multiple phases or retries;
- the working tree may contain staged, unstaged, or untracked work that matters;
- "agent said done" is not enough evidence.

## Core Rules

- Compare against the starting baseline, not just the latest transcript claim.
- Check the whole working tree, not only committed diffs.
- Re-run final mandatory commands once at the end for cross-phase regressions.
- Treat missing deliverables as a gap even if the narrative sounds complete.

## Workflow

1. Capture or identify the baseline reference before major work starts.
2. List the declared deliverables and acceptance criteria.
3. At the end, inspect the full working tree relative to that baseline:
   - committed changes;
   - staged changes;
   - unstaged changes;
   - deletions;
   - untracked deliverables.
4. Re-run the final mandatory verification commands.
5. Spot-check each deliverable against its declared acceptance criteria.
6. Report gaps explicitly and fix them before calling the task complete.

## Audit Output

Include:

- baseline reference used;
- deliverables checked;
- commands re-run;
- gaps found;
- fix-needed or complete verdict.

## Anti-Patterns

- Do not audit only what was committed if the working tree still matters.
- Do not rely on a prior mid-task pass as the final audit.
- Do not mark complete when a declared deliverable is absent or unverifiable.

## Final Report

State whether completion was confirmed against baseline, partially confirmed, or blocked by missing evidence.

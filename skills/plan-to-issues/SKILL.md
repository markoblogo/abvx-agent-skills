---
name: plan-to-issues
description: Break a PRD, plan, or spec into independently executable vertical slices. Use when a product artifact needs to become agent-ready or human-ready implementation tickets, especially for client, product, and multi-track project workflows. Prefer thin end-to-end slices, explicit blockers, and issue-tracker-neutral output.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Plan To Issues

Turn a plan into vertical slices that can actually be picked up and shipped.

## Workflow

1. Gather the parent artifact: PRD, plan, or spec.
2. Explore the repo only enough to understand the real seams.
3. Break the work into thin vertical slices:
   - end-to-end;
   - verifiable on their own;
   - blocker-aware;
   - small enough to review.
4. Classify slices:
   - agent-ready;
   - human-required;
   - blocked by decision or external dependency.
5. Show the proposed breakdown and adjust granularity before publishing or writing it down.

## Slice Rules

- Prefer many thin slices over a few thick ones.
- Each slice should cut through the relevant layers, not isolate one layer.
- A completed slice should be demoable, testable, or reviewable on its own.

## Output

For each slice include:

- title;
- type;
- what to build;
- acceptance criteria;
- blockers;
- parent reference when relevant.

## Rules

- Do not output horizontal slices like "DB layer", "API layer", "UI layer" unless the parent work truly is infrastructure-only.
- Keep issue-tracker-neutral language; publish to a tracker only if the workflow calls for it.
- If the plan is still fuzzy, route back to `spec-to-prd` or grilling first.

## Final Report

Summarize the slice graph, identify the first executable slice, and note what still needs a human decision.

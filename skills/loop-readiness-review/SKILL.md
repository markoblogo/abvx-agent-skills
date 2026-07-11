---
name: loop-readiness-review
description: Review whether a recurring or semi-autonomous agent loop is ready to run. Use before scheduling Codex, Claude Code, Grok, Opencode, CI, issue triage, PR babysitting, dependency sweeping, changelog drafting, or other repeated agent workflows.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Loop Readiness Review

Use this skill before turning repeated agent work into a scheduled or recurring loop.

## Use When

- a workflow may run on a cadence: cron, automation, `/loop`, GitHub Actions, or external scheduler;
- a runner will open worktrees, inspect CI, triage issues, update changelogs, watch PRs, or sweep dependencies;
- a SET bundle is being handed to a loop-capable orchestrator;
- a report-only loop is being promoted toward auto-fix or PR creation;
- you need to decide whether the loop is L0, L1, L2, or L3 ready.

## Readiness Levels

- `L0`: not loop-ready; missing state, verifier, or human gate.
- `L1`: report-only; can read, summarize, and propose actions.
- `L2`: proposal-first; can create retained output, worktree changes, or draft PRs behind review gates.
- `L3`: governed loop; has state, isolation, verifier, budget, run log, rollback/escalation, and human-controlled settlement.

## Readiness Checks

Review:

- cadence: trigger, frequency, quiet hours, stop rule;
- state: `STATE.md`, run ledger, or other durable memory outside the model;
- scope: allowed repos, paths, issues, branches, and denied targets;
- isolation: worktree, branch, sandbox, or retained-output directory;
- skills: triage, implementer, verifier, review lenses, and escalation roles;
- connectors: MCP, GitHub, CI, email, calendar, or other external tools with least privilege;
- verifier: deterministic checks, bounded eval, CI, human review, or maker/checker split;
- budget: token, time, run count, retry, and spend caps;
- run log: what happened, what changed, what failed, and why it stopped;
- human gate: approval boundary for writes, merges, releases, destructive actions, or external side effects;
- rollback: how to discard, revert, close, or pause the loop.

## Workflow

1. Identify the loop pattern and intended cadence.
2. Classify the current readiness level.
3. Check the readiness dimensions above.
4. List blockers that prevent promotion to the next level.
5. Recommend the smallest next step:
   - keep report-only;
   - add state file or run log;
   - add verifier;
   - add worktree isolation;
   - add budget caps;
   - add human gate;
   - stop or de-schedule the loop.

## Output Shape

Use:

- loop name or pattern;
- current level: `L0`, `L1`, `L2`, or `L3`;
- intended next level;
- checks passed;
- blockers;
- budget and stop rules;
- human gate;
- smallest next step;
- decision: `not-ready`, `report-only`, `proposal-first`, or `governed`.

## Guardrails

- Do not recommend auto-fix, auto-merge, production deploy, release, or destructive actions without an explicit human gate.
- Do not promote a loop beyond report-only without durable state and a run log.
- Do not promote beyond proposal-first without verifier evidence and rollback or discard path.
- Do not let the loop judge its own safety claims.
- Do not add scheduling when a one-shot task or manual checklist is enough.

## Pair With

- `context-degradation-review` before long loop handoffs or memory-heavy runs.
- `filesystem-context-discipline` for `STATE.md`, run logs, retained outputs, and proposal folders.
- `bounded-evaluation` for verifier and maker/checker gates.
- `reversible-agent-task` for proposal-first worktree or retained-output settlement.
- `agent-tool-contract-review` for MCP, CLI, and GitHub Action inputs used by the loop.

## Provenance

Adapted from loop readiness and loop engineering patterns in `cobusgreyling/loop-engineering`, narrowed into an ABVX review skill rather than a loop runtime.

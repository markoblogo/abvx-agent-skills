---
name: loop-run-contract
description: Draft and review a narrow L1 report-only or L2 proposal-first loop run contract with explicit state, budget, verifier, escalation, and stop conditions. Use before enabling repeated agent work for one project or workflow.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Loop Run Contract

Define one bounded loop packet before a runner repeats work. This skill specifies the work; it does not schedule it, spawn agents, grant tool access, or execute actions.

## Use when

- a project is considering recurring triage, evaluation, cleanup, or review work;
- a shadow workflow needs a stable run record and a safe stopping rule;
- a report-only loop may later become a proposal-first assisted loop;
- the operator can name the goal, watched scope, owner, escalation path, and budget.

## Select the level

| Level | Authority | Required boundary |
|---|---|---|
| `L1` | report-only | no writes, merges, releases, publishing, or external side effects |
| `L2` | proposal-first assisted | retained output or isolated branch/worktree/sandbox; separate verifier; human approval before any side effect |

Start at L1. Do not promote because a loop ran without errors; promote only after reviewed evidence shows useful findings, bounded cost, correct abstention, and no unsafe action attempts.

## Build the packet

1. State one goal, explicit non-goals, watched sources, cadence/event, and owner.
2. Declare authority and denied actions. Empty/no-action work exits early.
3. Define durable state and an append-only run log; never use chat history as the sole state.
4. Set max items, tool calls, retries, elapsed time, and token/spend budget.
5. Name stop, pause, and escalation triggers: ambiguity, missing evidence, budget breach, repeated failure, protected-data boundary, or any requested external effect.
6. For L2, isolate proposals and require a maker-checker verifier. Record verifier evidence and discard/rollback notes before human approval.

## Packet format

```yaml
version: 1
scope:
  project: owner/repository
  workflow: daily-triage
  level: L1
  enabled: false
goal: "Produce a bounded, evidence-linked report of actionable CI failures."
non_goals: [fix CI, open PRs, notify external systems]
state: {location: docs/ai/loop-state.json, durable: true}
run_log: {location: docs/ai/loop-runs.jsonl, append_only: true}
limits: {max_items: 10, max_tool_calls: 8, max_retries_per_item: 1, max_elapsed_minutes: 12}
stops: [empty-watchlist, budget-exceeded, ambiguous-evidence, repeated-failure]
escalate_on: [protected-data, requested-side-effect, missing-verifier]
L2_only:
  isolation: retained-output
  verifier: named-check
  approval_before: [write, merge, release, external-side-effect]
```

## Output contract

Return:

```text
Level and authority:
Goal / non-goals / watched scope:
State and append-only run log:
Budget and early-exit rule:
Stop, pause, and escalation triggers:
L2 verifier + isolation + discard/rollback notes (if applicable):
Rollout decision: disabled | L1 shadow/report | reviewed L2
```

## Non-goals

- Do not create a global scheduler, observer, session hook, or agent runtime.
- Do not infer permissions from a cadence or from prior successful runs.
- Do not allow a maker to self-certify a proposal at L2.
- Do not make L3/unattended operation part of this skill; it requires a separate governed runtime review.

## Attribution

Adapted from the L1/L2 readiness and safety discipline in [loop-engineering](https://github.com/cobusgreyling/loop-engineering), narrowed to ABVX proposal-first contracts.

---
name: repo-issue-triage
description: Triage bugs, enhancements, and backlog items through a small state machine that works with or without a formal issue tracker. Use when reviewing incoming requests, preparing work for an agent, deciding whether more info is needed, or keeping a multi-project backlog healthy.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Repo Issue Triage

Keep issues and backlog items moving through a small, explicit state machine.

## Roles

Category:

- `bug`
- `enhancement`

State:

- `needs-triage`
- `needs-info`
- `ready-for-agent`
- `ready-for-human`
- `wontfix`

Security-sensitive reports should first pass through `authorized-security-router` when scope, authorization, exploitability, or allowed verification level is unclear.

## Workflow

1. Read the full issue or request, including prior notes.
2. Inspect only the relevant code and docs.
3. Recommend category and state with reasoning.
4. For bugs, attempt a minimal reproduction before asking for more info.
5. If the request is underspecified, use grilling to close the gaps.
6. Apply the outcome in the tracker or in a local markdown backlog.

## Good Triage Notes

Capture:

- what is already established;
- what is still unclear;
- why the item is or is not ready for an agent;
- what exact human judgment is still needed.

## Rules

- Every item should end up with one category and one state.
- Do not ask for vague "more info"; ask for specific missing evidence.
- For `wontfix`, record the reason clearly enough that the same request is not rediscovered next week.
- Keep the system output-neutral: GitHub issue, Linear ticket, markdown backlog, or internal tracker.

## Final Report

State the category, the state, the reasoning, and the next actor: reporter, human maintainer, or agent.

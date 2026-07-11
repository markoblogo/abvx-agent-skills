---
name: context-degradation-review
description: Review agent work for context poisoning, lost-in-the-middle failures, distraction, context clash, and stale carryover. Use before long-session handoffs, SET runner handoffs, skill changes, memory writes, or any task where too much or conflicting context may degrade behavior.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Context Degradation Review

Use this skill to find when the context itself is making the agent worse.

## Use When

- a long session, handoff, or compaction summary may contain stale or conflicting instructions;
- a SET bundle, AGENTS.md, SKILL.md, or memory write mixes useful facts with outdated task history;
- the agent keeps optimizing for irrelevant prior work;
- tool output, logs, or retrieved docs may bury the decisive evidence;
- multiple sources disagree and the answer treats them as one coherent contract.

## Failure Modes

- `lost-in-middle`: key constraints are present but buried between low-signal material.
- `context-poisoning`: incorrect, stale, or speculative text is treated as authority.
- `distraction`: large but irrelevant context pulls work away from the current task.
- `context-clash`: two instructions, docs, memories, or artifacts conflict.
- `stale-carryover`: a prior goal continues after the user changed or stopped the task.

## Workflow

1. Identify the active task, current authority order, and expected output.
2. List the context sources used: user message, repo files, memory, docs, tool output, web sources, generated summaries.
3. Mark each source as `authoritative`, `supporting`, `stale-risk`, or `irrelevant`.
4. Check for the five failure modes above.
5. Propose the smallest context repair:
   - remove or ignore a stale source;
   - promote the decisive constraint near the active plan;
   - split task history from durable guidance;
   - ask for clarification only when the conflict blocks action;
   - rewrite a handoff or memory proposal with source boundaries.
6. Continue only after the active context is narrow enough to act safely.

## Output Shape

Use:

- verdict: `CONTEXT_OK`, `CONTEXT_DEGRADED`, or `CONTEXT_BLOCKED`;
- active task;
- context sources reviewed;
- degradation findings by mode;
- smallest repair;
- remaining risk.

## Guardrails

- Do not use this as a generic writing critique.
- Do not remove context just because it is long; remove or demote it only when it is low-signal, stale, or conflicting.
- Do not treat memory as higher authority than the current user message.
- Do not let stale rollout context override an explicit stop, pause, or changed task.

## Provenance

Adapted from context degradation patterns in `muratcankoylan/Agent-Skills-for-Context-Engineering`, narrowed into an ABVX review lens.

---
name: durable-context-maintenance
description: Keep repo-local agent context accurate after code and workflow changes. Use when docs/ai, AGENTS.md, runbooks, or context entrypoints have drifted from the codebase, after major feature work, after architecture changes, or when an agent keeps rediscovering the same repo facts. Refresh durable context, split groups only when needed, and preserve compact read order.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Durable Context Maintenance

Durable context should evolve with the repo. Otherwise every session pays for stale or missing knowledge.

## Goal

Keep repo-local context accurate, compact, and routable after the codebase changes.

## What Counts As Durable Context

- repo architecture summaries;
- test and verification docs;
- deployment or infrastructure flow notes;
- context entrypoints under `docs/ai/`, `process/context/`, or equivalent;
- startup guidance in `AGENTS.md` when it describes stable repo behavior.

If durable context is becoming too expensive to resend but still needs repeated factual recall, use `doc-to-lora-evaluator` to decide whether parametric document memory is worth testing instead of simply adding more startup prose.

## Maintenance Workflow

1. Read the current context entrypoints first.
2. Inspect the code or workflow changes that may have invalidated them.
3. Classify each affected doc:
   - still accurate;
   - stale;
   - missing a new topic;
   - too large and should split;
   - duplicated elsewhere.
4. Update only the owning durable docs.
5. If discovery paths changed, update the top-level routing file too.
6. Validate that the revised read order is still small and obvious.

## Update Triggers

Refresh durable context when:

- architecture or module boundaries changed;
- test commands or environments changed;
- a new durable workflow appeared;
- agents repeatedly rediscover the same repo facts;
- a compact startup file points to stale or renamed docs.

## Splitting Rules

- Split a topic when it becomes too large or multiple sessions need only one slice.
- Do not split just to look organized.
- Keep one clear entrypoint per group with:
  - scope;
  - read-when rules;
  - source paths;
  - update triggers.

## Guardrails

- Do not turn task history into durable context.
- Do not duplicate code comments, README text, and `docs/ai/` prose unless the duplication serves routing.
- Do not preserve stale guidance just because it reads well.
- After context-organization changes, mention what should be read first next time.

## Final Report

Include what changed in the repo, which context docs were refreshed, what stayed stable, and the new preferred read order.

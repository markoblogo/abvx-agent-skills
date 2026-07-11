---
name: filesystem-context-discipline
description: Use files as durable context without polluting the live prompt. Apply when a task needs scratchpads, plan persistence, retained outputs, proposal folders, handoffs, or repo-local context that agents can discover and audit later.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Filesystem Context Discipline

Use the filesystem to hold durable state, but keep it structured, discoverable, and reviewable.

## Use When

- a task is too long for one prompt or needs resumable state;
- generated output should be retained before apply;
- a plan, checklist, evidence ledger, or handoff must survive compaction;
- multiple agents or sessions need a shared artifact;
- repo-local context should be discoverable without always loading it.

## Context Types

- `scratchpad`: temporary reasoning support, not authoritative.
- `plan`: current intended steps, assumptions, and done criteria.
- `evidence`: commands, test results, source links, or reviewed facts.
- `retained_output`: proposal artifacts kept separate from the target workspace.
- `handoff`: compact continuation state for another session or agent.
- `durable_doc`: stable repo guidance that future agents should read on demand.

## Workflow

1. Choose the file type before writing.
2. Put the artifact in the narrowest sensible location:
   - repo docs for durable guidance;
   - task/proposal folder for retained output;
   - benchmark or run folder for validation evidence;
   - memory only when the user explicitly asks to preserve a cross-session lesson.
3. Add enough metadata for later discovery: task, source, status, owner, date, and apply state when relevant.
4. Keep scratchpads separate from durable docs.
5. Link retained outputs to their inspection and settlement decision.
6. Remove or ignore transient files before commit unless they are intentional artifacts.

## Output Shape

Use:

- artifact type;
- path;
- authority level: `scratch`, `proposal`, `evidence`, or `durable`;
- discovery cue;
- expiry or update trigger;
- related verification or settlement step.

## Guardrails

- Do not make every thought durable.
- Do not mix speculative scratchpad text into README, AGENTS.md, or SKILL.md.
- Do not treat retained output as applied work.
- Do not use hidden files as the only record of an important decision.
- Do not write memory unless the user explicitly asked for memory persistence.

## Provenance

Adapted from filesystem-context patterns in `muratcankoylan/Agent-Skills-for-Context-Engineering`, aligned with ABVX proposal-first and durable-context workflows.

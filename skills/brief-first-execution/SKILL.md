---
name: brief-first-execution
description: Create a single working brief before substantial implementation, audit, or migration work. Use when tasks are non-trivial, risks are real, or the session is likely to drift without one source of truth for scope, non-goals, verification, and done criteria.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
---

# Brief First Execution

Start non-trivial work with one live task brief.

## Goal

Reduce drift by creating a compact source of truth for:

- scope;
- non-goals;
- affected areas;
- risks;
- verification;
- done criteria.

## When To Use

Use for:

- multi-file implementation;
- behavior changes;
- migrations, audits, or refactors;
- long runs where context could drift;
- work with real operational or delivery risk.

Skip for:

- tiny one-file edits with obvious blast radius;
- trivial questions that do not create lasting change.

## Workflow

1. **Name the task**
   - write a short title that matches the real delivery target.
2. **Define scope**
   - describe what is in;
   - keep it concrete and delivery-shaped.
3. **Define non-goals**
   - state what this task will not do;
   - use this to stop opportunistic scope creep.
4. **List affected areas**
   - identify modules, docs, data flows, or systems likely to change.
5. **List risks**
   - focus on failure modes that matter for this task.
6. **Define verification early**
   - list the narrowest useful checks first;
   - add broader checks only where the blast radius warrants them.
7. **Define done criteria**
   - describe what must be true before closing the task.
8. **Keep the brief live**
   - update the brief when scope changes materially;
   - do not leave the brief frozen while the work mutates underneath it.

## Rules

- One task, one brief.
- Scope and non-goals should both be explicit.
- Verification belongs in the brief before heavy implementation starts.
- If the task changes enough, revise the brief rather than pretending it did not.

## Final Report

Return the brief itself and call out any unresolved scope or verification questions.

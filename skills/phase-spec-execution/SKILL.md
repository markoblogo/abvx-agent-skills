---
name: phase-spec-execution
description: Execute large tasks through explicit phases with acceptance criteria, required commands, and state updates. Use when work is too large for one implementation pass but too important to leave as a vague checklist. Keep phases falsifiable, end-to-end, and small enough that each one can be verified honestly before moving on.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Phase Spec Execution

Turn a large task into a sequence of falsifiable execution slices instead of one broad blob of work.

## Use When

- the task spans multiple files, layers, or user-visible milestones;
- there is real sequencing or dependency ordering;
- you need clearer state than "still working";
- the user wants autonomy without losing verification discipline.

## Core Rules

- Slice vertically where possible. Each phase should move observable behavior.
- Give every phase explicit acceptance criteria.
- Attach the narrowest mandatory commands that can prove the phase.
- Update state after each phase so the next pass does not rediscover context.
- Do not create more phases than the task needs.

## Phase Template

For each phase, define:

- objective;
- dependencies or prerequisites;
- files or surfaces likely to change;
- acceptance criteria;
- mandatory verification commands;
- known risks;
- handoff note if the phase cannot complete.

## Workflow

1. Identify the end state the user actually wants.
2. Break the work into the smallest useful number of ordered phases.
3. Write or state one clear objective per phase.
4. Before implementing a phase, restate its acceptance criteria.
5. Execute only the current phase.
6. Run the phase verification commands.
7. Record what changed, what passed, and what remains.
8. Only then advance to the next phase.

## State Discipline

Track at least:

- current phase;
- completed phases;
- failed checks and why;
- assumptions that changed;
- open risks for the next phase.

## Anti-Patterns

- Do not create "phase 1: backend, phase 2: frontend, phase 3: tests" by default.
- Do not advance on "looks good" when acceptance criteria are falsifiable.
- Do not let plan files become larger than the implementation itself.

## Final Report

Report completed phases, skipped phases, criteria met, criteria deferred, and any remaining integration risk.

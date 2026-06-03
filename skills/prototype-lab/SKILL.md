---
name: prototype-lab
description: Build throwaway prototypes to answer a specific product, UI, state-machine, data-model, or workflow question before committing production code. Use when the user asks to prototype, explore variants, sanity-check logic, try designs, make a playable mock, or learn quickly with code that will be deleted or absorbed.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Prototype Lab

A prototype answers one question. It is not production code with fewer tests.

## Pick The Prototype Question

Choose the branch:

- Logic prototype: state model, workflow, parser, scoring, queue, rules, or business logic.
- UI prototype: layout direction, interaction model, variants, motion, or product feel.
- Integration prototype: unknown API/tool behavior, deployment constraint, or browser capability.

If ambiguous, state the assumption and keep the artifact easy to delete.

## Rules

- Mark it as prototype/throwaway in path, UI, comments, or README.
- Use one command to run.
- Keep state in memory unless persistence is the thing being tested.
- Avoid broad abstractions, production plumbing, and hidden dependencies.
- Surface state after actions so learning is visible.
- Do not leave prototype code mixed with production code without a decision.

## UI Variant Pattern

When exploring design, create 2-4 meaningfully different variants. Let the user switch via route, query param, segmented control, or small debug toolbar. Do not make tiny color-only variations.

## Logic Pattern

When exploring state, make a terminal or local web harness that can run scripted cases and manual interactions. Print current state, event, output, and invariant violations.

## Closeout

When the prototype answers the question:

- capture the decision in an issue, ADR, notes file, commit message, or final report;
- delete the prototype or identify exactly what will be absorbed into production;
- list what remains unproven.

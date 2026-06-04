---
name: system-zoom-out
description: Go up one layer of abstraction and explain how a local piece of code fits into the larger system. Use when the current focus is too narrow, the user is unfamiliar with an area, an audit needs broader context, or a refactor should be explained through modules, seams, and callers instead of line-by-line detail.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# System Zoom Out

When local detail is crowding out system understanding, step back and draw the map.

## Output

Explain:

- the relevant modules;
- the entrypoints and callers;
- the key dependencies and boundaries;
- the domain language used in this area;
- why this local change matters to the wider system.

## Rules

- Use the repo's domain language, not generic abstractions.
- Prefer maps and relationships over line-by-line summaries.
- Name what is outside the current focus so the user sees the edge of the map.
- If the repo already has architecture docs, align with them or call out contradictions.

## Best Use Cases

- architecture audits;
- unfamiliar code areas;
- refactor proposals;
- onboarding into a subsystem;
- explaining blast radius before a change.

## Final Report

Give the map, the boundaries, and the best next file or module to inspect if the user wants to go deeper.

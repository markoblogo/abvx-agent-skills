---
name: wireframe-preflight
description: Build a low-fidelity wireframe before frontend implementation when layout, hierarchy, and flow are still unclear. Use for landing pages, editorial surfaces, partner-facing sections, and other UI work where a cheap structural pass can prevent expensive redesign loops.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
  abvx_eval_tier: structural_only
---

# Wireframe Preflight

Run one cheap structural pass before writing real frontend code.

Use this when the likely failure mode is not missing CSS polish but choosing the wrong layout, hierarchy, or flow and then burning time fixing it in implementation.

## Best Fit

- new landing pages;
- hero and first-screen redesigns;
- editorial/article/listing layouts;
- partner-facing product sections;
- pages with unclear section order or card hierarchy.

## Not The Best Fit

- narrow bug fixes;
- token or spacing corrections inside an already accepted layout;
- tasks where the user already approved a concrete visual direction and only wants implementation;
- dense application UIs that need product-task research more than layout exploration.

## Core Rule

Stay low fidelity.

Do not jump into final visual styling, animation, color systems, or polished copy. The point is to prove structure cheaply.

## Workflow

1. State the page job in one sentence:
   - what the page must make possible on first use;
   - what the primary action or understanding should be.
2. List the must-keep constraints:
   - approved copy, required sections, supplied assets, preserved routes, explicit owner limits.
3. Produce one primary wireframe approach:
   - section order;
   - content hierarchy;
   - desktop layout blocks;
   - mobile stacking behavior;
   - CTA placement;
   - where evidence, media, or proof surfaces belong.
4. Add one fallback approach only when the first real choice is ambiguous and the alternative is meaningfully different, not a cosmetic variation.
5. Call out the main risk before implementation:
   - empty hero, repeated card rhythm, weak proof placement, over-compressed mobile stack, or similar structural issue.
6. Hand off the chosen structure to implementation or to a downstream frontend skill.

## Output Shape

Return a compact wireframe package:

- `page job`
- `must keep`
- `desktop structure`
- `mobile structure`
- `primary risk`
- `implementation notes`

If the task benefits from a visual artifact, create only a simple low-fidelity sketch or static HTML wireframe. Do not turn the preflight into a design system.

## Guardrails

- Do not invent new product capabilities.
- Do not rewrite approved body copy unless the task explicitly allows it.
- Do not treat the wireframe as production proof.
- Do not create more than two approaches in one pass.
- Prefer one strong structural recommendation over a gallery of options.

## Final Report

Include:

- the chosen wireframe direction;
- the main structural risk avoided;
- whether a second approach was needed;
- the best downstream skill, such as `editorial-surface`, `corporate-surface`, `frontend-taste-layer`, or `browser-verification`.

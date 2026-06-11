---
name: frontend-taste-layer
description: Add a stronger anti-slop taste layer to frontend work. Use when the UI direction is too generic, templated, card-heavy, gradient-biased, typographically weak, or visually under-committed, especially for landing pages, portfolios, and brand-forward redesigns.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Frontend Taste Layer

Raise the taste level without turning the work into a random aesthetic stunt.

Use this after the task is understood and the surface register is known. If the project still lacks design context, start with `design-register-bootstrap`.

## Best Fit

- landing pages;
- portfolios;
- brand-forward promo pages;
- redesigns where the current UI feels boilerplate or interchangeable;
- hero sections and first-screen composition work.

## Not The Best Fit

- dense dashboards;
- table-heavy app UI;
- settings forms where utility matters more than expressive styling;
- projects that must preserve a strict existing enterprise design system.

## Design Read

Before changing code, state one sentence:

`Reading this as: <surface> for <audience>, with a <vibe> language, leaning toward <design family>.`

Do not skip this. Most generic output comes from styling before the read is explicit.

## Three Dials

Set these mentally for the pass:

- `variance`: symmetry versus surprise;
- `motion`: static versus cinematic;
- `density`: airy versus packed.

Use them to keep decisions consistent. Do not expose a pile of disconnected visual tweaks.

## Anti-Slop Rules

- Do not default to purple-blue AI gradients.
- Do not default to Inter plus slate gray plus centered hero.
- Do not solve every section with identical cards.
- Do not use decorative glass or blur everywhere.
- Do not use serif as a reflex for “premium” or “creative”.
- Do not make the page feel like a template category before it feels like this product or brand.

## Positive Moves

- Commit to a typography hierarchy with a real point of view.
- Use asymmetry when the surface benefits from it.
- Make one strong visual decision per screen: type, composition, color, or motion.
- If using motion, make it directional and purposeful, not generic reveal spam.
- Keep one palette family per page and lock the accent.
- Prefer a deliberate visual anchor over more decorative chrome.

## Brand Versus Product

- For `brand` surfaces, visual identity can lead.
- For `product` surfaces, taste should sharpen clarity, not compete with workflow.

If a surface is product-first, use this skill as a restraint-and-hierarchy layer, not an invitation to make it loud.

## Frontend Engineering Constraints

- Verify design choices against real viewport behavior.
- Text must stay inside containers.
- Contrast must survive the more expressive palette.
- Motion must respect reduced-motion settings.
- If the project already has tokens or a component system, bend them intelligently before replacing them.

## Final Report

Include:

- the design read;
- what anti-slop defaults were deliberately avoided;
- key visual decisions changed;
- what still remains intentionally plain because the product context demands it.

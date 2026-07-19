---
name: frontend-taste-layer
description: Set and review a bounded visual direction for marketing, editorial, portfolio, and brand-forward frontend work. Use when a surface needs an explicit design read, calibrated composition/motion/density, preservation-first redesign, layout-rhythm review, or desktop/mobile/reduced-motion verification. Route product UI to Lazyweb and UX review instead.
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

## Route Before Styling

- For marketing, editorial, portfolio, and brand-forward pages, continue with this skill.
- For dashboards, settings, onboarding, checkout, paywalls, and other product UI, use Lazyweb evidence first, then `user-experience`, `design-critique-polish`, or the project's product-specific skill.
- If one page mixes both registers, apply this skill only to the marketing/editorial regions. Product-task clarity wins at the seam.

## Design Read

Before changing code, state one sentence:

`Reading this as: <surface> for <audience>, with a <vibe> language, leaning toward <design family>.`

Do not skip this. Most generic output comes from styling before the read is explicit.

## Three Dials

Set these as relative directions for the pass; do not impose universal numeric defaults:

- `variance`: symmetry versus surprise;
- `motion`: static versus cinematic;
- `density`: airy versus packed.

Use them to keep decisions consistent. Do not expose a pile of disconnected visual tweaks.

## Audit First On Redesigns

Before changing an existing surface, write two short lists:

- preserve: approved copy, brand assets, tokens, working interactions, content hierarchy, accessibility behavior, and explicit owner constraints;
- reconsider: only the composition, typography, density, motion, or section rhythm that the brief permits changing.

Do not silently rewrite content, replace supplied assets, swap the design system, or broaden the redesign scope.

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

## Motion Taste Rules

- Every animation must communicate hierarchy, feedback, state change, or narrative. If its purpose cannot be stated in one sentence, remove it.
- Avoid motion on high-frequency or keyboard-triggered interactions.
- Prefer crisp, short, origin-aware motion over broad cinematic transitions in product UI.
- After implementing meaningful motion, run `motion-review-gate` before calling the surface ship-ready.

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

## Layout Rhythm Review

- Name each section's layout family, then flag accidental repetition that flattens distinct content roles.
- Repetition is not automatically a defect: navigation, lists, and comparable records may need it.
- When consecutive marketing sections repeat the same split, equal-card grid, or centered-stack composition without a content reason, change the smallest high-leverage section rather than reskinning the page.

## Evidence Pass

Before calling the reviewed surface ready, verify:

1. one representative desktop width;
2. one representative mobile width;
3. `prefers-reduced-motion` behavior when motion exists;
4. every visible string, including navigation, headings, buttons, labels, captions, alt text, and loading, empty, error, or disabled states that belong to the reviewed path;
5. preserved items from the redesign audit are still intact.

Build success and source inspection do not count as visual verification. If browser evidence is unavailable, report `INSUFFICIENT_VISUAL_EVIDENCE`.

## Final Report

Include:

- the design read;
- the relative variance, motion, and density direction;
- what was preserved during redesign;
- what anti-slop defaults were deliberately avoided;
- key visual decisions changed;
- desktop, mobile, reduced-motion, and visible-copy evidence;
- what still remains intentionally plain because the product context demands it.

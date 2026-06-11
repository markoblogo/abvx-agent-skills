---
name: design-critique-polish
description: Critique and polish frontend interfaces before shipping. Use when a page, component, or app surface feels unclear, inconsistent, flat, awkward, under-tested, or not yet production-grade, and when the next step should be a focused design/UX pass rather than a broad rewrite.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Design Critique Polish

Run a deliberate critique pass before shipping. This is not a vague “make it nicer” prompt.

## Use For

- pre-ship review of a frontend surface;
- critique after implementation but before release;
- “this feels off, but I do not know why” situations;
- tightening hierarchy, spacing, typography, copy, motion, and edge states.

## Inputs

Take:

- the page, component, or route to review;
- screenshots, live URL, or repo files;
- current `PRODUCT.md` / `DESIGN.md` if available;
- known constraints: ship date, design system, browser targets, accessibility requirements.

## Critique Order

Evaluate in this order:

1. **Surface fit**
   - does this look like the right class of product or brand?
2. **Hierarchy**
   - can a first-time user tell what matters first?
3. **Layout and rhythm**
   - spacing, grouping, alignment, section cadence, empty space.
4. **Typography**
   - font choice, scale, line length, display/body contrast, overflow.
5. **Color and contrast**
   - palette discipline, readable text, accent overuse, weak affordances.
6. **States and resilience**
   - hover, focus, loading, empty, error, disabled, overflow, long labels.
7. **Motion and interaction**
   - helpful versus noisy; reduced-motion handling.
8. **Technical quality**
   - responsive behavior, accessibility signals, obvious performance issues.

## Output Mode

Produce:

- `what works`
- `what fails`
- `highest-leverage fixes first`
- `ship blockers`

Keep findings concrete. Name the surface, the defect, and the consequence.

## Fix Strategy

- Prefer small, high-leverage corrections over full rewrites.
- If the core design language is wrong, say so explicitly instead of endlessly polishing local details.
- If the page is good enough to ship, say that too and focus on blockers only.

## Common Frontend Tells To Catch

- same card pattern repeated everywhere;
- weak first viewport with no real anchor;
- gray text that reads low-contrast on tinted backgrounds;
- spacing that is mechanically even instead of rhythmic;
- headings that overflow or collapse on tablet/mobile;
- decorative motion without task value;
- UI copy that sounds like implementation notes rather than product language.

## Final Report

Include:

- top issues ordered by severity;
- what should change now versus later;
- whether the surface is ship-ready;
- what to verify in-browser after changes.

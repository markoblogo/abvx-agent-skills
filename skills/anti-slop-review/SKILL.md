---
name: anti-slop-review
description: Review an implemented product UI for hard visual defects, design-system incoherence, and repeated template patterns without treating subjective taste as universal law. Use for pre-ship screenshots or browser review when a landing page, product surface, dashboard, or redesign may be generic, clipped, inaccessible, visually inconsistent, or overbuilt from familiar AI-generated patterns.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Anti-Slop Review

Review evidence, not vibes. This skill critiques an implemented interface; it does not replace the brief, design system, accessibility checks, or product requirements.

Use `frontend-taste-layer` while choosing a visual direction. Use this skill after implementation or on screenshots/live UI. Use `design-critique-polish` for broader polish and `web-quality-audit` for full accessibility, performance, privacy, and security coverage.

## Authority

Default authority is `read` and `proposal`. Inspect files, screenshots, and browser behavior; report findings. Change code only when the user asked to fix or polish the interface. Do not add dependencies, replace a design system, license fonts/assets, or invent brand/customer claims without authorization.

## Establish the contract

Before judging style, identify:

- surface and critical user task;
- audience and product/brand register;
- existing tokens, components, and design constraints;
- required breakpoints and input modes;
- references the user explicitly approved.

For dashboards, settings, admin tools, firmware UI, and other utility-first products, clarity and density may correctly outweigh novelty. A familiar pattern is not a defect merely because it is familiar.

## Review hierarchy

Classify every finding as exactly one type.

### HARD_DEFECT

Observable failures that can block shipment:

- content hidden when JavaScript, hydration, scroll observers, or animation fails;
- clipped text or controls near fixed heights, notches, masks, and `overflow: hidden`;
- unreadable contrast, missing focus, broken keyboard path, or ignored reduced motion;
- dead controls, fake interactivity, console errors, or missing loading/error/empty states;
- horizontal overflow, broken responsive layout, unsafe tap targets, or misaligned comparison rows;
- content or controls visibly off-center when centering is part of the design.

Hard defects require reproduced evidence: screenshot, viewport, interaction, console/network observation, or file/line location. Do not infer them from visual preference.

### COHERENCE

System-level problems that weaken comprehension or identity:

- typography, palette, geometry, shadows, iconography, and motion speak different visual languages;
- hierarchy does not reveal the primary task or first action;
- atmosphere ends after the hero and the remaining page becomes unrelated filler;
- decoration competes with workflow or brand expression overwhelms product utility;
- repeated labels, cards, borders, shadows, or motion treatments flatten distinct roles;
- fake examples, placeholder product data, or generic copy make the surface feel ungrounded.

Tie each finding to the brief, existing system, user task, or repeated inconsistency. “I dislike this font” is not evidence.

### TEMPLATE_RISK

Non-blocking signals that the surface may be interchangeable:

- centered hero stack or text-left/panel-right hero used without a product-specific reason;
- repeated icon tiles, tinted chips, card grids, paired fill/outline CTAs, generic pricing/testimonial/FAQ sequences;
- decorative app windows, code windows, glows, grids, glass, gradients, or floating cards that do not communicate real product behavior;
- trendy fonts, palettes, or motion selected by category stereotype rather than the brief;
- the same section skeleton or house style reused across unrelated products;
- avoidance-only design: removing every familiar device without adding a product-specific idea.

These are prompts for scrutiny, not bans. A pattern is acceptable when it serves the task, matches the design system, and is executed coherently.

## Evidence pass

When browser access is available, verify at minimum:

1. primary desktop and mobile viewports;
2. keyboard navigation and visible focus;
3. every control that appears interactive;
4. long copy, missing data, loading, error, and empty states where relevant;
5. reduced motion and a no-animation/no-JS fallback for content visibility;
6. clipping around masks, notches, fixed heights, sticky layers, and section overlaps;
7. alignment of repeated rows, cards, comparison columns, and anchored actions.

Use screenshots at the actual failing viewport. Zoom into suspected clipping or centering problems instead of relying on a normal-scale impression.

## Bounded findings

Return at most seven findings per pass. Use stable IDs `AS-001`, `AS-002`, and so on. Order by `HARD_DEFECT`, then user impact, then leverage.

Each finding contains:

```text
ID: AS-001
Type: HARD_DEFECT | COHERENCE | TEMPLATE_RISK
Severity: blocker | high | medium | low
Evidence: screenshot/viewport/interaction/file:line
Impact: concrete user or product consequence
Smallest correction: bounded change
Verification: browser or code check that proves resolution
```

Do not fill seven slots with cosmetic preferences. If there are no actionable findings, return `SHIP_READY_WITHIN_REVIEWED_SCOPE`.

## Fix pass

When authorized to change code:

1. fix hard defects first;
2. preserve product behavior and design-system contracts;
3. make the smallest coherent correction rather than reskinning the whole page;
4. do not add a dependency for one decorative effect;
5. rerun the exact evidence pass at affected viewports;
6. report unresolved findings and deliberate exceptions.

A style exception is valid when it follows explicit user direction or a documented design-system decision. Record the reason; do not repeatedly reopen it.

## On-demand reference

Read `references/review-catalog.md` only when a suspected template pattern is ambiguous, the user requests a comprehensive anti-slop pass, or repeated reviews keep producing the same surface-level result.

A local installation may also contain `references/slop-source.local.md`, the full user-supplied source. Load it only on explicit request or when the compact catalog cannot resolve a disputed pattern. It is not a point-by-point shipping checklist.

## Verdict

- `SHIP_BLOCKED`: at least one unresolved hard defect blocks the reviewed path;
- `REVISE`: no blocker, but high-impact coherence work remains;
- `SHIP_READY_WITHIN_REVIEWED_SCOPE`: no actionable blocker or high-impact finding;
- `INSUFFICIENT_EVIDENCE`: the surface, states, or viewport evidence cannot support a verdict.

## Attribution

Adapted from a user-supplied anti-slop design law with no supplied provenance or redistribution license. The original is not distributed in this repository. This contract retains only general review ideas and rewrites them as evidence-based, context-sensitive ABVX guidance.

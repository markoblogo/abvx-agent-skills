---
name: motion-review-gate
description: Review frontend motion and animation code before shipping, with strict checks for purpose, frequency, easing, duration, transform origin, interruptibility, GPU-safe properties, reduced-motion support, and hover behavior. Use when a diff touches transitions, keyframes, Framer Motion, Lottie, drawers, popovers, toasts, hover or press states, gesture motion, or branded motion assets.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Motion Review Gate

Review motion as a pre-ship gate. This skill does not design a whole interface and does not rewrite unrelated frontend code.

Use it after implementation or during review when the diff includes animation, transitions, gestures, Lottie assets, interaction states, or motion-heavy UI polish.
Pair it with `browser-verification` when the visual behavior must be checked in a real browser.

## Use For

- CSS transitions, keyframes, `@starting-style`, WAAPI, Framer Motion, Motion, or Lottie changes;
- drawers, popovers, menus, dropdowns, tooltips, toasts, command palettes, modals, hover states, press states, and gestures;
- frontend diffs where animation might hurt speed, accessibility, or product feel;
- checking whether motion should be removed rather than polished.

## Do Not Use For

- general frontend critique without motion-specific risk;
- visual hierarchy, brand direction, or typography review without interaction/motion changes;
- full accessibility or performance audits beyond animation-related issues.

## Review Order

1. **Purpose** — every animation must serve feedback, spatial consistency, state indication, explanation, or prevention of jarring change.
2. **Frequency** — keyboard-triggered and 100+ times/day actions should not animate; frequent actions should be reduced.
3. **Timing and easing** — most UI motion stays under 300ms; avoid `ease-in` for UI response; prefer strong ease-out or appropriate custom curves.
4. **Physicality** — avoid `scale(0)`; popovers, menus, and tooltips should originate from their trigger; modals can stay centered.
5. **Interruptibility** — rapidly triggered UI should retarget smoothly; prefer transitions or springs over restart-prone keyframes.
6. **Performance** — animate `transform` and `opacity`; avoid layout properties and parent CSS-variable recalc storms.
7. **Accessibility** — respect `prefers-reduced-motion`; gate hover motion behind real hover media queries.
8. **Cohesion** — motion should match the product surface: crisp for dashboards, more expressive only when the brand or moment earns it.

## Hard Blocks

Flag these as blockers unless the diff clearly justifies them:

- `transition: all`;
- `scale(0)` entrance motion;
- `ease-in` on UI interactions;
- animation on keyboard shortcuts, command palettes, or other high-frequency actions;
- UI animation over 300ms without product reason;
- trigger-anchored popovers, menus, dropdowns, or tooltips scaling from center;
- keyframes on rapidly triggered dynamic UI like toasts or toggles;
- animation of `width`, `height`, `margin`, `padding`, `top`, `left`, or similar layout properties;
- missing reduced-motion handling for movement;
- ungated hover motion that can fire on touch devices.

## Fix Preference

Prefer the smallest correction that removes the regression:

1. delete motion that should not exist;
2. reduce distance, duration, or animated properties;
3. fix easing and duration;
4. fix origin and entry scale;
5. make the motion interruptible;
6. move it to GPU-safe properties;
7. add reduced-motion and hover gating;
8. add polish only after the functional motion is correct.

## Output Format

Return a findings table first:

| Severity | Evidence | Fix | Why |
|---|---|---|---|
| block / high / medium / low | `file:line` and current behavior | concrete replacement or removal | user-facing reason |

Then include:

- **Decision:** `Block`, `Needs changes`, or `Approve`.
- **Verification:** what to check in browser, including reduced-motion and touch/hover behavior when relevant.

Keep the review narrow. If the diff has no material motion risk, say that and approve the motion layer.

## Attribution

Adapted from Emil Kowalski's public design engineering and animation-review guidance in `emilkowalski/skills` and animations.dev, re-shaped into ABVX's compact review-gate format.

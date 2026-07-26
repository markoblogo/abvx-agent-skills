---
name: fluid-interaction-review
description: Build or review gesture-driven web interactions such as drag, swipe, sheets, carousels, and draggable panels. Use when pointer tracking, interruption, velocity handoff, momentum projection, hysteresis, rubber-banding, spatial continuity, or motion/transparency/contrast fallbacks materially affect the interaction.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Fluid Interaction Review

Use this only for direct-manipulation surfaces. It complements `motion-review-gate`; it is not a general visual-style or Apple-look preset.

## Best Fit

- drawers, sheets, swipe actions, carousels, sliders, scrubbers, and draggable panels;
- gesture code using Pointer Events, Motion, Framer Motion, or a library with equivalent primitives;
- reviews where a transition looks acceptable after release but feels disconnected during manipulation.

## Do Not Use For

- ordinary buttons, forms, tables, or static marketing sections;
- adding glass, bounce, sound, or haptics as decoration;
- replacing stable library behavior without a reproduced interaction defect;
- imposing universal spring constants or visual styling.

## Interaction Contract

1. **Continuous tracking** — while dragging or swiping, the surface follows the pointer 1:1. Preserve the offset from the point where the user grabbed it; do not jump to the element center.
2. **Pointer ownership** — use Pointer Events and `setPointerCapture(pointerId)` when implementing custom gestures so tracking survives leaving the element bounds. Release or cancel capture cleanly.
3. **Interruptibility** — a moving surface can be grabbed and redirected immediately. Retarget from the current on-screen value and current velocity, not from a stale logical target. Never lock input until an animation finishes.
4. **Velocity handoff** — sample a short, timestamped movement history and pass release velocity into the settling spring. Guard zero distance, sparse events, and extreme velocity.
5. **Momentum projection** — when a flick can cross snap points, select the destination from a bounded projection of release velocity, then settle with the handed-off velocity. Do not choose solely from release position.
6. **Hysteresis** — keep the gesture undecided until movement exceeds a small, input-appropriate threshold. Resolve axis and intent before suppressing native scrolling or committing an action.
7. **Soft boundaries** — beyond a real bound, apply progressively increasing resistance. Do not hard-stop while the pointer is still moving. Clamp the final resting state to a valid target.
8. **Spatial continuity** — enter and exit use the same spatial path unless product meaning requires otherwise. Popovers and panels originate from their trigger or manipulation source; reversible motion preserves direction and velocity continuity.

Prefer a mature interaction library when it already satisfies the contract. Custom physics requires focused tests and browser evidence.

## Accessibility Fallbacks

Treat these as independent modes; test combinations, not only each mode alone:

- `prefers-reduced-motion: reduce`: remove momentum, elastic overshoot, parallax, and large spatial travel; retain state feedback through static change or a short non-spatial fade;
- `prefers-reduced-transparency: reduce`: replace translucent surfaces with a sufficiently opaque or solid surface when the browser supports the query; keep a solid default/fallback where it does not;
- `prefers-contrast: more`: strengthen surface separation, focus indication, controls, and text contrast without depending on blur or transparency.

Pointer behavior must retain keyboard, focus, click/tap, cancellation, and native-scroll semantics. Visual press feedback may start on pointer-down; destructive or committed actions still follow the component's accessible activation contract.

## Review Procedure

1. Identify the gesture state machine: idle, possible, active, settling, cancelled.
2. Trace pointer position, grab offset, timestamps, velocity, projected target, and bounds.
3. Interrupt the interaction during settling and reverse direction.
4. Test slow drag, fast flick, boundary overshoot, pointer cancellation, axis ambiguity, and repeated rapid input.
5. Test mouse/touch or faithful emulation, keyboard operation, native scrolling, and the three fallback modes.
6. Run `motion-review-gate` for general purpose, frequency, timing, GPU-property, and reduced-motion checks.

## Required Evidence

- browser and route/component tested;
- input modes tested;
- current-value interruption and reversal result;
- velocity/projection and boundary result;
- keyboard, focus, cancellation, and native-scroll result;
- reduced motion, transparency, and contrast result, including unsupported-query fallback;
- targeted automated tests, or an explicit reason they are not practical.

Source inspection or a successful build alone is insufficient interaction evidence.

## Output

Return findings first:

| Severity | Evidence | Contract breach | Smallest fix |
| --- | --- | --- | --- |
| block / high / medium / low | `file:line` plus observed behavior | named rule | bounded correction |

Then include:

- **Decision:** `Block`, `Needs changes`, or `Approve`.
- **Interaction evidence:** tested gesture and fallback matrix.
- **Unverified:** any input, browser, accessibility mode, or device not tested.

## Attribution

Adapted from Emil Kowalski's MIT-licensed `apple-design` skill, chiefly its direct-manipulation, interruptibility, velocity, momentum, hysteresis, resistance, spatial-consistency, and accessibility guidance. Re-shaped into a bounded ABVX web-interaction contract; it does not adopt Apple visual styling or universal physics constants.

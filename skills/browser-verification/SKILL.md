---
name: browser-verification
description: Verify frontend changes in a real browser, including layout, console errors, responsive states, network failures, screenshots, and interactions. Use after local or deployed web UI changes, visual fixes, forms, navigation, asset updates, canvas or 3D work, or whenever browser verification should replace static guessing.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Browser Verification

Trust the browser, not static guesses. Use real rendering for frontend claims.

## Setup

Prefer the repo's existing Playwright setup. If none exists, install browser tooling in a local tool directory or temporary environment rather than adding a production dependency.

Use a local static or dev server when file URLs would not match production behavior.

## Verification Loop

1. Start the app or static server.
2. Open the target URL in a browser-controlled session.
3. Check console errors and failed network requests.
4. Verify key selectors render and have nonzero bounding boxes.
5. Verify images/assets are complete and natural dimensions are nonzero.
6. Check desktop and mobile viewports.
7. Check horizontal overflow: `document.documentElement.scrollWidth <= innerWidth + 1`.
8. Exercise the primary interaction path.
9. For motion-heavy changes, check reduced-motion behavior and touch versus hover behavior, then pair with `motion-review-gate` for code-level motion review.
10. Capture screenshots only when useful for review or debugging.
11. Stop local servers before finalizing.

## Common Assertions

- page loaded with expected title or heading;
- no failed requests for CSS, JS, images, fonts, or data;
- no severe console errors;
- target controls are visible and enabled;
- form submission or navigation reaches expected state;
- responsive layout has no text overlap or horizontal scroll;
- animated/canvas/3D surfaces have nonblank rendered pixels when relevant;
- motion-heavy surfaces still work with `prefers-reduced-motion: reduce`.

## Guardrails

- Do not commit local Playwright tooling unless the repo already owns browser tests.
- Do not claim visual verification if only static checks ran.
- If browser install fails, report the fallback checks honestly.
- For authenticated or paid flows, avoid real side effects unless explicitly approved.

## Final Report

Include URLs, viewports, checks run, commands, failures found, and whether screenshots were captured.

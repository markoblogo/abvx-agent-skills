---
name: lottie-motion-builder
description: Build or refine small production-ready Lottie animations from SVGs, logos, UI states, loaders, and branded motion assets with a local preview harness, explicit inputs, and output verification. Use when the user asks for Lottie, JSON animation, SVG reveal animation, logo animation, or lightweight motion assets for product surfaces.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Lottie Motion Builder

Use Lottie for small deployable motion assets, not for full cinematic motion-design work.

## Good Fits

- SVG path reveal
- logo or wordmark animation
- loader, empty-state, success-state, and transition animation
- small branded motion element for web, mobile, or app onboarding

## Do Not Use It For

- long character animation
- complex scene choreography
- vague "make it cool" requests with no asset grounding
- motion work that does not need to ship as Lottie JSON

## Required Inputs

Before building, lock these down:

- source asset: SVG, screenshot, logo, icon, or concrete visual reference;
- target surface: landing page, app UI, loader, hero accent, onboarding, etc.;
- duration and loop behavior;
- target runtime: web, React Native, iOS, Android, or generic Lottie JSON;
- editable controls needed at runtime: background, color, size, stroke, speed, etc.

If the user gives only a vague motion request, ask for or derive one concrete asset first.

## Harness Rule

Use the external diffusionstudio/lottie harness rather than inventing a custom player.

- Read [references/external-harness.md](references/external-harness.md) before setup.
- Bootstrap or refresh the harness with `scripts/bootstrap_harness.sh`.
- Keep generated animation files inside the harness project while iterating.
- Treat the upstream harness as the rendering contract for preview and slot behavior.

## Workflow

1. Confirm the asset, target surface, duration, loop mode, and runtime target.
2. Bootstrap the external harness if needed.
3. Generate or edit `public/lottie.json` in the harness project.
4. Expose at least one background-color control and any explicitly requested controls.
5. Run the local preview and visually verify the result.
6. Run `motion-review-gate` when the asset is meant for a product UI surface rather than a throwaway demo.
7. Export the usable artifact set and summarize how to embed it.

## Output Contract

Produce these artifacts when the user asks for a usable result:

- `animation.json` or the final `lottie.json`;
- one visual verification artifact: screenshot, gif, or short mp4;
- a short embed note for the target runtime;
- any runtime-editable controls used by the animation.

## Verification

- The JSON parses in the harness.
- The motion is visible and not blank.
- Loop points are intentional.
- Background control exists.
- Dimensions, duration, and FPS match the request.
- The asset is small enough for the intended product surface.
- Product-surface motion has passed `motion-review-gate` or the exception is stated.

## Reporting

In the final report, include:

- source asset used;
- output path;
- preview path or URL;
- runtime target;
- controls exposed;
- known limitations.

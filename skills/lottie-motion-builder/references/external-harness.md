# External Harness Notes

This skill is intentionally backed by the upstream `diffusionstudio/lottie` harness instead of re-implementing its viewer rules inside ABVX Agent Skills.

## Upstream

- Repository: `https://github.com/diffusionstudio/lottie`
- Local clone used for adaptation: commit `3360f2e`
- Upstream skill name: `text-to-lottie`
- License: MIT

## Why Use The Upstream Harness

- It previews Lottie through Skia/Skottie rather than a custom ad hoc viewer.
- It already expects `public/lottie.json`.
- It includes a working local preview flow and control surface expectations.
- It is better to adapt a known rendering harness than to silently drift with a bespoke HTML page.

## Practical Constraints

- The harness is a full Vite/React project, not a lightweight standalone skill.
- It depends on `canvaskit-wasm`, React, Vite, and a postinstall copy step.
- That makes it useful as an external tool dependency, but too heavy to copy raw into this repository's core skillpack.

## ABVX Position

ABVX should treat the upstream repo as:

- external harness for preview and iteration;
- reference implementation for Lottie slot/control behavior;
- motion-asset lab for deployable outputs.

ABVX should not treat it as:

- a drop-in core skill with no adaptation;
- a generic substitute for all animation work;
- a justification to skip output verification.

## Stable Local Path

Preferred local install path:

`~/.codex/vendor/diffusionstudio-lottie`

Use `scripts/bootstrap_harness.sh` from this skill folder to clone or refresh that path.

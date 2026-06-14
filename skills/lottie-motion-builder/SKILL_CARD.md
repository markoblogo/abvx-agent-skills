# Skill Card: lottie-motion-builder

## Description
Builds small production-ready Lottie motion assets from concrete inputs with a local preview harness and verification gates.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for SVG reveals, logo motion, loaders, small UI state animations, and lightweight branded motion elements that should ship as Lottie JSON.

## Out of Scope
Do not use for long-form motion graphics, character animation, or vague decorative animation requests without grounded source assets.

## Sources and Attribution
ABVX adapted from diffusionstudio/lottie and local frontend verification practice.

## Inputs and Outputs
Inputs: SVG, logo, screenshot, brand cues, duration, runtime target, loop requirements, requested controls.

Outputs: Lottie JSON, local preview, verification artifact, and runtime embed notes.

## Risks and Mitigations
- Risk: blank or incompatible animation. Mitigation: use the upstream Skottie harness and preview locally.
- Risk: overbuilt animation. Mitigation: restrict the skill to small deployable motion assets.
- Risk: uneditable output. Mitigation: require explicit controls and always expose background color.

## Evaluation
Evaluated by harness parsing, visual preview, output review, and runtime-target handoff quality.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

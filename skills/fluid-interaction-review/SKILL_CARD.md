# Skill Card: fluid-interaction-review

## Description
Builds or reviews the physical behavior of drag, swipe, sheet, carousel, and draggable-panel interactions.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when direct manipulation needs continuous tracking, pointer capture, interruption from the current value, velocity handoff, momentum projection, hysteresis, soft boundaries, spatial continuity, or accessibility fallbacks.

## Out of Scope
Do not use as an Apple visual-style preset, a reason to add decorative glass or bounce, or a replacement for stable interaction-library behavior without evidence of a defect.

## Sources and Attribution
Adapted from Emil Kowalski's MIT-licensed `apple-design` skill and reworked into a bounded ABVX web-interaction contract.

## Inputs and Outputs
Inputs: gesture implementation, component/route, interaction constraints, browser evidence, and relevant automated tests.

Outputs: ranked contract findings, smallest fixes, an approval decision, tested gesture/fallback evidence, and explicit unverified states.

## Composable With
- `motion-review-gate`
- `browser-verification`
- `user-experience`
- project-specific frontend skills

## Risks and Mitigations
- Risk: unnecessary custom gesture physics. Mitigation: prefer mature libraries that already satisfy the contract.
- Risk: decorative Apple imitation. Mitigation: exclude visual styling and universal spring constants.
- Risk: pointer behavior breaks native input. Mitigation: require keyboard, focus, cancellation, and scroll evidence.
- Risk: accessibility modes are treated as one toggle. Mitigation: verify motion, transparency, and contrast independently and in combination.

## Evaluation
Evaluated by structural validation and a project routing pilot against MN7R drawers, swipe interactions, carousels, and draggable panels.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

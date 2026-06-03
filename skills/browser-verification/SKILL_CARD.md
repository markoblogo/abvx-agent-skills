# Skill Card: browser-verification

## Description
Verifies web pages with real browser automation after frontend or visual changes.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for responsive checks, asset rendering, console/network failures, forms, navigation, screenshots, canvas, and post-change frontend verification.

## Out of Scope
Do not use to create a permanent test suite unless the user asks or the repo already has that convention.

## Sources and Attribution
ABVX adapted from local Playwright/browser verification workflow.

## Inputs and Outputs
Inputs: URL, local server command, target selectors, expected interactions, viewport list.

Outputs: browser observations, screenshot paths if captured, failures, verification summary.

## Risks and Mitigations
- Risk: adding unwanted dependencies. Mitigation: use temporary/local tooling by default.
- Risk: false confidence from static checks. Mitigation: require real render for visual claims.
- Risk: unintended side effects. Mitigation: gate authenticated, paid, or destructive flows.

## Evaluation
Evaluated by structural validation and manual review against frontend verification workflows.

## Version
0.2.0

## Reporting Issues
Open an issue in the repository.

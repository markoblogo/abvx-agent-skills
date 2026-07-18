# Skill Card: anti-slop-review

## Description
Reviews implemented UI through hard defects, coherence problems, and template risks without turning aesthetic preferences into universal bans.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for bounded pre-ship screenshot, browser, or code review of landing pages, product surfaces, dashboards, and redesigns.

## Out of Scope
Not a replacement for a product brief, design system, accessibility audit, browser test suite, brand strategy, or frontend implementation skill.

## Sources and Attribution
Adapted from a user-supplied anti-slop design law. No author, source, or redistribution license was supplied, so the original text is retained only in the user's local installation and is not distributed here.

## Inputs and Outputs
Inputs: brief, design-system constraints, screenshots/live UI, viewport and interaction evidence, relevant files.

Outputs: at most seven stable findings, bounded corrections, verification steps, and a scoped ship verdict.

## Risks and Mitigations
- Risk: subjective taste blocks shipping. Mitigation: only reproduced hard defects block; style findings require contract evidence.
- Risk: marketing taste applied to utility UI. Mitigation: establish surface register and primary task first.
- Risk: checklist design. Mitigation: template patterns are scrutiny prompts, not bans.
- Risk: context bloat. Mitigation: compact core plus on-demand references.
- Risk: broad redesign. Mitigation: smallest coherent correction and explicit authority boundary.

## Composable With
- `frontend-taste-layer`
- `design-critique-polish`
- `web-quality-audit`
- `motion-review-gate`

## Evaluation
Scenario review should distinguish a real visibility/contrast/control defect from an intentional pill, gradient, familiar layout, or utility-first design choice.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

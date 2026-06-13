# Skill Card: html-diagram-artifact

## Description
Creates standalone HTML/SVG architecture and flow explainers with minimal prose and strong visual hierarchy.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for architecture communication, stack explanation, onboarding diagrams, request-path walkthroughs, and system-boundary explainers.

## Out of Scope
Do not use for production frontend implementation, app shells, marketing pages, or broad UI redesign.

## Sources and Attribution
ABVX adapted from `plannotator/effective-html` and the `html-effectiveness` standalone example corpus, then narrowed for validation-gated Codex-style project work.

## Inputs and Outputs
Inputs: user request, repo context, architecture notes, docs, optional screenshots, and any target system boundaries or flows.

Outputs: one self-contained HTML diagram artifact, optional lightweight interaction for flow highlighting, and an honest verification summary.

## Risks and Mitigations
- Risk: diagram becomes decorative instead of explanatory. Mitigation: prioritize structure and one or two key flows.
- Risk: artifact drifts into app UI work. Mitigation: keep prose light and interaction explanatory only.
- Risk: visual claims are unverified. Mitigation: require browser checks before completion.

## Evaluation
Evaluated by structural validation and manual review against standalone architecture-explainer workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

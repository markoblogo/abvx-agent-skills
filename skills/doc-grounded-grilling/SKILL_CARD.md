# Skill Card: doc-grounded-grilling

## Description
Aligns plans against the repo's existing docs, domain language, and decisions through a one-question-at-a-time grilling session.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use before implementation when a plan is ambiguous, terminology is fuzzy, or existing docs and ADRs must shape the decision.

## Out of Scope
Do not use as endless interrogation or as a replacement for implementation planning once the plan is already clear.

## Sources and Attribution
ABVX adapted from Matt Pocock's `grill-with-docs`, rewritten for ABVX repo docs, ADRs, design assets, and Codex-style project work.

## Inputs and Outputs
Inputs: user plan, repo docs, codebase signals, ADRs, context files.

Outputs: clarified language, resolved trade-offs, explicit open questions, and doc-refresh pointers.

## Risks and Mitigations
- Risk: over-questioning. Mitigation: stop when ambiguity is materially reduced.
- Risk: doc drift. Mitigation: cross-check answers against code and flag docs needing maintenance.
- Risk: terminological confusion. Mitigation: force canonical terms early.

## Evaluation
Evaluated by structural validation and manual review against planning and alignment sessions.

## Version
0.7.0

## Reporting Issues
Open an issue in the repository.

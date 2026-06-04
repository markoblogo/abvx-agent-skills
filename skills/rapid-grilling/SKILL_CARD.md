# Skill Card: rapid-grilling

## Description
Runs a lightweight one-question-at-a-time grilling session to sharpen vague ideas before heavier planning.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for brainstorming, product clarification, and early design exploration when fast alignment matters more than deep repo grounding.

## Out of Scope
Do not use once repo docs, ADRs, or code constraints become central; switch to `doc-grounded-grilling`.

## Sources and Attribution
ABVX adapted from Matt Pocock's `grill-me`, rewritten as a lightweight companion to the ABVX planning stack.

## Inputs and Outputs
Inputs: a vague plan, design idea, product concept, or change request.

Outputs: a clarified idea, resolved core questions, and a recommended next artifact.

## Risks and Mitigations
- Risk: shallow alignment. Mitigation: escalate to doc-grounded grilling when repo-specific constraints matter.
- Risk: endless questioning. Mitigation: stop when the next concrete artifact is obvious.

## Evaluation
Evaluated by structural validation and manual review against brainstorming and product-clarification sessions.

## Version
0.7.0

## Reporting Issues
Open an issue in the repository.

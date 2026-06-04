# Skill Card: spec-to-prd

## Description
Turns current discovery and repo understanding into a durable PRD for product, client, and internal roadmap work.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when a request is clear enough to become a PRD but still needs a structured product artifact before issue slicing or implementation.

## Out of Scope
Do not use when discovery is still too vague; clarify first.

## Sources and Attribution
ABVX adapted from Matt Pocock's `to-prd`, rewritten for issue-tracker-neutral output and ABVX planning flows.

## Inputs and Outputs
Inputs: current conversation context, repo understanding, clarified decisions.

Outputs: a PRD as markdown, issue body, or another durable planning artifact.

## Risks and Mitigations
- Risk: weak synthesis. Mitigation: send vague work back to grilling first.
- Risk: stale implementation detail. Mitigation: favor durable decisions over path-specific prose.
- Risk: fuzzy scope. Mitigation: require explicit out-of-scope and testing sections.

## Evaluation
Evaluated by structural validation and manual review against planning and productization workflows.

## Version
0.7.0

## Reporting Issues
Open an issue in the repository.

# Skill Card: assumption-excavation

## Description
Surfaces hidden assumptions in specs, plans, AGENTS.md, SKILL.md, SET bundles, and workflow contracts before implementation or handoff.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use before implementation, automation, or runner handoff when an artifact depends on unstated environment, dependency, behavioral, temporal, or success assumptions.

## Out of Scope
Do not use as a correctness proof, rewrite pass, or deployment gate without human review.

## Sources and Attribution
Adapted from the `assumption-excavator` lens in `aself101/agents-and-pipelines`, reduced into a compact ABVX skill.

## Inputs and Outputs
Inputs: plans, specs, generated repo docs, skill docs, SET planner exports, proof-loop contracts.

Outputs: EXAMINED/UNEXAMINED verdict, ranked assumptions, fragility notes, and clarification or verification steps.

## Risks and Mitigations
- Risk: over-blocking. Mitigation: assumptions are not automatically errors.
- Risk: mind-reading. Mitigation: phrase findings as what the text assumes.
- Risk: generic critique. Mitigation: require category and fragility ranking.

## Evaluation
Evaluated by structural validation and manual review against planning and repo-contract artifacts.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

# Skill Card: confidence-fragility-review

## Description
Reviews whether confident claims in docs, plans, releases, or workflow contracts are backed by evidence, tests, contracts, or safeguards.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use before shipping, publishing, accepting generated plans, or trusting workflow outputs that may sound stronger than their evidence.

## Out of Scope
Do not use as a full security audit, generic risk register, or substitute for actual tests.

## Sources and Attribution
Adapted from the `anxiety-reader` lens in `aself101/agents-and-pipelines`, compressed into an evidence-oriented ABVX review skill.

## Inputs and Outputs
Inputs: plans, READMEs, release notes, generated docs, SET exports, proof-loop artifacts.

Outputs: CONFIDENCE_WARRANTED/FRAGILITY_MASKED verdict, claim/evidence map, fragility register, and smallest proof step.

## Risks and Mitigations
- Risk: fear-driven false positives. Mitigation: separate justified fragility from projected worry.
- Risk: generic critique. Mitigation: require a specific claim and backing evidence.
- Risk: over-documentation. Mitigation: recommend the smallest proof step.

## Evaluation
Evaluated by structural validation and manual review against release, docs, and planning artifacts.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

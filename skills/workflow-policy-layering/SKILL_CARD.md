# Skill Card: workflow-policy-layering

## Description
Separates workflow steps from authority, forbidden actions, escalation paths, and validation gates so assistant specs stop contradicting themselves.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when agent instructions are getting muddled because process, permissions, review, and safety are all mixed into one unstable block.

## Out of Scope
Do not use as a substitute for actual legal, safety, or product policy review. It organizes policy; it does not invent trustworthy policy from nothing.

## Sources and Attribution
ABVX original, distilled from repeated assistant-boundary and workflow-layering work across product and development settings.

## Inputs and Outputs
Inputs: current workflow description, authority assumptions, escalation expectations, validation needs.

Outputs: layered spec with explicit workflow, authority, escalation, and validation sections.

## Risks and Mitigations
- Risk: fake certainty about authority. Mitigation: require explicit allowed / confirm / forbidden separation.
- Risk: vague refusals. Mitigation: define escalation as concrete next-step guidance.
- Risk: policy hidden in prose. Mitigation: split layers before rewriting.

## Evaluation
Evaluated by manual review against agent-policy cleanup scenarios and layered-spec rewrite tasks.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

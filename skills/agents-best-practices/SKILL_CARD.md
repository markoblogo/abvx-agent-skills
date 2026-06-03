# Skill Card: agents-best-practices

## Description
Guides provider-neutral design, audit, and implementation planning for agentic systems and agent harnesses.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for designing MVP agents, auditing harnesses, tool permission models, context strategy, evals, and safety gates.

## Out of Scope
Do not use to justify unbounded autonomy, broad unsafe tools, or prompt-only safety for high-risk actions.

## Sources and Attribution
ABVX adapted from local provider-neutral agent-harness guidance and public agent engineering practice.

## Inputs and Outputs
Inputs: domain brief, risk constraints, desired tools, deployment environment, validation criteria.

Outputs: MVP blueprint, harness review, permission matrix, eval plan, launch path.

## Risks and Mitigations
- Risk: over-engineering. Mitigation: start with one useful agent loop.
- Risk: unsafe action surface. Mitigation: typed tools and approval gates.
- Risk: context bloat. Mitigation: progressive disclosure and compaction.

## Evaluation
Evaluated by structural validation and manual review against agent-design workflows.

## Version
0.2.0

## Reporting Issues
Open an issue in the repository.

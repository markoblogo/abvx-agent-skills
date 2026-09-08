# Skill Card: role-skill-pack-design

## Description
Designs compact professional role agents and skill packs with explicit routing, context, donor provenance, authority, evaluation, and rollout rules.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when building assistant layers for teams, products, internal delivery, publishing, career work, or personal operations and when adapting an external professional-role catalog.

## Out of Scope
Do not use to write product-specific policy from scratch, replace domain docs, or force a role matrix where one base workflow is enough.

## Sources and Attribution
ABVX original, informed by practical extraction of private role/workflow skill packs into reusable public method. Professional-role decomposition and deliverable patterns were additionally informed by `msitarzewski/agency-agents`; the ABVX skill does not vendor its prompt corpus or inherit its memory, tools, metrics, or authority claims.

## Inputs and Outputs
Inputs: role list, workflow inventory, operating boundaries, existing docs, current assistant behavior.

Outputs: pack structure, initial roles, routing and handoffs, authority boundaries, donor adaptation record, evaluation plan, and rollout order.

## Risks and Mitigations
- Risk: too many skills too early. Mitigation: start with the smallest proving set.
- Risk: duplicate logic across roles. Mitigation: define a base workflow first and add difference layers.
- Risk: burying details in one giant file. Mitigation: keep `SKILL.md` short and push detail into references.
- Risk: treating a professional persona as proven expertise or authority. Mitigation: keep maturity states separate and promote per role and action through evidence.

## Evaluation
Evaluated by structural validation and manual review against product, internal-work, publishing, career, and personal-role design cases. Behavioral outcome testing remains required before role promotion.

## Version
0.2.0

## Reporting Issues
Open an issue in the repository.

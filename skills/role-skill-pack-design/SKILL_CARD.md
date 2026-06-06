# Skill Card: role-skill-pack-design

## Description
Designs compact role-specific or workflow-specific skill packs with explicit base layers, difference layers, references, boundaries, and rollout order.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when building assistant layers for teams, products, operating roles, or workflow stages and you need a reusable pack structure instead of one large prompt.

## Out of Scope
Do not use to write product-specific policy from scratch, replace domain docs, or force a role matrix where one base workflow is enough.

## Sources and Attribution
ABVX original, informed by practical extraction of private role/workflow skill packs into reusable public method.

## Inputs and Outputs
Inputs: role list, workflow inventory, operating boundaries, existing docs, current assistant behavior.

Outputs: pack structure, initial skill set, role layering model, and rollout order.

## Risks and Mitigations
- Risk: too many skills too early. Mitigation: start with the smallest proving set.
- Risk: duplicate logic across roles. Mitigation: define a base workflow first and add difference layers.
- Risk: burying details in one giant file. Mitigation: keep `SKILL.md` short and push detail into references.

## Evaluation
Evaluated by manual review against role-pack design tasks and structural consistency with the ABVX skill profile.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

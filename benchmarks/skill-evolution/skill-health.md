# Skill Health Gate

Use this lightweight gate before accepting a skill edit or adding a new skill.

## Checks

- Trigger fit: frontmatter description names the real activation scenarios.
- Actionability: the body tells the agent what to do differently.
- Generalization: the rule applies to a class of tasks, not one incident.
- Non-regression: the rule does not conflict with higher-priority instructions or existing skill boundaries.
- Context cost: added tokens are justified by avoided failures or repeated work.
- Validation: deterministic check, fixture, pairwise review, or human review is named.

## Decision

Use `accept`, `reject`, `revise`, or `invalid`. Record rejected ideas in the rejected ledger or rejected-edit buffer.

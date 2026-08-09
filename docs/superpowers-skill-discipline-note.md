# Superpowers Skill Discipline Note

`obra/superpowers` is useful to `abvx-agent-skills` as a discipline reference
for when and how skills should activate.

The compact adaptation is trigger clarity, evidence-backed skill behavior, and
finish/verification language. This repo should not copy the full Superpowers
workflow or become a mandatory development harness.

Source: https://github.com/obra/superpowers

## Adopted minimum

For new or materially changed skills:

- define the trigger narrowly enough that an agent can decide whether to use it;
- state when the skill should be skipped;
- keep owner/human approval boundaries explicit;
- connect quality claims to fixtures, rollout evidence, or bounded evals;
- make completion language distinguish changed, reviewed, verified, and shipped.

## Review checks

Before publishing a Superpowers-inspired skill change, check:

- does it add a sharper behavior check than existing skills?
- does it avoid duplicating `bounded-evaluation`, `delivery-baseline-audit`,
  `confidence-fragility-review`, or `agent-learning-layer-triage`?
- does catalog text describe the actual skill instead of the donor project?
- does the README route users to a skill only when it is a natural target?
- does any automation remain proposal-first and human-reviewed?

## Boundary

Do not import:

- mandatory subagent-driven development;
- worktree-per-task as a pack-wide rule;
- rigid test-first deletion rules;
- marketplace/plugin installation assumptions;
- telemetry-bearing companion features.

Use Superpowers as a quality lens for skill behavior, not as the governing
runtime for this pack.

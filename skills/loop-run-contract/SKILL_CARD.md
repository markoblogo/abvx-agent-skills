# Skill Card: loop-run-contract

## Description

Creates a compact L1/L2 contract for repeated agent work: scope, authority, durable state, append-only log, budget, stop rules, verifier, escalation, and human approval boundary.

## Owner

ABVX / Anton Biletskiy-Volokh

## License

MIT. See repository LICENSE.

## Intended Use

Use before enabling one recurring report, shadow evaluation, or proposal-first assisted workflow for a named project.

## Out of Scope

Not a scheduler, executor, tool-permission system, global hook, auto-merge policy, or unattended runtime.

## Sources and Attribution

Adapted from [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering); ABVX retains only the bounded L1/L2 contract discipline.

## Inputs and Outputs

Inputs: one goal, scope, cadence/event, owner, evidence sources, limits, risk boundary, and proposed level.

Outputs: reviewable run packet, L1/L2 authority decision, state/log locations, stop/escalation rules, and L2 verifier/rollback conditions.

## Risks and Mitigations

- Risk: automation expands silently. Mitigation: fixed level and explicit denied actions.
- Risk: cost growth on empty or weak queues. Mitigation: early exit and hard per-run budget.
- Risk: self-approved changes. Mitigation: L2 maker-checker split and human approval before effects.
- Risk: state disappears into chat. Mitigation: required durable state plus append-only log.

## Evaluation

Evaluate against a synthetic packet matrix: empty-watchlist early exit, budget breach, ambiguous evidence, L1 external-action request, L2 verifier failure, and approved human handoff.

## Version

0.1.0

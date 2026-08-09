# Skill Card: skill-health-audit

## Description
Audits agent skills for trigger fit, evidence depth, drift, overhead, safety, and readiness to publish at a stated evaluation tier.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use before publishing a new or materially changed skill, raising its evaluation tier, or reviewing the health of the public pack.

## Out of Scope
Do not use as an automatic skill editor, evaluator that invents runtime evidence, publisher, merger, or replacement for maintainer acceptance.

## Sources and Attribution
Original ABVX contract combining the repository's catalog hygiene, bounded evaluation, context degradation, confidence, and skill evolution rules.

## Inputs and Outputs
Inputs: skill files, cards, metadata, catalog/README projections, fixtures, reports, neighboring skills, and stated evaluation tier.

Outputs: review-only health report, ranked findings, evidence gaps, tier recommendation, and maintainer decision boundary.

## Risks and Mitigations
- Risk: structural polish mistaken for behavioral quality. Mitigation: separate structure from activation and rollout evidence.
- Risk: audit silently changes the pack. Mitigation: require read-only review output and explicit maintainer acceptance for edits.
- Risk: excessive review overhead. Mitigation: inspect the smallest evidence set that can justify the requested tier.

## Model Sensitivity
Requires disciplined distinction between observed fixtures, missing evidence, and inferred quality. Weaker models need fixed report fields and explicit negative activation cases.

## Composable With
- `bounded-evaluation`
- `context-degradation-review`
- `confidence-fragility-review`
- `private-vs-publishable-skill-audit`

## Anti-Patterns
- assigning `fixture_checked` or higher from metadata alone
- treating a generated catalog entry as independent evidence
- editing or publishing the audited skill without a separate approved task

## Evaluation
Structural-only in v0.13.0; its contract is covered by deterministic repository tests, while behavioral usefulness remains explicitly unclaimed.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

# Skill Card: bounded-growth-loop

## Description
Designs recurring product and go-to-market reviews with evidence checks, state, stop rules, and approval-gated outputs.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use before scheduling recurring content, SEO, analytics, funnel, partner, or product-positioning work.

## Out of Scope
Do not use as marketing automation, autonomous outreach, publishing, spend management, pricing control, or a scheduler runtime.

## Sources and Attribution
Adapted from the `marketing-loops` structure in `coreyhaines31/marketingskills`.

## Inputs and Outputs
Inputs: approved product context, source data, cadence, state store, verifier, budget, and approval rules.

Outputs: loop contract, readiness level, retained report or proposal, and explicit settle/escalate decision.

## Risks and Mitigations
- Risk: noisy or runaway automation. Mitigation: separate check cadence from action condition and require stop rules.
- Risk: unsafe side effects. Mitigation: default to report-only or proposal-first; require approval for every external write.
- Risk: false causal claims. Mitigation: require evidence thresholds and alternative explanations.

## Evaluation
Evaluated by structural validation and manual review against recurring content, funnel, and product-review scenarios.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

# Skill Card: hypothesis-diversification

## Description
Generates diverse hypotheses, explanations, or bounded proposals before evidence review.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for diversity-first research, adversarial review, incident or market analysis, product reasoning, and SkillOpt candidate proposal generation.

## Out of Scope
Do not use as a standalone decision method, probability calibration method, financial trading engine, or runtime autonomy layer.

## Sources and Attribution
Inspired by "Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity" (arXiv:2510.01171), rewritten for ABVX validation-gated agent work.

## Inputs and Outputs
Inputs: research questions, decisions, plans, SET bundles, SkillOpt targets, incident hypotheses.

Outputs: candidate hypotheses or proposals, evidence needs, disconfirming signals, adversarial notes, validation handoff.

## Risks and Mitigations
- Risk: persuasive but unsupported alternatives. Mitigation: rank by evidence readiness and hand off to validation.
- Risk: false precision from verbalized probabilities. Mitigation: forbid calibrated-probability claims.
- Risk: proposal sprawl. Mitigation: keep candidate sets small and bounded.

## Evaluation
Evaluated by structural validation and manual review against research, adversarial-review, and SkillOpt proposal-generation tasks.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

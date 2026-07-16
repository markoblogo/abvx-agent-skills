# Skill Card: project-hook-guardrails

## Description
Designs small, opt-in project hook rules with explicit scope, warning versus blocking behavior, conditions, evidence, bypass, and fixtures.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when one repository needs a bounded data-boundary or promotion guardrail without adopting global observers, session hooks, or a new runtime.

## Out of Scope
Do not use for organization-wide monitoring, silent enforcement, secret scanning replacement, or any rule with no named event, owner, verification path, and test fixtures.

## Sources and Attribution
Adapted from [ECC hookify-rules](https://github.com/affaan-m/ECC/blob/main/skills/hookify-rules/SKILL.md); ABVX keeps only opt-in per-project rule design.

## Inputs and Outputs
Inputs: project, event, risk, available evidence, false-positive tolerance, owner, and desired rollout.

Outputs: versioned rule packet, fixture matrix, evidence shape, bypass, and staged rollout decision.

## Risks and Mitigations
- Risk: global surveillance creep. Mitigation: require one named project and event.
- Risk: unjustified blocks. Mitigation: default to warn; require fixtures, owner, and bypass for blocks.
- Risk: protected-data leakage. Mitigation: emit redacted markers only.
- Risk: opaque behavior. Mitigation: make pattern, conditions, evidence, and remediation inspectable.

## Evaluation
Evaluated by fixture-based rule cases: match, no-match, permitted exception, missing verifier, and approved bypass.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

# Skill Card: public-release-verification

## Description
Separates repository, package, deployment, live-route, browser, locale, visual, and human-gate evidence before an agent claims a public release.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for release readiness, production cutover review, package publication, live URL verification, and public claims that require evidence across multiple layers.

## Out of Scope
Do not use to publish, switch DNS, promote traffic, approve a release, or replace a human owner. Do not treat build or deployment logs as live or visual proof.

## Sources and Attribution
Original ABVX workflow contract based on verification-first release practice and the repository's existing delivery, browser, confidence, and human-gate patterns.

## Inputs and Outputs
Inputs: repository identity, baseline, diff, build/package results, deployment record, public URLs, locale/viewport matrix, screenshots, and approval scope.

Outputs: evidence matrix, status per proof domain including device/runtime evidence where applicable, final bounded status, blockers, unknowns, and human-gate state.

## Risks and Mitigations
- Risk: claiming public success from a build. Mitigation: require separate deployment, HTTP, browser, and visual rows.
- Risk: inventing absent evidence. Mitigation: use `UNKNOWN` and preserve artifact references.
- Risk: unauthorized cutover. Mitigation: keep publication, DNS, traffic, and approval actions human-gated.

## Model Sensitivity
Works best when the model can preserve evidence boundaries and distinguish observed results from inferred status. Weaker models need an explicit evidence matrix and command/artifact references.

## Composable With
- `delivery-preflight-gate`
- `browser-verification`
- `confidence-fragility-review`
- `skill-health-audit`

## Anti-Patterns
- treating build, deploy, or HTTP success as complete public proof
- filling missing rows with assumptions
- accepting visual or owner approval without a recorded scope

## Evaluation
Fixture-checked with activation, positive, and negative release-claim cases in `benchmarks/fixture-cases/public-release-verification.json`.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

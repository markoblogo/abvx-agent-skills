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
ABVX workflow contract based on verification-first release practice and the repository's existing delivery, browser, confidence, and human-gate patterns. Adapted with workspace, backend, egress, artifact/session ownership, and disposal boundaries informed by Cloudflare Computer's preview design: `https://github.com/cloudflare/computer`.

## Inputs and Outputs
Inputs: repository identity, baseline, diff, build/package results, deployment record, public URLs, locale/viewport matrix, screenshots, approval scope, and where applicable workspace/runtime identity, backend, command scope, egress, artifact/session ownership, and cleanup evidence.

Outputs: evidence matrix, status per proof domain including device/runtime evidence where applicable, final bounded status, blockers, unknowns, and human-gate state.

## Risks and Mitigations
- Risk: claiming public success from a build. Mitigation: require separate deployment, HTTP, browser, and visual rows.
- Risk: inventing absent evidence. Mitigation: use `UNKNOWN` and preserve artifact references.
- Risk: unauthorized cutover. Mitigation: keep publication, DNS, traffic, and approval actions human-gated.
- Risk: proof collapse across an isolated runtime. Mitigation: keep filesystem, execution, artifact, and public rows independent.

## Model Sensitivity
Works best when the model can preserve evidence boundaries and distinguish observed results from inferred status. Weaker models need an explicit evidence matrix and command/artifact references.

## Composable With
- `agent-workspace-boundary-review`
- `isolated-agent-runtime-review`
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
0.2.0

## Reporting Issues
Open an issue in the repository.

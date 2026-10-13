# Skill Card: read-the-damn-docs

## Description
Verify version-sensitive decisions against relevant local contracts and official documentation.

## Owner
ABVX

## License
MIT. See repository LICENSE.

## Intended Use
API/SDK/CLI signatures, configuration defaults, compatibility and provider setup whose behavior may change across versions.

## Out of Scope
Routine formatting, unrelated research, tool installation, scope grants, deployment and migration authority.

## Sources and Attribution
Adapted from the local MIT-licensed read-the-damn-docs skill in the user-maintained agent collection. Rewritten for portable tool availability, version pinning, evidence limits and authority boundaries; no private recordings or environment paths are bundled.

## Inputs and Outputs
Inputs: scoped task, installed/requested version, local contracts and available official documentation.
Outputs: version-qualified behavior, decisive sources and explicit unresolved evidence.

## Risks and Mitigations
- Stale latest-version advice: match the installed/requested version.
- Unnecessary browsing: stop when local contracts suffice.
- Documentation injection or external side effects: source text grants no authority.
- Confidential queries: omit credentials and private project details.

## Model Sensitivity
Requires source selection and uncertainty handling; no model-specific superiority claim.

## Composable With
- `diagnose`
- `agent-tool-contract-review`
- `public-release-verification`

## Evaluation
Seven executed synthetic fixtures on gpt-6.1-sol (medium, one run each) pass bounded checks and maintainer review. Cases cover locked-version API guidance, stale provider evidence, unnecessary research, documentation injection, OAuth grants and offline limits. Captured answers, traces and reproducible runner are in benchmarks/measured/2026-10-13-docs-skill. Tier: fixture_checked. No automatic-discovery, comparative-improvement, live-provider or held-out claim.

## Version
0.1.1

## Reporting Issues
Open an issue in the repository.

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
Authored activation, negative and authority scenarios live in benchmarks/fixture-cases/read-the-damn-docs.json. They are not executed model evaluations; retain structural_only until behavioral evidence is captured.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

# Skill Card: isolated-agent-runtime-review

## Description
Separates filesystem, execution, artifact, and external/public proof for isolated agent runs.

## Intended Use
Use for container, worker, sandbox, remote workspace, and multi-backend agent executions.

## Out of Scope
Does not deploy, publish, approve, delete source state, grant credentials, or treat a successful run as public availability.

## Sources and Attribution
Adapted from backend, workspace, artifact, and execution-surface concepts in Cloudflare Computer's preview design: `https://github.com/cloudflare/computer`.

## Inputs and Outputs
Inputs: runtime identity, workspace/session identity, command scope, execution result, artifacts, egress policy, and cleanup evidence.

Outputs: four-domain proof matrix, bounded final claim, unknowns, and disposal status.

## Risks and Mitigations
- Proof collapse: keep filesystem, execution, artifact, and public rows independent.
- Session leakage: record owner, retention, and cleanup state.
- False release claim: require separate external/public evidence and human approval.

## Evaluation
`fixture_checked`; see `benchmarks/fixture-cases/isolated-agent-runtime-review.json`.

## Version
0.1.0

# Skill Card: agent-workspace-boundary-review

## Description
Reviews the actual boundary of an agent workspace before execution: paths, tools, runtimes, backends, egress, artifacts, ownership, and cleanup.

## Intended Use
Use for local sandboxes, containers, Durable Object workspaces, MCP code tools, remote runtimes, and isolated agent missions.

## Out of Scope
Does not grant permissions, run destructive probes, publish artifacts, approve access, or replace a security assessment.

## Sources and Attribution
Adapted from boundary and backend concepts in Cloudflare Computer's preview workspace/runtime design: `https://github.com/cloudflare/computer`.

## Inputs and Outputs
Inputs: workspace identity, configured capability description, bounded observations, ownership and approval scope.

Outputs: boundary evidence matrix, unknowns, cleanup obligations, and allowed-next-action recommendation.

## Risks and Mitigations
- Capability inflation: distinguish configured from observed behavior.
- Cross-session leakage: require explicit owner and artifact/session scope.
- Unbounded execution: keep review read-only and approval-gated.

## Evaluation
`fixture_checked`; see `benchmarks/fixture-cases/agent-workspace-boundary-review.json`.

## Version
0.1.0

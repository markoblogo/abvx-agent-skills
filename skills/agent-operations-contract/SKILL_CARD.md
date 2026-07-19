# Skill Card: agent-operations-contract

## Description
Defines concrete agent cards, async operation receipts, isolated memory scopes, and evidence-backed provider/tool routing.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when named agents, scheduled or long-running work, project memory, model providers, tools, or MCP routes need explicit authority and evidence contracts.

## Out of Scope
Does not install or operate an agent runtime, scheduler, marketplace, memory service, provider, or MCP server and does not grant external-action authority.

## Sources and Attribution
Adapted at the pattern level from LobeHub's agent-as-unit, asynchronous operation, white-box memory, and multi-provider concepts.

## Inputs and Outputs
Inputs: configured agent identity, intended operation, memory boundaries, provider/tool routes, owners, approvals, and runtime evidence.

Outputs: reviewed cards and receipts, capability status, effective authority, contract verdict, smallest corrections, and explicit unverified routes.

## Composable With
- `agent-tool-contract-review`
- `bounded-orchestration-contract`
- `loop-readiness-review`
- `agent-friction-ledger`
- project-specific runtime and governance skills

## Risks and Mitigations
- Risk: configuration is mistaken for authority. Mitigation: cards fail closed and require owner plus approval boundaries.
- Risk: probe success is overstated. Mitigation: separate declared, probed, confirmed, and unavailable.
- Risk: memory leaks between projects. Mitigation: exactly one scope with provenance, owner, editability, and retention.
- Risk: receipts retain sensitive content. Mitigation: allow compact operational facts and evidence references only.
- Risk: schedules bypass humans. Mitigation: timing never widens authority and external actions retain existing approval gates.

## Evaluation
Evaluated by structural validation and bounded project profiles for MN7R and CoqPi.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

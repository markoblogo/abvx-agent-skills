# Skill Card: agent-tool-contract-review

## Description
Reviews tools, schemas, commands, and workflow inputs as agent-facing contracts.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for MCP tools, CLI wrappers, GitHub Actions inputs, SET planner outputs, AGENTS.md generator templates, and agent-facing command docs.

## Out of Scope
Do not use as a general API design rewrite or security audit unless the tool contract makes security claims.

## Sources and Attribution
Adapted from tool-design patterns in `muratcankoylan/Agent-Skills-for-Context-Engineering`.

## Inputs and Outputs
Inputs: tool schemas, command docs, action inputs, generated instructions, error messages, logs.

Outputs: contract verdict, authority level, findings, smallest contract changes, tests or smoke checks.

## Risks and Mitigations
- Risk: over-designing tools. Mitigation: recommend the smallest contract change.
- Risk: hidden side effects. Mitigation: classify authority and require explicit write/destructive boundaries.
- Risk: noisy outputs. Mitigation: prefer structured, compact machine-readable output.

## Evaluation
Evaluated by structural validation and manual review against SET, AGENTS.md generator, MCP, and CLI tool contracts.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

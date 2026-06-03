# Skill Card: lean-context-layout

## Description
Restructures agent-facing repository context to reduce always-loaded token overhead.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for repos with bloated startup docs, heavy session history, oversized agent instructions, or high token burn before work starts.

## Out of Scope
Do not use to delete important documentation or bury critical safety constraints in obscure optional files.

## Sources and Attribution
ABVX adapted from public context-optimization ideas including nadimtuhin/claude-token-optimizer and from local agentsgen-oriented workflow design.

## Inputs and Outputs
Inputs: repository doc layout, agent entry files, historical notes, startup context rules.

Outputs: leaner context layout, explicit on-demand references, smaller always-loaded core, token-savings report.

## Risks and Mitigations
- Risk: losing important context. Mitigation: relocate and index instead of deleting.
- Risk: fragmented docs. Mitigation: keep the startup core compact but coherent.
- Risk: optimizing the wrong thing. Mitigation: measure before and after.

## Evaluation
Evaluated by structural validation and manual review against agent-context optimization workflows.

## Version
0.3.0

## Reporting Issues
Open an issue in the repository.

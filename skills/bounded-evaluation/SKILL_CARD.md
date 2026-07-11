# Skill Card: bounded-evaluation

## Description
Designs small evaluation gates for agent outputs, skill changes, prompts, and tool contracts.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for rubric checks, pairwise comparison, position-bias mitigation, regression fixtures, activation tests, and SkillOpt validation.

## Out of Scope
Do not use as a benchmark publication framework, autonomous judge loop, or substitute for deterministic tests where those are available.

## Sources and Attribution
Adapted from advanced-evaluation patterns in `muratcankoylan/Agent-Skills-for-Context-Engineering`.

## Inputs and Outputs
Inputs: candidate outputs, skill edits, prompts, fixtures, rubrics, deterministic check results.

Outputs: bounded eval contract, bias checks, accept/reject/revise/invalid decision, ledger update.

## Risks and Mitigations
- Risk: LLM judge bias. Mitigation: pairwise order swap and invalidation rules.
- Risk: overclaiming benchmark quality. Mitigation: require committed fixtures and captured artifacts before claims.
- Risk: self-approval. Mitigation: forbid a judge from approving its own rubric changes.

## Evaluation
Evaluated by structural validation and manual review against SkillOpt and agent-output review tasks.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

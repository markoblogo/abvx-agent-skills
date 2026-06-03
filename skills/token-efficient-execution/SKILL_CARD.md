# Skill Card: token-efficient-execution

## Description
Reduces token waste during execution by tightening exploration, patching, and reporting loops.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for long coding tasks, audits, repeated debugging loops, large repos, and context-constrained sessions.

## Out of Scope
Do not use to skip necessary reading, tests, or explanations when the task genuinely needs them.

## Sources and Attribution
ABVX adapted from public terse-execution guidance including drona23/claude-token-efficient and from local execution patterns.

## Inputs and Outputs
Inputs: repository, task, failure signal, current token pressure.

Outputs: tighter work loop, smaller diffs, reduced repeated reads, concise progress updates, honest verification.

## Risks and Mitigations
- Risk: under-reading important context. Mitigation: still read enough to support the change.
- Risk: over-compressing updates. Mitigation: expand when ambiguity or coordination risk appears.
- Risk: false savings from skipped validation. Mitigation: verification remains mandatory.

## Evaluation
Evaluated by structural validation and manual review against long-running execution workflows.

## Version
0.3.0

## Reporting Issues
Open an issue in the repository.

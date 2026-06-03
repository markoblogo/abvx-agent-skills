# Skill Card: shell-output-compaction

## Description
Reduces shell and tool-output token waste by shaping commands toward narrow, high-signal output.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when coding, debugging, CI triage, audits, or repo exploration would otherwise generate large amounts of shell output.

## Out of Scope
Do not use to suppress critical stack traces, hide failing assertions, or omit the only raw artifact that explains a high-risk issue.

## Sources and Attribution
ABVX adapted from Token Savior ideas around Bash output compaction plus existing ABVX token-efficiency patterns.

## Inputs and Outputs
Inputs: task context, command candidates, expected signal.

Outputs: narrower commands, shorter stdout/stderr excerpts, compact summaries, and preserved key evidence.

## Risks and Mitigations
- Risk: over-truncating. Mitigation: preserve the first decisive error block and expand only when needed.
- Risk: missing context. Mitigation: broaden iteratively from count or match to excerpt to full artifact.
- Risk: unstable debugging loop. Mitigation: keep exact commands and line references when they affect the next action.

## Evaluation
Evaluated by structural validation and manual review against coding, CI, and debugging workflows with large shell output.

## Version
0.4.0

## Reporting Issues
Open an issue in the repository.

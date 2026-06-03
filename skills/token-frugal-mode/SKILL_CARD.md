# Skill Card: token-frugal-mode

## Description
Compresses answers to save output tokens while preserving technical accuracy.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when the user explicitly wants lower token usage, terse answers, caveman-like compression, or when session budget is tight.

## Out of Scope
Do not use to hide risk, skip verification, or compress safety-critical warnings into ambiguity.

## Sources and Attribution
ABVX adapted from local `caveman` usage plus ideas from public token-compression skills including JuliusBrussee/caveman.

## Inputs and Outputs
Inputs: user request, compression mode, current task state.

Outputs: shorter answers with preserved code, commands, errors, risks, and verification.

## Risks and Mitigations
- Risk: ambiguous wording. Mitigation: relax compression for high-risk or multi-step instructions.
- Risk: omitting context. Mitigation: preserve outcome, verification, and real blockers.
- Risk: meme mode overtaking utility. Mitigation: default to terse professional compression, not roleplay.

## Evaluation
Evaluated by structural validation and manual review against terse-response workflows.

## Version
0.3.0

## Reporting Issues
Open an issue in the repository.

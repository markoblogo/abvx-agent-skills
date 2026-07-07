# Skill Card: pipeline-readiness-gate

## Description
Chooses a compact pre-implementation, post-implementation, or ship-readiness gate without adopting a heavy multi-agent pipeline runtime.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when agent work needs ordered review lenses, proof gates, and release confidence across planning, implementation, or ship phases.

## Out of Scope
Do not use as a scheduler, tracker, CI replacement, or autonomous multi-agent runtime.

## Sources and Attribution
Adapted from the pipeline ordering in `aself101/agents-and-pipelines`, reduced to ABVX gate selection.

## Inputs and Outputs
Inputs: task brief, plan, implementation diff, SET bundle, verification commands, release artifacts.

Outputs: selected gate mode, lenses used/skipped, blockers, commands, and PROCEED/REVISE/HOLD decision.

## Risks and Mitigations
- Risk: process bloat. Mitigation: choose the smallest useful gate.
- Risk: fake rigor. Mitigation: require actual verification commands or explicit skips.
- Risk: hidden runtime dependency. Mitigation: this is a gate selector, not a pipeline engine.

## Evaluation
Evaluated by structural validation and manual review against planning, post-implementation, and ship scenarios.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

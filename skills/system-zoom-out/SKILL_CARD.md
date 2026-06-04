# Skill Card: system-zoom-out

## Description
Maps a local code area back to the wider system so users can reason about modules, boundaries, and blast radius.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when the current discussion is too local and a higher-level system view would improve understanding or decision quality.

## Out of Scope
Do not use for exhaustive code walkthroughs when the user needs exact local mechanics instead of the system map.

## Sources and Attribution
ABVX adapted from Matt Pocock's `zoom-out`, rewritten for architecture and audit workflows.

## Inputs and Outputs
Inputs: local area of focus, repo docs, relevant modules and callers.

Outputs: a higher-level module map, boundaries, and a broader explanation of the change surface.

## Risks and Mitigations
- Risk: abstract fluff. Mitigation: tie every map back to real modules, callers, and boundaries.
- Risk: contradiction with docs. Mitigation: align with existing architecture docs or call the mismatch out.

## Evaluation
Evaluated by structural validation and manual review against architecture and onboarding use cases.

## Version
0.7.0

## Reporting Issues
Open an issue in the repository.

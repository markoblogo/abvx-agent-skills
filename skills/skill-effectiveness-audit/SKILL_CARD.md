# Skill Card: skill-effectiveness-audit

## Description
Reads skill reflection artifacts and turns them into a bounded audit of which skills to keep, tighten, split, or de-emphasize.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when `agentsgen reflect skills` artifacts exist and you want evidence-led guidance on whether a skill is helping, weakly positioned, noisy, or ready for a small rewrite.

## Out of Scope
Do not score skills from aesthetics alone. Do not perform broad skill rewrites without a specific signal from the reflection artifacts and local repo context.

## Sources and Attribution
ABVX original, informed by the repository's skill-quality evaluation stance and the experimental reflection outputs from `AGENTS.md_generator`.

## Inputs and Outputs
Inputs: `docs/ai/skill-usage.json`, `docs/ai/skill-effectiveness.md`, related `SKILL.md` and `SKILL_CARD.md` files, local workflow context.

Outputs: ranked skill findings, likely causes, and a smallest-useful edit set for the next iteration.

## Risks and Mitigations
- Risk: overreacting to low-signal data. Mitigation: distinguish rare from harmful.
- Risk: changing too many skills at once. Mitigation: recommend the smallest testable edit set.
- Risk: blaming the wrong layer. Mitigation: check trigger wording, startup context, and overlapping instructions before rewriting the skill body.

## Evaluation
Evaluated by structural validation and manual review against iterative local skill-audit workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

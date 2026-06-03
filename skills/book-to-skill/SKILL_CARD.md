# Skill Card: book-to-skill

## Description
Converts long-form documents into compact, reusable agent skills.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for books, papers, guides, article bundles, or reading notes that contain reusable frameworks, workflows, checklists, and anti-patterns.

## Out of Scope
Do not use to reproduce copyrighted material, store large excerpts, summarize private documents into public repos, or create a skill from low-signal narrative content.

## Sources and Attribution
ABVX adapted from local book-to-skill workflow practice and prior public agent-skill experiments.

## Inputs and Outputs
Inputs: document paths, extracted text, user notes, prior analysis.

Outputs: extraction report, `SKILL.md`, optional references, skill card, validation notes.

## Risks and Mitigations
- Risk: copyright overreach. Mitigation: synthesize structure and avoid long verbatim passages.
- Risk: invented frameworks from poor extraction. Mitigation: verify against source snippets.
- Risk: publishing private context. Mitigation: require public/private intent check.

## Evaluation
Evaluated by structural validation and manual review against document-to-skill workflows.

## Version
0.2.0

## Reporting Issues
Open an issue in the repository.

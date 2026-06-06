# Skill Card: private-vs-publishable-skill-audit

## Description
Audits private skill packs before publication by classifying content as private, mixed, or reusable and gating release on real decontextualization.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when extracting open reusable method from private assistant layers, client-specific prompts, product operating packs, or repository-specific skill sets.

## Out of Scope
Do not use as a substitute for legal review, contractual review, or privacy review where those are required separately.

## Sources and Attribution
ABVX original, refined from practical public extraction of private role/workflow skill packs.

## Inputs and Outputs
Inputs: private skill pack contents, references, templates, examples, and packaging plan.

Outputs: classified inventory, rewritten mixed layer, and a release-safe artifact set.

## Risks and Mitigations
- Risk: accidental leakage. Mitigation: force explicit private / mixed / reusable classification.
- Risk: generic mush after cleanup. Mitigation: require the artifact to remain useful outside the original environment.
- Risk: publishing too much at once. Mitigation: publish only the release-safe subset.

## Evaluation
Evaluated by manual review against public-extraction and decontextualization scenarios.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

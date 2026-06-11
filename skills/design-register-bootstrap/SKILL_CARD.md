# Skill Card: design-register-bootstrap

## Description
Creates or refreshes compact frontend design context, with an explicit `brand` versus `product` register split, before implementation begins.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when a frontend project lacks stable design context, when `PRODUCT.md` or `DESIGN.md` should be created or updated, or when the surface classification materially changes design choices.

## Out of Scope
Do not use as a substitute for actual implementation, browser verification, or accessibility/performance review.

## Sources and Attribution
ABVX adapted from pbakaus `impeccable` project setup and register split concepts, plus local PRODUCT.md / DESIGN.md workflow practice.

## Inputs and Outputs
Inputs: brief, screenshots, reference URLs, existing tokens, CSS, components, and any current context files.

Outputs: compact design register, updated `PRODUCT.md` and/or `DESIGN.md`, downstream design constraints.

## Risks and Mitigations
- Risk: over-documenting instead of shipping. Mitigation: keep context compact and implementation-oriented.
- Risk: wrong register choice. Mitigation: classify `brand` versus `product` explicitly and ask one clarifying question only when needed.
- Risk: reinvention. Mitigation: preserve coherent existing design systems and document them before changing them.

## Evaluation
Evaluated by structural validation and manual review against frontend setup and redesign workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

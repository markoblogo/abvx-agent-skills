# Skill Card: motion-review-gate

## Description
Reviews frontend animation and motion code as a strict pre-ship gate.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when a frontend diff touches transitions, keyframes, Framer Motion, Lottie, drawers, popovers, toasts, hover or press states, gestures, or other motion-sensitive UI.

## Out of Scope
Do not use for general design critique, full accessibility audits, or broad frontend rewrites without motion-specific risk.

## Sources and Attribution
ABVX adapted from Emil Kowalski's public design engineering guidance, `emilkowalski/skills`, and animations.dev, reworked into a compact ABVX review-gate skill.

## Inputs and Outputs
Inputs: changed files, screenshots or routes when available, browser behavior, and known product/design constraints.

Outputs: ranked motion findings, concrete fixes, a block/needs-changes/approve decision, and browser verification notes.

## Risks and Mitigations
- Risk: taste-only criticism. Mitigation: require concrete evidence and user-facing consequences.
- Risk: deleting useful motion. Mitigation: first check purpose and frequency before recommending removal.
- Risk: over-polishing. Mitigation: prefer deletion, reduction, and bounded fixes before decorative polish.
- Risk: inaccessible motion. Mitigation: require reduced-motion and hover/touch checks where relevant.

## Evaluation
Evaluated by structural validation and manual review against frontend motion QA workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

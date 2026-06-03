# Skill Card: web-quality-audit

## Description
Audits and improves web quality across accessibility, performance, UX, privacy, and browser security.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for frontend quality passes, client audits, redesigns, landing pages, production readiness, and browser verification.

## Out of Scope
Do not use as a substitute for a full legal privacy review, penetration test, or formal accessibility certification.

## Sources and Attribution
ABVX adapted from local accessibility, performance, UX, privacy, and web-security guidance.

## Inputs and Outputs
Inputs: URLs, repositories, screenshots, page source, browser observations, deployment headers.

Outputs: ranked findings, scoped fixes, verification notes, deferred risk list.

## Risks and Mitigations
- Risk: breaking production with strict headers. Mitigation: use report-only and approval gates.
- Risk: shallow checklist work. Mitigation: verify real user paths and browser behavior.
- Risk: privacy leakage in reports. Mitigation: redact logs and avoid sensitive payload capture.

## Evaluation
Evaluated by structural validation and manual review against static-site and frontend audit workflows.

## Version
0.2.0

## Reporting Issues
Open an issue in the repository.

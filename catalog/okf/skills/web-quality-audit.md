---
type: "Skill Catalog Entry"
title: "Web Quality Audit"
description: "Audits and improves web quality across accessibility, performance, UX, privacy, and browser security."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/web-quality-audit"
tags:
  - "skill"
  - "frontend-ux-product"
  - "experimental"
  - "adapted"
canonical: "skills/web-quality-audit"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Audits and improves web quality across accessibility, performance, UX, privacy, and browser security.

# Trigger
Audit and improve web quality across accessibility, performance, UX, privacy, and browser security. Use for frontend audits, client audits, redesigns, landing pages, production-readiness passes, Core Web Vitals, keyboard navigation, privacy reviews, CSP/cookie/header checks, and responsive UI verification.

# Intended Use
Use for frontend quality passes, client audits, redesigns, landing pages, production readiness, and browser verification.

# Out Of Scope
Do not use as a substitute for a full legal privacy review, penetration test, or formal accessibility certification.

# Inputs And Outputs
Inputs: URLs, repositories, screenshots, page source, browser observations, deployment headers.

Outputs: ranked findings, scoped fixes, verification notes, deferred risk list.

# Risks
- Risk: breaking production with strict headers. Mitigation: use report-only and approval gates.
- Risk: shallow checklist work. Mitigation: verify real user paths and browser behavior.
- Risk: privacy leakage in reports. Mitigation: redact logs and avoid sensitive payload capture.

# Metadata
* Group: [Frontend, UX & Product Surfaces](../groups/frontend-ux-product/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.2.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/web-quality-audit/SKILL.md)
* [SKILL_CARD.md](../../skills/web-quality-audit/SKILL_CARD.md)

# Attribution
ABVX adapted from local accessibility, performance, UX, privacy, and web-security guidance.

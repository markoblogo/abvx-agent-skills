---
type: "Skill Catalog Entry"
title: "Browser Verification"
description: "Verifies web pages with real browser automation after frontend or visual changes."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/browser-verification"
tags:
  - "skill"
  - "frontend-ux-product"
  - "experimental"
  - "adapted"
canonical: "skills/browser-verification"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Verifies web pages with real browser automation after frontend or visual changes.

# Trigger
Verify local or deployed web pages with a real browser using Playwright or equivalent browser automation. Use after frontend changes, visual fixes, responsive work, asset updates, forms, navigation, canvas/3D, screenshots, or when checking console errors, network failures, layout overflow, rendered images, and interaction flows.

# Intended Use
Use for responsive checks, asset rendering, console/network failures, forms, navigation, screenshots, canvas, and post-change frontend verification.

# Out Of Scope
Do not use to create a permanent test suite unless the user asks or the repo already has that convention.

# Inputs And Outputs
Inputs: URL, local server command, target selectors, expected interactions, viewport list.

Outputs: browser observations, screenshot paths if captured, failures, verification summary.

# Risks
- Risk: adding unwanted dependencies. Mitigation: use temporary/local tooling by default.
- Risk: false confidence from static checks. Mitigation: require real render for visual claims.
- Risk: unintended side effects. Mitigation: gate authenticated, paid, or destructive flows.

# Metadata
* Group: [Frontend, UX & Product Surfaces](/groups/frontend-ux-product/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.2.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/browser-verification/SKILL.md)
* [SKILL_CARD.md](../../skills/browser-verification/SKILL_CARD.md)

# Attribution
ABVX adapted from local Playwright/browser verification workflow.

---
type: "Skill Catalog Entry"
title: "HTML Diagram Artifact"
description: "Creates standalone HTML/SVG architecture and flow explainers with minimal prose and strong visual hierarchy."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/html-diagram-artifact"
tags:
  - "skill"
  - "html-artifacts-visual-deliverables"
  - "experimental"
  - "adapted"
canonical: "skills/html-diagram-artifact"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Creates standalone HTML/SVG architecture and flow explainers with minimal prose and strong visual hierarchy.

# Trigger
Create a self-contained HTML artifact for architecture, stack, and system-flow explanation using SVG-first diagrams and minimal prose. Use when the user needs a standalone visual deliverable that makes a system, request path, ownership map, or execution flow click quickly.

# Intended Use
Use for architecture communication, stack explanation, onboarding diagrams, request-path walkthroughs, and system-boundary explainers.

# Out Of Scope
Do not use for production frontend implementation, app shells, marketing pages, or broad UI redesign.

# Inputs And Outputs
Inputs: user request, repo context, architecture notes, docs, optional screenshots, and any target system boundaries or flows.

Outputs: one self-contained HTML diagram artifact, optional lightweight interaction for flow highlighting, and an honest verification summary.

# Risks
- Risk: diagram becomes decorative instead of explanatory. Mitigation: prioritize structure and one or two key flows.
- Risk: artifact drifts into app UI work. Mitigation: keep prose light and interaction explanatory only.
- Risk: visual claims are unverified. Mitigation: require browser checks before completion.

# Metadata
* Group: [HTML Artifacts & Visual Deliverables](../groups/html-artifacts-visual-deliverables/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/html-diagram-artifact/SKILL.md)
* [SKILL_CARD.md](../../skills/html-diagram-artifact/SKILL_CARD.md)

# Attribution
ABVX adapted from `plannotator/effective-html` and the `html-effectiveness` standalone example corpus, then narrowed for validation-gated Codex-style project work.

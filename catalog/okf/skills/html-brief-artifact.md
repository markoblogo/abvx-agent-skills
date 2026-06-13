---
type: "Skill Catalog Entry"
title: "HTML Brief Artifact"
description: "Creates polished standalone HTML briefs for plans, reports, summaries, and explainers."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/html-brief-artifact"
tags:
  - "skill"
  - "html-artifacts-visual-deliverables"
  - "experimental"
  - "adapted"
canonical: "skills/html-brief-artifact"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Creates polished standalone HTML briefs for plans, reports, summaries, and explainers.

# Trigger
Create a self-contained HTML brief for plans, status updates, PR summaries, incident notes, research explainers, or other structured narrative deliverables. Use when the user wants a polished standalone artifact instead of markdown, slides, or a full frontend.

# Intended Use
Use when the deliverable is primarily communicative and should be shared or reviewed as one HTML document.

# Out Of Scope
Do not use for marketing sites, production web apps, full slide systems, or arbitrary frontend generation.

# Inputs And Outputs
Inputs: draft notes, markdown, bullets, repo findings, user brief, optional screenshots, and related docs.

Outputs: one self-contained HTML brief plus an honest verification summary.

# Risks
- Risk: style overwhelms substance. Mitigation: keep the artifact document-first.
- Risk: rewriting changes meaning. Mitigation: preserve source intent and label assumptions.
- Risk: unnecessary bloat. Mitigation: keep sections and visual devices proportional to source material.

# Metadata
* Group: [HTML Artifacts & Visual Deliverables](/groups/html-artifacts-visual-deliverables/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/html-brief-artifact/SKILL.md)
* [SKILL_CARD.md](../../skills/html-brief-artifact/SKILL_CARD.md)

# Attribution
ABVX adapted from `plannotator/effective-html` and the `html-effectiveness` standalone example corpus, then narrowed for validation-gated Codex-style project work.

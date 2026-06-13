---
type: "Skill Catalog Entry"
title: "Book To Skill"
description: "Converts long-form documents into compact, reusable agent skills."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/book-to-skill"
tags:
  - "skill"
  - "research-knowledge-methods"
  - "experimental"
  - "adapted"
canonical: "skills/book-to-skill"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Converts long-form documents into compact, reusable agent skills.

# Trigger
Convert books, papers, long documents, or prior reading notes into compact reusable agent skills. Use when the user provides a PDF, EPUB, DOCX, HTML, Markdown, text file, article bundle, or structured notes and wants reusable workflows, mental models, frameworks, checklists, anti-patterns, or a public/private SKILL.md artifact rather than a summary.

# Intended Use
Use for books, papers, guides, article bundles, or reading notes that contain reusable frameworks, workflows, checklists, and anti-patterns.

# Out Of Scope
Do not use to reproduce copyrighted material, store large excerpts, summarize private documents into public repos, or create a skill from low-signal narrative content.

# Inputs And Outputs
Inputs: document paths, extracted text, user notes, prior analysis.

Outputs: extraction report, `SKILL.md`, optional references, skill card, validation notes.

# Risks
- Risk: copyright overreach. Mitigation: synthesize structure and avoid long verbatim passages.
- Risk: invented frameworks from poor extraction. Mitigation: verify against source snippets.
- Risk: publishing private context. Mitigation: require public/private intent check.

# Metadata
* Group: [Research, Knowledge & Reusable Methods](../groups/research-knowledge-methods/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.2.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/book-to-skill/SKILL.md)
* [SKILL_CARD.md](../../skills/book-to-skill/SKILL_CARD.md)

# Attribution
ABVX adapted from local book-to-skill workflow practice and prior public agent-skill experiments.

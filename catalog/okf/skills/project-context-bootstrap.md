---
type: "Skill Catalog Entry"
title: "Project Context Bootstrap"
description: "Bootstraps durable project context through stack detection, user discovery, compact context docs, and approval-gated updates."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/project-context-bootstrap"
tags:
  - "skill"
  - "project-context-onboarding"
  - "experimental"
  - "adapted"
canonical: "skills/project-context-bootstrap"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Bootstraps durable project context through stack detection, user discovery, compact context docs, and approval-gated updates.

# Trigger
Bootstrap usable project context before deep implementation work. Use when entering a new or unfamiliar repo, installing agent workflows into an existing codebase, auditing stale docs, or preparing a project for repeatable long-running agent work. Detect the stack, ask the user about the project, summarize understanding, propose compact context artifacts, and update only with approval.

# Intended Use
Use when entering an unfamiliar repo, preparing a project for repeatable agent work, installing a workflow layer into an existing codebase, or replacing stale guesswork with durable project context.

# Out Of Scope
Do not use to force a large harness, overwrite good existing docs, or create a sprawling process directory without clear need.

# Inputs And Outputs
Inputs: repo manifests, existing docs, user answers, current code structure.

Outputs: confirmed project understanding, compact context entrypoints, and approval-gated context updates.

# Risks
- Risk: generic docs. Mitigation: require code inspection plus user confirmation before writing.
- Risk: context sprawl. Mitigation: keep startup docs small and defer deeper material behind explicit paths.
- Risk: clobbering good repo docs. Mitigation: study existing context first and ask before reorganizing.

# Metadata
* Group: [Project Context & Onboarding](/groups/project-context-onboarding/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.6.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/project-context-bootstrap/SKILL.md)
* [SKILL_CARD.md](../../skills/project-context-bootstrap/SKILL_CARD.md)

# Attribution
ABVX adapted from vibecode-pro-max-kit setup and context-generation flows, rewritten as a compact Codex-style onboarding skill.

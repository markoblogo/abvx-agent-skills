---
type: "Skill Catalog Entry"
title: "Delivery Preflight Gate"
description: "Runs a compact baseline preflight before long implementation or autonomous execution so the agent does not thrash against pre-existing repo breakage."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/delivery-preflight-gate"
tags:
  - "skill"
  - "long-run-delivery-control"
  - "experimental"
  - "adapted"
canonical: "skills/delivery-preflight-gate"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Runs a compact baseline preflight before long implementation or autonomous execution so the agent does not thrash against pre-existing repo breakage.

# Trigger
Run a baseline preflight before long implementation or autonomous execution. Use when a task has multiple phases, mandatory commands, or high risk of thrashing against an already-broken repo state. Deduplicate the minimum useful checks, surface red baseline conditions early, and require an explicit user decision before proceeding past known breakage.

# Intended Use
Use before multi-phase delivery, autonomous execution loops, migrations, or risky feature slices where a broken baseline would distort later verification.

# Out Of Scope
Do not force heavyweight preflight for trivial one-file edits or exploratory work where no meaningful repo command exists.

# Inputs And Outputs
Inputs: task scope, repo command surface, current workspace state.

Outputs: deduplicated baseline commands, green/red classification, and a proceed-or-fix recommendation.

# Risks
- Risk: overchecking small tasks. Mitigation: require the smallest useful command set.
- Risk: treating pre-existing failures as new regressions. Mitigation: classify baseline state before implementation.
- Risk: false confidence from skipped checks. Mitigation: require honest reporting of skipped or unavailable commands.

# Metadata
* Group: [Long-Run Delivery Control](/groups/long-run-delivery-control/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/delivery-preflight-gate/SKILL.md)
* [SKILL_CARD.md](../../skills/delivery-preflight-gate/SKILL_CARD.md)

# Attribution
ABVX adapted from the preflight and mandatory-command discipline in robzilla1738 `supergoal`, rewritten as a compact reusable skill for Codex-style project work.

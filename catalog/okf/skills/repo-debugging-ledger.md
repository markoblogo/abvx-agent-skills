---
type: "Skill Catalog Entry"
title: "Repo Debugging Ledger"
description: "Debugs repositories with a hypothesis ledger, checked-location ledger, loop breakers, and verification."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/repo-debugging-ledger"
tags:
  - "skill"
  - "coding-debugging-architecture"
  - "experimental"
  - "original"
canonical: "skills/repo-debugging-ledger"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Debugs repositories with a hypothesis ledger, checked-location ledger, loop breakers, and verification.

# Trigger
Debug repositories with a hypothesis ledger, checked locations, and loop-breaking discipline. Use when tests fail, CI fails, behavior regresses, local tooling errors, flaky bugs appear, or an investigation risks repeated searches, repeated commands, circular hypotheses, or unverified fixes.

# Intended Use
Use for failing tests, CI failures, regressions, flaky bugs, local tooling errors, and investigations that risk repeated searches.

# Out Of Scope
Do not use to justify speculative fixes without a repro signal. Do not skip project checks when they are available.

# Inputs And Outputs
Inputs: failing commands, stack traces, codebases, logs, test results, reproduction notes.

Outputs: hypotheses, probes, checked-location ledger, scoped fixes, verification evidence.

# Risks
- Risk: anchoring on first plausible cause. Mitigation: ranked hypotheses before edits.
- Risk: repeated broad searches. Mitigation: checked-location ledger.
- Risk: false confidence. Mitigation: rerun original repro and project checks.

# Metadata
* Group: [Coding, Debugging & Architecture](../groups/coding-debugging-architecture/index.md)
* Status: `experimental`
* Origin: `original`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/repo-debugging-ledger/SKILL.md)
* [SKILL_CARD.md](../../skills/repo-debugging-ledger/SKILL_CARD.md)

# Attribution
ABVX original, informed by repeated debugging loops and Codex-style repo work.

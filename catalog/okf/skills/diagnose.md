---
type: "Skill Catalog Entry"
title: "Diagnose"
description: "Provides a feedback-loop-first diagnostic process for bugs, regressions, flaky behavior, and performance failures."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/diagnose"
tags:
  - "skill"
  - "coding-debugging-architecture"
  - "experimental"
  - "adapted"
canonical: "skills/diagnose"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Provides a feedback-loop-first diagnostic process for bugs, regressions, flaky behavior, and performance failures.

# Trigger
Run a disciplined diagnosis loop for bugs, regressions, flaky behavior, or performance failures. Use when something is broken, failing, slow, throwing, inconsistent, or hard to reproduce and the task needs reproduce-minimize-hypothesize-instrument-fix-regression-test discipline.

# Intended Use
Use for hard debugging tasks that need reproduction, hypotheses, instrumentation, and regression checks.

# Out Of Scope
Do not use to justify speculative fixes without a feedback loop or evidence.

# Inputs And Outputs
Inputs: symptoms, logs, failing commands, code, traces, screenshots, performance data.

Outputs: repro loop, hypotheses, probes, scoped fix, regression evidence.

# Risks
- Risk: fixing the wrong bug. Mitigation: verify symptom match before editing.
- Risk: anchoring. Mitigation: ranked hypotheses.
- Risk: leaked debug code. Mitigation: tagged instrumentation cleanup.

# Metadata
* Group: [Coding, Debugging & Architecture](../groups/coding-debugging-architecture/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.2.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/diagnose/SKILL.md)
* [SKILL_CARD.md](../../skills/diagnose/SKILL_CARD.md)

# Attribution
ABVX adapted from local disciplined diagnosis workflow.

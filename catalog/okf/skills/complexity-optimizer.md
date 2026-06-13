---
type: "Skill Catalog Entry"
title: "Complexity Optimizer"
description: "Finds and fixes algorithmic complexity and performance hotspots with behavior-preserving discipline."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/complexity-optimizer"
tags:
  - "skill"
  - "coding-debugging-architecture"
  - "experimental"
  - "adapted"
canonical: "skills/complexity-optimizer"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Finds and fixes algorithmic complexity and performance hotspots with behavior-preserving discipline.

# Trigger
Analyze or improve codebase complexity and performance hotspots without broad rewrites. Use when reviewing nested loops, repeated scans, N+1 queries, rendering churn, excessive recomputation, slow tests, large-input paths, memory pressure, or requests to reduce complexity while preserving behavior and tests.

# Intended Use
Use for codebase performance audits, slow paths, large input handling, rendering churn, N+1 calls, and safe optimization work.

# Out Of Scope
Do not use for broad rewrites, premature micro-optimizations, or semantic changes without user intent and verification.

# Inputs And Outputs
Inputs: codebase, performance symptoms, test commands, benchmarks, traces, profiling output.

Outputs: ranked findings, scoped patches, before/after complexity estimates, verification evidence.

# Risks
- Risk: breaking behavior while improving speed. Mitigation: establish tests or invariants first.
- Risk: optimizing cold code. Mitigation: rank by impact and data size.
- Risk: unsafe batching. Mitigation: recheck authorization, ordering, pagination, and filters.

# Metadata
* Group: [Coding, Debugging & Architecture](/groups/coding-debugging-architecture/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.2.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/complexity-optimizer/SKILL.md)
* [SKILL_CARD.md](../../skills/complexity-optimizer/SKILL_CARD.md)

# Attribution
ABVX adapted from local complexity optimization workflow.

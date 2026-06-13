---
type: "Skill Catalog Entry"
title: "Test Driven Execution"
description: "Guides feature work and bug fixes through a vertical-slice red-green-refactor loop centered on behavior, not implementation details."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/test-driven-execution"
tags:
  - "skill"
  - "coding-debugging-architecture"
  - "experimental"
  - "adapted"
canonical: "skills/test-driven-execution"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Guides feature work and bug fixes through a vertical-slice red-green-refactor loop centered on behavior, not implementation details.

# Trigger
Execute feature work and bug fixes with a tracer-bullet red-green-refactor loop. Use when building behavior that should be guided by tests, when fixing regressions, or when the user wants TDD or test-first execution. Prefer public interfaces, vertical slices, and behavior-focused tests that survive refactors.

# Intended Use
Use for coding tasks, regressions, and bug fixes where tests should drive the implementation and provide stable feedback.

# Out Of Scope
Do not force TDD where the repo has no realistic test seam and the cost would outweigh the feedback benefit.

# Inputs And Outputs
Inputs: desired behavior, current code, existing tests, public seams.

Outputs: behavior-focused tests, minimal implementation slices, and safer refactor steps.

# Risks
- Risk: implementation-coupled tests. Mitigation: require public-interface and refactor-survival checks.
- Risk: horizontal slicing. Mitigation: enforce one failing test at a time.
- Risk: overtesting. Mitigation: confirm priority behaviors before writing tests.

# Metadata
* Group: [Coding, Debugging & Architecture](../groups/coding-debugging-architecture/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.7.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/test-driven-execution/SKILL.md)
* [SKILL_CARD.md](../../skills/test-driven-execution/SKILL_CARD.md)

# Attribution
ABVX adapted from Matt Pocock's `tdd`, rewritten for compact ABVX execution loops.

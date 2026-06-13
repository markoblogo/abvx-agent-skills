---
type: "Skill Group"
title: "Long-Run Delivery Control"
description: "Catalog grouping for long-run delivery control."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/catalog/okf/groups/long-run-delivery-control"
tags:
  - "skill-group"
  - "long-run-delivery-control"
canonical: "README.md"
source: "abvx-agent-skills"
status: "active"
kind: "skill-group"
---

# Long-Run Delivery Control

## Skills

* [Delivery Baseline Audit](../../skills/delivery-baseline-audit.md) - Performs an end-of-task audit against the starting baseline and the full working tree so declared deliverables are checked as shipped artifacts, not just as transcript claims.
* [Delivery Preflight Gate](../../skills/delivery-preflight-gate.md) - Runs a compact baseline preflight before long implementation or autonomous execution so the agent does not thrash against pre-existing repo breakage.
* [Phase Spec Execution](../../skills/phase-spec-execution.md) - Runs large implementation tasks through explicit, falsifiable phases with per-phase criteria, verification, and lightweight state tracking.
* [Recovery Loop 3-Strike](../../skills/recovery-loop-3strike.md) - Adds a bounded retry-escalate-handoff loop so agents stop spinning on the same failure and preserve useful evidence when blocked.

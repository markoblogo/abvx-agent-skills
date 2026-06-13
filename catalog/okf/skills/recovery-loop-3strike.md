---
type: "Skill Catalog Entry"
title: "Recovery Loop 3-Strike"
description: "Adds a bounded retry-escalate-handoff loop so agents stop spinning on the same failure and preserve useful evidence when blocked."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/recovery-loop-3strike"
tags:
  - "skill"
  - "long-run-delivery-control"
  - "experimental"
  - "adapted"
canonical: "skills/recovery-loop-3strike"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Adds a bounded retry-escalate-handoff loop so agents stop spinning on the same failure and preserve useful evidence when blocked.

# Trigger
Recover from failed execution or verification with a bounded three-step loop: retry, focused fix-spec, then honest handoff. Use when an agent is likely to spin on the same failure, when flaky environment issues blur the signal, or when you need a disciplined stop condition instead of endless optimistic retries.

# Intended Use
Use when verification has failed, when autonomous execution needs a hard stop condition, or when environment noise and partial fixes make repeated retries expensive.

# Out Of Scope
Do not invoke for one-off typos that are already understood and fixed within the same loop.

# Inputs And Outputs
Inputs: failing signal, attempted verification, current phase or task context.

Outputs: bounded retries, focused fix-spec escalation, or a blocked handoff with evidence.

# Risks
- Risk: premature handoff. Mitigation: require one evidence-bearing retry and one focused fix-spec first.
- Risk: repetitive spinning. Mitigation: cap the loop at three materially different attempts.
- Risk: vague blocker reports. Mitigation: require a per-strike failure record.

# Metadata
* Group: [Long-Run Delivery Control](../groups/long-run-delivery-control/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/recovery-loop-3strike/SKILL.md)
* [SKILL_CARD.md](../../skills/recovery-loop-3strike/SKILL_CARD.md)

# Attribution
ABVX adapted from robzilla1738 `supergoal` three-strike recovery model, rewritten into a host-agnostic recovery discipline for ABVX skills.

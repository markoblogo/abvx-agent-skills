---
okf_version: "0.1"
title: "ABVX Skills Catalog"
description: "Open Knowledge Format export of the ABVX Agent Skills catalog."
source: "abvx-agent-skills"
status: "active"
---

# ABVX Skills Catalog

## Groups

* [Token Economy & Context Control](groups/token-economy-context-control/index.md) - 8 skills
* [Coding, Debugging & Architecture](groups/coding-debugging-architecture/index.md) - 8 skills
* [Frontend, UX & Product Surfaces](groups/frontend-ux-product/index.md) - 8 skills
* [HTML Artifacts & Visual Deliverables](groups/html-artifacts-visual-deliverables/index.md) - 2 skills
* [Project Context & Onboarding](groups/project-context-onboarding/index.md) - 2 skills
* [Discovery, Planning & Delivery](groups/discovery-planning-delivery/index.md) - 5 skills
* [Research, Knowledge & Reusable Methods](groups/research-knowledge-methods/index.md) - 8 skills
* [Workflow, Handoffs & Multi-Track Work](groups/workflow-handoffs-multitrack/index.md) - 3 skills
* [Long-Run Delivery Control](groups/long-run-delivery-control/index.md) - 4 skills
* [Structured Data & Spreadsheet Work](groups/structured-data-spreadsheet-work/index.md) - 1 skills

## Skills

* [Agents Best Practices](skills/agents-best-practices.md) - Guides provider-neutral design, audit, and implementation planning for agentic systems and agent harnesses.
* [Architecture Deepening Review](skills/architecture-deepening-review.md) - Reviews codebases for deeper modules, clearer seams, lower coupling, and better testability.
* [Book To Skill](skills/book-to-skill.md) - Converts long-form documents into compact, reusable agent skills.
* [Brief First Execution](skills/brief-first-execution.md) - Creates and maintains a single working brief for non-trivial tasks so scope, non-goals, risks, verification, and done criteria do not drift.
* [Browser Verification](skills/browser-verification.md) - Verifies web pages with real browser automation after frontend or visual changes.
* [Compaction Survival](skills/compaction-survival.md) - Preserves the minimum high-value working state so long sessions survive compaction without expensive re-derivation.
* [Complexity Optimizer](skills/complexity-optimizer.md) - Finds and fixes algorithmic complexity and performance hotspots with behavior-preserving discipline.
* [Delivery Baseline Audit](skills/delivery-baseline-audit.md) - Performs an end-of-task audit against the starting baseline and the full working tree so declared deliverables are checked as shipped artifacts, not just as transcript claims.
* [Delivery Preflight Gate](skills/delivery-preflight-gate.md) - Runs a compact baseline preflight before long implementation or autonomous execution so the agent does not thrash against pre-existing repo breakage.
* [Design Critique Polish](skills/design-critique-polish.md) - Runs a focused critique-and-polish pass for frontend interfaces before shipping.
* [Design Register Bootstrap](skills/design-register-bootstrap.md) - Creates or refreshes compact frontend design context, with an explicit `brand` versus `product` register split, before implementation begins.
* [DesignMD Brand Kit](skills/designmd-brand-kit.md) - Creates, inspects, and applies DESIGN.md brand kits for brand-aware frontend work and client research.
* [Diagnose](skills/diagnose.md) - Provides a feedback-loop-first diagnostic process for bugs, regressions, flaky behavior, and performance failures.
* [Doc Grounded Grilling](skills/doc-grounded-grilling.md) - Aligns plans against the repo's existing docs, domain language, and decisions through a one-question-at-a-time grilling session.
* [Durable Context Maintenance](skills/durable-context-maintenance.md) - Maintains repo-local durable context so agent-facing docs stay accurate, compact, and useful after code and workflow changes.
* [Dynamic Workflow Packets](skills/dynamic-workflow-packets.md) - Plans and runs large Codex tasks with compact workflow packets, risk gates, integration, and verification.
* [Evidence Ledger Research](skills/evidence-ledger-research.md) - Researches evidence-sensitive questions with source, date, unit, table, and operand discipline.
* [Frontend Product Builder](skills/frontend-product-builder.md) - Guides frontend implementation toward usable, brand-aware, responsive, verified product experiences.
* [Frontend Taste Layer](skills/frontend-taste-layer.md) - Adds an anti-slop frontend taste layer for landing pages, portfolios, and brand-forward redesigns where the default output is too generic.
* [Graph Guided Code Reading](skills/graph-guided-code-reading.md) - Reduces repository-reading token waste by navigating code through entrypoints, symbols, dependencies, and blast radius instead of broad reading.
* [Handoff](skills/handoff.md) - Creates compact, operational handoff documents for continuation across agents, sessions, or humans.
* [HTML Brief Artifact](skills/html-brief-artifact.md) - Creates polished standalone HTML briefs for plans, reports, summaries, and explainers.
* [HTML Diagram Artifact](skills/html-diagram-artifact.md) - Creates standalone HTML/SVG architecture and flow explainers with minimal prose and strong visual hierarchy.
* [Lean Context Layout](skills/lean-context-layout.md) - Restructures agent-facing repository context to reduce always-loaded token overhead.
* [LoopOps Protocol](skills/loopops-protocol.md) - Designs reusable agent behavior as the smallest reliable artifact: prompt, skill, checklist, script, workflow, or cost-bounded loop.
* [Phase Spec Execution](skills/phase-spec-execution.md) - Runs large implementation tasks through explicit, falsifiable phases with per-phase criteria, verification, and lightweight state tracking.
* [Plan To Issues](skills/plan-to-issues.md) - Breaks PRDs and plans into thin, end-to-end slices that can be executed by agents or humans.
* [Private Vs Publishable Skill Audit](skills/private-vs-publishable-skill-audit.md) - Audits private skill packs before publication by classifying content as private, mixed, or reusable and gating release on real decontextualization.
* [Project Context Bootstrap](skills/project-context-bootstrap.md) - Bootstraps durable project context through stack detection, user discovery, compact context docs, and approval-gated updates.
* [Prototype Lab](skills/prototype-lab.md) - Guides creation of throwaway prototypes that answer one concrete design, logic, or integration question.
* [Rapid Grilling](skills/rapid-grilling.md) - Runs a lightweight one-question-at-a-time grilling session to sharpen vague ideas before heavier planning.
* [Recovery Loop 3-Strike](skills/recovery-loop-3strike.md) - Adds a bounded retry-escalate-handoff loop so agents stop spinning on the same failure and preserve useful evidence when blocked.
* [Repo Debugging Ledger](skills/repo-debugging-ledger.md) - Debugs repositories with a hypothesis ledger, checked-location ledger, loop breakers, and verification.
* [Repo Issue Triage](skills/repo-issue-triage.md) - Moves bugs and enhancements through a compact state machine so backlog items become actionable instead of lingering in vague limbo.
* [Role Skill Pack Design](skills/role-skill-pack-design.md) - Designs compact role-specific or workflow-specific skill packs with explicit base layers, difference layers, references, boundaries, and rollout order.
* [RTK Assisted Shell](skills/rtk-assisted-shell.md) - Applies RTK-style output filtering to shell-heavy coding and debugging workflows to reduce context waste.
* [Session Retrospective](skills/session-retrospective.md) - Reads session reflection artifacts and turns them into a compact retrospective with concrete next-session changes.
* [Shell Output Compaction](skills/shell-output-compaction.md) - Reduces shell and tool-output token waste by shaping commands toward narrow, high-signal output.
* [Skill Effectiveness Audit](skills/skill-effectiveness-audit.md) - Reads skill reflection artifacts and turns them into a bounded audit of which skills to keep, tighten, split, or de-emphasize.
* [SkillOpt Evolve Skills](skills/skillopt-evolve-skills.md) - Improves local skills, AGENTS.md rules, and reusable agent workflows through validation-gated edits.
* [Spec To PRD](skills/spec-to-prd.md) - Turns current discovery and repo understanding into a durable PRD for product, client, and internal roadmap work.
* [Spreadsheet Workbook Forensics](skills/spreadsheet-workbook-forensics.md) - Edits and verifies spreadsheet workbooks while preserving structure, formatting, and target-cell correctness.
* [System Zoom Out](skills/system-zoom-out.md) - Maps a local code area back to the wider system so users can reason about modules, boundaries, and blast radius.
* [Test Driven Execution](skills/test-driven-execution.md) - Guides feature work and bug fixes through a vertical-slice red-green-refactor loop centered on behavior, not implementation details.
* [Token Efficient Execution](skills/token-efficient-execution.md) - Reduces token waste during execution by tightening exploration, patching, and reporting loops.
* [Token Frugal Mode](skills/token-frugal-mode.md) - Compresses answers to save output tokens while preserving technical accuracy.
* [Token Usage Audit](skills/token-usage-audit.md) - Audits token waste categories and maps them to the smallest useful corrective skill or policy change.
* [Web Quality Audit](skills/web-quality-audit.md) - Audits and improves web quality across accessibility, performance, UX, privacy, and browser security.
* [Workflow Policy Layering](skills/workflow-policy-layering.md) - Separates workflow steps from authority, forbidden actions, escalation paths, and validation gates so assistant specs stop contradicting themselves.

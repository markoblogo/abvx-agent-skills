# Skill Selection Guide

Choose the smallest relevant set. See the [quickstart](solo-dev-quickstart.md) for installation.


- **Need to save tokens?** Start with `rtk-assisted-shell`, `shell-output-compaction`, `token-efficient-execution`, and `lean-context-layout`. Add `compaction-survival` if your sessions run long enough to forget their own state.
- **Need to check whether context is hurting the run?** Start with `context-degradation-review` before trusting long handoffs, memory summaries, or bloated SET bundles.
- **Need to choose direct vs review-first vs loop vs human approval before work widens?** Start with [docs/ship-router-contract.md](docs/ship-router-contract.md), then route into the smallest sufficient follow-up skill set.
- **Need to debug a repo?** Start with `diagnose`, `repo-debugging-ledger`, and `graph-guided-code-reading`.
- **Need auditable red-to-green proof?** Add `bug-evidence-protocol` after `diagnose`; use risk-based approval and link recurrent lessons to a `cpat`.
- **Need code review discipline?** Run a Standards pass with `overengineering-review`, `minimal-diff-builder`, or `architecture-deepening-review`, then a Spec pass with `delivery-baseline-audit` against the issue, PRD, or task contract.
- **Need to review an agent-facing tool or external-skill adaptation?** Start with `agent-tool-contract-review` for MCP, CLI, SET inputs, AGENTS.md generator contracts, and source-linked `KEEP`/`ADAPT`/`ADD`/`REJECT` deltas.
- **Need to surface hidden assumptions before implementation?** Start with `assumption-excavation`, then use `pipeline-readiness-gate` when the work needs a pre/post/ship sequence.
- **Need competing explanations before review?** Start with `hypothesis-diversification`, then hand off to `evidence-ledger-research`, `confidence-fragility-review`, or a domain validator.
- **Need reversible agent work?** Start with `reversible-agent-task` when output should be retained and inspected before any `select`, `apply`, or `discard` decision.
- **Need to test whether confidence is earned?** Start with `confidence-fragility-review` before trusting release notes, public claims, generated plans, or SET handoff bundles.
- **Need the smallest correct implementation path?** Start with `minimal-diff-builder`, then add `delivery-preflight-gate` when the task is long or risky enough that baseline verification matters.
- **Need to cut bloat from an existing diff or repo slice?** Start with `overengineering-review`, and switch to `minimal-diff-builder` when you want the cuts implemented as the smallest correct patch.
- **Need to build frontend?** Start with `frontend-product-builder`, `designmd-brand-kit`, `browser-verification`, and `motion-review-gate` when interaction motion changes; add `fluid-interaction-review` for drag, swipe, sheets, carousels, or draggable panels. For browser-facing HTML, CSS, or client-side JavaScript, query the external [Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance) companion before implementation; keep it out of backend, CI, and generic tooling tasks.
- **Need named agents, scheduled/long-running operations, or durable decisions?** Use `agent-operations-contract` for capability cards, operation and decision receipts, revalidation, trust-graded scoped memory, public/private state boundaries, provider/tool evidence, and approval boundaries before enabling a route.
- **Need a small Lottie or SVG-driven motion asset?** Start with `lottie-motion-builder`, pair with `frontend-product-builder` when the animation needs to land inside a real UI surface, then run `motion-review-gate` before shipping.
- **Need a standalone HTML artifact?** Start with `html-diagram-artifact` for SVG-first architecture explainers, or `html-brief-artifact` for plans, summaries, reports, and research notes.
- **Need stronger UI taste or design setup?** Start with `design-register-bootstrap`, `frontend-taste-layer`, `design-critique-polish`, and `motion-review-gate` for motion-sensitive surfaces.
- **Need long-session continuity?** Start with `handoff`, `compaction-survival`, and `token-usage-audit`.
- **Need to onboard a new repo?** Start with `project-context-bootstrap` and follow with `durable-context-maintenance`.
- **Need durable files without prompt bloat?** Start with `filesystem-context-discipline` for scratchpads, retained outputs, plan persistence, evidence, and handoffs.
- **Need to explore dense agent docs interactively?** Start with `rabbithole-doc-exploration` when Rabbithole MCP is available, or use its direct-review fallback.
- **Need one local workspace across many domains?** Start with `personal-workspace-router` to create a root router, isolated domain context, user-triggered memory, decision logs, and sparse routing corrections.
- **Need discovery or product shaping?** Start with `rapid-grilling`, `doc-grounded-grilling`, and `spec-to-prd`. Use repo glossary/context files and ADRs as first-class artifacts when domain language or consequential decisions settle.
- **Need to compare strategic options under uncertainty?** Install the standalone [DecisionMap](https://github.com/markoblogo/decision-map) companion for explicit assumptions, trade-offs, breakpoints, and revisit triggers.
- **Need to turn plans into execution?** Start with `plan-to-issues`, `repo-issue-triage`, and `test-driven-execution`.
- **Need to take an idea all the way to a shipped slice?** Start with `idea-to-ship-gates`, then route into `spec-to-prd`, `plan-to-issues`, `delivery-preflight-gate`, and proof/review skills only where the current gate needs depth.
- **Need to publish or monitor social content safely?** Start with `social-publishing-gate` so drafts, audits, approvals, external posting, and follow-ups stay separate.
- **Need safer long delivery runs?** Start with `delivery-preflight-gate`, `phase-spec-execution`, `recovery-loop-3strike`, and `delivery-baseline-audit`.
- **Need to gate a branch before PR publication?** Start with `delivery-preflight-gate` push-gate mode, then add external tooling such as `no-mistakes` only when the repo benefits from an isolated disposable worktree.
- **Need to route security work?** Start with `authorized-security-router` before any defensive security review where authorization, target boundary, or allowed action level is not explicit.
- **Need to evaluate document memory?** Start with `doc-to-lora-evaluator` before proposing Doc-to-LoRA, RAG replacement, or adapter-based document recall.
- **Need to launch a bounded agent loop?** Start with `goal-loop-designer` before running long Codex, Claude Code, MiMo Code, or local-LLM loops.
- **Need to schedule a recurring agent loop?** Start with `loop-readiness-review` before enabling CI sweepers, PR babysitters, daily triage, changelog drafting, or dependency loops.
- **Need local model serving?** Start with `local-inference-tuning` before choosing MLX, llama.cpp, Ollama, or vLLM.
- **Need a full multi-track workflow?** Start with `dynamic-workflow-packets`.
- **Need a reviewed Planner/Reviewer/Executor workflow?** Start with `bounded-orchestration-contract`; keep it opt-in, stop after five review rounds, and require root integration and verification.
- **Need durable typed decisions or incident lessons?** Start with `git-native-context-contract`; reuse existing docs, keep new records in `draft`, and require explicit human approval for `accepted`.
- **Need to turn repeated prompts into loops?** Start with `loopops-protocol`, then use `skillopt-evolve-skills` to capture durable lessons.
- **Need a small eval gate?** Start with `bounded-evaluation` before using pairwise judging, LLM-as-judge, activation tests, or SkillOpt validation claims.
- **Need to decide where agent learning should live?** Start with `agent-learning-layer-triage` before promoting a lesson into memory, durable docs, `SKILL.md`, a script, or an eval.
- **Need to build reusable assistant packs?** Start with `role-skill-pack-design`, `workflow-policy-layering`, `brief-first-execution`, and `private-vs-publishable-skill-audit`.

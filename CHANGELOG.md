# Changelog

## Unreleased

- Add six optional Codex-native PR workflow skills adapted from tstack, with bounded OpenAI review, CI observation, intent-aware modernization, preserved contributor credit, concise PR writing and a no-merge readiness gate.
- Retain upstream MIT notices in every installable skill, add bounded CI-helper tests and synthetic decision fixtures, and regenerate catalog entries.
- Add a source-checkout installer that previews the selected skills and preserves local modifications. This change does not publish a new package release.

## 0.16.1 — post-release review corrections

- Preserve recreated local skills during repeated recovery without archive collisions; keep doctor reporting when managed paths are files, symlinks or unreadable directories.
- Restore payloads before retrying journal writes after installation failures.
- Hash evaluation prompts before/after execution and reject unknown command syntax, indirect script execution, external reads and network attempts.
- Preserve non-eligible original/unbounded docs-skill runs and execute a new seven-case protocol-constrained rerun with captured prompt hashes and manual review; qualify fixture_checked only for that bounded protocol.
- Reject zsh executable glob qualifiers, require successful completed reads as source evidence, and label the superseded smoke grade historical.

## 0.16.0 — managed skill profiles and recoverable installation

- Add whole-selection preflight and file-level preview, staged transactional installation, OS locking, retained replacement backups, rollback and interrupted-process recovery.
- Add context/debug/delivery profiles; bare install no longer selects the entire pack. Use named skills, --profile or explicit --all.
- Add per-destination manifests and doctor reporting for versions, hashes, updates and local/unmanaged changes; archive state stays outside agent discovery roots.
- Fix README table cells/continuity and grade partial model smoke runs without promotion; record complete post-run workspace inventories and reject unexpected changes.

- Re-review security exceptions against a fresh pinned static scan and bind accepted findings to current source hashes.
- Complete catalog status/origin metadata and categorize corporate, editorial and wireframe skills.
- Preserve product/design context and explicit detector waivers in frontend reviews without weakening hard-defect precedence.
- Add read-the-damn-docs with seven executed synthetic activation, negative and authority scenarios and retained evidence; promote only to fixture_checked.


- Add `professional-role-router` for task-time selection and handoff between bounded professional roles.
- Extend `role-skill-pack-design` with professional-role donor adaptation, maturity states, routing, handoffs, authority separation, and evaluation guidance.
- Extend `personal-workspace-router` so isolated personal domains can activate a small set of professional role profiles without broad context or permission inheritance.
- Record `msitarzewski/agency-agents` as a pattern source; the prompt corpus is not bundled.

## 0.14.0 — measured demos and task closeout

- Run the test suite in both validation CI and the publication build gate; include tests in the source distribution.
- Pin the audited SkillSpector revision, bind nine reviewed reference-resolution exceptions to full-file hashes and expiry dates, and fail the security gate when reports are absent.
- Add proportional task closeout audits and evidence receipts to `durable-context-maintenance` and `handoff`, preserving cleanup approval and explicit memory-update boundaries.
- Make quickstart commands install three named skills, move the long selection guide out of README, and remove unsupported total-token savings implications.
- Add paired, reproducible synthetic demos for `minimal-diff-builder`, `token-efficient-execution`, and `public-release-verification`, with raw task traces, grading, token usage, and limitations.
- Include the post-0.13.0 design preflight and surface guidance already merged on main.

Measured demos are small single-model pilots, not held-out validation or universal performance claims. See `benchmarks/measured/2026-09-07/README.md` for results and scope.

## 0.13.0 — proof-first release

- Added `public-release-verification` for separated repository, package,
  deployment, live-route, browser, locale, visual, and human-gate evidence.
- Added `skill-health-audit` for review-only skill quality, evaluation-tier,
  drift, overhead, and safety audits.
- Added fixture-checked activation and negative cases for five key skills.
- Raised `minimal-diff-builder`, `diagnose`, `reversible-agent-task`, and
  `browser-verification` to `fixture_checked`.
- Hardened catalog governance, attribution, design-context persistence, and
  materially changed skill-card versions.
- Regenerated the public catalog and aligned package version `0.13.0`.

This release does not claim held-out behavioral validation or automatic skill
evolution. Public, deployment, visual, and human approval claims remain
separate evidence gates.

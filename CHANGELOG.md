# Changelog

## Unreleased

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

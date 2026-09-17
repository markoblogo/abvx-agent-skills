# Chrome DevTools MCP pilot

This is an optional verification companion, not a runtime dependency of the
ABVX projects.

**Current status (2026-09-17): `INSTALL_BLOCKED`.** The official npm package
could not be downloaded in the current Codex environment, so no MCP browser
result is claimed yet. Resume the pilot when npm access is available.

## Scope

Run the pilot on the next substantive web PR in `SET` or `ABVXsite`. Do not
replay it retroactively on an old release and do not use it for backend-only,
CLI, firmware, or private-data workflows.

## Local setup

Use a current LTS Node.js and Chrome. Configure the MCP client with the example
in the root README, including `--isolated`, `--no-usage-statistics`, and
`--no-performance-crux`. Keep update checks disabled with
`CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS=1`.

If the package cannot be downloaded in the current environment, record that as
`INSTALL_BLOCKED` and stop; do not claim a browser result from another tool as
an MCP result.

## Pilot protocol

1. Record repository, PR, commit, target preview URL, Chrome version, and MCP
   configuration flags.
2. Open the target route in the isolated browser profile.
3. Exercise one user-visible success path and one relevant empty, error, or
   responsive state.
4. Capture console errors, failed network requests, accessibility-tree output,
   and a screenshot. Add a performance trace when the PR changes loading or
   interaction work.
5. Classify each observation as `BLOCKER`, `FOLLOW_UP`, or `PASS` and link the
   evidence from the PR.
6. Re-run the same path after fixes and report the before/after result.

## Evidence boundary

MCP output proves behavior in the inspected Chrome session and URL. It does not
prove CI, production deployment, real-user analytics, hardware behavior, or
cross-browser compatibility. Keep those claims as separate gates.

## Graduation rule

After one clean, reviewable pilot, consider extracting a shared
`web-release-verification` skill. Until then, keep this as documentation and an
optional companion so projects do not inherit an unnecessary browser service.

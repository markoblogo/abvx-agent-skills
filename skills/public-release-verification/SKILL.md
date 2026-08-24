---
name: public-release-verification
description: Verify whether a software release is publicly proven across repository identity, baseline, build, package, deployment, HTTP routes, SEO metadata, browser desktop/mobile behavior, locale content, visual availability, and human approval. Use when an agent is preparing or reviewing a release and must separate build proof, live proof, and owner-gated public claims.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
  abvx_eval_tier: fixture_checked
---

# Public Release Verification

Use this skill to decide what a release has actually proved. A green build is
one input, not a public-release claim.

## Verification Contract

Capture one evidence row for each applicable domain:

1. **repository/commit identity** — repository, branch/tag, commit, and clean
   or intentionally dirty baseline;
2. **baseline and diff** — starting state, changed scope, and unrelated-change
   check;
3. **build/package proof** — tests, build, package contents, and metadata;
4. **deployment proof** — deployment provider, deployment identifier, and
   completed status;
5. **HTTP/route proof** — actual public URL, status code, redirects, and key
   routes;
6. **SEO/metadata proof** — title, description, canonical, robots, and social
   metadata where applicable;
7. **browser desktop/mobile proof** — real browser observations, responsive
   states, interaction, console, and network failures;
8. **locale/content proof** — requested locales, visible strings, fallback
   behavior, and content constraints;
9. **device/runtime proof** — real-device or runtime-specific observations
   where the release target is hardware or a constrained runtime;
10. **visual/public availability proof** — screenshots or equivalent observed
   public rendering and availability window;
11. **human approval and cutover status** — named approval evidence, approval
   scope, and whether DNS, traffic, or publication gates remain open.

For releases produced through an isolated agent runtime, also capture:

12. **workspace identity** — workspace/session/tenant owner, source baseline,
    path scope, and read-only mounts;
13. **backend identity** — selected backend, runtime version, command/module
    surface, and observed rather than merely configured capability;
14. **command scope and egress policy** — exact command or module scope,
    network destinations, blocked destinations, and credential boundary;
15. **artifact/session ownership** — artifact destination, digest, retention,
    repository or session owner, and whether the artifact is private, staged,
    or public;
16. **cleanup and disposal state** — process/handle disposal, workspace expiry,
    temporary data cleanup, pending sync, and retry state.

Mark each row `PROVEN`, `PARTIAL`, `BLOCKED`, or `UNKNOWN`, with command,
URL, artifact path, timestamp, and verifier where available. Use `N/A` only
when the row genuinely does not apply and explain why.

## Claim Rules

- Build proof is not live proof.
- Deployment proof is not HTTP proof.
- HTTP proof is not browser or visual proof.
- Browser proof is not owner approval or public cutover authorization.
- Filesystem proof is not execution proof; execution proof is not artifact or
  public proof.
- A configured backend, egress rule, artifact binding, or cleanup policy is not
  observed proof until the relevant runtime evidence exists.
- Missing evidence is `UNKNOWN`, not success.
- A final `PROVEN` claim requires every applicable release-critical row to be
  `PROVEN` and the human gate to be explicit.
- Report `PARTIAL` when useful evidence exists but a release-critical row is
  incomplete; report `BLOCKED` when a required check failed or access prevents
  verification.

## Safe Route

1. Record the repository identity and baseline before running release checks.
2. Run the narrowest package/build checks, then collect deployment evidence.
3. Verify the actual public URL and routes with the intended locale and
   viewport matrix.
4. Inspect metadata, visible copy, console/network errors, and screenshots.
5. Attach the evidence matrix and list unknowns, blockers, and human gates.
6. Ask the owner for approval only after the evidence packet is reviewable.

Do not auto-publish, switch DNS, promote traffic, accept visual approval, or
claim public availability on behalf of a human. Do not use a deployment log as
a substitute for an observed public route.

## Output

```text
Release: <name/version>
Repository: <repo>@<commit/tag>
Status: PROVEN | PARTIAL | BLOCKED | UNKNOWN

<domain>: <status> — <evidence reference or reason>
...

Human gate: <approved / pending / not applicable, with scope>
Open blockers: <none or list>
Claim boundary: <what this packet proves and does not prove>
```

## Composition

- Use `delivery-preflight-gate` before a risky release run.
- Use `browser-verification` for the browser evidence row.
- Use `confidence-fragility-review` when the release summary sounds stronger
  than its evidence.
- Use `skill-health-audit` when reviewing this contract or its fixtures.
- Use `agent-workspace-boundary-review` before an isolated runtime starts.
- Use `isolated-agent-runtime-review` to separate runtime proof from release
  proof.

---
name: isolated-agent-runtime-review
description: Review an isolated agent runtime by separating filesystem, execution, artifact, and external/public proof before accepting its result.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
  abvx_eval_tier: fixture_checked
---

# Isolated Agent Runtime Review

Use this skill when an agent runs in a sandbox, container, worker, remote workspace, or multi-backend runtime and someone needs to know what the run actually proves.

The runtime is a provider. It does not become the source of truth, release authority, or human approver.

## Four proof domains

Keep separate evidence rows for:

1. **Filesystem proof** — which workspace identity, paths, files, mounts, hashes, and source versions were actually read or changed;
2. **Execution proof** — which backend, command/module, runtime version, exit code, stdout/stderr, limits, and egress policy were observed;
3. **Artifact proof** — what output was created, where it is stored, who owns the session/repository, its digest, retention, and whether it is only a private artifact;
4. **External/public proof** — whether anything was actually deployed, reachable, rendered, published, approved, or made public.

Use `PROVEN`, `PARTIAL`, `BLOCKED`, or `UNKNOWN` per domain. Never promote filesystem or execution proof into artifact or public proof.

## Required runtime identity

Record runtime/backend identity, workspace/session owner, command scope, network/egress policy, source baseline, artifact destination, and cleanup/disposal result. If a value was configured but not observed, mark it `UNKNOWN` or `PARTIAL`.

## Safe output

```text
Runtime: <provider/backend/runtime version>
Workspace: <identity/session/owner>
Filesystem proof: <status> — <evidence>
Execution proof: <status> — <evidence>
Artifact proof: <status> — <evidence>
External/public proof: <status> — <evidence>
Cleanup/disposal: <status> — <evidence or unknown>
Final claim: <bounded statement>
```

Do not auto-publish, change DNS, grant credentials, accept visual approval, delete source state, or retry an external action because an isolated run succeeded. Use `public-release-verification` for the release-level claim.

## Composition

Pair with `agent-workspace-boundary-review` before execution and `public-release-verification` after a release candidate exists. Use `browser-verification` or device-specific skills for their respective proof domains.

---
name: happy-handoff
description: Continue the current Codex Desktop task in Happy on Android when the user says "ухожу", asks to move or hand off to Happy, or invokes this skill explicitly.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
  abvx_eval_tier: fixture_checked
---

# Happy Handoff

Resume the same Codex task in Happy after reaching a safe checkpoint. The handoff request authorizes starting Happy for the current task. It does not authorize commits, pushes, deployments, destructive actions, or unrelated changes.

## Workflow

1. Finish the current tool call or other indivisible operation.
2. Preserve the workspace. Do not clean, stash, commit, or rewrite dirty work for the handoff.
3. Capture a compact checkpoint: completed work, current branch or directory, validation state, dirty files, active processes, and the next concrete step.
4. Require `CODEX_THREAD_ID`, the current working directory, an authenticated Happy CLI, and the system `script` command. If a prerequisite is unavailable, report the exact blocker instead of opening an unrelated session.
5. As the final tool action, run:

   ```bash
   python3 "${CODEX_HOME:-$HOME/.codex}/skills/happy-handoff/scripts/launch.py"
   ```

6. Immediately return the checkpoint so it is stored in the task before Happy resumes it. Say that the handoff is scheduled and ask the user to open Happy on Android.

The launcher waits briefly, then starts `happy codex --resume` for the exact task in the same directory. Use `--dry-run` to validate prerequisites without scheduling a session.

## Guardrails

- Never add `--yolo`, bypass approval settings, or expand permissions.
- Do not claim that Android received the task until the user observes it there.
- Do not enable voice or daemon autostart as part of a handoff.
- Starting the Happy daemon when it is needed is allowed by the handoff request.
- Windows is currently unsupported; macOS and Linux use different `script` syntax and are handled explicitly.

## Output Shape

Report:

- checkpoint;
- task ID and workspace;
- launcher status: `dry-run`, `scheduled`, or `blocked`;
- next step in Happy;
- unverified boundary: Android receipt until observed.

## Provenance

Original ABVX workflow around the MIT-licensed `slopus/happy` CLI. Happy is an external companion and is not bundled with this repository.

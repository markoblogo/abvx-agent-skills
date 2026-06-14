# Demo: diagnose

## Problem

Coding agents often guess fixes before they have a stable repro.

## Task

Debug one failing command, test, or behavior by reproducing it, ranking hypotheses, and verifying the actual fix.

## Without the skill

Likely failure mode:

- proposes fixes before reproducing the error
- changes multiple areas at once
- reports success without proving the original failure is gone

## With the skill

Expected behavior:

- establish one pass/fail loop first
- rank hypotheses instead of editing blindly
- test the narrowest plausible fix
- rerun the original signal before saying done

## Try it

```bash
gh skill preview markoblogo/abvx-agent-skills diagnose
gh skill install markoblogo/abvx-agent-skills diagnose --agent codex --scope user
```

Then tell the agent:

```text
Use diagnose. Reproduce the failure, rank hypotheses, and verify the fix before closing the task.
```

# Demo: token-economy

## Problem

Shell-heavy coding sessions often waste context on noisy logs, repeated reads, and oversized diffs.

## Task

Keep the session compact while still preserving the real debugging or implementation signal.

## Without the skills

Likely failure mode:

- dumps long stdout blocks into the conversation
- rereads the same files repeatedly
- loses the important error inside build or test noise

## With the skills

Expected behavior:

- route shell-heavy work through `rtk-assisted-shell`
- compact logs and diffs with `shell-output-compaction`
- avoid repeated reads with `token-efficient-execution`
- preserve only the information needed for the next decision

## Try it

```bash
gh skill preview markoblogo/abvx-agent-skills rtk-assisted-shell
gh skill install markoblogo/abvx-agent-skills rtk-assisted-shell --agent codex --scope user
gh skill install markoblogo/abvx-agent-skills shell-output-compaction --agent codex --scope user
gh skill install markoblogo/abvx-agent-skills token-efficient-execution --agent codex --scope user
```

Then tell the agent:

```text
Use rtk-assisted-shell, shell-output-compaction, and token-efficient-execution. Keep this shell-heavy task compact and only surface the decisive signal.
```

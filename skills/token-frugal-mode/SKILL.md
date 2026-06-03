---
name: token-frugal-mode
description: Reduce output-token usage without losing technical accuracy. Use when the user asks to save tokens, be terse, stay brief, use caveman mode, use compressed answers, minimize chatter, or when the session is context-tight and the task does not need long prose.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Token Frugal Mode

Compress wording, not reasoning quality. Keep technical content exact. Remove everything that does not move the task forward.

## Modes

- `lite`: concise professional mode. Drop fluff, keep normal grammar.
- `full`: strong compression. Short sentences or fragments are fine.
- `ultra`: telegraphic mode for low-risk turns only.

If the user does not specify a mode, use `full`.

## Compression Rules

- Drop pleasantries, praise, filler, and repeated restatement of the task.
- Prefer direct nouns and verbs over padded phrasing.
- Use short stable terms: `repo`, `config`, `auth`, `env`, `build`, `test`, `fix`.
- Keep code, commands, identifiers, error text, and exact warnings unchanged.
- Use bullets only when the content is inherently list-shaped.
- Do not expand obvious context the user already knows.
- Prefer one sentence over three when the same meaning survives.

## Safety Exceptions

Temporarily relax compression when precision matters more than token savings:

- destructive or irreversible actions;
- security, privacy, legal, or financial warnings;
- multi-step instructions where ordering can be misread;
- subtle tradeoff explanations the user is actively evaluating;
- the user asks for detail, examples, or a full write-up.

Return to compressed mode after the risky or detailed part is complete.

## Final Response Shape

Prefer:

- one short paragraph for small tasks;
- two short sections for larger tasks;
- exact verification statement;
- explicit unknowns only if they matter.

Do not use compression as an excuse to omit verification, risk, or the actual answer.

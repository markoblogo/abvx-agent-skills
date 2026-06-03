---
name: token-usage-audit
description: Audit where tokens are being wasted across startup context, shell output, repeated file reads, bloated agent docs, oversized summaries, and compaction loss. Use when token budget is tight, sessions are degrading, or an agent setup needs measurement-driven optimization.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Token Usage Audit

Save tokens by measuring the waste categories before optimizing them.

## Waste Categories

Audit these in order:

1. startup-context weight;
2. shell and tool-output noise;
3. repeated file reads or re-analysis;
4. oversized handoffs and summaries;
5. stale skills, prompts, or always-loaded docs;
6. compaction loss and re-derivation cost.

## Audit Workflow

1. Identify the current failure mode:
   - output overflow;
   - startup bloat;
   - long-session decay;
   - repeated repo rediscovery.
2. Estimate which category dominates.
3. Apply the narrowest corrective skill:
   - `rtk-assisted-shell` or `shell-output-compaction`;
   - `graph-guided-code-reading`;
   - `token-efficient-execution`;
   - `lean-context-layout`;
   - `compaction-survival`;
   - `token-frugal-mode`.
4. Re-check after the intervention:
   - fewer broad reads;
   - shorter command output;
   - smaller startup docs;
   - cleaner resume state.
5. Record what changed so the same waste is not rediscovered next session.

## Practical Signals

- top-level agent file is large and generic;
- same README or module keeps getting reopened;
- shell output dominates the conversation;
- compaction causes “what were we doing?” recovery turns;
- too many installed skills are irrelevant to current work;
- long status updates cost more than the actual edit.

## Deliverable

Report:

- biggest waste category;
- corrective skills used;
- what was changed;
- expected future savings.

## Guardrails

- Do not chase precision that costs more tokens than it saves.
- Do not instrument everything if a clear dominant waste category is already visible.
- Optimize the highest recurring cost first, not the most novel one.

---
name: doc-to-lora-evaluator
description: Evaluate whether Doc-to-LoRA is the right path for turning documents into parametric memory, and guide a safe proof-of-concept before investing in a full plugin or training pipeline. Use when a user wants to internalize long documents, reduce repeated context costs, compare Doc-to-LoRA against RAG or long-context prompting, or assess hardware/model/data risks for document-to-adapter workflows.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Doc To LoRA Evaluator

Evaluate Doc-to-LoRA as an engineering option before treating it as a production memory layer.

Doc-to-LoRA is a research pattern where a hypernetwork generates a LoRA adapter from a document so later queries can use the internalized information without re-sending the original long context. This skill is a decision and proof-of-concept gate, not a promise that every local machine can run the full pipeline.

## Use For

- comparing Doc-to-LoRA against RAG, long-context prompting, summaries, fine-tuning, or ordinary LoRA training;
- deciding whether a document set is a good fit for parametric memory;
- planning a small local or GPU-backed proof of concept with the public SakanaAI implementation;
- designing validation prompts that compare base-model, long-context, RAG, and internalized-adapter behavior;
- identifying hallucination, staleness, licensing, privacy, model-compatibility, and VRAM risks before implementation.

## Do Not Use For

- ordinary document QA where RAG or direct context is simpler and cheap enough;
- irreversible model updates or production deployment without evaluation;
- private or licensed documents unless the user explicitly authorizes local processing and artifact storage;
- claiming model memory improvements without side-by-side tests.

## Decision Gate

Prefer Doc-to-LoRA only when most of these are true:

- the same document or knowledge bundle will be queried repeatedly;
- re-sending the full context is expensive, slow, or exceeds the target model context window;
- the document is stable enough that adapter regeneration is acceptable;
- answers need durable factual recall more than open-ended retrieval transparency;
- the team can run the target model and generated adapters in a controlled environment;
- evaluation can compare against direct-context or RAG baselines.

Prefer RAG, summaries, or long-context prompting when:

- source provenance must be shown on every answer;
- documents change frequently or require fine-grained deletes;
- the task is one-off;
- available hardware cannot run the target model plus Doc-to-LoRA stack;
- user trust depends on visible retrieved passages.

## Preflight Checklist

Before implementation, capture:

1. target host: local machine, workstation GPU, cloud GPU, or hosted notebook;
2. model family and license constraints;
3. document size, format, sensitivity, and update frequency;
4. expected query pattern: one-shot QA, repeated support, personal memory, research corpus, or product feature;
5. baseline approach to compare against: direct context, RAG, summary, fine-tune, or ordinary LoRA;
6. success metrics: factual accuracy, latency, memory use, adapter size, regeneration time, and failure behavior;
7. rollback path: reset adapter, delete generated artifact, or fall back to RAG/direct context.

## Proof-Of-Concept Workflow

1. Read the official implementation and paper narrowly enough to confirm current setup commands, supported checkpoints, and caveats.
2. Select one small, non-sensitive document with known answerable facts.
3. Create an evidence ledger with at least 8-12 questions:
   - direct factual recall;
   - negative controls not in the document;
   - source-confusable questions;
   - stale or changed-fact questions when relevant.
4. Run or specify baselines:
   - base model without context;
   - model with raw document context when feasible;
   - RAG or summary baseline if this is the realistic alternative;
   - Doc-to-LoRA internalized adapter.
5. Compare answers for accuracy, unsupported claims, latency, memory use, and operational complexity.
6. Decide: `Reject`, `Prototype further`, or `Promote to plugin/tool wrapper`.

## Risk Gates

Block promotion beyond PoC if:

- generated adapters cannot be traced back to source documents and version IDs;
- private documents are persisted without an explicit storage and deletion policy;
- evaluation only tests positive recall and skips negative controls;
- the approach hides citations that the product actually needs;
- hallucinations increase compared with RAG or direct context;
- hardware assumptions are unrealistic for the intended users;
- model or document licenses do not permit the intended usage.

## Output Contract

Return a compact decision memo:

```text
Decision: Reject | Prototype further | Promote to wrapper/plugin
Use case:
Document set:
Baseline compared:
Hardware/model assumptions:
Expected upside:
Main blockers:
PoC plan:
Verification questions:
Rollback/deletion plan:
```

If implementation is requested, produce a minimal plan first. Do not start by building a general plugin.

## Attribution

Adapted from SakanaAI's public Doc-to-LoRA research and reference implementation into an ABVX evaluation gate for coding-agent workflows.

# Skill Card: doc-to-lora-evaluator

## Description
Evaluates whether Doc-to-LoRA is a rational path for document-to-adapter memory, and guides a small proof-of-concept before plugin or pipeline work.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when a user wants to internalize long documents, reduce repeated context costs, compare Doc-to-LoRA against RAG or long-context prompting, or assess hardware/model/data risks for document-to-adapter workflows.

## Out of Scope
Do not use as a replacement for ordinary document QA, RAG design, model fine-tuning, or production deployment without a measured proof-of-concept.

## Sources and Attribution
ABVX adapted from SakanaAI's public Doc-to-LoRA research article, paper, and reference implementation.

## Inputs and Outputs
Inputs: document set, target model or host, expected query pattern, privacy/licensing constraints, baseline approach, and evaluation questions.

Outputs: reject/prototype/promote decision, baseline comparison plan, risk gates, verification questions, and rollback or deletion plan.

## Composable With
- `book-to-skill`
- `evidence-ledger-research`
- `durable-context-maintenance`
- `token-efficient-execution`

## Risks and Mitigations
- Risk: treating a research demo as production infrastructure. Mitigation: require a small PoC and baseline comparison before plugin work.
- Risk: losing provenance versus RAG. Mitigation: explicitly decide when citations and retrieved passages are required.
- Risk: private document leakage through generated adapters. Mitigation: require artifact storage, deletion, and licensing checks.
- Risk: fake token-savings claims. Mitigation: compare latency, memory, and answer quality against direct context or RAG.

## Evaluation
Evaluated by structural validation and manual review against document-memory workflow decisions.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.

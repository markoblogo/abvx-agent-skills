# ABVX + Chisle benchmark — 2026-09-19

Eight synthetic tasks, three arms, one run per arm: **24 fresh Codex sessions**.
Five tasks edit code and run checks; three explain evidence packets. Model:
`gpt-6-astra` at `medium` effort; CLI: `codex-cli 0.155.0-alpha.9.2`.

| Arm | Checks | Explanation points retained | Input + output tokens | Coding diff lines | Tool output bytes |
|---|---:|---:|---:|---:|---:|
| baseline | 8/8 | 15/15 | 464,553 | 83 | 10,801 |
| abvx | 8/8 | 15/15 | 465,792 | 85 | 7,528 |
| abvx_chisle | 8/8 | 15/15 | 486,190 | 49 | 5,816 |

## Decision

Chisle improved diff and tool-output economy without reducing acceptance scores, but increased total tokens. Two unique stopping/scope rules are promoted; the complete Chisle ruleset is not adopted.

Compared with ABVX alone, ABVX + Chisle used **+4.4%** total tokens
(+4.5% coding; +4.2% explanation), changed
**-36** coding lines (-42.4%), and produced
**-22.7%** tool-output bytes.
Correctness and information retention must not decline for a candidate to qualify.

## Arms

- `baseline`: task only, with local skills, plugins, apps, skill search, and project instructions disabled.
- `abvx`: task plus the checked-in `token-efficient-execution` skill.
- `abvx_chisle`: ABVX arm plus the vendored Chisle v3.5.0 rules snapshot at commit
  `a0202aac0c7342d33a18848818c58a7ce9eb5212`.

Chisle is not installed globally and is not added to repository instructions.
For Codex, this evaluates Chisle's static rules only; its tool-result compression
hooks target other supported agents and are outside this comparison.

## Measures

- Correctness: hidden Python assertions for five coding tasks.
- Information loss: five predeclared evidence points and an exact source set for
  each explanation task, 15 points total per arm.
- Tokens: CLI `input_tokens + output_tokens`; cached input remains a subset.
- Diff size: added plus removed lines in coding fixtures.
- Tool output: bytes in completed command outputs from the retained event stream.

The runner rotates arm order to reduce simple ordering bias. Every session uses
a fresh Git fixture and an ephemeral Codex home. The initial inventory probe must
return `NONE`; external local-skill reads invalidate the run.

## Grading correction

The first runner version mistakenly named explanation expectations `P1`–`P5`,
while the fixtures and all unchanged answers use their actual evidence IDs:
`E1`–`E5`, `A1`–`A5`, and `R1`–`R5`. The original failed grades remain in
`summary.json` as `original_grade`; `grade` is the deterministic corrected score.
No answer, token count, trace, or diff was regenerated or discarded.

## Evidence and limits

`manifest.json` retains fixtures, prompts, hashes, host, model, and arm order.
`results.json` is the runner's original output. `summary.json` adds corrected
grades and token totals; `aggregates.json` contains the table inputs. Each run
directory retains prompt, answer, sanitized event trace, diff, and raw metrics.

This is one model, one run per arm, and eight author-designed synthetic tasks.
There are no repeats, confidence intervals, cost conversion, or cross-model
claims. Prompt length contributes to token totals, so an added ruleset must earn
back its own context cost to count as an improvement.

## Reproduce

```bash
python scripts/run_chisle_benchmark.py \
  --work-dir /tmp/abvx-chisle-work-NEW \
  --output /tmp/abvx-chisle-results-NEW \
  --model gpt-6-astra --effort medium
```

Regenerate this report from retained evidence:

```bash
python scripts/summarize_chisle_benchmark.py
```

# LLM-summary validation of anchor-compressed memory on generated agent traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-summary-validation-of-anchor-compressed-memory-on-gene-5a7d9296a7`
Run ID: `llm-summary-validation-of-anchor-compressed-memory-on-gene-5a7d9296a7-20260629T200311135789+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Anchor-compressed memory on LLM-generated agent traces with lossy summaries: enoch://control-plane/projects/anchor-compressed-memory-on-llm-generated-agent-traces-wit-ca9373ed8f/runs/anchor-compressed-memory-on-llm-generated-agent-traces-wit-ca9373ed8f-20260629T193239779869+0000
- Parent run decision: Anchor-compressed agent memory vs flat-vector and full-transcript: enoch://control-plane/projects/anchor-compressed-agent-memory-vs-flat-vector-and-full-transcript-ba4e30b0d89d/runs/anchor-compressed-agent-memory-vs-flat-vector-and-full-transcript-ba4e30b0d89d-20260629T191222120781+0000

## What looked useful

Anchor compression is not free: at 128 tokens it is roughly tied with recency and far below unanchored key-value answer recall. At 512 tokens it improves source-supported answers over recency from 0.405833 to 0.517083, and at 1024 tokens from 0.706458 to 0.992500. Unanchored key-value summaries reached 1.0 answer accuracy at budgets >=256 but had 0.0 source-anchor support.

## Boundaries and scale limits

Synthetic traces, template summaries, exact-match validation, no real LLM summarizer or LLM judge, no naturalistic production agent traces, and short CPU-only runs under one second per condition.

## Claim scope

On deterministic generated agent traces with state overwrites and distractors, anchor-compressed summaries provide checkable source-event support and outperform equal-token recency windows at moderate token budgets, while unanchored key-value summaries remain more token-efficient for answer-only recall but provide no retained source-anchor evidence.

## Why it stopped

Evidence is bounded to generated traces and deterministic template validation, so it supports a mechanism but not a paper-ready claim about LLM summaries on real agent traces.

## Recommended next action

Stop this run as a synthetic no-paper useful signal; next run should replace template summaries and exact-match validation with real LLM-generated summaries and LLM or human validation against a hidden event ledger.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-authored anchor summaries on naturalistic agent traces with hidden-ledger validation
- Success threshold: Anchored summaries improve verifier-supported answer accuracy by at least 10 percentage points over equal-token recency and reduce unsupported accepted answers by at least 50% versus unanchored summaries, across at least 500 naturalistic trace-query pairs.
- Stop condition: Stop if anchored summaries fail to beat recency by 5 percentage points in verifier-supported answer accuracy at two moderate budgets, or if LLM validators cannot reliably distinguish supported from unsupported anchor claims above 0.8 accuracy on calibration items.

## Evidence references

- Artifact root: `<local-path>/projects/llm-summary-validation-of-anchor-compressed-memory-on-gene-5a7d9296a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

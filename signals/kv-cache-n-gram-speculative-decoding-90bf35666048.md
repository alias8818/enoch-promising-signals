# KV-Cache N-Gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-n-gram-speculative-decoding-90bf35666048`
Run ID: `kv-cache-n-gram-speculative-decoding-90bf35666048-20260601T040551357628+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8016b872fcd7

## What looked useful

On local Python stdlib code, word/punctuation tokens reached a 2.067x conservative proxy target-call speedup at n=4/max_draft=8; local docs reached 1.294x; duplicated controller prompts reached 8.892x only when the repeated block fit in context. A 512-token window preserved 1.838x on code but only 1.129x on docs.

## Boundaries and scale limits

No real transformer verifier, no GPU serving path, no tokenizer-matched production model, no batching/latency measurement, and corpora were local fallback slices after public corpus download exceeded the smoke setup budget.

## Claim scope

Trace-level verifier proxy shows context-local n-gram drafting can produce accepted multi-token continuations in repetitive prompts and code-like text, with weaker gains on local natural-language documentation.

## Why it stopped

Bounded proxy evidence supports the mechanism in some domains but does not validate real model serving speedup or quality.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the draft policy into a small greedy transformer decoder and measure accepted length, tokens/sec, and output equivalence against no speculation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-integrated KV-cache n-gram drafting on a small decoder
- Success threshold: At least 20% wall-clock tokens/sec improvement on code/repetitive prompt sets, no regression beyond 5% on ordinary prose prompts, and byte-identical greedy outputs.
- Stop condition: Stop if lookup plus verification overhead eliminates speedup, if accepted length falls below 0.25 tokens per position on target prompts, or if output equivalence fails.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-n-gram-speculative-decoding-90bf35666048`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

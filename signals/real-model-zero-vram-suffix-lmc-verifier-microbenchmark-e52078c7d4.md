# Real-model zero-VRAM suffix-LMC verifier microbenchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-zero-vram-suffix-lmc-verifier-microbenchmark-e52078c7d4`
Run ID: `real-model-zero-vram-suffix-lmc-verifier-microbenchmark-e52078c7d4-20260611T092729586996+0000`

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

- Parent run decision: KV-cache verifier benchmark for zero-VRAM suffix-LMC drafting: enoch://control-plane/projects/kv-cache-verifier-benchmark-for-zero-vram-suffix-lmc-draft-e750ece9a8/runs/kv-cache-verifier-benchmark-for-zero-vram-suffix-lmc-draft-e750ece9a8-20260611T090100148850+0000
- Parent run decision: Suffix-LMC Speculative Decoding with Zero Draft VRAM on GB10: enoch://control-plane/projects/suffix-lmc-speculative-decoding-with-zero-draft-vram-on-gb10-fec1fe5b47a1/runs/suffix-lmc-speculative-decoding-with-zero-draft-vram-on-gb10-fec1fe5b47a1-20260611T053739748453+0000

## What looked useful

Correctness is strong when suffixes are token-ID concatenated and prefix KV caches are tensor-cloned. Performance is mixed: isolated zero-VRAM CPU cached verifier is 0.117x the CPU full baseline on short prefixes but 1.080x on long prefixes; GPU cached is slower than GPU full in both main workloads.

## Boundaries and scale limits

One small pretrained GPT-2-family model, synthetic prompt/suffix cases, 72 short-prefix cases and 64 long-prefix cases, no batched multi-suffix cache scoring, no 7B+ model, no production inference engine, and no broad tokenizer/model-family sweep.

## Claim scope

On distilgpt2 with fixed token suffixes, a zero-VRAM CPU suffix-cache verifier can match full-context logprob scores and gives a small long-prefix CPU speedup, but it is much slower on short prefixes and does not beat the GPU full-context baseline.

## Why it stopped

Tier-2 real-model benchmarks produced mixed direct evidence rather than a robust win: the mechanism is correct, but performance only helps modestly for long CPU prefixes and loses badly for short prefixes and against the GPU full-context baseline.

## Recommended next action

Stop this run as no-paper useful signal; the only bounded next test worth running is a batched multi-suffix zero-VRAM verifier on a larger local model to determine whether batching removes token-by-token overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batched zero-VRAM suffix-LMC verifier on a larger local causal LM
- Success threshold: On the long-prefix workload, isolated zero-VRAM CPU batched cached scoring is at least 1.5x faster than isolated CPU full-context scoring with max absolute logprob difference below 0.001 and identical score ordering; short-prefix slowdown must be quantified and bounded.
- Stop condition: Stop if batched cached scoring is below 1.2x CPU full-context speed on long prefixes or fails the 0.001 max logprob agreement threshold.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-zero-vram-suffix-lmc-verifier-microbenchmark-e52078c7d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

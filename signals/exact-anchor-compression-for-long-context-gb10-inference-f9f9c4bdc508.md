# Exact Anchor Compression for Long-Context gb10 Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-compression-for-long-context-gb10-inference-f9f9c4bdc508`
Run ID: `exact-anchor-compression-for-long-context-gb10-inference-f9f9c4bdc508-20260609T150513898701+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7d6a4a111bc8

## What looked useful

The algebraic mechanism is sound for explicit duplicate-key groups using a log-count softmax correction, with 1.96x to 2.71x speedups at 4096 to 8192 tokens in the synthetic benchmark. The broader exact-anchor hypothesis is not supported for ordinary repeated token anchors because positional/contextual K/V states differ; naive RoPE anchor merging produced large output error and the transformer KV identity check found zero exact repeated-anchor K/V matches.

## Boundaries and scale limits

Synthetic attention tensors up to sequence length 16384, 8 heads, 128 head dimension, one decode query, float32; small random 4-layer GPT-2-style model for architecture KV identity; no trained long-context checkpoint or end-to-end serving stack.

## Claim scope

On a GB10 PyTorch decode-query microbenchmark, exact KV anchor compression is numerically valid and faster only when anchor keys are truly identical; repeated anchor token IDs in a GPT-2-style transformer architecture did not produce identical K/V cache entries.

## Why it stopped

Bounded early falsification: the exact duplicate mechanism works in a synthetic proxy, but the required identical-key condition failed in the direct transformer-architecture check and naive positional anchor merging changed outputs substantially.

## Recommended next action

Stop this exact-anchor-compression run as a no-paper useful signal; only revisit exact compression if a model or serving stack explicitly guarantees shared anchor keys.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained-checkpoint frequency of near-duplicate anchor KV states
- Success threshold: At least 25% of repeated anchor K/V entries cluster at tolerance 1e-4 while keeping attention output max absolute error below 1e-3 and showing at least 1.5x decode-attention speedup at sequence length 8192.
- Stop condition: Stop if exact matches remain zero and near-duplicate clustering below tolerance 1e-4 covers less than 5% of repeated anchor entries or output max absolute error exceeds 1e-2.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-compression-for-long-context-gb10-inference-f9f9c4bdc508`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

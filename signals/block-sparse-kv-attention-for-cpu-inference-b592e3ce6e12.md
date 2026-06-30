# Block-Sparse KV Attention for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `block-sparse-kv-attention-for-cpu-inference-b592e3ce6e12`
Run ID: `block-sparse-kv-attention-for-cpu-inference-b592e3ce6e12-20260609T000141298490+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/aa358701de54

## What looked useful

Low-retention block-sparse KV attention has a measurable CPU latency mechanism at long context, but the simple block-loop implementation loses much of the benefit as retention rises, especially around 50% retained tokens.

## Boundaries and scale limits

Synthetic KV tensors and random block masks only; no real model quality, mask-selection cost, quantized KV, fused C++ kernel, batched serving, NUMA tuning, or end-to-end LLM throughput validation.

## Claim scope

On a CPU-only Xeon host with synthetic FP32 KV tensors, exact block-sparse single-token decode attention is faster than dense attention primarily when a small fraction of KV tokens is retained; 12.5% retained KV won 19/20 single-thread cases with 2.62x median speedup, while 50% retained KV was usually slower.

## Why it stopped

No-paper closure: local synthetic evidence is useful but insufficient for a publication-grade CPU inference claim.

## Recommended next action

Run a bounded deepen follow-up with a fused C++/SIMD sparse KV kernel plus a real small-LLM block-selection policy, measuring both decode latency and quality at long context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU Block-Sparse KV Attention with Real Policy Cost
- Success threshold: At least 1.5x end-to-end decode speedup at 12.5-25% retained KV with less than 2% relative degradation on the selected quality metric.
- Stop condition: Stop if policy overhead plus sparse kernel latency is not at least 1.2x faster than dense attention in two long-context settings, or if quality degradation exceeds 5% relative at 25% retained KV.

## Evidence references

- Artifact root: `<local-path>/projects/block-sparse-kv-attention-for-cpu-inference-b592e3ce6e12`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

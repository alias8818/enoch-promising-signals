# Low-rank KV projection for long-context CPU decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `low-rank-kv-projection-for-long-context-cpu-decoding-3c4797b37fa9`
Run ID: `low-rank-kv-projection-for-long-context-cpu-decoding-3c4797b37fa9-20260629T121602018139+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b2fd3306bddb

## What looked useful

The mechanism is conditionally promising: low-rank KV projection is accurate only when the cache is actually low-intrinsic-rank and the basis is matched. High-rank controls show near-total attention-output distortion despite memory and latency gains.

## Boundaries and scale limits

No real transformer KV cache, no learned projection training, no perplexity or task metric, no prefill-cost accounting, no multi-layer model evaluation, and no production LLM runtime. Largest synthetic cache was seq_len 8192, d_model 256, 64 decode queries.

## Claim scope

Synthetic Numpy CPU decode-attention probe: oracle low-rank KV projection can reduce cache bytes by about 7-8x and improve decode-only latency by about 1.3-2.1x at rank 32 while preserving attention outputs on rank-32 low-intrinsic-rank caches, but fails on high-rank Gaussian caches.

## Why it stopped

No-paper useful signal: this run is a synthetic mechanism probe, not direct model-quality or serving evidence.

## Recommended next action

Run a bounded real-model follow-up on GPT-2-small-class long-context KV caches with fitted per-layer projection bases, measuring dense-vs-projected decode throughput plus perplexity/logit-KL at matched quality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV cache low-rank projection on GPT-2-small-class decoding
- Success threshold: At rank <=25% of head dimension, achieve >=1.3x CPU decode speedup and >=3x KV-byte reduction while keeping mean next-token logit KL <=0.02 or perplexity increase <=2% on the bounded prompt set.
- Stop condition: Stop if fitted projections exceed 5% perplexity increase or logit KL remains above 0.05 at ranks that provide at least 3x KV-byte reduction.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-kv-projection-for-long-context-cpu-decoding-3c4797b37fa9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

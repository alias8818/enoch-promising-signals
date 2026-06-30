# Tiered KV cache with exact anchors and low-rank compression for 32k local inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-kv-cache-with-exact-anchors-and-low-rank-compression-for-32k-local-inference-412723538811`
Run ID: `tiered-kv-cache-with-exact-anchors-and-low-rank-compression-for-32k-local-inference-412723538811-20260602T152201451082+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e07d7bd80473

## What looked useful

At 32k, rank 16 used 14.3% of full KV storage and gave about 2.1x decode-attention speedup with very low error on synthetic low-rank and exact-anchor retrieval cases, but it catastrophically missed a dominant off-anchor retrieval needle. Rank 32 recovered the synthetic off-anchor needle at 26.6% KV storage and about 1.8x speedup.

## Boundaries and scale limits

No real transformer KV traces, no multi-layer or multi-head model, no generation-quality benchmark, and no production fused-kernel implementation were tested.

## Claim scope

Synthetic CUDA single-query decode attention at 32k context, dim 128, with exact recent tokens, periodic anchors, and SVD low-rank old-token KV reconstruction.

## Why it stopped

No-paper useful signal: the mechanism is supported only by synthetic single-query evidence and includes a clear failure mode for rank 8/16 non-anchor retrieval.

## Recommended next action

Run a bounded deepen test on real 32k model KV/Q traces comparing periodic anchors to adaptive salience/outlier anchors before attempting a production cache or paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive exact anchors on real 32k KV traces
- Success threshold: At rank 16 and below 20% KV storage, adaptive anchors keep relative attention-output error below 0.05 and preserve at least 90% of full-attention needle mass on real-trace retrieval cases where periodic anchors fail.
- Stop condition: Stop if adaptive anchors cannot beat periodic anchors on real traces at the same memory ratio or if rank 16 still loses more than 25% of dominant needle attention mass.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-cache-with-exact-anchors-and-low-rank-compression-for-32k-local-inference-412723538811`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

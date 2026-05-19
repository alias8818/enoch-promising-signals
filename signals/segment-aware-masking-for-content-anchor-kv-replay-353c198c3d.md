# Segment-aware masking for content-anchor KV replay

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `segment-aware-masking-for-content-anchor-kv-replay-353c198c3d`
Run ID: `segment-aware-masking-for-content-anchor-kv-replay-353c198c3d-20260516T064522661287+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Segment-aware masking for content-anchor KV replay: internal_generated:segment-aware-masking-for-content-anchor-kv-replay-353c198c3d

## What looked useful

The mechanism is supported: segment-aware masks eliminate cross-segment leakage and preserve exact logits in packed replay. The practical inference claim remains unsupported because dense packed attention does not realize the theoretical KV-token and allowed-pair savings without a block-sparse or paged execution path.

## Boundaries and scale limits

Validation used synthetic/random-weight transformer models up to 8 layers, width 256, 32 segments, anchor length 64, suffix length 64 on one GB10. It did not test pretrained LLM weights, production paged-attention kernels, real KV cache allocators, or long-context serving workloads. Dense PyTorch packed attention was slower than exact batched evaluation at the largest tested shape.

## Claim scope

In a deterministic transformer harness with shared anchors, repeated segment-local positions, and fixed random weights, segment-aware masking made packed content-anchor replay numerically equivalent to exact per-segment causal evaluation while naive packed causal masking leaked across segments and changed suffix logits.

## Why it stopped

Moderate direct mechanism validation succeeded, but the paper-level practical claim was not established: the evidence is synthetic/random-weight and the dense prototype becomes about 5.1x slower than exact batched evaluation at the largest tested packing shape.

## Recommended next action

Stop this run as no-paper useful evidence; the bounded next action is to implement or adapt a sparse/paged attention replay kernel and require exactness plus wall-time and memory wins at 32+ segments.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sparse/paged execution for exact segment-aware content-anchor KV replay
- Success threshold: At 32+ segments and anchor length at least 64, sparse/paged segment-aware replay must keep max suffix-logit error below 1e-5, keep foreign-segment leakage at zero, reduce measured KV memory by at least 35%, and improve wall time by at least 1.25x versus exact per-segment evaluation.
- Stop condition: Stop if exactness fails, if leakage is nonzero, or if the sparse/paged implementation cannot beat exact batched evaluation wall time by 1.25x at the target shape after one bounded kernel/prototype implementation pass.

## Evidence references

- Artifact root: `<local-path>/projects/segment-aware-masking-for-content-anchor-kv-replay-353c198c3d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

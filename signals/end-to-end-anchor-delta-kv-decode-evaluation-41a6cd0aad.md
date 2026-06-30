# End-to-End Anchor-Delta KV Decode Evaluation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-anchor-delta-kv-decode-evaluation-41a6cd0aad`
Run ID: `end-to-end-anchor-delta-kv-decode-evaluation-41a6cd0aad-20260526T162201279169+0000`

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

- Parent run decision: Anchor-Delta KV Compression for Long Context: enoch://control-plane/projects/anchor-delta-kv-compression-for-long-context-9d6611a628c9/runs/anchor-delta-kv-compression-for-long-context-9d6611a628c9-20260525T221521568958+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3a0eedd186f6

## What looked useful

Anchor-delta KV reconstruction has a plausible bounded operating point on this small direct test, but decode stability is brittle: block sizes 2, 6, 8, and 16 diverged on one prompt despite low aggregate reconstruction RMSE. Aggregate cache error alone is not a sufficient stability predictor.

## Boundaries and scale limits

No larger model, long-context workload, sampled decoding, broad prompt suite, fused compressed-attention kernel, or measured production allocator savings. Runtime is from a Python/Torch prototype that reconstructs full KV tensors before each decode step.

## Claim scope

Small direct fp16 autoregressive decode test on distilgpt2 over 6 prompts x 32 generated greedy tokens. A naive anchor-delta KV cache with block sizes 3-4 preserved greedy outputs with low KL and estimated 1.48x-1.58x cache compression, while several other block sizes diverged.

## Why it stopped

Tier 1 direct evidence was completed and is no-paper: it supports a mechanism in narrow settings but shows brittle end-to-end decode behavior and lacks optimized memory-resident serving evidence.

## Recommended next action

Run a bounded deepen test with exact-prefix teacher-forced logits, first-divergence/top-margin diagnostics, and adaptive per-head or per-channel scaling before any larger-model or kernel implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-Delta KV Exact-Prefix Stability and Adaptive Scaling
- Success threshold: At least one adaptive configuration reaches >=1.5x estimated KV compression, >=99% exact-prefix top-1 agreement, mean KL <=0.01, and no prompt with autoregressive greedy match below 95% over the bounded suite.
- Stop condition: Stop if matched-compression adaptive variants still show recurrent first-divergence on low-margin steps or fail to beat the naive block-4 stability/compression tradeoff.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-anchor-delta-kv-decode-evaluation-41a6cd0aad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

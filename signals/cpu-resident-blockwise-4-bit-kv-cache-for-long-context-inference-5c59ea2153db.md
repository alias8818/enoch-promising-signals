# CPU-Resident Blockwise 4-bit KV Cache for Long Context Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-resident-blockwise-4-bit-kv-cache-for-long-context-inference-5c59ea2153db`
Run ID: `cpu-resident-blockwise-4-bit-kv-cache-for-long-context-inference-5c59ea2153db-20260527T150010950222+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/33375f50b68e

## What looked useful

Blockwise int4 KV reduced cache bytes by 6.4x versus fp32 at block size 32 and gave up to 1.54x single-thread speedup in one synthetic row, but it lost to the parallel fp32 baseline in every 4-thread and 8-thread configuration and produced 0.132-0.156 relative L2 output error versus fp32.

## Boundaries and scale limits

No full transformer, no GPU/PCIe/UMA transfer path, no fp16/bf16 serving baseline, no real model quality metrics, and no optimized SIMD int4 unpack/dequant kernel. Compression versus fp16/bf16 is derived as 3.2x at block size 32, not directly benchmarked.

## Claim scope

Synthetic CPU microbenchmark of one-token attention over blockwise signed int4 K/V caches with per-block fp32 scales, compared against an fp32 K/V baseline for sequence lengths up to 32768, 4 heads, head dimension 128.

## Why it stopped

Useful bounded CPU evidence only: compression is supported, but scalar int4 dequantization is not reliably faster than parallel fp32 and synthetic output error is nontrivial, so this is not a full validation of CPU-resident long-context inference.

## Recommended next action

Stop paper path for this run; a bounded deepen follow-up should test an optimized AVX2/AVX-512 int4 unpack/dequant kernel against a real fp16/bf16 KV baseline and include a small real-model quality check.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SIMD int4 KV attention versus fp16 KV baseline with small real-model quality check
- Success threshold: At sequence length at least 16384, int4 KV must be no slower than fp16/bf16 baseline in median one-token decode latency, preserve at least 3x KV byte reduction versus fp16/bf16 including scales, and keep real-model perplexity increase under 5% or logit relative L2 under a predeclared small threshold.
- Stop condition: Stop if optimized int4 remains slower than fp16/bf16 by more than 10% at sequence length 16384 or if real-model quality degradation exceeds the threshold despite block sizes 16 and 32.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-resident-blockwise-4-bit-kv-cache-for-long-context-inference-5c59ea2153db`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

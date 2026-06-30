# 4-bit Groupwise KV Cache for 16k Local Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-groupwise-kv-cache-for-16k-local-inference-237ade9e0a3a`
Run ID: `4-bit-groupwise-kv-cache-for-16k-local-inference-237ade9e0a3a-20260601T031503693373+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/24bdd0ffe31a

## What looked useful

Packed int4 plus fp16 group metadata reduces estimated KV-cache memory by 3.2x-3.76x. Normal synthetic attention outputs retain high cosine at 16k, but relative L2 is about 0.106-0.143 and outlier-stressed inputs degrade to about 0.313-0.388 at 16k. Naive dequantize-then-attend is about 13x-14x slower than fp16 at 16k.

## Boundaries and scale limits

No real transformer model, perplexity, task quality, full serving stack, or fused int4 attention kernel was tested. Runtime uses naive full-cache dequantization before attention and should be treated as an upper-bound proxy, not an optimized implementation.

## Claim scope

Synthetic single-query CUDA decode probe for per-token per-head asymmetric 4-bit groupwise KV-cache quantization up to sequence length 16384 with heads=8 and head_dim=128.

## Why it stopped

Closed as a proxy useful-signal result: memory savings are supported, but naive runtime and outlier sensitivity prevent a practical or paper-ready claim.

## Recommended next action

Do not write a paper from this run; next run should implement or use a fused int4 decode kernel and evaluate a small real transformer at 16k against fp16 KV for perplexity/task quality and tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused 4-bit KV decode on a small real 16k-context model
- Success threshold: At 16k, group-size-32 int4 KV must reduce peak KV memory by at least 3x, keep quality within 2% relative perplexity or equivalent task metric of fp16 KV, and achieve at least parity decode tokens/sec versus fp16 KV.
- Stop condition: Stop if fused int4 decode remains slower than fp16 by more than 10% at 16k or if real-model quality degradation exceeds 2% after group-size and clipping/outlier ablations.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-groupwise-kv-cache-for-16k-local-inference-237ade9e0a3a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

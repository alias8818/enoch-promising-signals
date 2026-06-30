# KV-cache 4-bit compression for CPU long-context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-4-bit-compression-for-cpu-long-context-9f9f4c916070`
Run ID: `kv-cache-4-bit-compression-for-cpu-long-context-9f9f4c916070-20260628T033721986528+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/426e03455cca

## What looked useful

Packed int4+fp32-scale KV used 6.4x less memory than fp32 and 3.2x less than estimated fp16, but single-thread int4 dequantization plus attention was 2.67x-4.77x slower than fp32 attention and produced 0.127-0.153 relative L2 output error on random-tensor one-token attention. Naive full dequantization is therefore not an automatic CPU long-context speed win; it is mainly a capacity tradeoff unless fused/blocked kernels avoid materializing full fp32 K/V each token.

## Boundaries and scale limits

No real transformer, perplexity/task-quality evaluation, production serving trace, fp16 executable latency baseline, SIMD/fused int4 kernel, or calibrated model-specific KV distribution was tested. Largest direct test was 65,536 synthetic tokens on one 8-core CPU worker and completed in seconds.

## Claim scope

Bounded synthetic CPU microbenchmark: packed signed int4 groupwise KV cache with fp32 scales, one-token attention over random K/V tensors, context lengths up to 65,536, heads=8, dim=64, NumPy implementation. Evidence supports memory-capacity benefit but not latency benefit for naive full dequantization.

## Why it stopped

Bounded proxy evidence is sufficient to reject the naive full-dequantization version as paper-ready; the result is not full validation because it lacks real-model quality and a fused CPU kernel.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement or use a fused/blocked CPU int4 attention path that consumes packed KV directly and compare latency/error against fp32 and fp16/bfloat16 baselines on a small real transformer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU int4 KV attention for long-context decode
- Success threshold: At 32k and 64k context, packed-int4 direct attention is no more than 1.25x slower than the strongest uncompressed CPU baseline while using at least 2.5x less KV memory than fp16/bfloat16 and causing no more than 2% perplexity degradation or an agreed small KL threshold.
- Stop condition: Stop if direct packed-int4 attention remains more than 2x slower than the uncompressed baseline after a minimal blocked/SIMD implementation, or if real-model quality degradation exceeds 5% at 8k context.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-4-bit-compression-for-cpu-long-context-9f9f4c916070`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# 4-bit KV Cache on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-kv-cache-on-cpu-2d8938dd7c29`
Run ID: `4-bit-kv-cache-on-cpu-2d8938dd7c29-20260525T052950981823+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fa784b59fdfb

## What looked useful

Packed int4 KV storage reduced bytes by about 7.9x versus fp32, but the naive CPU decode path was 15.6x to 70.0x slower than fp32 single-thread and 76.5x to 90.2x slower in a 4-thread calibration, with relative output L2 error around 0.14-0.20.

## Boundaries and scale limits

Tested only NumPy vectorized CPU microbenchmarks up to seq_len=4096 and dim=512 on an Intel Xeon Silver 4114-class worker. Did not test fused SIMD int4 kernels, real LLM perplexity/task quality, grouped-query attention, end-to-end serving, or large production contexts.

## Claim scope

Synthetic single-token CPU decode attention with fp32 K/V baseline compared against int8 and packed signed-int4 K/V storage using per-token symmetric scales and unpack/dequantization inside the timed decode path.

## Why it stopped

Early local falsification of the naive packed int4 CPU KV-cache path: memory savings are real, but latency and quantization error are not competitive in the tested implementation; this is not a full validation or rejection of optimized fused kernels.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test a fused AVX2/AVX-512 int4 attention microkernel that avoids full dequant materialization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused SIMD int4 KV-cache attention on CPU
- Success threshold: Packed int4 stores at least 7x fewer KV bytes than fp32, reaches within 1.5x fp32 median decode latency at seq_len=4096 and dim=512, and keeps relative output L2 error below 0.08.
- Stop condition: Stop as negative if fused int4 remains more than 2x slower than fp32 or relative output L2 error remains above 0.10 after one optimized CPU kernel attempt.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-kv-cache-on-cpu-2d8938dd7c29`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

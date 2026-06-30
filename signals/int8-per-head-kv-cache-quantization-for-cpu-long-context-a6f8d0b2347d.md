# INT8 Per-Head KV Cache Quantization for CPU Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-per-head-kv-cache-quantization-for-cpu-long-context-a6f8d0b2347d`
Run ID: `int8-per-head-kv-cache-quantization-for-cpu-long-context-a6f8d0b2347d-20260607T224505301568+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fd8255f1ed89

## What looked useful

Per-head INT8 K/V cache quantization is mechanically promising for CPU long-context decode because it cuts cache bandwidth and memory footprint, but single-scale-per-head quantization is visibly outlier-sensitive. Normal synthetic traces at length 8192 had mean 2.15x speedup and 0.016 relative L2 output error over five seeds; outlier traces had mean 2.66x speedup but 0.065 relative L2 error and much larger max absolute output error.

## Boundaries and scale limits

Synthetic K/V/Q tensors only; no real transformer KV traces, no perplexity or task metric, no end-to-end model serving stack, no SIMD-optimized production kernel, no batching or multilayer cache behavior. Results compare against float32 KV cache, not fp16/bfloat16 production baselines.

## Claim scope

In a local scalar C++ CPU single-token decode-attention benchmark with 8 heads, head dimension 64, and synthetic context lengths up to 16384, per-head symmetric INT8 K/V cache quantization reduced K/V cache memory by about 4x and improved per-token attention latency by about 1.9x to 2.8x for medium and long contexts, with low error for normal-like caches but materially larger error under outlier-heavy cache distributions.

## Why it stopped

No-paper useful signal: the local benchmark directly supports a memory/speed mechanism but remains a synthetic kernel-level proxy and exposes outlier sensitivity, so it is insufficient for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up using real small-transformer KV traces and an end-to-end CPU inference baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV-Trace Replay for Per-Head INT8 CPU Cache Quantization
- Success threshold: At context length at least 8192 on real model traces, achieve at least 1.5x CPU decode-attention or end-to-end decode speedup versus float32 KV, at least 3.5x KV memory reduction, mean attention KL below 0.001, relative output L2 below 0.03 for most layers, and perplexity degradation below 1%.
- Stop condition: Stop if real KV traces show repeated per-layer relative L2 error above 0.05 or perplexity degradation above 2% with per-head scales, unless an outlier-aware variant fixes the failures within the same bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/int8-per-head-kv-cache-quantization-for-cpu-long-context-a6f8d0b2347d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Per-Head Quantized KV-Cache on CPU for Long Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `per-head-quantized-kv-cache-on-cpu-for-long-context-a4e1700936dd`
Run ID: `per-head-quantized-kv-cache-on-cpu-for-long-context-a4e1700936dd-20260605T044814108706+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/752afe044432

## What looked useful

The core memory-footprint mechanism is supported locally: a simple allocation-free int8 per-head decode loop was faster than FP32 at long context and used one-quarter of the KV-cache storage, but this remains microbenchmark evidence only.

## Boundaries and scale limits

Not end-to-end model serving; no real transformer activations, perplexity, generation-quality, prefill, batching, GQA/MQA, FP16/BF16 baseline, or optimized SIMD kernel validation. Tested heads=8, dim=64 up to seq=65536, plus a tiny smoke case.

## Claim scope

In a single-threaded C++ CPU microbenchmark for one-token attention decode with synthetic random tensors, per-head symmetric int8 KV-cache quantization reduced KV-cache bytes by about 4x and improved decode latency by 1.75x to 3.48x for 1K-65K-token contexts while keeping output relative L2 below 0.02 versus FP32.

## Why it stopped

Microbenchmark evidence supports the mechanism but is not a full validation of long-context model serving or quality.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next, integrate per-head int8 KV cache into a small CPU transformer inference path and measure latency, RSS, and perplexity against FP32/FP16/BF16 KV-cache baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU transformer validation for per-head int8 KV cache
- Success threshold: At 16K tokens or longer, int8 KV cache should reduce peak KV-cache storage by at least 3.8x, improve decode latency by at least 1.3x, and keep perplexity/logprob degradation within a predeclared small tolerance versus the strongest local baseline.
- Stop condition: Stop if end-to-end decode is not faster than the strongest baseline at 16K+ context or if quality/perplexity degradation exceeds the tolerance despite the memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-quantized-kv-cache-on-cpu-for-long-context-a4e1700936dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

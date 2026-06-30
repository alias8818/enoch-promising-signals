# Bounded KV-Cache Compression for Volunteer Worker Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-kv-cache-compression-for-volunteer-worker-inference-e14382e2f1bd`
Run ID: `bounded-kv-cache-compression-for-volunteer-worker-inference-e14382e2f1bd-20260620T212402471040+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/48917399b75b

## What looked useful

KV quantization is the locally supported bounded-memory mechanism; pure eviction to sink+recent tokens is an early negative under middle-token dependency. FP32 protection for sink/recent tokens gave only marginal error improvement over uniform per-vector quantization while increasing memory.

## Boundaries and scale limits

Proxy-only evidence: no real LLM weights, natural-language perplexity, benchmark task accuracy, optimized attention kernels, GPU decode path, batching, heterogeneous volunteer-device scheduling, or network/offload behavior were tested.

## Claim scope

In a deterministic NumPy decode-attention proxy with 8 heads, 64-dimensional heads, 128 query steps, 3 seeds, and cache lengths up to 4096, per-vector int8 KV quantization preserved attention outputs with relative L2 error near 0.006 while reducing estimated KV memory to roughly 26-29% of FP32. Sink+recent-only eviction failed when middle tokens remained query targets.

## Why it stopped

The run produced reproducible proxy evidence, but the result is not full validation because it does not include end-to-end model inference or optimized serving kernels.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded deepen test should integrate int8/int4 KV policies into a small real model runtime and measure perplexity, tokens/sec, and peak memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-model KV quantization on memory-constrained worker hardware
- Success threshold: Int8 KV policy achieves at least 50% peak KV-memory reduction, <=2% relative quality loss, and <=10% decode throughput loss versus the full-cache baseline.
- Stop condition: Stop if int8 KV causes >2% relative quality loss, >10% throughput loss, or implementation overhead prevents a fair bounded comparison within the local worker budget.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-kv-cache-compression-for-volunteer-worker-inference-e14382e2f1bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

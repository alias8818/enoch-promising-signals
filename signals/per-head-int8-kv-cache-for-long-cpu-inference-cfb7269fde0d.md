# Per-head int8 KV-cache for long CPU inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `per-head-int8-kv-cache-for-long-cpu-inference-cfb7269fde0d`
Run ID: `per-head-int8-kv-cache-for-long-cpu-inference-cfb7269fde0d-20260604T223104735130+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e621841cbccf

## What looked useful

Per-head int8 KV-cache is a plausible CPU long-context inference mechanism: it gives clear memory compression and synthetic decode-attention latency gains, while per-head scales improve quantization error over global scales when head ranges differ. The result is no-paper because it is proxy evidence against an fp32 baseline rather than direct real-model inference evidence.

## Boundaries and scale limits

Synthetic Q/K/V only; no full transformer stack, real model KV distributions, perplexity/task metrics, production fp16/bf16 KV baseline, batching, multi-layer cache effects, or optimized threaded production kernels were evaluated.

## Claim scope

In a local single-process C++ synthetic decode-attention microbenchmark on an Intel Xeon Silver 4114 CPU, per-head symmetric int8 KV-cache storage reduced fp32 KV-cache memory by about 4x and improved one-token attention latency by 1.64x to 2.88x over context lengths 1,024 to 16,384, with relative output RMSE around 1.5 percent for equal-scale synthetic heads. Under a 16x heterogeneous head-scale control, per-head scaling reduced output error versus global int8 scaling.

## Why it stopped

Closed as no-paper useful signal: the mechanism is supported by a synthetic CPU microbenchmark, but direct full-model evidence is required before any publication-grade claim.

## Recommended next action

Run a bounded real-model CPU inference follow-up in an existing inference stack, comparing fp16 or bf16 KV cache against per-head int8 KV cache on latency and perplexity over long contexts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU validation of per-head int8 KV cache
- Success threshold: At context length at least 8k, achieve at least 1.2x decode-latency speedup or a clear memory-pressure win versus fp16/bf16 KV, with perplexity degradation no worse than 1 percent relative or an equivalently bounded task-quality loss.
- Stop condition: Stop if per-head int8 is slower than fp16/bf16 at 8k context without a compensating memory-pressure benefit, or if quality loss exceeds the bounded tolerance after reasonable scale calibration.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-int8-kv-cache-for-long-cpu-inference-cfb7269fde0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

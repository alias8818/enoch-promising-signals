# Tiny Router Cascade for Local CPU Model Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-router-cascade-for-local-cpu-model-serving-dfb191f57783`
Run ID: `tiny-router-cascade-for-local-cpu-model-serving-dfb191f57783-20260528T021603382360+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/323a2ef4999d

## What looked useful

Tiny router cascades are promising only when the skipped fallback path includes materially expensive preprocessing or feature extraction. For pure scoring-only serving, router overhead was break-even to negative.

## Boundaries and scale limits

Not tested on autoregressive LLMs, quantized transformer CPU kernels, real prompt distributions, batching, KV-cache workloads, or judged generation quality. The benchmark used 20k train, 2k validation, 3k test examples and three random seeds.

## Claim scope

On an AG News CPU text-classification proxy using NumPy/stdlib Multinomial Naive Bayes models, a confidence-threshold tiny router preserved most fallback accuracy while improving full text-to-prediction pipeline throughput, but did not improve pre-vectorized scoring throughput.

## Why it stopped

Proxy evidence is mixed: full-pipeline speedup was reproducible, but scoring-only speedup was not, and the workload is not a real local LLM serving benchmark.

## Recommended next action

Stop this run as no-paper useful signal; next direct test should use two real local CPU models and include end-to-end preprocessing plus inference latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Model Router Cascade Benchmark
- Success threshold: Across at least two seeds or request shuffles, the routed cascade improves end-to-end p50 latency by >=20% versus always-large while quality remains within 1 percentage point or predeclared judged-quality tolerance.
- Stop condition: Stop if router overhead makes routed p50 latency less than 10% faster than always-large or if held-out quality drops by more than 2 percentage points at any threshold with meaningful routing.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-router-cascade-for-local-cpu-model-serving-dfb191f57783`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Trace-Driven Paged-KV Anchor Cache Serving Benchmark

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `28`
Project ID: `trace-driven-paged-kv-anchor-cache-serving-benchmark-5d60334321`
Run ID: `trace-driven-paged-kv-anchor-cache-serving-benchmark-5d60334321-20260518T064432754755+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `28`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Trace-Driven Paged-KV Anchor Cache Serving Benchmark: internal_generated:trace-driven-paged-kv-anchor-cache-serving-benchmark-5d60334321

## What looked useful

Paged-KV LRU reuse gave clear gains over no-cache in hot shared-prefix traces, but explicit anchor-aware retention did not separate from LRU: main-suite TTFT p95 delta was 0.0% across workloads and the largest cache-pressure improvement was under 0.05%.

## Boundaries and scale limits

Synthetic trace generation and modeled latency only; no real production traces, no vLLM/SGLang/TensorRT-LLM implementation, no GPU scheduler or batching measurement, and no datacenter-scale replay.

## Claim scope

Deterministic simulated paged-KV serving traces with 12,000 requests per workload/seed, four workload regimes, fixed seeds, no-cache and LRU baselines, random-anchor control, and fixed-capacity sensitivity sweeps.

## Why it stopped

Moderate synthetic trace-driven evidence found a useful negative signal: standard LRU paged-KV captures nearly all anchor reuse, and anchor-aware retention produced no practically meaningful direct metric improvement over LRU.

## Recommended next action

Stop this follow-up at depth 4; do not write a paper from this result because the bounded direct simulation falsifies a meaningful anchor-over-LRU serving advantage and the controller lineage is capped.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/trace-driven-paged-kv-anchor-cache-serving-benchmark-5d60334321`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

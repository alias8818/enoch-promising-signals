# Bounded model cascade with KV compression for local GPU serving under queue pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-model-cascade-with-kv-compression-for-local-gpu-serving-under-queue-pressure-eb6f3a37d127`
Run ID: `bounded-model-cascade-with-kv-compression-for-local-gpu-serving-under-queue-pressure-eb6f3a37d127-20260611T094815390773+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/29ac784301c8

## What looked useful

At 20-30 req/s, large-only policies dropped 100-1125 of 2400 requests under the modeled memory cap, while cascade and cascade_kv served all 2400 with p95 latency about 0.35-0.43 s. Cascade_kv used fewer small-model routes than cascade-only, preserving a higher quality proxy at the same pressure.

## Boundaries and scale limits

Synthetic BF16 matmul calibration only; no real LLM serving stack, batching, tokenizer, real KV-compression kernel, measured answer quality, request trace, or long-duration stability test. Results cover 2400-request simulated workloads at 8-30 req/s on modeled two-lane serving.

## Claim scope

In a bounded deterministic queueing simulator whose service rates are calibrated by same-host GB10 synthetic decode-like GPU kernels, queue-pressure model cascading improves served requests and tail latency under overload; modeled KV compression improves the cascade latency/quality tradeoff but is not sufficient as a large-only strategy at high pressure.

## Why it stopped

Proxy/synthetic evidence supports a mechanism but is not direct serving validation and is not publication-grade.

## Recommended next action

Stop this run as no-paper proxy evidence; next run should implement a real local two-model serving harness with actual KV compression and measure latency, drops, GPU memory, and quality under the same pressure schedule.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real local serving validation for queue-pressure cascade plus KV compression
- Success threshold: cascade_kv must reduce p95 latency by at least 25% versus large_only_kv and reduce small-model routing by at least 20% versus cascade at matched drop rate, with measured quality loss below 5%.
- Stop condition: Stop if real KV compression overhead erases latency gains or if measured quality loss exceeds 5% at the pressure level where cascade latency improves.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-model-cascade-with-kv-compression-for-local-gpu-serving-under-queue-pressure-eb6f3a37d12`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

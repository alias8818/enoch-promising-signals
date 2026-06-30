# Local Cascade Router for GB10: Tiered Draft-Verify with Bounded Queue Backpressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-cascade-router-for-gb10-tiered-draft-verify-with-bounded-queue-backpressure-c9b6091c74df`
Run ID: `local-cascade-router-for-gb10-tiered-draft-verify-with-bounded-queue-backpressure-c9b6091c74df-20260629T042041512189+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1af9aa073b79

## What looked useful

At 4.0x load, bounded static-base cascade capped the memory proxy at 768 MB and p95 latency at 3.733 s, while unbounded static-base cascade reached 20096 MB proxy memory and 57.679 s p95. Strong-tier bounded routing reduced overloaded p95 to 2.663 s with lower memory proxy but slightly lower rps and higher rejects; tiny-tier routing collapsed early.

## Boundaries and scale limits

No real model weights, tokenizer, CUDA kernels, batching, KV-cache allocation, GPU utilization, or measured draft acceptance traces were used. Results are proxy-only and should not be treated as GB10 serving throughput validation.

## Claim scope

A dependency-free discrete-event proxy shows that bounded queues and backpressure can cap latency and memory growth for a local draft/verify cascade under overload, and that tier choice materially affects the overload tradeoff.

## Why it stopped

Closed as no-paper useful signal because evidence is a synthetic router-control proxy, not direct GB10 model-serving validation.

## Recommended next action

Run a bounded GB10 real-model serving follow-up using one small draft model and one verifier model, with the same bounded-queue policies and measured accepted tokens/s, p95/p99 latency, rejects, GPU utilization, and MemAvailable/UMA telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 real-model bounded draft/verify router benchmark
- Success threshold: At a load level where verifier-only bounded serving rejects at least 20% of requests, the bounded cascade must improve completed accepted tokens/s by at least 20% while keeping p95 latency under 50% of the unbounded cascade and without sustained MemAvailable collapse.
- Stop condition: Stop if real-model acceptance rates or draft overhead make cascade completion throughput no better than verifier-only bounded serving at two adjacent load levels, or if UMA pressure grows without a stable admission cap.

## Evidence references

- Artifact root: `<local-path>/projects/local-cascade-router-for-gb10-tiered-draft-verify-with-bounded-queue-backpressure-c9b6091c74df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

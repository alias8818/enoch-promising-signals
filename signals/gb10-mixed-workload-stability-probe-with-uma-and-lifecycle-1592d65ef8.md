# GB10 mixed workload stability probe with UMA and lifecycle pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gb10-mixed-workload-stability-probe-with-uma-and-lifecycle-1592d65ef8`
Run ID: `gb10-mixed-workload-stability-probe-with-uma-and-lifecycle-1592d65ef8-20260613T180012003576+0000`

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

- Parent run decision: Tier-0 volunteer worker liveness and capability probe: enoch://control-plane/projects/tier-0-volunteer-worker-liveness-and-capability-probe-3231811523a1/runs/tier-0-volunteer-worker-liveness-and-capability-probe-3231811523a1-20260613T171451904256+0000
- Parent run decision: Bounded GB10 worker stability probe: enoch://control-plane/projects/bounded-gb10-worker-stability-probe-8d101af373/runs/bounded-gb10-worker-stability-probe-8d101af373-20260613T173517533727+0000

## What looked useful

Mixed pressure met the local stability threshold with no observed CUDA/lifecycle failures and bounded throughput/latency degradation.

## Boundaries and scale limits

Synthetic workload; medium local duration; no full model server, overnight soak, multi-node load, reboot cycle, or production concurrency.

## Claim scope

One GB10 host running PyTorch CUDA fp16 matmul under bounded UMA memory pressure and repeated CUDA subprocess lifecycle churn.

## Why it stopped

Tier 2 local confirmation produced useful bounded evidence but not publication-grade direct evidence.

## Recommended next action

Stop as no-paper useful signal; next bounded step is a real model-serving lifecycle test with the same MemAvailable and subprocess telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real model load/unload lifecycle pressure on GB10 UMA
- Success threshold: No process/CUDA failures, mixed throughput >=50% of baseline, p95 request latency <=2x baseline, and MemAvailable remains above 10% of host memory.
- Stop condition: Stop on any CUDA reset/OOM/process failure, MemAvailable below 10%, or mixed throughput below 50% baseline in two repeated trials.

## Evidence references

- Artifact root: `<local-path>/projects/gb10-mixed-workload-stability-probe-with-uma-and-lifecycle-1592d65ef8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

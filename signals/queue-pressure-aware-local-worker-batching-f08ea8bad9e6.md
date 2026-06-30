# Queue-Pressure-Aware Local Worker Batching

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-pressure-aware-local-worker-batching-f08ea8bad9e6`
Run ID: `queue-pressure-aware-local-worker-batching-f08ea8bad9e6-20260614T024401535344+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/34cc0b7659b0

## What looked useful

Pressure-aware policies consistently beat the best fixed p95 latency control in 15/15 paired seed comparisons: bursty_overload mean p95 delta -6.81%, spiky_near_capacity -16.79%, steady_70pct -2.61%, with near-zero throughput delta.

## Boundaries and scale limits

Evidence is simulator-only and uses an assumed service-time curve; it does not validate real local worker runtimes, multi-worker coordination, OS scheduler effects, serialization overheads, or production traces.

## Claim scope

In a deterministic single-worker discrete-event simulation with bursty arrivals, queue-pressure-aware batching improved p95 latency versus the best fixed-size batching control by 2.6% to 16.8% at effectively equal throughput across three workload regimes and five seeds.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported in a reproducible simulator, but direct real-worker evidence is required before any publication-grade claim.

## Recommended next action

Run a bounded live-worker benchmark that replays the same arrival traces against real local batched work and compares the selected pressure-aware policies against fixed-batch controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live local-worker replay benchmark for pressure-aware batching
- Success threshold: Pressure-aware batching wins p95 latency in at least 12 of 15 paired workload/seed comparisons with no more than 1% throughput loss and no p99 regression above 5%.
- Stop condition: Stop if pressure-aware batching loses p95 latency to fixed controls in two or more workload regimes or requires more than 1% throughput loss to show a tail-latency gain.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-aware-local-worker-batching-f08ea8bad9e6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

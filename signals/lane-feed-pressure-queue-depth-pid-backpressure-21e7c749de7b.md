# Lane feed pressure: queue-depth PID backpressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lane-feed-pressure-queue-depth-pid-backpressure-21e7c749de7b`
Run ID: `lane-feed-pressure-queue-depth-pid-backpressure-21e7c749de7b-20260628T031443559907+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/426e03455cca

## What looked useful

Anti-windup PID reduced p95 latency by 66.1% and queue RMS target error by 71.7% versus no-backpressure, but throughput was 2.65% lower and the offered-load drop/shedding rate was 1.99 percentage points higher. Versus bang-bang, anti-windup PID reduced p95 latency by 18.6% with near-equal throughput/drop.

## Boundaries and scale limits

Synthetic single-lane simulation only; no production Enoch lane telemetry, no real producer/consumer service, no multi-lane coupling, no network feedback, and no real task runtime distribution. The result does not validate a full lane feed pressure deployment.

## Claim scope

In a deterministic synthetic single-lane finite-queue benchmark with bursty offered load and a downstream service brownout, queue-depth PID backpressure reduced p95 queueing latency and queue-depth target error versus no-backpressure and fixed caps, and anti-windup PID modestly improved latency and target tracking versus a simple bang-bang controller.

## Why it stopped

Closed as no-paper useful signal: synthetic evidence supports latency/tracking benefits but not a general or publication-grade backpressure improvement, and the throughput/drop tradeoff remains unresolved.

## Recommended next action

Run a bounded direct producer/consumer queue-service benchmark or lane replay with tuned bang-bang, PI, and anti-windup PID controllers under an explicit SLA-weighted objective.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct producer-consumer queue benchmark for queue-depth PID backpressure
- Success threshold: Anti-windup PID beats tuned bang-bang by at least 20% on p95 latency or overload recovery time while completed throughput is no worse than 2% lower and offered-load drop rate is no more than 1 percentage point higher.
- Stop condition: Stop if tuned bang-bang matches PID within 5% on p95 latency/recovery at equal or better throughput/drop across the replay windows, or if PID requires workload-specific tuning that does not transfer across seeds/traces.

## Evidence references

- Artifact root: `<local-path>/projects/lane-feed-pressure-queue-depth-pid-backpressure-21e7c749de7b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

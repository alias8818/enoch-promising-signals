# Trace replay for zero-promotable queue pressure gating

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-replay-for-zero-promotable-queue-pressure-gating-a4bb0b10c6`
Run ID: `trace-replay-for-zero-promotable-queue-pressure-gating-a4bb0b10c6-20260605T231148407142+0000`

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

- Parent run decision: Queue Pressure with Zero Promotable Count: enoch://control-plane/projects/queue-pressure-with-zero-promotable-count-6b7170b89936/runs/queue-pressure-with-zero-promotable-count-6b7170b89936-20260605T223355248328+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f9f83ddb00d4

## What looked useful

Across three controlled 96-request traces, baseline made 21, 59, and 204 futile zero-promotable probes; gated replay made 0 in all cases and produced identical schedules. A 24/4, 96/8, and 192/16 request/capacity sweep also met the same schedule-equivalence and >=90% futile-probe-reduction threshold.

## Boundaries and scale limits

Synthetic CPU-only trace replay only; no real serving traces, GPU/model execution, concurrent scheduler implementation, KV-cache block movement, cancellations, preemption, or production arrival distribution was tested.

## Claim scope

In deterministic small trace replay with explicit arrive_at, promotable_at, and service_ticks fields, zero-promotable queue gating eliminated futile promotion probes while preserving exact per-request start and completion schedules.

## Why it stopped

Closed as no-paper useful signal: the controlled direct replay supports the mechanism but is not production or publication-grade evidence.

## Recommended next action

Run a bounded integrated scheduler replay using real or captured serving traces and record CPU scheduler time, lock pressure, latency, and throughput versus the ungated baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated scheduler replay for zero-promotable gating
- Success threshold: At least 25% lower scheduler CPU or lock-pressure metric and no more than 1% p95 latency regression, with identical completion set and no missed-promotable events.
- Stop condition: Stop if gated replay changes completion correctness, misses promotable events, or fails to reduce scheduler CPU/lock pressure by 10% on two representative traces.

## Evidence references

- Artifact root: `<local-path>/projects/trace-replay-for-zero-promotable-queue-pressure-gating-a4bb0b10c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

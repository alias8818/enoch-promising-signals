# Adaptive Queue-Triggered Cascade Routing for CPU Workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-queue-triggered-cascade-routing-for-cpu-workers-e712bef12722`
Run ID: `adaptive-queue-triggered-cascade-routing-for-cpu-workers-e712bef12722-20260611T140359695525+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7ef12d062dbc

## What looked useful

Across 12 replicas, adaptive routing reduced p95 latency versus static cascade by 23.86% at 45 arrivals/s with -0.36 expected-quality points and by 50.62% at 55 arrivals/s with -0.82 expected-quality points. At 65 and 75 arrivals/s it reduced queueing further but exceeded the quality-loss threshold.

## Boundaries and scale limits

Synthetic service-time and expected-quality model only; no real CPU worker pool, real model pair, calibrated confidence curve, production trace, or live serving validation. The adaptive policy exceeded the predeclared quality-loss bound at heavier overload.

## Claim scope

In a deterministic synthetic 8-worker CPU queue simulation with bursty arrivals, raising the cascade fast-path threshold when estimated queue wait grows reduced p95 latency versus a static cascade threshold at moderate overload while keeping expected-quality loss below 1.5 points.

## Why it stopped

No-paper closure: this run is a synthetic/proxy mechanism test, not full validation; it supports a bounded follow-up but cannot justify a publication-grade claim.

## Recommended next action

Run a bounded direct-evidence follow-up with an actual CPU worker pool, measured fast/slow model service times, calibrated confidence-to-quality curves, and replayed bursty traces against static and always-large baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Replayed CPU Worker Cascade With Real Fast/Slow Model Timings
- Success threshold: At one or more documented moderate-overload operating points, p95 latency improves by >=20% versus static cascade while expected-quality loss remains <1.5 points and p99 latency does not regress versus static.
- Stop condition: Stop if measured fast/slow timing separation is too small to create queue relief, confidence calibration cannot preserve the quality-loss bound, or trace replay shows no >=10% p95 improvement at any stable load point.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-queue-triggered-cascade-routing-for-cpu-workers-e712bef12722`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

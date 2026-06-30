# Confidence-Routed Model Cascade for Queue Pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-routed-model-cascade-for-queue-pressure-ebab2b729b05`
Run ID: `confidence-routed-model-cascade-for-queue-pressure-ebab2b729b05-20260630T011759180078+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/3ca416d3c523

## What looked useful

Pressure-aware thresholding consistently improved held-out utility versus confidence-only by +0.0039 to +0.0122 and versus fast-only by +0.0294 to +0.1034 across four synthetic load scenarios. A value-pressure variant overloaded the slow queue, showing that queue-aware routing needs explicit throttling.

## Boundaries and scale limits

Synthetic only: no real model logits, real correctness labels, production traces, GPU batching, cache effects, or multi-tenant serving interference. Evidence is not publication-grade and does not validate datacenter-scale deployment behavior.

## Claim scope

In a synthetic discrete-event cascade simulator with bursty arrivals, confidence-correlated correctness, trained thresholds, and held-out seeds, a queue-pressure-adjusted confidence threshold improved utility over static confidence-only routing in four tested load regimes.

## Why it stopped

Closed as no-paper useful signal: mechanism supported in a synthetic proxy, but direct/full evidence is required before any publication or deployment claim.

## Recommended next action

Run a bounded deepen study on real or open-model serving traces with actual confidence scores, correctness labels, GPU-backed service times, batching behavior, and the same held-out policy-selection discipline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-backed confidence and queue-pressure routing for model cascades
- Success threshold: Pressure-threshold routing improves mean held-out utility by at least 0.005 over confidence-only while keeping SLA violation rate no worse than confidence-only in at least three of four trace/load regimes.
- Stop condition: Stop if confidence calibration is unavailable, if pressure-threshold utility is not better than confidence-only on held-out traces, or if SLA violation rate increases by more than 10% relative to confidence-only.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-routed-model-cascade-for-queue-pressure-ebab2b729b05`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

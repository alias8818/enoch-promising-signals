# Bounded Work Admission via Queue-Pressure Gating

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-work-admission-via-queue-pressure-gating-3129ed6f101b`
Run ID: `bounded-work-admission-via-queue-pressure-gating-3129ed6f101b-20260528T105817427131+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b486f625560c

## What looked useful

The mechanism of rejecting likely-late work is supported versus admit-all, but a tuned fixed cap of 4 in the bursty scenario achieved useful value 5315.6 and interactive on-time 0.668 versus the best pressure gate useful value 3808.9 and interactive on-time 0.409. Near capacity, pressure_gate_1.20 and static_limit_8 were essentially tied on useful value, with the fixed cap slightly better on interactive deadlines and p95 latency.

## Boundaries and scale limits

Synthetic discrete-event workload only; no real GPU inference serving, production traces, batching stack, retry behavior, or multi-node validation. Runs were CPU-only and lasted under one minute each.

## Claim scope

In a deterministic synthetic four-server deadline queue, pressure gating improves useful completion and tail latency versus unbounded admission and loose fixed caps, but it does not dominate tuned small fixed queue caps under severe burst overload.

## Why it stopped

Synthetic evidence supports the broad overload-control mechanism but falsifies the stronger policy claim against a tuned fixed-cap baseline in severe bursts.

## Recommended next action

Stop this run as no-paper mixed evidence; if continuing, run a bounded hybrid pressure-plus-hard-cap experiment against tuned fixed caps on the same synthetic workload before considering real serving traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid pressure gating with hard queue caps
- Success threshold: Hybrid policy must beat the best fixed cap by at least 5% useful value without reducing interactive on-time rate or increasing p95 latency in the bursty scenario, and must remain within 1% of best useful value in near-capacity.
- Stop condition: Stop if the hybrid fails to beat the best fixed cap on bursty useful value or interactive on-time rate after a 60-seed sweep.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-work-admission-via-queue-pressure-gating-3129ed6f101b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

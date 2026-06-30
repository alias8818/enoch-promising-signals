# Integrated scheduler replay for zero-promotable gating

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `integrated-scheduler-replay-for-zero-promotable-gating-a6f54f91c7`
Run ID: `integrated-scheduler-replay-for-zero-promotable-gating-a6f54f91c7-20260607T034855318556+0000`

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

- Parent run decision: Queue Pressure with Zero Promotable Count: enoch://control-plane/projects/queue-pressure-with-zero-promotable-count-6b7170b89936/runs/queue-pressure-with-zero-promotable-count-6b7170b89936-20260605T223355248328+0000
- Parent run decision: Trace replay for zero-promotable queue pressure gating: enoch://control-plane/projects/trace-replay-for-zero-promotable-queue-pressure-gating-a4bb0b10c6/runs/trace-replay-for-zero-promotable-queue-pressure-gating-a4bb0b10c6-20260605T231148407142+0000

## What looked useful

Integrated replay reduced stall ticks by 29.44% and increased throughput by 57.95% versus strict gating with zero rollbacks, but lost to a real aging fallback baseline by 36.41% throughput and 117.68% more stall ticks on average. Context and safety ablations show the mechanism matters, but not enough to beat the real baseline.

## Boundaries and scale limits

No production traces, distributed scheduler, GPU kernel scheduler, or end-to-end model training/serving workload was tested.

## Claim scope

Fixed-seed scheduler simulation of zero-promotable fallback policies across bottleneck, bursty, and mixed workloads.

## Why it stopped

Tier-2 fixed-seed simulation produced mixed mechanism support but failed the real-baseline throughput/backlog comparison required for a positive research result.

## Recommended next action

Stop this branch as no-paper useful signal unless real scheduler traces are available to test a hybrid replay-plus-aging policy against an aging fallback.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Hybrid replay-plus-aging fallback on trace-calibrated zero-promotable workloads
- Success threshold: Hybrid policy matches aging-baseline throughput within 5%, reduces p95 latency by at least 25%, does not increase end backlog by more than 10%, and keeps rollback rate at 0 across all tested workloads.
- Stop condition: Stop if the hybrid policy misses the throughput/backlog threshold on two or more workloads or introduces any nonzero rollback rate under the safety guard.

## Evidence references

- Artifact root: `<local-path>/projects/integrated-scheduler-replay-for-zero-promotable-gating-a6f54f91c7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

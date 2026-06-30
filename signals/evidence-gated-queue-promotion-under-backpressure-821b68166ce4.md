# Evidence-Gated Queue Promotion Under Backpressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-gated-queue-promotion-under-backpressure-821b68166ce4`
Run ID: `evidence-gated-queue-promotion-under-backpressure-821b68166ce4-20260620T015832435652+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5b2f9aeee881

## What looked useful

Readiness gating reduced premature work and improved on-time completion versus immediate FIFO in the tested overloaded queue. In the medium run, evidence_gated completed 58.33% on time versus 45.18% for immediate FIFO, while wasted attempts fell from 756.6 to 0.25 per 20,000-arrival run. Sensitivity sweeps showed a positive completion-rate delta in all 9 tested cost/evidence-delay cells, but evidence_gated was effectively identical to ready_fifo.

## Boundaries and scale limits

No production traces, no distributed queue implementation, no evidence classifier noise, no multi-tenant fairness validation, and no GPU/model workload. The deadline-aware evidence_gated policy did not outperform the simpler ready_fifo control.

## Claim scope

Synthetic overloaded two-stage queue simulation with observable evidence readiness, stochastic evidence delays, fixed worker pool, job deadlines, and wasted worker time when jobs are promoted before evidence exists.

## Why it stopped

Synthetic evidence supports a practical readiness-gating mechanism but does not support a paper-ready or novel deadline-aware queue-promotion claim because the simple ready-FIFO control matched evidence_gated.

## Recommended next action

Stop this no-paper run; the next concrete action is a bounded trace-replay follow-up comparing readiness gating against ready-FIFO with measured queue evidence delays, service times, cancellations, and tenant fairness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Replay Validation of Readiness-Gated Queue Promotion
- Success threshold: Evidence-gated or ready-gated promotion must improve useful completion by at least 10% relative to immediate FIFO under backpressure while staying within 5% of ready-FIFO p95 latency and showing no tenant starvation regression.
- Stop condition: Stop if readiness gating fails to beat immediate FIFO by 5% useful completion in two backpressure settings, or if it improves throughput only by increasing p95 latency or tenant starvation by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-gated-queue-promotion-under-backpressure-821b68166ce4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

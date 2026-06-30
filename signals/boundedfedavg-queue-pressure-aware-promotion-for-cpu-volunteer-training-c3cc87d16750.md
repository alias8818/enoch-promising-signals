# BoundedFedAvg: Queue-Pressure-Aware Promotion for CPU Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `boundedfedavg-queue-pressure-aware-promotion-for-cpu-volunteer-training-c3cc87d16750`
Run ID: `boundedfedavg-queue-pressure-aware-promotion-for-cpu-volunteer-training-c3cc87d16750-20260620T032342514375+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dcea8b09bcc8

## What looked useful

Over 10 seeds, queue-pressure promotion matched FIFO final loss (0.29869 vs 0.29838), slightly improved accuracy (0.87277 vs 0.87211), improved client fairness entropy (0.85875 vs 0.72052), and reduced mean used staleness (2.40 vs 6.35 versions). It also beat freshness-only selection on final loss and fairness.

## Boundaries and scale limits

Simulator-only evidence; no real volunteer hosts, network traces, CPU thermal behavior, neural model workload, or wall-clock distributed training. The result should not be generalized to full CPU volunteer training without direct multi-process or multi-host validation.

## Claim scope

In a bounded synthetic CPU-volunteer FedAvg simulator with heterogeneous worker speeds, non-IID logistic-regression clients, bounded per-client queues, stale-update caps, and server aggregation bottlenecks, queue-pressure-aware promotion improved contribution fairness and reduced used-update staleness versus FIFO while preserving FIFO-like final loss.

## Why it stopped

No-paper useful signal: bounded synthetic proxy supports the scheduling mechanism but does not materially improve final loss over FIFO and is not direct volunteer-training evidence.

## Recommended next action

Run a bounded direct multi-process CPU FedAvg harness with real worker queues and a small public dataset to test whether the fairness/staleness signal persists outside the simulator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU-process validation of queue-pressure-aware FedAvg promotion
- Success threshold: Queue-pressure policy matches FIFO validation loss within 1% relative, improves contribution fairness entropy by at least 0.10 absolute or 10% relative, and reduces mean used staleness by at least 25% without lowering wall-clock update throughput by more than 5%.
- Stop condition: Stop if queue-pressure promotion loses more than 1% relative validation loss versus FIFO in at least 4 of 5 seeds, or if fairness/staleness gains disappear under direct process-level queueing.

## Evidence references

- Artifact root: `<local-path>/projects/boundedfedavg-queue-pressure-aware-promotion-for-cpu-volunteer-training-c3cc87d16750`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

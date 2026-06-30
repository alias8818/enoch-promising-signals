# Volunteer grid training coordinator for heterogeneous GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-grid-training-coordinator-for-heterogeneous-gpus-d9db880249ac`
Run ID: `volunteer-grid-training-coordinator-for-heterogeneous-gpus-d9db880249ac-20260609T081405282435+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/eca178203750

## What looked useful

Naive equal synchronous sharding was consistently non-viable under heterogeneity, reaching only 10.6% to 33.5% of weighted-sync throughput. A no-oracle async lease coordinator gave consistent but modest median speedups over weighted sync: 0.8% balanced, 5.2% bursty, 1.1% extreme heterogeneity, and 3.3% scarce availability.

## Boundaries and scale limits

No real model training, optimizer convergence, network bandwidth, checkpoint I/O, privacy/security, adversarial behavior, or volunteer incentive effects were tested. Results should not be generalized to production volunteer training without a real multi-worker prototype.

## Claim scope

Scheduler-only discrete-event simulation of heterogeneous volunteer GPU workers with synthetic online/offline traces; fixed 10-second async leases modestly improved completed-token throughput over throughput-weighted synchronous rounds and strongly outperformed equal synchronous sharding.

## Why it stopped

Synthetic scheduler proxy supports a practical mechanism but does not provide direct training or real volunteer-grid evidence.

## Recommended next action

Stop this run as no-paper useful signal; next build a bounded multi-process training prototype that compares loss-per-wall-clock for weighted sync versus async short leases under injected churn.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-process churned training prototype for async volunteer GPU leases
- Success threshold: Async short leases achieve at least 3% median improvement in loss-per-wall-clock over weighted synchronous scheduling with no worse final validation loss after matched wall-clock budget.
- Stop condition: Stop if async leases improve completed tokens but fail to improve loss-per-wall-clock, or if checkpoint/network overhead erases the simulated throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-grid-training-coordinator-for-heterogeneous-gpus-d9db880249ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Volunteer Grid Distributed Training with Queue-Based Work Stealing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `volunteer-grid-distributed-training-with-queue-based-work-stealing-3556365f233e`
Run ID: `volunteer-grid-distributed-training-with-queue-based-work-stealing-3556365f233e-20260608T034343430250+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/19c7a26103ad

## What looked useful

Across 20 seeds per scenario, queue stealing produced 2.59x throughput in the mild setting and 14.32x in the harsh setting, reduced idle ratio from 0.548 to 0.004 and from 0.861 to 0.041 respectively, and kept validation accuracy comparable or slightly higher.

## Boundaries and scale limits

Synthetic CPU-only proxy; no real multi-host networking, GPU kernels, optimizer state sharding, checkpoint/replay, adversarial churn, or transformer-scale training was tested.

## Claim scope

In a deterministic local simulator of heterogeneous volunteer workers training a logistic classifier, asynchronous queue-based work stealing improved simulated useful throughput versus synchronous fixed assignment while preserving validation accuracy under equal processed-example budgets.

## Why it stopped

The result is a useful proxy mechanism signal but not direct/full validation of volunteer-grid distributed training.

## Recommended next action

Run a bounded local multi-process PyTorch or JAX implementation with real queues, injected worker churn, checkpoint/replay, and the same sync-fixed baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Local Multi-Process Queue-Stealing Training with Churn Injection
- Success threshold: Queue stealing achieves at least 1.5x examples/second, reduces idle time by at least 50%, and keeps validation accuracy within 0.5 percentage points of the synchronous baseline.
- Stop condition: Stop as unsupported if queue stealing gives less than 1.2x throughput or loses more than 1.0 validation accuracy point in two tested churn regimes.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-grid-distributed-training-with-queue-based-work-stealing-3556365f233e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

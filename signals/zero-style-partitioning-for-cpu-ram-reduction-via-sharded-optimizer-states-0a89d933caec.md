# ZeRO-style Partitioning for CPU RAM Reduction via Sharded Optimizer States

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `zero-style-partitioning-for-cpu-ram-reduction-via-sharded-optimizer-states-0a89d933caec`
Run ID: `zero-style-partitioning-for-cpu-ram-reduction-via-sharded-optimizer-states-0a89d933caec-20260610T134951972464+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7ed7bd294395

## What looked useful

Optimizer-state sharding produced the predicted CPU RAM reduction under direct smaps_rollup telemetry. Allocation-hold PSS was 3734.52 MiB replicated versus 2361.25 MiB sharded; 5-step peak PSS was 5120.87 MiB versus 2638.90 MiB.

## Boundaries and scale limits

Synthetic arrays only; no PyTorch training loop, no real model forward/backward, no distributed collectives, no checkpointing, and no end-to-end throughput or convergence validation. Local update-time speedups exclude communication cost.

## Claim scope

In a local 4-rank synthetic NumPy benchmark with 60M float32 parameters per rank, ZeRO stage-1-style Adam optimizer-state sharding reduced persistent aggregate CPU PSS by 36.8%, matching the 37.5% expected payload reduction when parameters and gradients remain replicated.

## Why it stopped

Closed as no-paper useful signal because the result directly supports the memory mechanism in a synthetic benchmark but does not validate a full training system.

## Recommended next action

Run a bounded real-training follow-up with a PyTorch Adam baseline and a ZeRO-style sharded optimizer on the same small model, measuring RSS/PSS across forward, backward, optimizer, and checkpoint phases with loss-equivalence checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real training-loop validation of CPU optimizer-state sharding
- Success threshold: Persistent optimizer-related aggregate PSS reduction within 10 percentage points of the theoretical ZeRO stage-1 reduction, with loss within 1% of the replicated baseline after the bounded run.
- Stop condition: Stop if sharded optimizer memory reduction is below 20% at 4 ranks, if loss diverges from the replicated baseline by more than 1%, or if communication/synchronization overhead makes the bounded run non-comparable.

## Evidence references

- Artifact root: `<local-path>/projects/zero-style-partitioning-for-cpu-ram-reduction-via-sharded-optimizer-states-0a89d933caec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

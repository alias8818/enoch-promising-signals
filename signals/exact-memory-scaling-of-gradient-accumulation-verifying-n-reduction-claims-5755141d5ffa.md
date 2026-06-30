# Exact Memory Scaling of Gradient Accumulation: Verifying N× Reduction Claims

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `exact-memory-scaling-of-gradient-accumulation-verifying-n-reduction-claims-5755141d5ffa`
Run ID: `exact-memory-scaling-of-gradient-accumulation-verifying-n-reduction-claims-5755141d5ffa-20260525T170030999461+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2982fedee8c3

## What looked useful

Exact accounting shows total_peak(N) = fixed_training_state + activation_peak(1)/N. At effective batch 64, activation bytes fell 64x, but total peak fell only 7.455x for the GPT-2-small-like scenario, 3.637x for activation-heavy MLP, and 1.066x for state-heavy embedding model.

## Boundaries and scale limits

Evidence is from deterministic tensor byte accounting for synthetic/GPT-2-small-like scenarios on CPU, not from real PyTorch/CUDA allocator telemetry, multi-node training, activation checkpointing, mixed precision, or 7B+ model runs.

## Claim scope

For fixed effective batch training, gradient accumulation reduces the batch-linear saved-activation term by N, but it does not reduce total peak training memory by N when parameters, gradients, and optimizer state are included.

## Why it stopped

The exact byte-accounting proxy directly falsifies the broad total-memory N-fold claim, while acknowledging that direct allocator measurements would be needed for framework-specific constants.

## Recommended next action

Stop this run as a proxy/early falsification of the broad exact N-fold total-memory claim; a bounded follow-up should run the same accounting against real PyTorch allocator peaks in a clean CPU/GPU environment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Allocator-level validation of gradient accumulation memory scaling
- Success threshold: Measured total peak reduction must remain substantially below N whenever fixed training state is at least 20% of baseline peak, with residuals against the accounting model explained within 25%.
- Stop condition: Stop if a clean PyTorch environment cannot be created within bounded local resources or if smoke tests cannot report allocator peaks reproducibly.

## Evidence references

- Artifact root: `<local-path>/projects/exact-memory-scaling-of-gradient-accumulation-verifying-n-reduction-claims-5755141d5ffa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Gradient Checkpointing for CPU Memory-constrained Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-checkpointing-for-cpu-memory-constrained-training-ca5e7e16a7b9`
Run ID: `gradient-checkpointing-for-cpu-memory-constrained-training-ca5e7e16a7b9-20260610T143101910536+0000`

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

Checkpointing delivered a reproducible CPU memory reduction in the bounded benchmark: baseline peak RSS was about 267 MiB, checkpoint peak RSS was 110-136 MiB across segment sizes 2, 4, and 8, with exact loss and gradient aggregate agreement.

## Boundaries and scale limits

Synthetic NumPy only; one training step; no optimizer state, dataloader, convergence measurement, transformer attention, PyTorch/JAX runtime behavior, or GPT-2-small-class baseline.

## Claim scope

In a one-step synthetic activation-heavy NumPy MLP-block CPU backward pass, segmented gradient checkpointing preserved computed loss and aggregate gradient norm while reducing peak RSS by about 49-59% at about 15-27% wall-clock overhead.

## Why it stopped

No-paper useful signal: this run directly supports the memory-saving mechanism in a synthetic one-step CPU benchmark, but it is not a full validation of memory-constrained model training.

## Recommended next action

Run a bounded PyTorch or JAX CPU transformer benchmark under a fixed memory cap, including optimizer state and multiple steps, before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Framework CPU memory-cap validation of checkpointed transformer training
- Success threshold: Checkpointed training completes at least 20 consecutive CPU steps under a memory cap where the baseline fails or must use at least 25% smaller batch, with less than 2x wall-clock overhead and no loss divergence beyond numerical tolerance.
- Stop condition: Stop if checkpointing does not reduce measured peak CPU memory by at least 25%, if overhead exceeds 2x at equal batch/model size, or if framework installation/runtime issues prevent a valid controlled comparison within the CPU budget.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-checkpointing-for-cpu-memory-constrained-training-ca5e7e16a7b9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

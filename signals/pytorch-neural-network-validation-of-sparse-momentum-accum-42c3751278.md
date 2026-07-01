# PyTorch neural-network validation of sparse momentum accumulation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pytorch-neural-network-validation-of-sparse-momentum-accum-42c3751278`
Run ID: `pytorch-neural-network-validation-of-sparse-momentum-accum-42c3751278-20260531T143127013977+0000`

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

- Parent run decision: Sparse-Update Optimizer With Momentum Accumulation: enoch://control-plane/projects/sparse-update-optimizer-with-momentum-accumulation-6d26d6646d20/runs/sparse-update-optimizer-with-momentum-accumulation-6d26d6646d20-20260531T111213457416+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/95f52623c2d6

## What looked useful

Corrected row-wise sparse momentum passed the Tier 1 threshold: mean validation loss improved from 0.3776206474 to 0.3149927358 (16.5848748% relative improvement), mean validation accuracy improved from 0.8188476562 to 0.8598632812 (+0.041015625), and max untouched-row delta remained 0.0.

## Boundaries and scale limits

Synthetic task only; 5000-item vocabulary, 32-dimensional embedding, 4096 training samples, 2048 validation samples, 18 epochs, 3 seeds. No real dataset, no long training, no GPT-2-scale model, no production optimizer implementation, and no comparison to SparseAdam or dense parameter-matched baselines.

## Claim scope

Small controlled PyTorch CUDA neural-network validation on a synthetic sparse-feature binary classification task: row-wise sparse momentum accumulation improved validation loss and accuracy versus a no-momentum sparse SGD control while updating only touched embedding rows.

## Why it stopped

Tier 1 mechanism evidence was positive but synthetic and small-scale; paper gate remains closed because mechanism support is not publication readiness.

## Recommended next action

Run a bounded medium direct validation on a real or more realistic sparse workload with SparseAdam and dense/standard baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium sparse momentum validation with stronger optimizer baselines
- Success threshold: Pass if sparse momentum improves validation loss by at least 5% or task accuracy by at least 2 percentage points versus sparse no-momentum SGD, has max_untouched_row_delta == 0, and is not clearly dominated by SparseAdam on both quality and runtime.
- Stop condition: Stop if sparse momentum fails to beat sparse no-momentum SGD on mean validation loss and task metric, mutates untouched rows, or is clearly dominated by SparseAdam on both quality and runtime.

## Evidence references

- Artifact root: `<local-path>/projects/pytorch-neural-network-validation-of-sparse-momentum-accum-42c3751278`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Medium sparse momentum validation with stronger optimizer baselines

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-sparse-momentum-validation-with-stronger-optimizer-3f18f2d238`
Run ID: `medium-sparse-momentum-validation-with-stronger-optimizer-3f18f2d238-20260531T182647069725+0000`

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

- Parent run decision: Sparse-Update Optimizer With Momentum Accumulation: enoch://control-plane/projects/sparse-update-optimizer-with-momentum-accumulation-6d26d6646d20/runs/sparse-update-optimizer-with-momentum-accumulation-6d26d6646d20-20260531T111213457416+0000
- Parent run decision: PyTorch neural-network validation of sparse momentum accumulation: enoch://control-plane/projects/pytorch-neural-network-validation-of-sparse-momentum-accum-42c3751278/runs/pytorch-neural-network-validation-of-sparse-momentum-accum-42c3751278-20260531T143127013977+0000

## What looked useful

Sparse momentum has a real bounded mechanism signal: at 10% support it beats sparse SGD by 16.62 validation points and no-momentum SGD by 12.65 points, but trails AdamW by 3.51 points and dense momentum by 4.03 points. Tuning to 30% support nearly matches AdamW while still trailing dense momentum by 0.55 points; 50% support matches dense momentum, weakening the medium-sparse claim.

## Boundaries and scale limits

Single dataset, small CNN, 3 epochs, 20000 training examples, 3 seeds. Sparse optimizer uses dense tensors with enforced logical sparsity, so memory/bandwidth savings are not directly measured. No language-model, distributed, long-horizon, or sparse-storage validation was run.

## Claim scope

On a 3-seed MNIST small-CNN optimizer comparison, top-k sparse momentum improves substantially over sparse SGD/no-momentum controls, but 10-20% logical momentum support does not match dense SGD+momentum and only approaches AdamW after tuning. Dense-momentum parity appeared only at 50% support.

## Why it stopped

Medium confirmation with fixed seeds, ablations, and real baselines produced mixed no-paper evidence: mechanism support is present, but the medium-sparse setting fails the dense-momentum baseline and parity requires much less sparse 50% support.

## Recommended next action

Stop paper escalation for this run; only revisit if implementing real sparse optimizer storage and testing whether 10-30% support can match dense momentum on a harder model/dataset with measured memory or bandwidth savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sparse-storage momentum validation at 20-30% support on a harder dataset
- Success threshold: At 20-30% support, sparse momentum is within 0.5 validation-accuracy points of dense SGD+momentum and AdamW across at least 3 seeds while showing at least 2x measured optimizer-state memory or update-bandwidth reduction.
- Stop condition: Stop if 20-30% support remains more than 1.0 validation point below dense momentum, if measured sparse-storage savings are under 2x, or if parity again requires 50% or greater support.

## Evidence references

- Artifact root: `<local-path>/projects/medium-sparse-momentum-validation-with-stronger-optimizer-3f18f2d238`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

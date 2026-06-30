# Small-transformer trained-weight residual codebook validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-transformer-trained-weight-residual-codebook-validat-abb4c7450e`
Run ID: `small-transformer-trained-weight-residual-codebook-validat-abb4c7450e-20260526T222801294221+0000`

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

- Parent run decision: Trained-weight residual codebook validation: enoch://control-plane/projects/trained-weight-residual-codebook-validation-e62fcf9525/runs/trained-weight-residual-codebook-validation-e62fcf9525-20260526T161151232056+0000
- Parent run decision: Block-wise residual codebooks for 1-bit inference: enoch://control-plane/projects/block-wise-residual-codebooks-for-1-bit-inference-2a440fb9b3eb/runs/block-wise-residual-codebooks-for-1-bit-inference-2a440fb9b3eb-20260525T222531346967+0000

## What looked useful

Residual stages and shorter vector blocks improve reconstruction and validation loss, and trained assignments beat random/shuffled controls, but the best tested RVQ result remains 0.295 validation-loss points worse than dense and 0.259 points worse than scalar4 on the 4-float-block sensitivity run.

## Boundaries and scale limits

Small character-level language model only; post-training k-means codebooks only; no activation-aware fitting, layerwise bit allocation, fine-tuning after quantization, full byte-accurate storage accounting, larger corpora, or GPT-2-small-class validation.

## Claim scope

On a 4-layer 128-width causal transformer trained for 1200 steps on TinyShakespeare across seeds 1, 2, and 3, post-training residual vector codebooks over trained weights show monotonic improvement with more residual stages but do not preserve validation loss competitively versus dense, scalar4, scalar8, or single256 baselines.

## Why it stopped

Tier 2 fixed-seed direct validation produced a reproducible negative result against real baselines, with only mechanism support and no publication-grade positive evidence.

## Recommended next action

Stop this validation as no-paper evidence; only continue with a bounded task-aware residual-codebook follow-up that must beat scalar4 and single256 on the same benchmark before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Task-aware layerwise residual codebooks for small-transformer trained weights
- Success threshold: Task-aware/layerwise RVQ must achieve mean validation-loss delta <= 0.05 versus dense and beat both scalar4 and single256 mean validation loss across all three seeds with honest storage accounting.
- Stop condition: Stop if the method remains >0.10 validation-loss points worse than scalar4 or single256 after the bounded fitting and ablation pass.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-trained-weight-residual-codebook-validat-abb4c7450e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

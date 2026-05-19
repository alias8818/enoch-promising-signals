# ResidualFP-Extreme: 1-bit Weights with Principled FP16 Residual Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residualfp-extreme-1-bit-weights-with-principled-fp16-residual-channels-eb9b28f112e3`
Run ID: `residualfp-extreme-1-bit-weights-with-principled-fp16-residual-channels-eb9b28f112e3-20260517T144308830694+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a6cce9232f27

## What looked useful

Residual channels gave a monotonic regression gain: top-error residual8/32/64 reduced MSE versus pure 1-bit by 8.72%, 22.67%, and 32.20% respectively. Top-error selection beat random by 1.07%, 3.55%, and 3.94% relative MSE at the same residual budgets. Dense remained much better, with residual_top64 still leaving about 45% of the dense-vs-1-bit gap.

## Boundaries and scale limits

No transformer, language-model, real dataset, fused inference kernel, or long training validation was run. The classification task saturated at 1.0 accuracy for all variants and is not discriminative. PyTorch training used float master weights and optimizer state, so results support quality behavior rather than actual deployed memory or speed gains.

## Claim scope

In a five-seed synthetic MLP teacher-regression probe, adding FP16 residual output channels to 1-bit per-output-scaled weights reduces test MSE versus pure 1-bit weights, and selecting residual channels by largest quantization error modestly beats random same-budget channel selection.

## Why it stopped

Moderate proxy evidence supports the residual-channel mechanism but does not directly validate the original extreme 1-bit-weight claim on transformers or real language-model metrics.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded action is a tiny-transformer language-model follow-up with dense, pure 1-bit, random residual, and top-error residual controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: ResidualFP channels in a tiny transformer language model
- Success threshold: Top-error residual channels must reduce the pure-1-bit validation loss gap to dense by at least 50%, beat random residual allocation by at least 5% relative validation loss at the same budget, and retain at least 4x bit-equivalent compression.
- Stop condition: Stop as negative if top-error residual channels fail to beat random allocation or reduce less than 25% of the pure-1bit-to-dense validation loss gap after the bounded training budget.

## Evidence references

- Artifact root: `<local-path>/projects/residualfp-extreme-1-bit-weights-with-principled-fp16-residual-channels-eb9b28f112e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# 8-bit AdamW with sparse gradient updates for 6GB GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adamw-with-sparse-gradient-updates-for-6gb-gpus-e9a95bae632f`
Run ID: `8-bit-adamw-with-sparse-gradient-updates-for-6gb-gpus-e9a95bae632f-20260608T185536024412+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/086b66cb6420

## What looked useful

8-bit optimizer-state storage is viable as a memory mechanism, but sparse top-k updates on dense gradients are an early negative mechanism result: they saved update work in this script while leaving final loss near the starting loss.

## Boundaries and scale limits

Single GB10 host, synthetic dense regression with a 1024x1024 parameter tensor, no real 6GB GPU, no transformer/LLM training, no fused production optimizer, and peak CUDA memory includes temporary dequantized tensors.

## Claim scope

On a bounded CUDA synthetic dense-regression probe, blockwise 8-bit AdamW reduced optimizer-state memory by about 75% and matched fp32 AdamW at lr=1e-3, but top-k sparse optimizer updates at 1%-25% density failed to reduce loss from initialization.

## Why it stopped

Bounded proxy evidence supports 8-bit state memory savings but early-falsifies naïve sparse top-k updates on dense gradients; this is not full 6GB/LLM validation.

## Recommended next action

Stop this broad claim as no-paper evidence; only revisit sparse updates for naturally sparse-gradient workloads or with error-feedback/fused optimizer controls.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: 8-bit AdamW for naturally sparse embedding gradients on 6GB-class memory budgets
- Success threshold: Sparse-gradient 8-bit AdamW reaches within 5% relative validation loss of dense 8-bit AdamW while reducing optimizer touched-state bytes or optimizer step time by at least 25%.
- Stop condition: Stop if sparse-gradient 8-bit AdamW is more than 10% worse in validation loss than dense 8-bit AdamW after the fixed budget, or if measured peak memory/step time does not improve.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-with-sparse-gradient-updates-for-6gb-gpus-e9a95bae632f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

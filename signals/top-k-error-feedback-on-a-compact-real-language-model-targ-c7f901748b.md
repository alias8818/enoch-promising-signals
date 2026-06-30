# Top-k Error Feedback on a Compact Real Language-Model Target

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `top-k-error-feedback-on-a-compact-real-language-model-targ-c7f901748b`
Run ID: `top-k-error-feedback-on-a-compact-real-language-model-targ-c7f901748b-20260620T113501081758+0000`

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

- Parent run decision: Gradient Sparsification with Top-k Error Feedback for Low-Bandwidth Volunteer Training: enoch://control-plane/projects/gradient-sparsification-with-top-k-error-feedback-for-low-bandwidth-volunteer-training-ec8995da3121/runs/gradient-sparsification-with-top-k-error-feedback-for-low-bandwidth-volunteer-training-ec8995da3121-20260620T111400402146+0000
- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/35b446046754

## What looked useful

Top-k error feedback was active but underperformed the no-feedback sparse baseline: mean validation loss was dense 1.8008, top-k no-feedback 2.1048, and top-k error-feedback 2.1314. Error feedback accumulated residual norms around 2.93-3.14 while raw gradient norms were about 1.42-1.69, and transmitted update norms rose to about 1.22-1.28x raw gradient norm versus about 0.70x for no-feedback.

## Boundaries and scale limits

Small single-GPU Tier 1 direct test only: character-level Tiny Shakespeare, 3 seeds, 2,000 updates, one model size, one sparsity level, one optimizer, and no large-token/subword/GPT-2-scale validation.

## Claim scope

In a 627k-parameter causal Transformer trained for 2,000 updates on Tiny Shakespeare character language modeling with AdamW, naive per-tensor top-5% gradient sparsification with residual error feedback did not improve validation loss over top-5% sparsification without feedback and remained far worse than dense gradients.

## Why it stopped

A direct small real-LM test did not meet the success condition that error feedback should improve top-k sparsified training; it was worse than no-feedback on average and on two of three paired seeds.

## Recommended next action

Stop this run as a bounded negative/useful signal; the next concrete adjacent test would be a new project testing residual damping or clipping under the same compact LM protocol before any larger-scale run.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Damped or clipped residual error feedback for top-k compact LM training
- Success threshold: Damped or clipped error feedback beats top-k no-feedback by at least 0.03 mean validation cross-entropy over three paired seeds at 2,000 updates while keeping transmitted-to-raw gradient norm below 1.05 at final evaluation.
- Stop condition: Stop as negative if damped/clipped error feedback fails to beat no-feedback on mean validation loss or still shows transmitted-to-raw gradient norm above 1.05 at the final evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/top-k-error-feedback-on-a-compact-real-language-model-targ-c7f901748b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

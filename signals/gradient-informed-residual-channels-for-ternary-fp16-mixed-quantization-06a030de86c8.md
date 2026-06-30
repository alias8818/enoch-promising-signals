# Gradient-Informed Residual Channels for Ternary+FP16 Mixed Quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gradient-informed-residual-channels-for-ternary-fp16-mixed-quantization-06a030de86c8`
Run ID: `gradient-informed-residual-channels-for-ternary-fp16-mixed-quantization-06a030de86c8-20260529T045713337571+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/bab3238b6373

## What looked useful

Gradient-informed residual channels showed mixed synthetic MLP behavior and underperformed quantization-error channel selection in the distilgpt2 probe. Researchers should compare against quantization-error and magnitude controls before scaling this idea.

## Boundaries and scale limits

No standard-corpus GPT-2-small-class benchmark, no large-model validation, no kernel/storage implementation, and no training-time quantization were tested. The distilgpt2 probe used a small repeated local text corpus and short calibration/evaluation batches.

## Claim scope

Bounded local evidence from synthetic MLP PTQ runs and a small distilgpt2 PTQ probe does not support calibration-gradient channel scoring as a robust selector for FP16 residual channels under ternary quantization.

## Why it stopped

Moderate bounded evidence, including a direct small-LM proxy, failed to show a robust advantage for gradient-informed residual-channel selection and found a stronger simple control.

## Recommended next action

Stop this gradient-selector project as no-paper evidence; branch a bounded quantization-error residual-channel PTQ test on a standard small-LM perplexity benchmark.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Quantization-Error Residual Channels for Ternary Small-LM PTQ
- Success threshold: Quantization-error selection reduces perplexity degradation by at least 20% relative to the best non-error selector at two or more residual budgets without relying on a single calibration slice.
- Stop condition: Stop if quantization-error selection fails to beat the best gradient or magnitude control by at least 10% relative perplexity-degradation reduction on the first standard-corpus small-LM run.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-informed-residual-channels-for-ternary-fp16-mixed-quantization-06a030de86c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

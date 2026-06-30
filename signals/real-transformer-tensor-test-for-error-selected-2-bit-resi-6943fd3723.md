# Real Transformer Tensor Test for Error-Selected 2-bit Residual Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-transformer-tensor-test-for-error-selected-2-bit-resi-6943fd3723`
Run ID: `real-transformer-tensor-test-for-error-selected-2-bit-resi-6943fd3723-20260520T094106629267+0000`

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

- Parent run decision: Cheap Residual Coding for Error-Selected 2-bit Channels: enoch://control-plane/projects/cheap-residual-coding-for-error-selected-2-bit-channels-8c70450907/runs/cheap-residual-coding-for-error-selected-2-bit-channels-8c70450907-20260520T093559429310+0000
- Parent run decision: Principled Residual Channels for 2-bit Weight Quantization with Iso-Budget Baseline: enoch://control-plane/projects/principled-residual-channels-for-2-bit-weight-quantization-with-iso-budget-baseline-8b9a61126ad6/runs/principled-residual-channels-for-2-bit-weight-quantization-with-iso-budget-baseline-8b9a61126ad6-20260520T092209492583+0000

## What looked useful

Error-low 2-bit channel selection reduced held-out residual relative MSE by 47.0% to 53.7% versus random across 12.5%, 25%, and 50% 2-bit fractions, but low-magnitude selection matched or slightly beat it. Calibration 2-bit error and activation energy were highly correlated (mean layerwise Pearson 0.906), with selected-set Jaccard overlap 0.683 to 0.888 depending on fraction.

## Boundaries and scale limits

Single small pretrained transformer, Wikitext-2 test text, post-training activation reconstruction/logit-lens analysis only; no fused quantized inference path, no GPT-2-small-class training/eval, no 7B-class model, no latency or memory-bandwidth measurement.

## Claim scope

On distilgpt2 Wikitext-2 residual activations, assigning 2-bit precision to calibration-low-error channels preserves held-out residual tensors and final-layer logit-lens outputs much better than random or high-error channel assignment, but not better than a low-activation-magnitude baseline.

## Why it stopped

Medium real-tensor evidence supports selective 2-bit assignment versus random/high-error controls but fails the stronger novelty/control bar because a simple magnitude baseline is equivalent or slightly better.

## Recommended next action

Stop this error-selection paper path unless a future bounded test can show advantage over low-magnitude selection in a real quantized forward path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantized Forward Test of Low-Magnitude Versus Error-Selected Residual Channels
- Success threshold: At one or more 2-bit fractions between 12.5% and 50%, error-low selection must reduce propagated perplexity or logit KL by at least 10% relative to magnitude-low selection while remaining clearly better than random across at least 3 fixed seeds.
- Stop condition: Stop if error-low remains within 5% of magnitude-low or worse on propagated perplexity/logit KL, because the error-selection mechanism is then not distinct enough from magnitude selection.

## Evidence references

- Artifact root: `<local-path>/projects/real-transformer-tensor-test-for-error-selected-2-bit-resi-6943fd3723`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Mixed-Precision Residual Channels: FP16 Residual + 2-bit Weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mixed-precision-residual-channels-fp16-residual-2-bit-weights-b6ddd8e5163f`
Run ID: `mixed-precision-residual-channels-fp16-residual-2-bit-weights-b6ddd8e5163f-20260523T033354520417+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/10977f3518e6

## What looked useful

Across three MNIST MLP seeds, plain 2-bit quantization averaged 88.78% accuracy versus 97.86% FP32. Top-error FP16 residual output channels improved accuracy to 91.74% at 1% channels, 92.33% at 2%, and 92.59% at 10%, while random residual channels only reached 89.39%, 89.44%, and 90.03% respectively. The selection mechanism is useful, but the quality gap remains large.

## Boundaries and scale limits

Not tested on transformers, GPT-2-small-class models, language-model perplexity, quantization-aware training, packed 2-bit kernels, latency, bandwidth, energy, or large-scale training/inference. Effective bit counts exclude scale/min metadata and bias storage.

## Claim scope

Small MNIST post-training probe: row-wise 2-bit quantized MLP weights plus FP16-simulated residual corrections for selected output channels. Error-selected residual channels consistently recover part of the accuracy lost to 2-bit quantization and outperform random residual channels at the same residual budget.

## Why it stopped

No-paper useful signal: the local evidence supports error-selected FP16 residual channels as better than random residuals, but this was a small post-training MLP probe and recovered only part of the 2-bit quality loss.

## Recommended next action

Run a bounded deepen follow-up on a small transformer or GPT-2-small-class language model with perplexity, matched parameter/storage accounting, and the same top-error versus random residual-channel controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-channel 2-bit weights on a small language model
- Success threshold: At 5% or lower residual-channel budget, error-selected residuals recover at least half of the perplexity degradation from plain 2-bit quantization and outperform random residuals by at least 20% relative recovery.
- Stop condition: Stop if error-selected residual channels fail to beat random residuals on perplexity recovery in two independent runs or if the storage overhead needed to recover quality exceeds 4 effective bits per weight before metadata.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-precision-residual-channels-fp16-residual-2-bit-weights-b6ddd8e5163f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

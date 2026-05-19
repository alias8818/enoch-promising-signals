# Gradient-Informed Residual Channel Preservation for 1.58-bit Quantization

Status: `useful_signal`
Project ID: `gradient-informed-residual-channel-preservation-for-1-58-bit-quantization-7b3e6b413461`
Run ID: `gradient-informed-residual-channel-preservation-for-1-58-bit-quantization-7b3e6b413461-20260516T200951411199+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/9f35e150e0c8

## What looked useful

Residual channel preservation is a useful mechanism in the local probe, but the tested gradient-informed ranking is mixed: mean loss improvement versus fully quantized weights trailed random by 0.0008, 0.0080, 0.0193, and 0.0518 at 2.5%, 5%, 10%, and 20% preservation respectively.

## Boundaries and scale limits

Small MLP classifier only; no transformer LM, GPT-2-class model, 7B model, language-model perplexity, quantization-aware training, or deployment-efficiency validation was run.

## Claim scope

On a 10-seed sklearn-digits MLP post-training ternary quantization probe, preserving a small fraction of full-precision output channels reduces loss, but the tested gradient-error selector does not consistently outperform random or activation-magnitude channel selection.

## Why it stopped

Proxy early falsification: the local MLP evidence does not support the specific gradient-informed selector as superior, although it does not fully refute possible transformer-scale variants.

## Recommended next action

Stop this run as a bounded no-paper useful signal; the only warranted next action is a direct small-transformer LM PTQ follow-up with perplexity gradients and the same random/activation/norm controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer perplexity test for gradient-informed residual channel preservation
- Success threshold: Gradient-informed selection must beat random and activation selectors by at least 3% relative held-out loss recovery at 5% and 10% preservation, with the effect present in at least 4 of 5 seeds or calibration subsets.
- Stop condition: Stop if gradient-informed selection fails to beat random or activation on mean held-out loss recovery at both 5% and 10% preservation, or if the effect appears only on calibration loss and not held-out loss.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-informed-residual-channel-preservation-for-1-58-bit-quantization-7b3e6b413461`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Activation-selected residual channels with error-aware 2-bit quantization

Status: `useful_signal`
Project ID: `activation-selected-residual-channels-with-error-aware-2-b-ad5a87cb53`
Run ID: `activation-selected-residual-channels-with-error-aware-2-b-ad5a87cb53-20260516T085033004894+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Activation-selected residual channels with error-aware 2-bit quantization: internal_generated:activation-selected-residual-channels-with-error-aware-2-b-ad5a87cb53

## What looked useful

Activation-aware and activation-times-error channel selection beat random and a low-score negative control on OPT-125M at equal residual budget, but the best 25 percent residual result still had NLL 8.5657 versus FP NLL 3.5257. On Pythia-70M, all tested 2-bit residual variants were catastrophic and the best 25 percent residual selector was weight-error alone, not activation-aware selection.

## Boundaries and scale limits

Two small open causal LMs, Wikitext-2 validation only, 32,768 evaluation tokens per run, 8,192 calibration tokens, simulated dequantized weights rather than packed kernels, and no GPTQ/AWQ/Hessian-aware base quantizer.

## Claim scope

On Pythia-70M-deduped and OPT-125M with Wikitext-2 validation, simulated per-row affine 2-bit linear weight quantization plus exact residual input channels does not preserve causal LM perplexity. Activation/error residual selection shows a useful allocation signal on OPT-125M but not a practical or consistently general mechanism across both tested model families.

## Why it stopped

Direct small-model perplexity validation falsified the practical threshold for the tested method: even at 25 percent residual channels, quantized NLL remained far from FP on both models, with catastrophic failure on Pythia-70M.

## Recommended next action

Stop this run as no-paper evidence; only pursue one capped deepen follow-up if replacing the weak per-row affine 2-bit base quantizer with GPTQ/AWQ-style 2-bit quantization while preserving the same residual-channel controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-channel selection on top of GPTQ/AWQ-style 2-bit quantization
- Success threshold: At 16 percent or lower residual channels, act_error must beat random by at least 0.25 NLL on both model families and keep final NLL within 1.0 of FP on OPT-125M and within 2.0 of FP on Pythia-70M.
- Stop condition: Stop negative if the stronger base quantizer plus act_error residual selection still fails to beat random by 0.25 NLL on either model or remains more than 2.0 NLL above FP at 25 percent residual channels.

## Evidence references

- Artifact root: `<local-path>/projects/activation-selected-residual-channels-with-error-aware-2-b-ad5a87cb53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

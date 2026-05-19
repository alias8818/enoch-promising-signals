# Robust 3-bit activation-weight residual split validation

Status: `useful_signal`
Project ID: `robust-3-bit-activation-weight-residual-split-validation-cf24b41197`
Run ID: `robust-3-bit-activation-weight-residual-split-validation-cf24b41197-20260516T180229449002+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/78b0bfec3762

## What looked useful

Residual split q3 W+A mean validation loss was 2.251516 versus 2.337342 for naive q3 and 2.247269 for FP32; the split recovered 95.29% of the naive q3 loss gap but ran slower in the PyTorch fake-quant implementation.

## Boundaries and scale limits

Evidence is limited to fake-quantized training on a small character-level Transformer for 400 steps and 3 seeds. It does not validate packed int3 kernels, GPT-2-small-class or larger models, pretrained-model post-training quantization, long-run convergence, multiple corpora, or production memory/latency tradeoffs.

## Claim scope

In a controlled Tier 1 small direct test on a 618k-parameter Tiny Shakespeare residual Transformer, two-component 3-bit residual splitting for both activations and linear weights improved validation loss over naive single-component 3-bit activation+weight fake quantization across 3 seeds and recovered 95.29% of the naive q3 loss gap to FP32.

## Why it stopped

No paper-ready closure: the Tier 1 small direct fake-quantized training test supports the mechanism, but larger model and kernel/backend evidence are required before publication claims.

## Recommended next action

Run a bounded medium confirmation on a GPT-2-small-class or parameter-matched token-level model with FP32, naive q3 W+A, and residual-split q3 W+A under matched training tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium GPT-2-class residual-split q3 W+A confirmation
- Success threshold: Residual-split q3 W+A must beat naive q3 W+A mean validation loss and recover at least 50% of the naive q3 validation-loss gap to FP32 across at least 3 seeds, without training instability.
- Stop condition: Stop if residual-split q3 W+A does not beat naive q3 W+A after matched training tokens, if it recovers less than 25% of the naive q3 gap on two or more seeds, or if throughput/memory overhead makes the method impractical for the scoped model.

## Evidence references

- Artifact root: `<local-path>/projects/robust-3-bit-activation-weight-residual-split-validation-cf24b41197`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Checkpointed GPT-2 intermediate KL heads for actual speculative decoding throughput

Status: `useful_signal`
Project ID: `checkpointed-gpt-2-intermediate-kl-heads-for-actual-specul-9042abd5e4`
Run ID: `checkpointed-gpt-2-intermediate-kl-heads-for-actual-specul-9042abd5e4-20260516T172832772240+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Checkpointed GPT-2 intermediate KL heads for actual speculative decoding throughput: internal_generated:checkpointed-gpt-2-intermediate-kl-heads-for-actual-specul-9042abd5e4

## What looked useful

Intermediate heads can draft accepted tokens, and a layer-10 KL affine adapter improved gamma-4 acceptance from 0.566 to 0.688 and throughput from 114.7 to 154.4 tok/s, but the best speculative result remained far below the cached GPT-2 baseline of 310.5 tok/s.

## Boundaries and scale limits

Single-model GPT-2-small, single GB10, batch size 1, 32-prompt medium benchmark, Python/Hugging Face implementation, short 250-step affine KL-adapter training. Larger models, batched serving, sampling, longer prompt distributions, and fused custom cache implementations were not tested.

## Claim scope

On GPT-2-small greedy decoding on one NVIDIA GB10, intermediate logit/KL heads at layers 10-11 did not improve actual emitted tokens/sec versus a cached GPT-2 autoregressive baseline across 32 WikiText-style prompts of 64 prompt tokens and 64 generated tokens.

## Why it stopped

Direct bounded validation of actual throughput found the best intermediate-head speculative configuration at 154.4 tok/s versus 310.5 tok/s for cached GPT-2, so the throughput hypothesis is unsupported despite a useful KL-head acceptance signal.

## Recommended next action

Stop this as a paper claim; only run a final depth-4 deepen if it implements an optimized exact self-speculative cache path and requires at least 1.10x cached GPT-2-small baseline throughput on the same benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized exact cache path for GPT-2 intermediate-head self-speculation
- Success threshold: Mean emitted tokens/sec at least 1.10x cached GPT-2 baseline on 32 or more prompts while producing byte-identical greedy continuations.
- Stop condition: Stop if optimized exact cache handling still remains below 1.00x cached GPT-2 baseline or if correctness diverges from greedy target decoding.

## Evidence references

- Artifact root: `<local-path>/projects/checkpointed-gpt-2-intermediate-kl-heads-for-actual-specul-9042abd5e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

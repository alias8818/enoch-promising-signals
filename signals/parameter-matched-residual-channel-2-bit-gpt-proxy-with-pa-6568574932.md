# Parameter-Matched Residual-Channel 2-Bit GPT Proxy With Packed Kernels

Status: `compute_scale_blocked`
Project ID: `parameter-matched-residual-channel-2-bit-gpt-proxy-with-pa-6568574932`
Run ID: `parameter-matched-residual-channel-2-bit-gpt-proxy-with-pa-6568574932-20260515T024822462371+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/08a94314b5ab

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 proxy supported the residual-channel 2-bit modeling mechanism but directly failed the implemented packed-kernel throughput threshold, so this is not full validation or paper-ready evidence.

## Recommended next action

Stop this run as a proxy/early no-paper result; next, implement a fused packed 2-bit projection kernel and rerun the same GB10 shapes against cached fp16/dequant baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused Packed 2-Bit Residual-Channel Projection Kernel on GB10
- Success threshold: Fused packed projection is at least 1.10x faster than cached dequantized matmul on the benchmark shape and does not increase TinyGPT eval loss by more than 5% relative to the residual2bit_160_r12p5 result.
- Stop condition: Stop if the fused packed kernel is slower than cached dequantized matmul by more than 5%, fails correctness tolerance, or cannot be integrated into the TinyGPT projection path within the bounded follow-up.

## Evidence references

- Artifact root: `<local-path>/projects/parameter-matched-residual-channel-2-bit-gpt-proxy-with-pa-6568574932`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

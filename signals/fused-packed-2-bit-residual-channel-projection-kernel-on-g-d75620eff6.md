# Fused Packed 2-Bit Residual-Channel Projection Kernel on GB10

Status: `compute_scale_blocked`
Project ID: `fused-packed-2-bit-residual-channel-projection-kernel-on-g-d75620eff6`
Run ID: `fused-packed-2-bit-residual-channel-projection-kernel-on-g-d75620eff6-20260515T025416830688+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Fused Packed 2-Bit Residual-Channel Projection Kernel on GB10: internal_generated:fused-packed-2-bit-residual-channel-projection-kernel-on-g-d75620eff6

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Medium direct microbenchmark, not full validation: fused packed 2-bit projection beat explicit unpacking by 3.65x-18.62x and beat dense baselines by about 2.17x on (64,4096,4096), but it lost to dense fp16/materialized-quantized baselines on the 2048-wide shape sweep and was not end-to-end model integrated.

## Recommended next action

Stop paper consideration for this run; the Tier 2 direct kernel benchmark is mixed, with a real unpack-avoidance mechanism and one large-shape win but dense-baseline regressions on most 2048-wide shapes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Autotuned GB10 Fused 2-Bit Projection With End-to-End Residual-Channel Validation
- Success threshold: Geometric mean fused speedup >=1.25x versus dense fp16 over the predeclared projection shape set, no individual common shape below 0.90x, and end-to-end projection-stage latency improvement with correctness error within the dense dequantized fp16 reference tolerance.
- Stop condition: Stop if autotuning cannot eliminate the 2048-wide dense-baseline regressions or if end-to-end integration shows no projection-stage latency or memory benefit.

## Evidence references

- Artifact root: `<local-path>/projects/fused-packed-2-bit-residual-channel-projection-kernel-on-g-d75620eff6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

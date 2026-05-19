# End-to-end sampled-gradient recomputation for volunteer spot checks

Status: `useful_signal`
Project ID: `end-to-end-sampled-gradient-recomputation-for-volunteer-sp-0f3fe3b385`
Run ID: `end-to-end-sampled-gradient-recomputation-for-volunteer-sp-0f3fe3b385-20260517T162234288441+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/211406be87da

## What looked useful

Tier 1 direct test supports the mechanism: 25/25 honest sampled recomputations passed with zero numeric error at 1e-12 tolerance, 25/25 sampled tampered packages were detected, mean recomputation time was 0.000719 s, and audit package size was 66,896 bytes per sampled step.

## Boundaries and scale limits

Not validated on real corpora, GPT-2-small-class or larger models, AdamW/momentum optimizer state, distributed training, mixed precision, cross-device verifiers, adaptive adversaries, privacy-preserving data access, or real volunteer network constraints.

## Claim scope

In a deterministic CPU float64 toy training run with a 4,181-parameter MLP, SGD, synthetic seeded batches, and 25 sampled audit packages from 120 steps, volunteer-style recomputation from pre-step state and batch seed exactly reproduced honest gradients/updates and detected all sampled package tampering controls.

## Why it stopped

Tier 1 direct mechanism evidence is positive but controlled and small; it is useful no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen test on a small transformer with AdamW optimizer state and cross-device or mixed-precision verifier tolerances before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-device AdamW sampled-gradient recomputation on a small transformer
- Success threshold: Across at least 60 total sampled honest checks, honest false-positive rate <= 1%, all sampled tamper controls detected, and audit overhead remains documented and locally runnable.
- Stop condition: Stop as unsupported if honest false positives exceed 5% after reasonable tolerance calibration or if any sampled tamper class has detection below 95%.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-sampled-gradient-recomputation-for-volunteer-sp-0f3fe3b385`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

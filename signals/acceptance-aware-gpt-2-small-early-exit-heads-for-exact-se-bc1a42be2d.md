# Acceptance-aware GPT-2-small early-exit heads for exact self-speculative decoding

Status: `useful_signal`
Project ID: `acceptance-aware-gpt-2-small-early-exit-heads-for-exact-se-bc1a42be2d`
Run ID: `acceptance-aware-gpt-2-small-early-exit-heads-for-exact-se-bc1a42be2d-20260516T124823526022+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Acceptance-aware GPT-2-small early-exit heads for exact self-speculative decoding: internal_generated:acceptance-aware-gpt-2-small-early-exit-heads-for-exact-se-bc1a42be2d

## What looked useful

Acceptance-aware heads improved exact final-argmax acceptance by +11.90, +13.66, and +15.67 percentage points at layers 4, 6, and 8 respectively, while reducing corpus next-token accuracy. This supports the acceptance-targeting mechanism but not a paper-ready speedup claim.

## Boundaries and scale limits

Validated offline on 131,072 WikiText validation positions with 500 update steps per head. Serving speed is modeled analytically, not measured in a multi-token KV-cache implementation; no larger models, sampled decoding, or broad domain robustness were tested.

## Claim scope

For frozen GPT-2-small on WikiText-103 validation, linear LM-head-initialized early-exit heads trained to predict the final model greedy token increase exact greedy verifier acceptance versus standard next-token CE heads at layers 4, 6, and 8.

## Why it stopped

Mechanism supported, but practical exact self-speculative decoding speedup was only analytically proxied; publication-grade evidence requires measured multi-token serving latency.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is a measured multi-token exact greedy self-speculative decoder using the layer-4 acceptance-aware head with KV-cache reuse and wall-clock latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measured multi-token exact GPT-2-small self-speculative decoding with acceptance-aware layer-4 heads
- Success threshold: At least 1.10x measured tokens/sec improvement over standard greedy GPT-2-small decoding with exact output equality on a held-out prompt set, and at least 0.05x speedup over the true-token CE head under the same schedule.
- Stop condition: Stop if measured speedup is below 1.00x for the layer-4 acceptance-aware head after tuning draft length and confidence thresholds, or if exact output equality fails.

## Evidence references

- Artifact root: `<local-path>/projects/acceptance-aware-gpt-2-small-early-exit-heads-for-exact-se-bc1a42be2d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Calibration-trained ternary residual channels for GPT-2-small sub-2-bit perplexity

Status: `useful_signal`
Project ID: `calibration-trained-ternary-residual-channels-for-gpt-2-sm-59c820e71a`
Run ID: `calibration-trained-ternary-residual-channels-for-gpt-2-sm-59c820e71a-20260519T043805376630+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/eef056bc5fd5

## What looked useful

Calibration-trained residual channels strongly rescue catastrophic ternary-only GPT-2-small projection quantization under a sub-2 idealized projection-bit budget, but the recovered model remains roughly 2x worse than dense and is not a paper-positive sub-2-bit GPT-2-small result.

## Boundaries and scale limits

Tier 1 small direct test only: 1024 WikiText-2 calibration blocks, 256 eval blocks, one seed, 128-token contexts, no packed kernel, no end-to-end model bit accounting, and embeddings/lm_head/layernorms/biases excluded from compression accounting.

## Claim scope

On GPT-2-small with transformer Conv1D projection/MLP matrices ternarized per output channel, calibration-trained rank-4 residual channels recovered validation perplexity from 25214.78 ternary-only to 118.88, and test perplexity from 27130.45 ternary-only to 136.87, at an idealized 1.696 projection bits/weight. Dense GPT-2-small remained substantially better at 53.08 validation PPL and 64.74 test PPL.

## Why it stopped

No-paper useful signal: the Tier 1 direct test supports the recovery mechanism but does not close the original sub-2-bit GPT-2-small perplexity claim because dense perplexity is still much better and compression accounting is projection-only.

## Recommended next action

Run a medium confirmation with full WikiText-2 validation/test evaluation, standard 2-bit quantization baselines, multiple seeds, and explicit end-to-end bit accounting including embeddings and layer norms.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium confirmation of rank-4 ternary residual GPT-2-small against 2-bit baselines
- Success threshold: Residual ternary GPT-2-small must beat the standard 2-bit baseline on full WikiText-2 validation and test perplexity while staying below 2.0 bits/parameter under explicit end-to-end accounting, or come within 25% relative PPL of dense if no baseline beats that threshold.
- Stop condition: Stop if end-to-end accounting exceeds 2.0 bits/parameter, if residual PPL is worse than the 2-bit baseline on both validation and test, or if rank-4 results fail to reproduce within 10% PPL across seeds/checks.

## Evidence references

- Artifact root: `<local-path>/projects/calibration-trained-ternary-residual-channels-for-gpt-2-sm-59c820e71a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

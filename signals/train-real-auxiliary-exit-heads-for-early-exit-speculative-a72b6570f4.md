# Train Real Auxiliary Exit Heads for Early-Exit Speculative Drafting

Status: `useful_signal`
Project ID: `train-real-auxiliary-exit-heads-for-early-exit-speculative-a72b6570f4`
Run ID: `train-real-auxiliary-exit-heads-for-early-exit-speculative-a72b6570f4-20260515T203123302082+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Train Real Auxiliary Exit Heads for Early-Exit Speculative Drafting: internal_generated:train-real-auxiliary-exit-heads-for-early-exit-speculative-a72b6570f4

## What looked useful

Auxiliary heads trained on real hidden states are a real mechanism: L1 acceptance improved from 11.37% tied control to 20.87% +/- 0.39%; L2 from 15.05% to 24.00% +/- 0.48%; L4 from 31.04% to 37.40% +/- 0.51%. The only optimistic one-token speed-positive result was L1 at 1.044x +/- 0.004x, so this is not paper-ready evidence of practical speculative acceleration.

## Boundaries and scale limits

Local medium confirmation only: distilgpt2, 512 train blocks, 192 validation blocks, three fixed seeds, one-token greedy agreement. No wall-clock speculative decoding loop, no KV-cache-aware serving benchmark, no multi-token acceptance simulation, no larger model, and no long training sweep.

## Claim scope

On frozen distilgpt2 with WikiText-2 validation text, real trained auxiliary exit heads improve early-layer next-token CE, label accuracy, and exact full-model greedy top-1 agreement over random and tied-LM controls. Only the layer-1 head is narrowly positive under an optimistic one-token compute bound; layers 2 and 4 remain speed-negative.

## Why it stopped

No-paper useful signal: direct fixed-seed metrics support trained auxiliary heads as a mechanism, but practical acceleration is only a narrow optimistic layer-1 compute-bound result and not a wall-clock serving validation.

## Recommended next action

Run a bounded KV-cache-aware wall-clock speculative decoding follow-up using the trained layer-1 head on fixed prompts, comparing tokens/sec and exact greedy output preservation against full-model greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Wall-clock KV-cache validation of layer-1 auxiliary speculative drafting
- Success threshold: Median tokens/sec at least 1.05x the full-model greedy baseline with exact greedy output preservation and trained layer-1 head outperforming the tied-LM control.
- Stop condition: Stop if the trained layer-1 implementation is below 1.05x median tokens/sec, fails exact greedy output preservation, or does not beat the tied-LM control on acceptance and latency.

## Evidence references

- Artifact root: `<local-path>/projects/train-real-auxiliary-exit-heads-for-early-exit-speculative-a72b6570f4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

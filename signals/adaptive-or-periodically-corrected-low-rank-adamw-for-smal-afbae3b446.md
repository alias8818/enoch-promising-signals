# Adaptive or periodically corrected low-rank AdamW for small LM training

Status: `useful_signal`
Project ID: `adaptive-or-periodically-corrected-low-rank-adamw-for-smal-afbae3b446`
Run ID: `adaptive-or-periodically-corrected-low-rank-adamw-for-smal-afbae3b446-20260518T100607224788+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Adaptive or periodically corrected low-rank AdamW for small LM training: internal_generated:adaptive-or-periodically-corrected-low-rank-adamw-for-smal-afbae3b446

## What looked useful

Medium scale barely passed at about 1.049x AdamW validation loss with 56.7%-62.5% optimizer-state ratio, and the no-residual ablation failed catastrophically. Tier 3 failed: best corrected variants were about 1.059x AdamW validation loss with 54.9%-59.2% state ratio and 0.57x-0.70x AdamW speed.

## Boundaries and scale limits

Validated on local GB10 with character-level Tiny Shakespeare models up to 4 layers, width 128, 1800 steps, seeds 0/1/2. Not GPT-2-small BPE, not large-corpus pretraining, not fused/distributed optimizer implementation, and memory is optimizer-state element accounting rather than isolated peak CUDA memory.

## Claim scope

On Tiny Shakespeare character-level small-transformer LM training, periodic row/column residual correction makes low-rank AdamW second-moment compression stable and memory-saving, but it does not meet AdamW-quality validation loss on the Tier 3 4-layer benchmark.

## Why it stopped

Direct Tier 3 validation against AdamW on fixed seeds missed the validation-loss target despite satisfying optimizer-state and speed constraints.

## Recommended next action

Stop this follow-up chain; the bounded direct Tier 3 validation fails the quality threshold, and the obvious rank/refresh-interval fixes did not close the gap.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-or-periodically-corrected-low-rank-adamw-for-smal-afbae3b446`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Practical Randomized-SVD Hybrid Spectral AdamW on Small Transformers

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `practical-randomized-svd-hybrid-spectral-adamw-on-small-tr-e7c4eede14`
Run ID: `practical-randomized-svd-hybrid-spectral-adamw-on-small-tr-e7c4eede14-20260518T091407378847+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Practical Randomized-SVD Hybrid Spectral AdamW on Small Transformers: internal_generated:practical-randomized-svd-hybrid-spectral-adamw-on-small-tr-e7c4eede14

## What looked useful

The practical randomized/periodic update reduced exact-SVD overhead enough to reach 0.52x-0.54x AdamW speed on the medium benchmark and 0.61x-0.70x on Tier 3 while storing 54.9%-62.5% of AdamW state. It barely passed the medium loss threshold with median ratios 1.0493-1.0497, but Tier 3 variants missed the threshold at about 1.059x AdamW validation loss. The no-residual ablation diverged or produced unusable losses, reinforcing that row/column residual statistics are necessary.

## Boundaries and scale limits

Evidence is limited to local Tiny Shakespeare character language modeling, seeds 0/1/2, 234k-parameter and 4-layer 128-wide small Transformers, single GB10 execution, no GPT-2-small-class tokenized corpus, no mixed precision, no distributed/sharded optimizer state, and no fused production optimizer kernels.

## Claim scope

On Tiny Shakespeare character-level small Transformers, randomized/periodic SVD Hybrid Spectral AdamW can preserve about 55% to 63% of dense AdamW optimizer-state elements and run at more than 0.5x AdamW speed, but it only met the <=1.05x AdamW validation-loss threshold on the prior 234k-parameter medium benchmark and failed that threshold on the larger Tier 3 4-layer 128-wide Transformer.

## Why it stopped

Bounded Tier 3 validation directly tested the target metric and found median validation-loss ratios around 1.059x AdamW, above the preset <=1.05x success threshold, despite passing state and speed constraints.

## Recommended next action

Stop this follow-up chain as no-paper useful evidence: the practical randomized-SVD optimizer is computationally plausible but failed the Tier 3 direct validation-loss threshold, and further work would require a substantive optimizer redesign rather than another bounded parameter tweak.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/practical-randomized-svd-hybrid-spectral-adamw-on-small-tr-e7c4eede14`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

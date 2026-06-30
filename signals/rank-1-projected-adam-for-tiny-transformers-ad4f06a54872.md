# Rank-1 projected Adam for tiny transformers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `rank-1-projected-adam-for-tiny-transformers-ad4f06a54872`
Run ID: `rank-1-projected-adam-for-tiny-transformers-ad4f06a54872-20260604T224114072422+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e621841cbccf

## What looked useful

Rank1ProjectedAdamW trained without numerical failure but ended at mean validation loss 3.2786 versus 2.3616 for AdamW, a 0.917 loss gap and 38.8% relative increase, while running 6.44x slower in this implementation. Final projected matrix-gradient energy retained averaged 56.5%.

## Boundaries and scale limits

Synthetic task, CPU-only implementation, 80,640-parameter transformer, 256k training tokens per run, 3 seeds. Not evidence about optimized low-rank kernels, error-feedback variants, adaptive rank, real text corpora, or GPT-2-small/full-scale training.

## Claim scope

Naive per-step top-SVD rank-1 projection of matrix gradients before AdamW moments does not preserve useful optimization quality for an 80k-parameter tiny causal transformer on a synthetic recurrence next-token task over 3 seeds and 250 matched-token steps.

## Why it stopped

Bounded early falsification: on the direct tiny-transformer proxy task, the naive rank-1 projected optimizer was consistently worse than AdamW at matched steps/tokens and had much lower throughput; this is not full-scale validation.

## Recommended next action

Stop this naive rank-1 projection line as a drop-in AdamW replacement; only revisit with a bounded variant that adds residual/error-feedback or adaptive rank and demonstrates matched-token recovery on a small real text task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-feedback low-rank AdamW for tiny transformers
- Success threshold: Residual-feedback rank-1 reaches within 5% of AdamW final validation loss at matched tokens and shows a concrete memory or communication benefit versus AdamW, while outperforming naive rank-1 by at least 0.3 validation-loss points.
- Stop condition: Stop if residual-feedback rank-1 remains more than 10% worse than AdamW validation loss at matched tokens or removes any practical memory/communication advantage.

## Evidence references

- Artifact root: `<local-path>/projects/rank-1-projected-adam-for-tiny-transformers-ad4f06a54872`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

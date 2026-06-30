# Deduplication threshold ablation for tiny CPU pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `deduplication-threshold-ablation-for-tiny-cpu-pretraining-bd1d844be0cf`
Run ID: `deduplication-threshold-ablation-for-tiny-cpu-pretraining-bd1d844be0cf-20260628T153501906211+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6a792cdac89d

## What looked useful

Deduplication reduced duplicate-family skew but removed useful near-duplicate variation; no deduplication had the best uniform, rare-family, and novel-family validation NLL.

## Boundaries and scale limits

Synthetic corpus, three seeds, tiny non-transformer model, short CPU-only training run, and no real web/text corpus or contamination/memorization evaluation.

## Claim scope

In a synthetic near-duplicate corpus with a tiny NumPy context-MLP next-token model trained on CPU for a fixed update budget, all tested shingle-Jaccard deduplication thresholds worsened held-out NLL versus no deduplication.

## Why it stopped

Proxy-scale direct toy evidence did not support deduplication thresholds improving tiny CPU pretraining; this is not a full natural-corpus validation.

## Recommended next action

Stop this run as a bounded early negative; only deepen if a follow-up can test a small real-text corpus with a transformer/GRU at matched token and update budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text small-LM deduplication threshold ablation
- Success threshold: A moderate dedup threshold beats no-dedup and aggressive dedup by at least 1 percent held-out NLL or shows an equal-loss memorization/contamination reduction with retained-token accounting.
- Stop condition: Stop if no threshold beats no-dedup on validation loss or memorization proxy after matched-budget small real-text runs.

## Evidence references

- Artifact root: `<local-path>/projects/deduplication-threshold-ablation-for-tiny-cpu-pretraining-bd1d844be0cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

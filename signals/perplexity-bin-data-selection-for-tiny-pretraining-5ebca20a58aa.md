# Perplexity-Bin Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-bin-data-selection-for-tiny-pretraining-5ebca20a58aa`
Run ID: `perplexity-bin-data-selection-for-tiny-pretraining-5ebca20a58aa-20260530T072113586297+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/38af9342d8d1

## What looked useful

Global perplexity bins and within-book perplexity bins both underperformed random selection. Global random reached 3.221403 validation bits/byte; best bin was high at 3.233495 (+0.012092 bits/byte). Within-book random reached 3.216497 validation bits/byte; best bin was mid at 3.218039 (+0.001542 bits/byte).

## Boundaries and scale limits

Tested only byte n-gram LMs, 8 Gutenberg books, 2048-byte chunks, 300000 selected bytes per condition, 5 seeds, and validation on two held-out books. It does not validate neural Transformer pretraining, large web corpora, tokenizer effects, downstream transfer, or long training runs.

## Claim scope

In a bounded public-domain-text proxy using byte n-gram tiny language models, selecting equal training bytes from low, mid, or high external-perplexity bins did not improve held-out byte perplexity over random equal-budget selection.

## Why it stopped

Proxy evidence did not support perplexity-bin selection for tiny pretraining: in both global and within-book 5-seed runs, random equal-budget selection produced the lowest held-out validation bits/byte.

## Recommended next action

Stop this run as an early proxy falsification; only revisit with a bounded neural Transformer follow-up that controls source mix and compares against random and quality-filter baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural Tiny-Transformer Check for Source-Balanced Perplexity-Bin Selection
- Success threshold: Mid-perplexity selection must beat random by at least 0.02 validation nats/token or 1% relative perplexity on the neural LM mean across seeds, without worse instability or source-mix artifacts.
- Stop condition: Stop if random is best or if the best perplexity bin improves by less than 0.02 nats/token and less than 1% relative perplexity after the matched-token neural run.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-bin-data-selection-for-tiny-pretraining-5ebca20a58aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

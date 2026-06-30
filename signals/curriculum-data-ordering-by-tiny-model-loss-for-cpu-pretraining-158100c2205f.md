# Curriculum Data Ordering by Tiny-Model Loss for CPU Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `curriculum-data-ordering-by-tiny-model-loss-for-cpu-pretraining-158100c2205f`
Run ID: `curriculum-data-ordering-by-tiny-model-loss-for-cpu-pretraining-158100c2205f-20260607T110545263340+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/051d97438448

## What looked useful

The tiny scorer cleanly separated easy, medium, and hard sequence classes, but every tested tiny-loss ordering worsened validation loss versus random order. Mean deltas were +0.0701 for easy_to_hard, +0.0803 for hard_to_easy, and +0.0366 for middle_out, with 0/10 wins versus random for each.

## Boundaries and scale limits

Synthetic corpus only; no real text tokenizer, no transformer or GPT-2-small-class baseline, no large-scale pretraining, and no production CPU throughput or energy validation.

## Claim scope

Naive static ordering of synthetic next-token pretraining examples by tiny trigram-model loss was tested against random order using a small NumPy MLP language model on CPU for 10 seeds.

## Why it stopped

Proxy/local early falsification: random order beat all tested static tiny-loss curricula across 10 seeds, so this does not support paper writing or larger static-sort validation now.

## Recommended next action

Stop this naive static-sort line as no-paper evidence; run a bounded follow-up that uses tiny-loss buckets while preserving local distribution mixing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-Loss Bucket Mixing for CPU Pretraining
- Success threshold: A bucketed or weighted tiny-loss scheduler improves mean final validation loss by at least 0.02 NLL versus random and wins at least 7/10 paired seeds without increasing wall-clock by more than 10%.
- Stop condition: Stop if all distribution-mixed tiny-loss schedulers fail to beat random on mean validation loss or win fewer than 6/10 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-data-ordering-by-tiny-model-loss-for-cpu-pretraining-158100c2205f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

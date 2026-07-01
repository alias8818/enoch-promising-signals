# Near-dedup + classifier quality filter cascade for tiny pretraining data

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `near-dedup-classifier-quality-filter-cascade-for-tiny-pretraining-data-9c3ae8f443c2`
Run ID: `near-dedup-classifier-quality-filter-cascade-for-tiny-pretraining-data-9c3ae8f443c2-20260523T042435429484+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/afe971b0d332

## What looked useful

Classifier-only filtering reached high quality precision but selected fewer duplicate families. Adding near-dedup improved clean held-out NLL from 1.5696 to 1.4360 at threshold 0.82 for classifier_then_dedup and to 1.4590 for dedup_then_classifier. The best order was threshold-sensitive, so the useful result is the combined filter mechanism, not a fixed dedup-first recipe.

## Boundaries and scale limits

Synthetic corpus only; word trigram LM proxy only; no neural LM training; no real web crawl; 8 seeds per threshold and three near-dedup thresholds.

## Claim scope

On a controlled synthetic tiny-pretraining corpus with injected near-duplicates and low-quality boilerplate, combining a quality classifier with near-deduplication improved fixed-budget clean held-out trigram-LM loss and selected-cluster diversity relative to classifier-only or dedup-only filtering.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and the exact cascade order is mixed across thresholds.

## Recommended next action

Run a bounded deepen follow-up on a small real public text corpus using a tiny neural LM, with the same classifier-only, dedup-only, dedup_then_classifier, and classifier_then_dedup ablations at fixed sequence-item budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data tiny neural LM ablation for classifier plus near-dedup filtering
- Success threshold: Combined classifier+dedup condition reduces neural-LM validation loss by at least 3% versus classifier_only while increasing selected duplicate-family diversity by at least 15% at the same token budget in at least two of three seeds.
- Stop condition: Stop if no combined condition beats classifier_only validation loss by 1% or more and diversity by 10% or more under two reasonable dedup thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/near-dedup-classifier-quality-filter-cascade-for-tiny-pretraining-data-9c3ae8f443c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

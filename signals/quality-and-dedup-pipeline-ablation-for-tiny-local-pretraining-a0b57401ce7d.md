# Quality and dedup pipeline ablation for tiny local pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quality-and-dedup-pipeline-ablation-for-tiny-local-pretraining-a0b57401ce7d`
Run ID: `quality-and-dedup-pipeline-ablation-for-tiny-local-pretraining-a0b57401ce7d-20260621T131853496036+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/612f04cc27a5

## What looked useful

Raw averaged 0.6205 clean validation loss. Quality-only was essentially tied at 0.6222, dedup-only was worse at 0.6479, and quality+dedup was worse at 0.6307. The memorization-gap proxy was not reduced by dedup: raw averaged 0.1484, dedup-only 0.1534, and quality+dedup 0.2063.

## Boundaries and scale limits

Synthetic corpus only; char-level tokenizer; small model; 900 optimizer steps per seed; no natural web text, no GPT-2-small-class scale, no MinHash/LSH production dedup, no downstream task evaluation, and no long learning-curve validation.

## Claim scope

In a controlled synthetic tiny-pretraining setup with a 366,528-parameter char-level Transformer, three seeds, fixed 900-step CUDA training budgets, exact/near duplicates, and simple quality-filterable noise, a quality+dedup preprocessing pipeline did not improve mean clean held-out loss over raw data and did not reduce the duplicate-memorization-gap proxy.

## Why it stopped

Bounded proxy evidence is mixed-to-negative for the combined quality+dedup hypothesis and is not publication-grade full validation.

## Recommended next action

Do not write a paper from this run; run one bounded deepen test on a small natural-text corpus with a subword tokenizer and MinHash-style dedup before spending larger training budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-text tiny-LM quality and MinHash dedup ablation
- Success threshold: Quality+dedup must beat raw mean clean validation loss by at least 2% and reduce duplicate-memorization gap by at least 20% across three seeds without relying on synthetic-only artifacts.
- Stop condition: Stop if quality+dedup fails to beat raw on mean clean validation loss or fails to reduce duplicate-memorization gap across the first three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/quality-and-dedup-pipeline-ablation-for-tiny-local-pretraining-a0b57401ce7d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# MinHash dedup threshold sweep at GPT-2-tiny scale

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `minhash-dedup-threshold-sweep-at-gpt-2-tiny-scale-0cf9aafd6f7f`
Run ID: `minhash-dedup-threshold-sweep-at-gpt-2-tiny-scale-0cf9aafd6f7f-20260630T054201292289+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a87d697cf665

## What looked useful

Threshold 0.70 reduced leakage-probe mean max train Jaccard from 0.649 to 0.476 while retaining about 86% of documents, but did not improve leakage-probe loss; mild thresholds 0.95/0.90 had the lowest mean losses but loss deltas were within seed noise.

## Boundaries and scale limits

Three seeds, 1420 raw training documents, byte-level 4-layer/128-hidden tiny GPT, 3000 optimizer steps per threshold, injected contamination rather than natural web-scale duplication, combined train-dedup and validation-decontamination policy.

## Claim scope

On a Wikitext-2-derived contaminated corpus with injected near duplicates, MinHash/Jaccard thresholding at GPT-like tiny scale reliably trades retained documents for lower train/eval near-duplicate exposure, but downstream clean and leakage validation loss differences are smaller than seed-to-seed variance.

## Why it stopped

The direct tiny-GPT threshold sweep produced reproducible retention/leakage evidence, but model-quality deltas were not robust enough for a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should separate train-only dedup from validation decontamination on a naturally duplicated corpus before scaling model size.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Separate train-only dedup and validation decontamination on natural near-duplicate text
- Success threshold: A threshold policy changes leakage or memorization metrics by at least 20% while clean validation loss degradation remains below one-third of the observed seed-to-seed standard deviation.
- Stop condition: Stop if natural near-duplicate prevalence is too low to move leakage metrics, or if all threshold-induced loss changes remain smaller than seed variance after three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-dedup-threshold-sweep-at-gpt-2-tiny-scale-0cf9aafd6f7f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

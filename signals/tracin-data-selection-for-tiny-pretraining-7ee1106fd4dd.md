# TracIn data selection for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tracin-data-selection-for-tiny-pretraining-7ee1106fd4dd`
Run ID: `tracin-data-selection-for-tiny-pretraining-7ee1106fd4dd-20260604T172340958352+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b57543c984e7

## What looked useful

TracIn scoring consistently enriched target examples versus random selection, with mean target fraction 0.892 in top-k versus 0.331 for random, but naive top-k selection did not reliably improve downstream target validation loss and lost to random on mean loss due to one seed failure.

## Boundaries and scale limits

Does not test real text corpora, transformer-scale models, full-parameter TracIn, long pretraining, or large-scale data selection. Synthetic task is useful for mechanism probing only.

## Claim scope

Toy synthetic tiny-language-model pretraining with a 384-example mixed corpus, 96-example selected subsets, TracIn-style head-gradient scoring against target validation sequences, and three random seeds.

## Why it stopped

Bounded synthetic evidence is mixed: ranking signal is supported, but the stronger top-k selection benefit is early-falsified by unstable downstream retraining versus random. This is not a full validation or paper-ready result.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded diversity-aware TracIn follow-up before considering any larger or real-corpus validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-aware TracIn selection for tiny pretraining
- Success threshold: Diversity-aware TracIn beats random subset target validation loss in at least 5 of 6 seeds and has lower mean loss than naive TracIn without reducing mean target fraction below 0.80.
- Stop condition: Stop if diversity-aware selection fails to beat random in at least 4 of the first 6 seeds or if target enrichment falls to random-like levels.

## Evidence references

- Artifact root: `<local-path>/projects/tracin-data-selection-for-tiny-pretraining-7ee1106fd4dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

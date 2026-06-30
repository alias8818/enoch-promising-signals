# Curriculum data ordering by compressibility for tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `curriculum-data-ordering-by-compressibility-for-tiny-pretraining-29a8ce466231`
Run ID: `curriculum-data-ordering-by-compressibility-for-tiny-pretraining-29a8ce466231-20260604T113722194178+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/25e28f9bf1f5

## What looked useful

Random ordering beat both compressible-first and incompressible-first curricula at every paired seed. At 1,000 steps, mean final validation loss was 2.1020 for random, 2.1615 for compressible-first, and 2.1704 for incompressible-first.

## Boundaries and scale limits

Tested only byte-level Wikitext-2, 8,192 train blocks, 512 validation blocks, 3 seeds, and 350/1,000 optimizer-step horizons. Not a tokenizer-level GPT-2-small or large-corpus validation; does not test bucketed, mixed, or warmup-only curricula.

## Claim scope

In a bounded direct tiny-pretraining test on Wikitext-2 byte blocks with a 1.34M-parameter causal Transformer, global monotone ordering by zlib compressibility did not improve held-out language-model loss over random ordering.

## Why it stopped

Proxy-scale but direct tiny-pretraining evidence consistently falsified the simple monotone compressibility-ordering hypothesis; this is not a full-scale validation, but it is enough to avoid presenting the recipe as promising.

## Recommended next action

Stop this monotone-sorting claim as an early bounded negative; if continuing, run a separate bucketed or temperature-mixed compressibility curriculum that preserves local randomness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bucketed compressibility curriculum with local shuffling
- Success threshold: Bucketed or temperature-mixed compressibility scheduling must beat random ordering by at least 0.02 mean validation-loss reduction at 1,000 steps across 3 paired seeds, with no seed worse than random by more than 0.01.
- Stop condition: Stop if all compressibility-based mixed schedules are worse than random by at least 0.01 mean validation loss or if gains appear only in one seed without paired consistency.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-data-ordering-by-compressibility-for-tiny-pretraining-29a8ce466231`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

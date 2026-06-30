# Tiny Pretraining with Data Selection via Hard-Example Scoring

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiny-pretraining-with-data-selection-via-hard-example-scoring-fa7806aee1e0`
Run ID: `tiny-pretraining-with-data-selection-via-hard-example-scoring-fa7806aee1e0-20260604T000343823537+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/45d77e07dfa2

## What looked useful

Probe-loss scoring successfully separated hard, random, and easy chunks, but hard-only top-K selection was worse than random in 3/3 seeds and worse than easy in 3/3 seeds. Mean hard-minus-random validation NLL was +0.01188, and mean hard-minus-easy validation NLL was +0.01692, where positive means hard selection was worse.

## Boundaries and scale limits

The result uses a small byte-level model, two Project Gutenberg books, short training schedules, and three main seeds. It does not validate or falsify transformer-scale, subword-tokenized, long-run, large-corpus pretraining or mixed/curriculum selection methods.

## Claim scope

In a bounded CPU-local NumPy byte-level causal language model on public-domain English text, selecting only the top-loss hard chunks after a short probe did not improve equal-budget tiny pretraining versus random or easy selection.

## Why it stopped

Proxy-scale early falsification of the naive hard-only data selection hypothesis: the direct small byte-LM test found consistent validation degradation versus random and easy controls, not a full large-scale validation.

## Recommended next action

Stop this run as a bounded negative/useful signal; if continuing, run a separate medium-scale follow-up testing moderate-hard or hard/random mixture selection rather than naive top-loss hard-only filtering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Moderate-Hard and Mixed Hard/Random Selection for Tiny LM Pretraining
- Success threshold: Moderate-hard or hard/random mixture selection beats random selection by at least 0.02 validation NLL or equivalent perplexity improvement in at least 3 of 4 seeds without worsening final validation loss on any seed.
- Stop condition: Stop if hard/mixed variants are not better than random after the planned equal-token budget, or if the effect is smaller than 0.02 validation NLL and inconsistent across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-pretraining-with-data-selection-via-hard-example-scoring-fa7806aee1e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

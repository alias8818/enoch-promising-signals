# Mid-Perplexity Data Filtering for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `mid-perplexity-data-filtering-for-tiny-pretraining-ce0047571adc`
Run ID: `mid-perplexity-data-filtering-for-tiny-pretraining-ce0047571adc-20260527T125013226826+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/127bf6091a35

## What looked useful

Mid-perplexity filtering was worse than random in all three token-matched medium seeds: validation-loss deltas mid minus random were +0.3009, +0.1937, and +0.5975, mean +0.3641. Random was best in two seeds; low-perplexity was best in one; mid was never best.

## Boundaries and scale limits

This is not a standard-corpus or large-scale pretraining validation. WikiText live download/cache access stalled, the corpus is local technical documentation, the reference scorer is a simple bigram LM rather than a frozen neural LM, and target training is tiny.

## Claim scope

On a local /usr/share/doc technical-text corpus, with documents scored by a seed-trained add-smoothed word bigram reference model and identical tiny causal Transformers trained from scratch under token-budget-matched low/mid/high/random filters for 450 steps across three seeds, mid-perplexity filtering did not improve held-out validation loss over random filtering.

## Why it stopped

Token-budget-matched direct tiny-pretraining evidence did not support the mid-perplexity filtering hypothesis; result is no-paper useful signal rather than full validation.

## Recommended next action

Stop this run as a bounded local negative; only revisit with a standard natural-language corpus and a stronger frozen neural reference scorer under the same token-budget-matched protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-matched mid-perplexity filtering with a neural reference scorer on a standard corpus
- Success threshold: Mid-perplexity filtering must beat random by at least 0.05 validation loss on mean across three seeds, with no seed worse than random by more than 0.02 loss.
- Stop condition: Stop as negative if mid-perplexity is not better than random on mean validation loss after three token-budget-matched seeds, or if any observed gain disappears when bucket diversity is matched.

## Evidence references

- Artifact root: `<local-path>/projects/mid-perplexity-data-filtering-for-tiny-pretraining-ce0047571adc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

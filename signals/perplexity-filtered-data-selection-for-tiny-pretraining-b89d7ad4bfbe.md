# Perplexity-Filtered Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-filtered-data-selection-for-tiny-pretraining-b89d7ad4bfbe`
Run ID: `perplexity-filtered-data-selection-for-tiny-pretraining-b89d7ad4bfbe-20260609T013645128075+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6efc1435e55d

## What looked useful

Perplexity filtering behaved like a band-pass filter: middle-perplexity documents beat random in 3/3 seeds by mean -0.0205 validation NLL, but low-perplexity and high-perplexity selections were worse than random by +0.0853 and +0.1343 NLL respectively.

## Boundaries and scale limits

Single corpus, three seeds, tiny model, 300 optimizer steps, 50k selected tokens per condition, word-level 8k vocabulary, and smoothed bigram reference scorer. This is not evidence for large-scale pretraining or neural-reference perplexity filtering.

## Claim scope

On WikiText-2 with a 50k-token selected budget and a 2-layer 128-wide tiny causal Transformer trained for 300 steps, middle-band bigram-reference-perplexity selection slightly improved held-out NLL over random selection, while lowest- and highest-perplexity selection hurt.

## Why it stopped

No-paper closure: the local result is useful but small-scale and partly proxy-based, so it should not be treated as full validation of perplexity-filtered tiny pretraining.

## Recommended next action

Run a bounded medium confirmation with a neural reference scorer, GPT-2-small-class or parameter-matched target model, two corpora, multiple token budgets, and document-length/topic controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural-reference medium confirmation of middle-perplexity band-pass selection
- Success threshold: Middle-perplexity selection improves mean validation NLL over random by at least 0.03 on at least two corpora and is better than low/high selection in at least 75% of seed-budget-corpus comparisons.
- Stop condition: Stop if middle-perplexity selection fails to beat random on both corpora at the smallest two budgets or if gains vanish after length/duplicate controls.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtered-data-selection-for-tiny-pretraining-b89d7ad4bfbe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

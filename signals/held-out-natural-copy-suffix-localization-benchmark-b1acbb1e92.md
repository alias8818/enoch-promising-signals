# Held-out natural copy suffix localization benchmark

Status: `useful_signal`
Project ID: `held-out-natural-copy-suffix-localization-benchmark-b1acbb1e92`
Run ID: `held-out-natural-copy-suffix-localization-benchmark-b1acbb1e92-20260516T162703049935+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Held-out natural copy suffix localization benchmark: internal_generated:held-out-natural-copy-suffix-localization-benchmark-b1acbb1e92

## What looked useful

A medium benchmark with fixed seeds, ablations, and real baselines shows that unordered token overlap is confounded by shuffled controls, while an order-sensitive token LCS diagnostic cleanly separates copied suffixes from shuffled controls and localizes copied suffixes within 100 characters.

## Boundaries and scale limits

Queries are constructed suffixes with synthetic whitespace, truncation, character-noise, and shuffled controls; this does not test real model-generated memorized continuations, larger corpora, paraphrastic copying, adversarial near-duplicates, or production-scale retrieval.

## Claim scope

On 240 held-out 20 Newsgroups test passages across three fixed seeds, an order-sensitive token LCS window localizes constructed natural copied suffixes within 100 characters while rejecting shuffled-token no-copy controls at threshold 0.70.

## Why it stopped

No-paper closure: the result is a useful medium-tier benchmark/mechanism signal, but the queries are constructed rather than model-generated, so this is not publication-grade direct evidence of memorized copy suffix localization.

## Recommended next action

Run the same accept/reject and localization diagnostic on actual language-model continuations with controlled source exposure before considering a bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-generated copy suffix localization with controlled exposure
- Success threshold: Across at least three fixed seeds, ordered-token LCS or a stronger order-sensitive method should achieve at least 0.80 accepted-copy localization within 100 characters with shuffled/topic-matched false accept rate at or below 0.05, and beat exact find by at least 0.20 absolute on noisy or partial copies.
- Stop condition: Stop as negative if model-generated continuations do not produce enough labeled copying events for evaluation or if order-sensitive localization cannot beat exact find and unordered overlap under the predeclared accept/reject thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-natural-copy-suffix-localization-benchmark-b1acbb1e92`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

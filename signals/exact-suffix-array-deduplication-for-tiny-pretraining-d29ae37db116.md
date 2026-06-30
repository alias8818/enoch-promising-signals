# Exact Suffix Array Deduplication for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-suffix-array-deduplication-for-tiny-pretraining-d29ae37db116`
Run ID: `exact-suffix-array-deduplication-for-tiny-pretraining-d29ae37db116-20260608T153153110521+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ddd8ca4fc941

## What looked useful

Exact suffix-array deduplication is mechanically viable for small corpora and, in this controlled tiny-pretraining probe, reduced memorization of duplicated exact canaries without materially harming held-out validation loss.

## Boundaries and scale limits

Synthetic corpus only; character-level GRU only; no tokenizer-based transformer, no real pretraining dataset, no downstream tasks, no extraction/exposure evaluation, and no comparison against optimized production dedup baselines.

## Claim scope

On a deterministic 188 KB synthetic byte corpus with exact repeated boilerplate and canary strings, iterative suffix-array/LCP deduplication at a 48-byte threshold removed 72.5% of bytes, verified no remaining adjacent suffix LCP >= 48, and increased duplicated-canary loss in matched tiny character-GRU pretraining while leaving held-out validation loss essentially unchanged.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic and proxy-scale, not a full validation of exact suffix-array deduplication for real tiny pretraining.

## Recommended next action

Run a bounded deepening experiment on a real small text corpus with a tokenizer-based tiny transformer, exact suffix-array dedup, and a hash/n-gram dedup baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact suffix-array deduplication on a real tiny-transformer pretraining corpus
- Success threshold: Exact suffix-array dedup must reduce canary memorization/exposure by at least 25% versus raw while keeping validation perplexity within 2% of raw and showing a clear advantage or tradeoff relative to hash/n-gram dedup.
- Stop condition: Stop if exact suffix-array dedup worsens validation perplexity by more than 5%, fails to reduce memorization/exposure versus raw, or is dominated by hash/n-gram dedup on both quality and resource cost.

## Evidence references

- Artifact root: `<local-path>/projects/exact-suffix-array-deduplication-for-tiny-pretraining-d29ae37db116`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

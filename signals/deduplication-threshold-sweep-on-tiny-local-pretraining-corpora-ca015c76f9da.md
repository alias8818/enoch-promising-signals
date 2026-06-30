# Deduplication threshold sweep on tiny local pretraining corpora

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deduplication-threshold-sweep-on-tiny-local-pretraining-corpora-ca015c76f9da`
Run ID: `deduplication-threshold-sweep-on-tiny-local-pretraining-corpora-ca015c76f9da-20260619T113807990990+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ccc5d030cabd

## What looked useful

Exact-only/high-threshold dedup left a large clean-minus-contaminated NLL gap of 3.145 at threshold 1.0. Threshold 0.4 removed 96.6% of same-family duplicate pairs, retained 20.5% of tokens, preserved all topic families, and reduced the gap to 1.986 with slightly better clean eval NLL in the fixed-vocabulary proxy.

## Boundaries and scale limits

Tiny synthetic corpus only; word trigram proxy only; no transformer pretraining, tokenizer study, real corpus, multi-seed robustness, or production MinHash/LSH scaling was tested.

## Claim scope

On a deterministic 72-document synthetic/local pretraining-style corpus with known near-duplicate families, 5-gram Jaccard deduplication thresholds around 0.4 to 0.6 reduced contaminated-eval advantage versus exact/high-threshold filtering while preserving clean held-out trigram-LM NLL and all topic-family coverage.

## Why it stopped

Closed as a no-paper useful signal because the evidence is a synthetic tiny proxy rather than direct full validation.

## Recommended next action

Run a bounded deepen follow-up on a real small text corpus with a tokenizer and small neural LM, comparing thresholds 1.0, 0.8, 0.6, 0.4, and 0.3 across validation loss plus memorization/extraction metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus neural LM confirmation of tiny-corpus deduplication threshold effects
- Success threshold: A threshold in 0.4 to 0.6 reduces memorization/extraction by at least 25% versus exact-only dedup while keeping clean validation loss within 2% and retaining at least 40% of training tokens.
- Stop condition: Stop if mid-threshold dedup increases clean validation loss by more than 2% at comparable compute, removes cross-topic content at unacceptable precision, or fails to reduce memorization/extraction by at least 10%.

## Evidence references

- Artifact root: `<local-path>/projects/deduplication-threshold-sweep-on-tiny-local-pretraining-corpora-ca015c76f9da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

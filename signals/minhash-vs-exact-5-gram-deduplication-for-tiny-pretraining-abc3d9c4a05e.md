# MinHash vs Exact 5-gram Deduplication for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `minhash-vs-exact-5-gram-deduplication-for-tiny-pretraining-abc3d9c4a05e`
Run ID: `minhash-vs-exact-5-gram-deduplication-for-tiny-pretraining-abc3d9c4a05e-20260609T204209956848+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e1d7582ea778

## What looked useful

Across five seeds, MinHash improved duplicate recall over exact 5-gram signatures by 0.1575 +/- 0.0050 at equal synthetic-label precision, removed about 7.0% more training tokens, raised exposed-validation NLL by 0.0668, and slightly improved clean-test NLL by 0.0161. Boolean exposed contamination was unchanged because train-only dedup keeps a canonical neighbor.

## Boundaries and scale limits

Synthetic corpus only; smoothed word-trigram proxy only; no neural transformer training; no real web corpus; no large-scale indexing-cost study; training-only deduplication does not eliminate train-validation contamination when one canonical near-duplicate remains.

## Claim scope

On deterministic synthetic tiny-pretraining corpora with labeled exact and near-duplicate clusters, MinHash/LSH over 5-gram shingles removes substantially more true duplicate variants than exact 5-gram-set signature deduplication and produces the expected reduction in exposed-validation overfitting signal without hurting clean held-out trigram NLL.

## Why it stopped

Evidence is a bounded synthetic/proxy confirmation of the mechanism, not direct publication-grade pretraining evidence.

## Recommended next action

Stop this worker run as no-paper useful signal; the concrete next bounded test is a tiny transformer run on a real small corpus with train/eval boundary deduplication and memorization probes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Real-Corpus Dedup Boundary Test
- Success threshold: MinHash must reduce train/eval near-duplicate exposure by at least 50% relative to exact 5-gram signatures, reduce memorization/exposed-validation advantage, and keep clean validation loss within 1% of the best baseline at matched token or compute budget.
- Stop condition: Stop if MinHash fails to improve train/eval exposure reduction by at least 20% over exact signatures or if clean validation loss degrades by more than 3% at matched budget.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-vs-exact-5-gram-deduplication-for-tiny-pretraining-abc3d9c4a05e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

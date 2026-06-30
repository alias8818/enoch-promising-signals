# MinHash Deduplication Threshold Sweep for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `minhash-deduplication-threshold-sweep-for-tiny-pretraining-dc4b969a8803`
Run ID: `minhash-deduplication-threshold-sweep-for-tiny-pretraining-dc4b969a8803-20260609T163955345161+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/000e22f99bde

## What looked useful

Moderate thresholds around 0.7-0.85 reduced duplicate leakage while retaining all base identities and slightly improving held-out clean NLL; threshold 0.5 over-merged distinct documents and degraded NLL.

## Boundaries and scale limits

No natural web corpus, no tokenizer-level transformer baseline, no long pretraining, and no large-scale dedup pipeline. The threshold values should not be treated as universal defaults.

## Claim scope

Synthetic 320-base-document corpora across three seeds with injected near-duplicates, MinHash word-5-shingle deduplication thresholds, and fixed-budget tiny GRU word-level LM training.

## Why it stopped

Local synthetic tiny-LM evidence is useful but not paper-ready; the run closed before claiming full validation because direct natural-corpus transformer evidence is still missing.

## Recommended next action

Run the same sweep on a small public natural-language corpus with injected and naturally occurring near-duplicates, using a tiny transformer and reporting retention, false merges, duplicate leakage, and held-out loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-corpus MinHash threshold sweep for tiny transformer pretraining
- Success threshold: A threshold band retains at least 98% audited unique documents, cuts duplicate leakage by at least 50% versus raw, and matches or improves clean validation loss within 1% across three seeds.
- Stop condition: Stop if all thresholds that cut duplicate leakage by at least 50% either lose more than 2% audited unique documents or worsen clean validation loss by more than 1% across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-deduplication-threshold-sweep-for-tiny-pretraining-dc4b969a8803`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

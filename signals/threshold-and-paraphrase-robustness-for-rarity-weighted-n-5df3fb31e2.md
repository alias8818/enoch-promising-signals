# Threshold and paraphrase robustness for rarity-weighted n-gram decontamination

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `threshold-and-paraphrase-robustness-for-rarity-weighted-n-5df3fb31e2`
Run ID: `threshold-and-paraphrase-robustness-for-rarity-weighted-n-5df3fb31e2-20260528T181343274220+0000`

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

- Parent run decision: Small-transformer validation of rarity-weighted n-gram decontamination: enoch://control-plane/projects/small-transformer-validation-of-rarity-weighted-n-gram-dec-5658090628/runs/small-transformer-validation-of-rarity-weighted-n-gram-dec-5658090628-20260528T153013401823+0000
- Parent run decision: Contamination-aware n-gram filtering for pretraining: enoch://control-plane/projects/contamination-aware-n-gram-filtering-for-pretraining-b12df577d4e7/runs/contamination-aware-n-gram-filtering-for-pretraining-b12df577d4e7-20260528T114612824177+0000

## What looked useful

Across seeds 13, 37, and 101, IDF 5-gram containment had low threshold CV (0.0070) but only 0.0606 heavy-paraphrase F1 at its global threshold; IDF cosine had 0.0000 heavy-paraphrase F1. Token BM25 control reached 0.9858 heavy-paraphrase F1, showing the task was solvable by a non-5-gram lexical baseline.

## Boundaries and scale limits

Medium public-corpus retrieval benchmark only; heavy paraphrases are controlled lexical transformations rather than human paraphrases; no web-scale contamination corpus, human paraphrase set, or downstream model memorization evaluation was run.

## Claim scope

On a fixed-seed 20 Newsgroups contamination benchmark with exact, light-paraphrase, heavy controlled-paraphrase, and same-topic clean negatives, rarity-weighted 5-gram scoring can stabilize selected thresholds but does not provide paraphrase robustness when source 5-gram overlap is nearly eliminated.

## Why it stopped

Direct medium benchmark gives a no-paper useful signal: rarity weighting stabilizes some thresholds but fails the core paraphrase robustness condition when 5-gram overlap is removed.

## Recommended next action

Stop this rarity-weighted 5-gram paper path; if continuing, test a bounded hybrid BM25-plus-rare-ngram detector on human paraphrase pairs before any larger-scale claim.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Hybrid BM25 and rare n-gram decontamination on human paraphrases
- Success threshold: Hybrid detector improves heavy/human paraphrase F1 by at least 0.10 absolute over BM25 or 5-gram-only baselines while keeping exact-copy precision at or above 0.98 and clean-negative FPR at or below 0.02.
- Stop condition: Stop if the hybrid does not beat BM25 by at least 0.03 F1 on paraphrase detection or if exact-copy precision falls below 0.98 at the selected threshold.

## Evidence references

- Artifact root: `<local-path>/projects/threshold-and-paraphrase-robustness-for-rarity-weighted-n-5df3fb31e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

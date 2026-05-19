# Long-context model-integrated candidate ranking for cache-aware n-gram drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `long-context-model-integrated-candidate-ranking-for-cache-61d531a365`
Run ID: `long-context-model-integrated-candidate-ranking-for-cache-61d531a365-20260514T030916799540+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Long-context model-integrated candidate ranking for cache-aware n-gram drafting: internal_generated:long-context-model-integrated-candidate-ranking-for-cache-61d531a365

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct validation found consistent raw acceptance gains from target-model ranking, but even favorable cache-aware scoring cost made accepted tokens per target-position cost 20x-37x worse than simple n-gram baselines.

## Recommended next action

Stop this target-model scoring approach as not paper-ready; if continuing the line, branch to a cheap learned or heuristic prefilter that must beat recency/longest on end-to-end tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Cheap ranker for cache-aware n-gram candidate selection
- Success threshold: At least 10% higher end-to-end tokens/sec than the best recency/longest n-gram baseline while retaining at least 75% of oracle candidate-selection accepted-token gain on the same candidate sets.
- Stop condition: Stop if the cheap ranker fails to beat recency/longest on accepted tokens per cost in offline evaluation or fails to improve end-to-end tokens/sec in a bounded decoder run.

## Evidence references

- Artifact root: `<local-path>/projects/long-context-model-integrated-candidate-ranking-for-cache-61d531a365`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

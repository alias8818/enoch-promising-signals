# Reference-Direction Cosine Similarity Filter

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `reference-direction-cosine-similarity-filter-3722237c4dd5`
Run ID: `reference-direction-cosine-similarity-filter-3722237c4dd5-20260629T123246650848+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4aed25db8fa9

## What looked useful

Across 72 medium scenarios, the reference cosine filter raised coverage@0.95 from 0.197 for score-only top-k to 0.993, improved mean best-reference cosine by 0.323, achieved normalized direction entropy of 1.000, and retained 0.885 of score-only top-k mean score with negligible latent front-quality loss.

## Boundaries and scale limits

Tested only on synthetic 3D and 5D simplex candidate pools with 20,000-25,000 candidates per scenario and fixed lattice reference directions; no real embedding retrieval, many-objective benchmark, downstream task metric, or million-candidate scaling was tested.

## Claim scope

In a controlled synthetic simplex-selection task with directional scalar-score bias, assigning candidates to fixed reference directions by cosine similarity and selecting high-scoring bin representatives prevents angular coverage collapse while retaining most scalar score.

## Why it stopped

The result is a proxy mechanism confirmation, not a direct/full validation; paper-level support would require real retrieval or many-objective benchmark evidence with downstream task metrics.

## Recommended next action

Stop this run as no-paper useful synthetic evidence; next, run a bounded real embedding retrieval benchmark against MMR, DPP, and score-only top-k.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Reference-direction cosine filtering on real embedding retrieval benchmarks
- Success threshold: Reference-direction filtering improves diversity coverage by at least 25% over score-only top-k while retaining at least 95% of the best non-random baseline relevance metric or clearly wins the diversity/relevance Pareto tradeoff.
- Stop condition: Stop if it fails to beat score-only top-k on diversity by 10% or loses more than 10% relevance against both MMR and DPP-style baselines on the same benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/reference-direction-cosine-similarity-filter-3722237c4dd5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

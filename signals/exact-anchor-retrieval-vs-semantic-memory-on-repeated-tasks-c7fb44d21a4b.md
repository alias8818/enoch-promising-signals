# Exact-Anchor Retrieval vs Semantic Memory on Repeated Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-retrieval-vs-semantic-memory-on-repeated-tasks-c7fb44d21a4b`
Run ID: `exact-anchor-retrieval-vs-semantic-memory-on-repeated-tasks-c7fb44d21a4b-20260613T005032005174+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0070cdeede09

## What looked useful

Semantic retrieval was perfect when full natural-language discriminators were present, but collapsed toward chance on anchor-only and underspecified repeat queries as near-duplicate cluster size increased. Exact-anchor lookup remained 1.0 top-1 whenever the anchor was present.

## Boundaries and scale limits

Synthetic data only; TF-IDF semantic baseline only; no LLM agent, learned embedding retriever, production memory system, or real task corpus was tested. Main run was 40 families, cluster sizes 2/5/10/20/40, 8 seeds, and 1,600 maximum memory rows per condition.

## Claim scope

In a synthetic repeated-task retrieval benchmark with explicit stable anchors and dense near-duplicate task clusters, exact-anchor lookup and exact-then-semantic hybrid retrieval avoid semantic nearest-neighbor collision errors for identity-style repeat requests.

## Why it stopped

The result is a bounded synthetic retrieval probe, not full validation of LLM agent memory behavior or production semantic-memory systems.

## Recommended next action

Stop this run as a no-paper useful signal; next run should replay realistic repeated-task logs with modern embedding retrieval plus exact-anchor and hybrid baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic repeated-task replay with embedding semantic memory versus exact anchors
- Success threshold: Hybrid retrieval improves top-1 success by at least 20 percentage points over embedding-only semantic retrieval on identity-style repeat requests, while staying within 5 percentage points of semantic retrieval on fully specified repeat requests.
- Stop condition: Stop if modern embedding or reranked semantic retrieval matches hybrid within 5 percentage points on identity-style repeat requests across all near-duplicate cluster sizes, or if anchors are not preserved reliably enough to support exact lookup.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-retrieval-vs-semantic-memory-on-repeated-tasks-c7fb44d21a4b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Memory-Architecture Semantic Compression Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-architecture-semantic-compression-test-dd77e12e9ea9`
Run ID: `memory-architecture-semantic-compression-test-dd77e12e9ea9-20260613T062159904822+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4bf95f7e8bbc

## What looked useful

Semantic compression reached 12/12 accuracy with a 0.106 answer-state compression ratio; transcript search and flat retrieval each reached 2/12 because stale first mentions defeated current-fact queries.

## Boundaries and scale limits

Synthetic corpus only; deterministic regex extraction and exact-match scoring; no live LLM memory writer/reader, embeddings, natural production logs, or broad task distribution.

## Claim scope

On a 12-task deterministic synthetic replay corpus, a layered latest-fact semantic-compression memory state preserved current facts under aliases, conflicts, and noise better than no-memory, transcript-search, and flat first-match retrieval baselines while reducing answer-state words from 385 to 41.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism but is not direct/full validation for a paper.

## Recommended next action

Stop this run as no-paper useful proxy evidence; deepen with a medium real-agent replay harness over at least hundreds of human-authored or logged tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Real-Agent Semantic Compression Memory Replay
- Success threshold: Semantic compression improves current-fact accuracy by at least 15 percentage points over both baselines while using at most 35% of transcript tokens, with non-overlapping bootstrap confidence intervals.
- Stop condition: Stop if semantic compression fails to beat the best baseline by at least 5 percentage points after the first 100 tasks or if memory-writing failures dominate more than 25% of cases.

## Evidence references

- Artifact root: `<local-path>/projects/memory-architecture-semantic-compression-test-dd77e12e9ea9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

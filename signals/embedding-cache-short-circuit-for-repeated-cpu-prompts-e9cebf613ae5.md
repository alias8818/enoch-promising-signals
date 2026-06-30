# Embedding-cache short-circuit for repeated CPU prompts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `embedding-cache-short-circuit-for-repeated-cpu-prompts-e9cebf613ae5`
Run ID: `embedding-cache-short-circuit-for-repeated-cpu-prompts-e9cebf613ae5-20260611T091741876122+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7c9d6f5d0952

## What looked useful

Corrected main benchmark showed 7.2x-29.2x mean speedups at 0.90-0.99 hit rates, 0.93x-0.95x slowdowns for all-unique prompts, and only 1.01x speedup when a small cache reduced observed hits to 0.064.

## Boundaries and scale limits

Evidence is local CPU-only and proxy-based: no real transformer embedding model, no production traffic trace, no multi-process cache contention, no distributed cache, and no end-to-end serving integration were tested.

## Claim scope

In a deterministic CPU embedding proxy, exact-key prompt embedding caching provides large latency reductions for repeated prompt streams with high cache hit rates, but adds overhead for all-unique streams and provides little benefit when cache capacity thrashes.

## Why it stopped

No-paper useful signal: proxy evidence supports the cache mechanism and boundary conditions, but direct production/model evidence is missing.

## Recommended next action

Run a bounded real-model follow-up using a small CPU sentence embedding model and trace-shaped prompt distributions; stop treating this proxy result as sufficient for a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU embedding model validation for exact repeated-prompt cache short-circuiting
- Success threshold: At least 3x mean latency improvement at observed hit rate >= 0.80 with identical embeddings on cache hits, plus <= 10% overhead in all-unique controls.
- Stop condition: Stop if real-model cached runs fail correctness checks, show < 1.5x speedup at hit rate >= 0.80, or impose > 25% overhead on all-unique prompts.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-cache-short-circuit-for-repeated-cpu-prompts-e9cebf613ae5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

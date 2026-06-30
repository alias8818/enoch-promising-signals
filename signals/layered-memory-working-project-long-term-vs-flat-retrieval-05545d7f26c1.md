# Layered Memory: Working/Project/Long-Term vs Flat Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layered-memory-working-project-long-term-vs-flat-retrieval-05545d7f26c1`
Run ID: `layered-memory-working-project-long-term-vs-flat-retrieval-05545d7f26c1-20260621T074031475776+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/37227f7a15f9

## What looked useful

Fixed working/project/long-term tiering reduced dot products by 89.04% versus exhaustive flat search and slightly improved recall versus exhaustive search in the medium run, but lost to an equal-budget flat recency baseline by 9.0 recall@5 points. Perfect router hints still trailed flat recency by about 8.1 points, so tier labels alone were not enough.

## Boundaries and scale limits

Not tested on real LLM agent memory traces, production embeddings, writes/promotions/evictions, or strong ANN flat indexes. The layered method used a fixed heuristic budget allocation and noisy scope hints, not a learned router or optimized index.

## Claim scope

Synthetic retrieval benchmark with 37,376 normalized vectors across working, project, and long-term tiers; active-context query distribution; recall@5, dot-count, and latency comparison of flat exact, flat recent budgeted, and fixed-allocation layered budgeted retrieval.

## Why it stopped

Proxy synthetic early falsification: the naive fixed-budget layered policy did not beat the strongest equal-budget flat baseline, so the scoped hypothesis is not ready for paper writing.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should evaluate adaptive tier budget allocation plus a stronger long-term ANN baseline against flat recency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Tier Budgeting for Layered Memory Retrieval
- Success threshold: At the same mean candidate budget as flat recency, adaptive layered retrieval improves total recall@5 by at least 5 percentage points while preserving at least 95% of flat recency working-tier recall and recovering at least 10% long-term recall.
- Stop condition: Stop if adaptive layered retrieval fails to beat flat recency total recall@5 by at least 2 percentage points across three seeds or if working-tier recall falls below 95% of flat recency.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-working-project-long-term-vs-flat-retrieval-05545d7f26c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

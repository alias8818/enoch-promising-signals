# Layered Memory vs Flat Retrieval on Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-vs-flat-retrieval-on-repeated-agent-tasks-70931faa820d`
Run ID: `layered-memory-vs-flat-retrieval-on-repeated-agent-tasks-70931faa820d-20260619T031742160535+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/02d6a3a11c2b

## What looked useful

Layered latest-summary memory achieved 100% accuracy at top-k 1 with 16 mean context tokens, while flat BM25 over all events achieved 36.6% accuracy at top-k 1 with 42 tokens and needed top-k 10 / about 420 tokens to reach 99.8% accuracy, while still carrying stale conflicting values in about 71.6% of queries.

## Boundaries and scale limits

Synthetic data only; 3 medium seeds; 1,800 update events and 610 queries per seed; deterministic answerer; BM25 retrieval; no LLM agent, embedding retriever, noisy summarizer, real user traces, or end-to-end task success measurement.

## Claim scope

In a deterministic synthetic repeated-agent-task retrieval benchmark with time-aware memory snapshots, a layered latest-summary memory retrieved current entity-slot facts with less context and no stale conflicts compared with flat BM25 over all historical event notes.

## Why it stopped

Closed as no-paper useful signal: the result is a synthetic/proxy mechanism test, not direct publication-grade validation of repeated agent task performance.

## Recommended next action

Run a bounded follow-up with a real LLM answerer and embedding retrieval on semi-real repeated agent workflows, measuring task success, context tokens, stale-conflict sensitivity, and consolidation-error failures.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layered Memory Under LLM Answering on Repeated Agent Workflows
- Success threshold: Layered memory improves task success by at least 5 percentage points or reduces context tokens by at least 30% at matched task success, with no more than a 2 percentage point increase in consolidation-caused failures.
- Stop condition: Stop if layered memory fails to beat flat retrieval on either task success or context-token cost across at least two seeds/task subsets, or if consolidation errors dominate the observed gains.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-vs-flat-retrieval-on-repeated-agent-tasks-70931faa820d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

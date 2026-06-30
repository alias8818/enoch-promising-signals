# Layered Memory Architecture vs Flat Retrieval on Repeated Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layered-memory-architecture-vs-flat-retrieval-on-repeated-tasks-7d71144ee55e`
Run ID: `layered-memory-architecture-vs-flat-retrieval-on-repeated-tasks-7d71144ee55e-20260620T213411972654+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/737af98364f9

## What looked useful

Layered memory's main supported advantage is retrieval-work reduction for current-state repeated tasks. Accuracy improvement is not robust to a simple recency-aware flat baseline.

## Boundaries and scale limits

Synthetic symbolic data only; no embeddings, no LLM answer generation, no learned or lossy summarization, no realistic natural-language task distribution, and no long-running model/agent workload.

## Claim scope

On a deterministic synthetic repeated task-key-value benchmark, layered per-task summaries matched a recency-aware flat retriever's accuracy while reducing retrieval work from about 6358-6362 scored chunks per query to 1 scored summary entry; layered memory also avoided the 23-26% stale-answer rate of a tie-naive flat retriever.

## Why it stopped

No paper-ready result: this is a CPU-only synthetic proxy with a useful efficiency signal, and the accuracy advantage disappears against a recency-aware flat baseline.

## Recommended next action

Run a bounded follow-up with realistic repeated tasks, vector retrieval plus recency/reranking baselines, and imperfect LLM-generated summaries before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layered summaries vs vector retrieval with recency on realistic repeated tasks
- Success threshold: Layered memory achieves at least 98% of the best flat baseline accuracy while reducing retrieved context tokens or scored candidates by at least 5x, with summary-induced error below 2%.
- Stop condition: Stop if layered summary errors exceed 5% or if vector+recency flat retrieval matches both accuracy and retrieval/context cost within 20%.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-architecture-vs-flat-retrieval-on-repeated-tasks-7d71144ee55e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

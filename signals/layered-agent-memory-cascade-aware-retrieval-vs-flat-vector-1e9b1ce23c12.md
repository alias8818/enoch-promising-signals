# Layered Agent Memory: Cascade-Aware Retrieval vs Flat Vector

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-cascade-aware-retrieval-vs-flat-vector-1e9b1ce23c12`
Run ID: `layered-agent-memory-cascade-aware-retrieval-vs-flat-vector-1e9b1ce23c12-20260610T211358190247+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7322411afbae

## What looked useful

Across three medium seeds with 48,000 memories and 4,500 queries per seed, layered_cascade reached mean recall@5 0.5713 vs flat_cosine 0.0235 and MRR@5 0.3617 vs 0.0118, while using 37.5 vs 48,000 mean dot products per query.

## Boundaries and scale limits

Synthetic embeddings and oracle-like query type/layer metadata only; no real LLM agent traces, production embedding model, memory write/update errors, summarization drift, or downstream task accuracy were tested.

## Claim scope

On a reproducible synthetic long-horizon agent-memory benchmark with recent, episodic, and semantic retrieval regimes, a metadata-aware layered cascade substantially improved recall@5 and MRR@5 while using far fewer dot products than exhaustive flat cosine retrieval.

## Why it stopped

Closed as no-paper useful signal because the result is synthetic/proxy evidence despite stable medium-scale local support for the mechanism.

## Recommended next action

Run a bounded direct-evidence follow-up on real or semi-real agent memory traces using a production embedding model, comparing flat cosine, metadata-aware flat reranking, and layered cascade on retrieval and downstream QA accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Based Cascade-Aware Agent Memory Retrieval
- Success threshold: Layered cascade improves downstream QA accuracy by >=10 percentage points over flat cosine, uses >=10x fewer vector comparisons than exhaustive metadata-aware flat reranking, and does not lose more than 2 percentage points QA accuracy versus that metadata-aware reranking control.
- Stop condition: Stop if metadata-aware flat reranking matches or beats layered cascade at similar compute, or if cascade gains disappear on trace-derived queries across two independent seeds/datasets.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-cascade-aware-retrieval-vs-flat-vector-1e9b1ce23c12`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

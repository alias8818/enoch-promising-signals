# Real-corpus doctrine memory vs embedding RAG on superseded and exception rules

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-doctrine-memory-vs-embedding-rag-on-superseded-aa2e13b3c8`
Run ID: `real-corpus-doctrine-memory-vs-embedding-rag-on-superseded-aa2e13b3c8-20260621T021933268089+0000`

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

- Parent run decision: Operator-doctrine memory vs flat vector retrieval: enoch://control-plane/projects/operator-doctrine-memory-vs-flat-vector-retrieval-fc0e4875df62/runs/operator-doctrine-memory-vs-flat-vector-retrieval-fc0e4875df62-20260621T015827126028+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/736bfc6bce23

## What looked useful

Plain embedding retrieval reached 0.60 top-1 accuracy and ranked forbidden stale/exception documents first on 0.40 of queries. Doctrine-memory reranking reached 1.00 top-1 accuracy and 0.00 forbidden top-1 rate on the same chunks.

## Boundaries and scale limits

Small hand-authored query set; manually encoded doctrine status and exception metadata; no end-to-end answer generation; no independent/blinded annotation; limited distractor pressure from only 71 focused chunks.

## Claim scope

On a 10-source public legal corpus with 10 targeted supersession/exception queries, explicit doctrine-memory reranking corrected all observed top-1 embedding retrieval failures caused by overruled or exception-specific doctrine chunks.

## Why it stopped

Tier 1 direct small test produced useful mechanism support, but not publication-grade breadth or independence.

## Recommended next action

Run a held-out 50-100 query real-corpus benchmark with independently authored questions, automatic query-intent inference, and ablations for status-only and exception-only memory before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out doctrine-memory benchmark with inferred intent and ablations
- Success threshold: Full doctrine memory improves top-1 accuracy by at least 15 percentage points over embedding RAG and cuts forbidden top-1 retrieval rate by at least 50% without reducing exception-query accuracy.
- Stop condition: Stop if full doctrine memory fails to beat the best ablation by at least 5 percentage points top-1 accuracy or if inferred query intent is below 80% accurate on held-out queries.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-doctrine-memory-vs-embedding-rag-on-superseded-aa2e13b3c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

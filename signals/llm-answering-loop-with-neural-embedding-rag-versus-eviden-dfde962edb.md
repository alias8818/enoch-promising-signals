# LLM answering loop with neural embedding RAG versus evidence ledger on noisy repeated state tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-answering-loop-with-neural-embedding-rag-versus-eviden-dfde962edb`
Run ID: `llm-answering-loop-with-neural-embedding-rag-versus-eviden-dfde962edb-20260630T172304089488+0000`

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

- Parent run decision: Evidence-Ledger Agent Memory vs No-Memory and Flat-RAG on Repeated Multi-Step Tasks: enoch://control-plane/projects/evidence-ledger-agent-memory-vs-no-memory-and-flat-rag-on-repeated-multi-step-tasks-37906bc16765/runs/evidence-ledger-agent-memory-vs-no-memory-and-flat-rag-on-repeated-multi-step-tasks-37906bc16765-20260630T160914924721+0000
- Parent run decision: LLM-agent evidence-ledger memory vs embedding RAG on noisy repeated stateful tasks: enoch://control-plane/projects/llm-agent-evidence-ledger-memory-vs-embedding-rag-on-noisy-b313f9430d/runs/llm-agent-evidence-ledger-memory-vs-embedding-rag-on-noisy-b313f9430d-20260630T164103216731+0000

## What looked useful

Small-k neural embedding RAG degraded from 0.911 mean accuracy at 120 events to 0.328 at 2400 events for k=3, and from 0.995 to 0.643 for k=10. The evidence ledger stayed at 1.000 across all lengths. RAG k=50 reached 0.994 at 2400 events, and recency-weighted k=50 reached 1.000, showing the failure is retrieval design and temporal-state handling rather than semantic embeddings being categorically unusable.

## Boundaries and scale limits

Tested only synthetic schema-regular traces up to 2400 events, 5 seeds per length, 2995 queries per method, MiniLM embeddings, and deterministic parser-based answering. No generative LLM answerer, natural document corpus, learned reranker, hybrid search, or production RAG controls were evaluated.

## Claim scope

On a deterministic synthetic repeated-state benchmark with parseable authoritative updates, fixed small-k MiniLM embedding RAG often fails to retrieve the latest evidence as trace length grows, while an explicit evidence ledger remains exact. Larger retrieval breadth plus recency weighting can recover on this benchmark.

## Why it stopped

Synthetic retrieval-proxy evidence is useful but not direct publication-grade validation of an LLM answering loop.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same traces with a real LLM answerer and controlled RAG variants including metadata filtering, temporal reranking, and hybrid retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM answerer and temporal RAG controls on repeated-state memory traces
- Success threshold: Ledger or temporal-state retrieval beats plain embedding RAG k=10 by at least 10 absolute accuracy points at 1200+ events while using no more context tokens, and retrieval recall explains at least 80% of answer errors.
- Stop condition: Stop if plain embedding RAG with a real LLM is already within 2 accuracy points of ledger across 1200+ and 2400 event traces, or if LLM generation errors dominate retrieval errors so the memory mechanism cannot be isolated.

## Evidence references

- Artifact root: `<local-path>/projects/llm-answering-loop-with-neural-embedding-rag-versus-eviden-dfde962edb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

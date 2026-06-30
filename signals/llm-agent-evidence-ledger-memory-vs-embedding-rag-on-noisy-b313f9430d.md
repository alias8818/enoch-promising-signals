# LLM-agent evidence-ledger memory vs embedding RAG on noisy repeated stateful tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-agent-evidence-ledger-memory-vs-embedding-rag-on-noisy-b313f9430d`
Run ID: `llm-agent-evidence-ledger-memory-vs-embedding-rag-on-noisy-b313f9430d-20260630T164103216731+0000`

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

- Parent run decision: Evidence-Ledger Agent Memory vs No-Memory and Flat-RAG on Repeated Multi-Step Tasks: enoch://control-plane/projects/evidence-ledger-agent-memory-vs-no-memory-and-flat-rag-on-repeated-multi-step-tasks-37906bc16765/runs/evidence-ledger-agent-memory-vs-no-memory-and-flat-rag-on-repeated-multi-step-tasks-37906bc16765-20260630T160914924721+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e261507cbe2

## What looked useful

Across 40,000 confirmation queries, the ledger achieved 100% accuracy in every noise condition. Retrieval policies ranged from 12.6% to 74.82% accuracy, with severe degradation when stale restatements and irrelevant mentions were both present. The mechanism signal is that semantic similarity and retrieved chunk recency do not reliably encode current state under contradictory repeated memory.

## Boundaries and scale limits

Synthetic account-state traces only; lexical cosine retriever rather than neural embeddings; deterministic heuristic answer extraction rather than a full LLM-agent loop; one seed and one top-k setting for the confirmation grid; CPU-only local run with 40 entities, 500 updates/trial, 250 trials per noise condition, and 8 noise conditions.

## Claim scope

On a local synthetic repeated-state benchmark with stale restatements and irrelevant high-overlap noise, a typed evidence-ledger memory recovered current state exactly while lexical embedding-style retrieval over text chunks failed frequently under the same traces.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is proxy-only for embedding RAG and LLM-agent behavior, so it is not a full validation or paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; next run should replace lexical retrieval with a real embedding index and an actual LLM answering loop on the same benchmark scaffold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM answering loop with neural embedding RAG versus evidence ledger on noisy repeated state tasks
- Success threshold: Ledger-backed answering beats neural embedding RAG by at least 20 absolute accuracy points on high-noise conditions while keeping stale-answer rate below 5%.
- Stop condition: Stop if neural embedding RAG plus reasonable top-k/prompt tuning matches ledger accuracy within 5 absolute points on high-noise conditions or if no local LLM/embedding stack can run reproducibly.

## Evidence references

- Artifact root: `<local-path>/projects/llm-agent-evidence-ledger-memory-vs-embedding-rag-on-noisy-b313f9430d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

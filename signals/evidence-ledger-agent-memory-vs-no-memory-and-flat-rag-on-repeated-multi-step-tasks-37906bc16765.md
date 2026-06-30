# Evidence-Ledger Agent Memory vs No-Memory and Flat-RAG on Repeated Multi-Step Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-memory-vs-no-memory-and-flat-rag-on-repeated-multi-step-tasks-37906bc16765`
Run ID: `evidence-ledger-agent-memory-vs-no-memory-and-flat-rag-on-repeated-multi-step-tasks-37906bc16765-20260630T160914924721+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e261507cbe2

## What looked useful

The run produced reproducible evidence that ledger-style structured latest-fact memory can reduce stale-slot errors and context size versus small-window flat RAG on repeated multi-step stateful tasks. Flat RAG can recover when the retrieval window is large enough, making the result a context-efficiency signal rather than proof that RAG cannot solve the task.

## Boundaries and scale limits

Synthetic CPU-only benchmark; no LLM agent, embedding RAG, noisy extraction, real task corpus, latency/cost service stack, or human evaluation was tested.

## Claim scope

In a deterministic synthetic repeated-task benchmark where decisions require the newest values of four entity slots, a structured evidence ledger matched oracle accuracy with about 45 retrieved tokens per task, while flat lexical RAG needed a much larger retrieval window to match accuracy and used 126-548 mean retrieved tokens depending on distractor rate.

## Why it stopped

Useful synthetic mechanism evidence but not direct publication-grade validation of LLM-agent memory behavior.

## Recommended next action

Stop this run as no-paper synthetic evidence; next run should test the same task family with actual LLM agents, noisy evidence extraction, and an embedding RAG baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-agent evidence-ledger memory vs embedding RAG on noisy repeated stateful tasks
- Success threshold: Evidence ledger achieves at least 95% of the best baseline accuracy while reducing stale-fact errors by at least 30% or prompt/retrieved tokens by at least 50% versus tuned embedding RAG on the same tasks.
- Stop condition: Stop if ledger extraction errors erase the stale-fact advantage or if tuned embedding RAG matches accuracy and stale-fact rate within 5% while using no more than 1.5x ledger prompt tokens.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-memory-vs-no-memory-and-flat-rag-on-repeated-multi-step-tasks-37906bc16765`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Agent Memory Architecture: Layered Memory vs. Retrieval Baseline

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-architecture-layered-memory-vs-retrieval-baseline-6c711cc38d11`
Run ID: `agent-memory-architecture-layered-memory-vs-retrieval-baseline-6c711cc38d11-20260630T175512785723+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f63d6ff79a1f

## What looked useful

Retrieval-only memory was perfect without distractors but fell to 25.7%-66.9% accuracy with distractors at top-k=8, while layered memory stayed at 100% with 2 context items/query. A top-k=32 stress check still left retrieval at 25.1%-40.8% accuracy on high-distractor settings.

## Boundaries and scale limits

Synthetic CPU-only benchmark; no LLM extraction/generation, no embedding retriever or reranker, no production traces, no human evaluation, no model training, and no privacy or write-error modeling.

## Claim scope

On deterministic synthetic current-fact memory streams with typed updates and stale same-entity distractors, a layered current-state memory plus episodic summaries outperformed a lexical retrieval-only top-k baseline under constrained context.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic and proxy-only; it supports the stale-history mechanism but not a full agent-memory architecture validation.

## Recommended next action

Run a bounded deepen follow-up with an embedding/reranking retrieval baseline, temporal filtering, and an LLM reader/writer on the same synthetic task before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layered memory versus embedding-reranked retrieval with LLM read/write errors
- Success threshold: Layered memory beats the strongest retrieval baseline by at least 10 percentage points accuracy at equal or lower context budget on high-distractor settings, while write errors remain below 5%.
- Stop condition: Stop if embedding/reranked retrieval with temporal filtering reaches within 5 percentage points of layered accuracy at comparable context budget, or if layered write errors exceed the observed retrieval advantage.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-architecture-layered-memory-vs-retrieval-baseline-6c711cc38d11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

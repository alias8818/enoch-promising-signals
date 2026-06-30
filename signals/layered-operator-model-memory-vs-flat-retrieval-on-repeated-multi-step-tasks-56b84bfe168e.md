# Layered Operator-Model Memory vs Flat Retrieval on Repeated Multi-Step Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-operator-model-memory-vs-flat-retrieval-on-repeated-multi-step-tasks-56b84bfe168e`
Run ID: `layered-operator-model-memory-vs-flat-retrieval-on-repeated-multi-step-tasks-56b84bfe168e-20260619T044852423232+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5b7f316d89e1

## What looked useful

Layered doctrine memory reached 1.000 exact match on the main 216-task synthetic replay, while flat retrieval reached 0.366 exact match and 0.738 mean layer accuracy. Sensitivity variants preserved a layered advantage of +0.396 to +0.667 exact match.

## Boundaries and scale limits

Local CPU-only synthetic proxy: 216 main tasks plus three 96-task sensitivity variants. No LLM agent, real operator trace, embedding retriever, learned reranker, human evaluation, or production memory-write validation was tested.

## Claim scope

In a deterministic synthetic replay benchmark of repeated multi-step tasks, typed layered operator/model/task memory with explicit current/stale conflict handling outperformed untyped flat lexical retrieval at recovering current operator doctrine, current model/runtime constraints, and stable task facts.

## Why it stopped

Synthetic proxy supports the mechanism but is not direct publication-grade evidence for live agent memory systems.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same typed-memory mechanism on real or LLM-generated traces with embedding/reranking flat-retrieval controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Based Layered Memory vs Tuned Flat Retrieval
- Success threshold: Layered memory beats the strongest flat baseline by at least 0.15 exact-match rate and 0.08 mean layer accuracy with no worse than 0.05 regression on stable task facts.
- Stop condition: Stop if tuned flat retrieval closes the exact-match gap below 0.05 or if label extraction for typed/current memories cannot be reproduced without oracle simulator fields.

## Evidence references

- Artifact root: `<local-path>/projects/layered-operator-model-memory-vs-flat-retrieval-on-repeated-multi-step-tasks-56b84bfe168e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

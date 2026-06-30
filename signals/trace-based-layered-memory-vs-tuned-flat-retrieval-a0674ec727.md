# Trace-Based Layered Memory vs Tuned Flat Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-based-layered-memory-vs-tuned-flat-retrieval-a0674ec727`
Run ID: `trace-based-layered-memory-vs-tuned-flat-retrieval-a0674ec727-20260619T051458956538+0000`

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

- Parent run decision: Layered Operator-Model Memory vs Flat Retrieval on Repeated Multi-Step Tasks: enoch://control-plane/projects/layered-operator-model-memory-vs-flat-retrieval-on-repeated-multi-step-tasks-56b84bfe168e/runs/layered-operator-model-memory-vs-flat-retrieval-on-repeated-multi-step-tasks-56b84bfe168e-20260619T044852423232+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5b7f316d89e1

## What looked useful

Layered memory avoided stale-first-session and noisy-retrospective retrieval failures that persisted for tuned flat retrieval even at 800 tokens. This supports the update-resolution and compaction mechanism but not publication readiness.

## Boundaries and scale limits

Synthetic traces only; 24 scenarios, 620 events, 168 queries, 126 held-out queries; no real operator corpus, dense retrieval, reranking, imperfect extraction, or LLM answer generation tested.

## Claim scope

In a deterministic synthetic repeated-session trace benchmark with perfect structured extraction and oracle evidence-based answering, trace-based layered current-fact memory outperformed a tuned BM25-style flat retriever by 29.5 to 52.3 accuracy points across 80 to 800 token context budgets.

## Why it stopped

Tier 1 direct synthetic validation produced useful mechanism support, but the result is no-paper because corpus realism, extraction robustness, LLM answering, and stronger flat baselines remain untested.

## Recommended next action

Run a bounded deepen test with imperfect extraction and a dense or reranked flat baseline on real or benchmark repeated-agent traces before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Imperfect-extraction layered memory vs dense reranked flat retrieval on repeated-agent traces
- Success threshold: At least +10 percentage points held-out answer accuracy for layered memory over the tuned dense/reranked flat baseline at two or more matched context budgets, with bootstrap 95% confidence intervals excluding zero and extraction F1 at or above 0.85.
- Stop condition: Stop if dense/reranked flat retrieval matches layered memory within 5 percentage points at all budgets, or if extraction F1 falls below 0.75 and failures are dominated by extraction rather than retrieval/update resolution.

## Evidence references

- Artifact root: `<local-path>/projects/trace-based-layered-memory-vs-tuned-flat-retrieval-a0674ec727`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

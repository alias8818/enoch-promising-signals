# Agent memory compression: semantic vs retrieval-only on repeated tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-memory-compression-semantic-vs-retrieval-only-on-repeated-tasks-c5332271aec4`
Run ID: `agent-memory-compression-semantic-vs-retrieval-only-on-repeated-tasks-c5332271aec4-20260611T003839864107+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d8ae7b0184f5

## What looked useful

Semantic compression is conditionally useful rather than universally better: it improves stable repeated-task recall at intermediate budgets, but whole-summary eviction hurts tight budgets and majority summaries lag after preference drift.

## Boundaries and scale limits

No real LLM agent, no learned embeddings, no non-oracle semantic extraction, no real user/project traces, and no long-horizon deployment. The result is a local proxy for memory representation behavior, not a full validation of agent memory systems.

## Claim scope

Synthetic repeated-task memory benchmark with oracle fact extraction, fixed character budgets, 40 seeds, 160 entities, stable and late-drift preference regimes. Semantic summaries beat retrieval-only at intermediate budgets but lose at very tight budgets and under drift when retrieval can retain recent raw episodes.

## Why it stopped

Proxy-only synthetic evidence gives a useful no-paper signal but is not publication-grade evidence about real LLM agents.

## Recommended next action

Run a bounded LLM-in-the-loop follow-up with real memory extraction and embedding retrieval on repeated coding/task traces, preserving the stable-vs-drift and memory-budget grid.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop repeated-task memory compression benchmark
- Success threshold: Across at least 20 seeds or trace folds, semantic memory improves stable intermediate-budget held-out success by at least 10 percentage points over embedding retrieval while losing no more than 5 percentage points on drift after adding recency/conflict handling.
- Stop condition: Stop if semantic extraction errors remove the stable-budget advantage or if embedding retrieval matches semantic memory across stable and drift regimes under equal budgets.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-compression-semantic-vs-retrieval-only-on-repeated-tasks-c5332271aec4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

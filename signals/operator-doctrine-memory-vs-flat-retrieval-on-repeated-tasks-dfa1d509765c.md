# Operator-Doctrine Memory vs Flat Retrieval on Repeated Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-dfa1d509765c`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-dfa1d509765c-20260629T012802002978+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ed5246c3b5cb

## What looked useful

Across 50 seeds and 6751 scored queries, layered_doctrine_memory reached 1.000 accuracy versus flat_retrieval at 0.609; paired-seed layered-minus-flat mean was 0.3905 with 95% interval 0.378871 to 0.402129. The largest flat retrieval failures were query_after_exception and query_after_stale_note contamination.

## Boundaries and scale limits

Synthetic only; no live LLM agent, embedding index, private operator trace, production workflow, or long-horizon deployment was tested. The layered method is advantaged by access to generated event-type labels.

## Claim scope

In a deterministic synthetic repeated-task replay with explicit event-type semantics, layered operator-doctrine memory preserved durable doctrine across corrections, stale notes, and one-time exceptions better than recency-weighted flat retrieval.

## Why it stopped

Local synthetic mechanism test completed; evidence is useful but not paper-positive because it does not test live agents or real replay traces.

## Recommended next action

Run a bounded deepen follow-up where event types must be inferred from ambiguous natural-language transcripts by an LLM or parser before doctrine memory is updated.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language doctrine memory replay with inferred update semantics
- Success threshold: Layered doctrine memory improves accuracy over flat retrieval by at least 10 percentage points overall and at least 20 percentage points on exception/stale-note query slices across at least 20 seeds or an equivalent fixed replay set.
- Stop condition: Stop if semantic inference accuracy is below 80% on update type labels or if layered doctrine memory fails to beat flat retrieval by 5 percentage points overall.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-dfa1d509765c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

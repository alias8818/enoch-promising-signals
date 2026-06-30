# Agent memory compression with semantic retrieval vs flat vector baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-memory-compression-with-semantic-retrieval-vs-flat-vector-baseline-b25c4e81726a`
Run ID: `agent-memory-compression-with-semantic-retrieval-vs-flat-vector-baseline-b25c4e81726a-20260619T065541492341+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/698232ea40db

## What looked useful

Compression is useful when queries require several facts from the same semantic unit and the retrieval budget cannot hold enough individual memories. The benefit is budget-dependent and can vanish when flat retrieval has enough context. Low-dimensional hashing is unsafe for high-cardinality memory identifiers.

## Boundaries and scale limits

Synthetic corpus only; no learned embeddings, no LLM reader, no real agent traces, no online update/contradiction handling. Medium run used 75,000 memories, 5,000 summaries, and 2,000 queries on one CPU process.

## Claim scope

In a synthetic persistent-memory retrieval task with exact sparse TF-IDF, entity-level compressed summaries outperformed flat individual-memory retrieval for multi-fact profile queries at tight 32- and 48-token context budgets, while flat retrieval matched or nearly matched compressed retrieval for point queries and at a 96-token budget.

## Why it stopped

Synthetic proxy evidence supports a bounded mechanism but is not direct/full validation of agent memory compression.

## Recommended next action

Stop this run as no-paper useful signal; next run should replay the same comparison on realistic agent memory traces with learned embeddings and an LLM answer evaluator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic trace evaluation of compressed semantic memory retrieval
- Success threshold: At 32- and 48-token-equivalent budgets, compressed retrieval improves multi-fact answer accuracy by at least 20 percentage points over flat retrieval while point-query accuracy remains within 3 percentage points of the flat baseline.
- Stop condition: Stop if learned-summary compression loses more than 5% of required facts before retrieval or if flat retrieval matches compressed retrieval within 5 percentage points across tight budgets.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-compression-with-semantic-retrieval-vs-flat-vector-baseline-b25c4e81726a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

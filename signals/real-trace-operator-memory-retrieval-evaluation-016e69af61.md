# Real-Trace Operator Memory Retrieval Evaluation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `68`
Project ID: `real-trace-operator-memory-retrieval-evaluation-016e69af61`
Run ID: `real-trace-operator-memory-retrieval-evaluation-016e69af61-20260629T185208155349+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Operator-Trace Memory Compression vs Flat Retrieval: enoch://control-plane/projects/operator-trace-memory-compression-vs-flat-retrieval-18ab5f998d61/runs/operator-trace-memory-compression-vs-flat-retrieval-18ab5f998d61-20260629T182146791775+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d384553fe35e

## What looked useful

On the available real trace, BM25 achieved 0.933 hit@1 and 1.000 hit@3 for evidence lookup, but only 0.062 hit@1 and 0.188 hit@3 for intent-to-command retrieval. Lexical methods beat recency overall but fail the action-intent retrieval task.

## Boundaries and scale limits

Only one trace, trace-derived labels, no human gold labels, no independent operator sessions, no semantic retriever, and no cross-project validation. The run is a smoke/feasibility evaluation, not a broad memory retrieval validation.

## Claim scope

Single local real Codex worker trace from this project: 27 usable trace records, 16 command memories, and 31 deterministic retrieval tasks. Lexical retrieval recovered command/output evidence well but did not recover intent-to-command action memories.

## Why it stopped

Useful small real-trace signal produced, but evidence is weak and below the declared medium-confidence floor; this is not full validation or paper-grade evidence.

## Recommended next action

Run a bounded deepen evaluation on at least 5 independent real operator traces with at least 100 human- or policy-labeled retrieval tasks, comparing lexical, semantic, and hybrid retrievers by task type.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Trace Operator Memory Retrieval Benchmark
- Success threshold: Hybrid or semantic retrieval improves intent/action hit@1 by at least 20 percentage points over BM25 and recency, with evidence-lookup hit@1 remaining at or above 0.85.
- Stop condition: Stop if fewer than 100 labeled real-trace tasks can be assembled or if semantic/hybrid retrieval fails to beat BM25 by at least 10 percentage points on intent/action hit@1.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-operator-memory-retrieval-evaluation-016e69af61`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

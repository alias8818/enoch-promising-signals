# Direct Trace Doctrine Memory vs Reranked Flat Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-trace-doctrine-memory-vs-reranked-flat-retrieval-f4fb26d64d`
Run ID: `direct-trace-doctrine-memory-vs-reranked-flat-retrieval-f4fb26d64d-20260630T034314249898+0000`

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

- Parent run decision: Operator-Doctrine Memory Beats Flat Vector Retrieval on Repeated Multi-Turn Tasks: enoch://control-plane/projects/operator-doctrine-memory-beats-flat-vector-retrieval-on-repeated-multi-turn-tasks-7b99d40be8c8/runs/operator-doctrine-memory-beats-flat-vector-retrieval-on-repeated-multi-turn-tasks-7b99d40be8c8-20260629T152901995504+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65a9515b260a

## What looked useful

Direct trace doctrine memory reached 300/300 accuracy on the primary run versus 263/300 for flat reranked retrieval and 268/300 for a recency/correction-biased flat variant. With 30 distractors it stayed 300/300 while flat retrieval fell to 251/300.

## Boundaries and scale limits

300-task synthetic primary run plus one 300-task higher-distractor stress probe; no real operator traces, no LLM generation, no embedding or cross-encoder reranker, no production persistence layer.

## Claim scope

In a deterministic synthetic replay benchmark with explicit doctrine correction events and stale lexical distractors, direct trace doctrine memory recovered the current doctrine more reliably than BM25-like flat reranked retrieval.

## Why it stopped

Synthetic mechanism evidence is useful but not publication-grade or broad enough for a paper; this run should close as no-paper evidence.

## Recommended next action

Run a bounded real-trace replay benchmark with annotated current doctrine and a stronger embedding or cross-encoder reranked flat baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace doctrine replay against strong reranked flat retrieval
- Success threshold: Direct trace doctrine memory improves current-doctrine recovery by at least 5 percentage points over the strongest flat baseline with non-overlapping or materially shifted bootstrap confidence intervals and no larger privacy/omission failure rate.
- Stop condition: Stop if direct trace doctrine memory fails to beat the strongest flat baseline by 5 percentage points, if labels cannot be produced without private data exposure, or if most wins vanish under embedding/cross-encoder reranking.

## Evidence references

- Artifact root: `<local-path>/projects/direct-trace-doctrine-memory-vs-reranked-flat-retrieval-f4fb26d64d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

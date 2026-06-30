# Compact trace index inside real LLM memory summarization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compact-trace-index-inside-real-llm-memory-summarization-3bb709e09d`
Run ID: `compact-trace-index-inside-real-llm-memory-summarization-3bb709e09d-20260528T192713576761+0000`

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

- Parent run decision: Exact Anchor Retrieval for Compressed Agent Memory: enoch://control-plane/projects/exact-anchor-retrieval-for-compressed-agent-memory-e480a1d6afcc/runs/exact-anchor-retrieval-for-compressed-agent-memory-e480a1d6afcc-20260528T004413366451+0000
- Parent run decision: Trace-based exact-anchor retrieval under LLM memory compression: enoch://control-plane/projects/trace-based-exact-anchor-retrieval-under-llm-memory-compre-9f8b03f13b/runs/trace-based-exact-anchor-retrieval-under-llm-memory-compre-9f8b03f13b-20260528T150020990709+0000

## What looked useful

Trace indexing is useful for preserving low-salience details in readable/source-aware memory summaries, but the advantage is small versus summary-only and mixed versus compact key-value memory. At 2048 bytes trace_index reached 0.422 exact QA accuracy versus 0.415 summary_only, 0.018 recency, 0.430 kv_index, 0.007 random-trace ablation, and 0.000 no-value ablation.

## Boundaries and scale limits

No runnable LLM stack or API credentials were available, so this is a representation-level benchmark rather than end-to-end real LLM summarization/generation. Conversations are synthetic; no real user-memory corpus or production episodic retrieval stack was tested. The trace index does not reliably beat a simpler key-value baseline at larger budgets.

## Claim scope

In a fixed-seed synthetic long-conversation memory benchmark, a compact value-bearing trace index inside a budgeted memory object improves exact fact answerability over verbose summary-only and recency baselines under 768-2048 byte budgets, with ablations showing the value-bearing trace entries are necessary.

## Why it stopped

Tier 2 representation-level evidence supports the mechanism but not publication readiness: the test proxies real LLM summarization, and the compact trace index is not consistently superior to the key-value baseline.

## Recommended next action

Stop as no-paper useful signal; the only worthwhile deepen test is an end-to-end local/API LLM memory-summarization evaluation comparing generated QA accuracy, hallucination rate, and source attribution against summary-only, key-value, and episodic retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end LLM QA with compact trace-index memory summaries
- Success threshold: Trace_index improves generated exact QA accuracy by at least 5 absolute percentage points over summary_only, does not trail kv_index or episodic retrieval by more than 2 points, and reduces unsupported hallucinated answers versus summary_only under at least three of four budgets.
- Stop condition: Stop if trace_index fails to beat summary_only by 2 absolute points on generated exact QA or has a higher unsupported hallucination rate in two consecutive budgets/seeds batches.

## Evidence references

- Artifact root: `<local-path>/projects/compact-trace-index-inside-real-llm-memory-summarization-3bb709e09d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

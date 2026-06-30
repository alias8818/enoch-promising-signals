# Agent memory cascade: cheap vector to semantic-compress to LLM-load on repeated tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-cascade-cheap-vector-to-semantic-compress-to-llm-load-on-repeated-tasks-a3e52774e0d1`
Run ID: `agent-memory-cascade-cheap-vector-to-semantic-compress-to-llm-load-on-repeated-tasks-a3e52774e0d1-20260621T164212200409+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/02abaca87fa0

## What looked useful

Across five seeds, cascade_budget reached 85.05% task success and 95.74% mean required-fact recall at about 641 tokens, versus vector_budget at 0.60% success and 24.99% recall at about 626 tokens. A 4x-budget vector-only control reached 40.25% success and 78.13% recall at about 2,579 tokens.

## Boundaries and scale limits

Synthetic corpus only; compression used structured fact extraction rather than unstructured real-log summarization; no actual LLM/agent answer-quality evaluation; no stale/conflicting memory stress test; no production vector database or embedding retrieval.

## Claim scope

In a deterministic synthetic repeated-task memory benchmark with 80 projects, 1,440 memory chunks, 480 atomic facts, and 400 tasks per run, a cheap lexical retrieval plus structured semantic compression cascade loaded substantially more required task facts into a 650-token final context than raw vector chunks.

## Why it stopped

No-paper useful signal: the local synthetic benchmark supports the mechanism, but the result is proxy-only and lacks real traces, non-oracle compression, and actual LLM task-success evidence.

## Recommended next action

Run a bounded real-trace evaluation using noisy agent memory logs, a non-oracle compressor, and downstream LLM answer grading before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace validation of cheap-retrieval semantic-compression agent memory cascade
- Success threshold: At the same final context budget, cascade improves required-fact inclusion or LLM answer accuracy by at least 20 absolute percentage points over raw vector retrieval, with no more than 10% relative increase in retrieval/compression latency versus vector-only plus summarization overhead acceptable for agent use.
- Stop condition: Stop if non-oracle compression fails to beat raw vector retrieval by at least 10 absolute percentage points on required-fact inclusion in a 100-task real/replayed trace sample, or if compression introduces stale/conflicting facts often enough to reduce downstream answer accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-cascade-cheap-vector-to-semantic-compress-to-llm-load-on-repeated-tasks-a3e52774e0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

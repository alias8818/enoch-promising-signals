# Anchor-Pinned Compressed Memory vs Full-Transcript Retrieval for Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-pinned-compressed-memory-vs-full-transcript-retrieval-for-repeated-agent-tasks-815669f50ee6`
Run ID: `anchor-pinned-compressed-memory-vs-full-transcript-retrieval-for-repeated-agent-tasks-815669f50ee6-20260630T151034569660+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e261507cbe2

## What looked useful

At a 220-token budget over 500 generated episodes, anchor-pinned compressed memory achieved 1.00 correct and 1.00 anchor recall, while full-transcript BM25 retrieval and recent compressed memory achieved 0.00 correct because they retained the task fact but missed the durable anchor. A budget sweep showed baselines recovered only at a 700-token budget.

## Boundaries and scale limits

Synthetic transcripts only; no real agent traces, semantic/vector retrieval, learned summarization, or downstream LLM answer evaluation. The result supports a mechanism, not broad deployed-agent performance.

## Claim scope

In a deterministic synthetic repeated-task benchmark with early durable anchors, later task facts, distractors, and a fixed context budget, anchor-pinned compressed memory preserved required information at budgets where BM25-style full-transcript retrieval and recency-only compressed memory dropped the anchor.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal but not direct real-agent or publication-grade evidence.

## Recommended next action

Run a bounded trace-replay follow-up with realistic repeated-agent transcripts and LLM answer scoring against BM25, vector retrieval, learned summarization, recent memory, and anchor-pinned memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace replay validation of anchor-pinned memory for repeated agent tasks
- Success threshold: Anchor-pinned memory reduces anchor-violation rate by at least 30% relative to the best retrieval or summarization baseline at equal context budget, without reducing task-fact recall by more than 5%.
- Stop condition: Stop if anchor-pinned memory does not beat the best baseline on anchor-violation rate in two independently generated or collected trace sets, or if gains disappear once vector retrieval and LLM summarization baselines are included.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-pinned-compressed-memory-vs-full-transcript-retrieval-for-repeated-agent-tasks-815669f50e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

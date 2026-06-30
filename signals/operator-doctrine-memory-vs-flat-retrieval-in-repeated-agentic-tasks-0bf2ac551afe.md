# Operator-doctrine memory vs flat retrieval in repeated agentic tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-in-repeated-agentic-tasks-0bf2ac551afe`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-in-repeated-agentic-tasks-0bf2ac551afe-20260610T233631898018+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/603d8d89d296

## What looked useful

Doctrine abstraction appears useful after enough repeated feedback exists, especially when transcript noise makes flat retrieval context-expensive. The same mechanism is brittle at very small history sizes where rules are under-supported.

## Boundaries and scale limits

Synthetic deterministic task/action benchmark only; no real LLM agent, no real operator traces, no embedding retriever, no tool-use tasks, no doctrine drift, and no external organizational corpus. Runtime was a 91 second CPU-only local sweep.

## Claim scope

In a synthetic repeated-task benchmark with stable feature-conditioned operator preferences, compact doctrine memory beat the best flat episodic retrieval baseline by 4.0 to 10.0 accuracy points once history reached 120 to 1000 examples, while using 11.5x to 723.9x fewer context tokens. At 40 examples doctrine memory underperformed flat retrieval by 1.8 to 5.3 points.

## Why it stopped

Closed as no-paper useful signal because the positive mechanism is supported only by a synthetic proxy benchmark, not by direct real-agent task success evidence.

## Recommended next action

Run a bounded direct LLM-agent evaluation on curated repeated tasks with natural operator corrections, comparing summarized doctrine memory against vector flat retrieval under matched context budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM-agent doctrine memory benchmark on curated repeated tasks
- Success threshold: Doctrine memory improves held-out task success by at least 5 percentage points over best flat retrieval at equal or lower context cost for histories of 100+ episodes, without losing more than 2 points at 40 episodes.
- Stop condition: Stop if doctrine memory fails to beat best flat retrieval by 3 percentage points at 100+ histories or if gains disappear when feedback is natural-language rather than structured labels.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-in-repeated-agentic-tasks-0bf2ac551afe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

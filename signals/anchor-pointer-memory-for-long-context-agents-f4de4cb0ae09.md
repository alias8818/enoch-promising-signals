# Anchor-Pointer Memory for Long-Context Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-pointer-memory-for-long-context-agents-f4de4cb0ae09`
Run ID: `anchor-pointer-memory-for-long-context-agents-f4de4cb0ae09-20260610T064159071631+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/40ad4bcae45f

## What looked useful

Anchor-pointer memory had 0.537 mean source-grounded accuracy overall versus 0.390 for recency, 0.197 for periodic anchors, and 0.182 for reservoir, and reached 0.953 source-grounded accuracy at a 2,048-unit budget. However, compact summaries without source pointers reached 0.648 value accuracy overall and dominated anchor-pointer for value-only retrieval.

## Boundaries and scale limits

Synthetic CPU-only benchmark; exact entity keys; no trained LLM agent, natural-language aliasing, vector retrieval baseline, multi-hop reasoning, or full context-window integration. Maximum stream length was 50,000 generated events with 2,000 entities and 12 seeds per condition.

## Claim scope

In a synthetic exact-key long event-stream memory task, anchor-pointer memory improves source-grounded latest-fact retrieval over event-only recency, reservoir, and periodic-anchor baselines at moderate budgets, but does not beat a compact per-entity summary baseline for value-only queries.

## Why it stopped

Closed as no-paper useful signal because the experiment is a proxy benchmark and the mechanism is mixed: useful for source-grounded exact-key retrieval, not superior for value-only memory.

## Recommended next action

Run a bounded deepen follow-up with natural-language observations and a compact summary-plus-source-id baseline; do not write a paper from this proxy result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language source-grounded anchor-pointer memory against summary-plus-source baselines
- Success threshold: At matched memory budget, anchor-pointer must improve joint answer-and-source accuracy by at least 10 percentage points over the best non-anchor baseline on 3 or more seeds without worse than 20 percent latency overhead.
- Stop condition: Stop if summary-plus-source-id matches anchor-pointer within 3 percentage points joint accuracy or if alias/entity-link failures dominate more than half of anchor-pointer errors.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-pointer-memory-for-long-context-agents-f4de4cb0ae09`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

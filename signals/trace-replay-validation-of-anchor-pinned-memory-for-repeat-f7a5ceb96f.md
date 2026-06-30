# Trace replay validation of anchor-pinned memory for repeated agent tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-replay-validation-of-anchor-pinned-memory-for-repeat-f7a5ceb96f`
Run ID: `trace-replay-validation-of-anchor-pinned-memory-for-repeat-f7a5ceb96f-20260630T153203436590+0000`

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

- Parent run decision: Anchor-Pinned Compressed Memory vs Full-Transcript Retrieval for Repeated Agent Tasks: enoch://control-plane/projects/anchor-pinned-compressed-memory-vs-full-transcript-retrieval-for-repeated-agent-tasks-815669f50ee6/runs/anchor-pinned-compressed-memory-vs-full-transcript-retrieval-for-repeated-agent-tasks-815669f50ee6-20260630T151034569660+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e261507cbe2

## What looked useful

Anchor pinning is useful only with revision/invalidation semantics. In 5,000 stable synthetic episodes, revision-aware pinned memory reached 1.000 task success versus 0.0102 for recency and 0.4662 for lossy summary. In 5,000 revision episodes, revision-aware pinned memory stayed at 1.000, while naive no-revision pinning fell to 0.1002 with 1.7476 stale-anchor errors per episode.

## Boundaries and scale limits

No real LLM agent was run. Anchor extraction, semantic ambiguity, production trace diversity, multi-session behavior, and latency/cost in an actual agent framework were not tested. The result is a bounded proxy, not publication-grade validation.

## Claim scope

Synthetic trace replay with four task-critical anchors, controlled distractors, fixed token-like memory budgets, and optional explicit anchor revisions. Revision-aware anchor-pinned memory preserved all current anchors in these generated traces, while recency and lossy summaries frequently dropped anchors.

## Why it stopped

Proxy/synthetic replay produced a useful mechanism signal and a stale-anchor failure mode, but it is not direct real-agent validation.

## Recommended next action

Run a bounded LLM-in-the-loop trace replay where anchors are extracted from natural-language agent logs and must be revised or invalidated correctly before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop validation of revision-aware anchor-pinned memory
- Success threshold: Revision-aware pinned memory improves task success by at least 20 percentage points over the best baseline while keeping stale-anchor errors below 1% and retained-token cost within 1.5x of the matched recency budget.
- Stop condition: Stop if extraction F1 is below 0.80, stale-anchor errors exceed 5%, or task-success lift over the best baseline is below 5 percentage points on at least 200 labeled replay episodes.

## Evidence references

- Artifact root: `<local-path>/projects/trace-replay-validation-of-anchor-pinned-memory-for-repeat-f7a5ceb96f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

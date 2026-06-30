# Semantic Compression Memory on Real Agent Task Reuse Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `semantic-compression-memory-on-real-agent-task-reuse-trace-5fe88edad7`
Run ID: `semantic-compression-memory-on-real-agent-task-reuse-trace-5fe88edad7-20260612T213510390091+0000`

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

- Parent run decision: Semantic compression memory store vs flat vector retrieval for small agent task reuse: enoch://control-plane/projects/semantic-compression-memory-store-vs-flat-vector-retrieval-for-small-agent-task-reuse-c3750752a5fe/runs/semantic-compression-memory-store-vs-flat-vector-retrieval-for-small-agent-task-reuse-c3750752a5fe-20260612T210901664344+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5ed6553a91ed

## What looked useful

Semantic compression retained reusable command intent under tight character budgets: 1.000 vs raw 0.667 at 80 chars/event, tie at 120 chars/event, and 1.000 vs raw 0.889 at 200 chars/event; recency remained strong at 0.889 across budgets.

## Boundaries and scale limits

Single trace, 14 command events, 9 held-out reuse queries per budget, heuristic action labels, retrieval-only outcome, no downstream agent task success measurement.

## Claim scope

On one local real Codex/Enoch command trace, semantic compressed memories improved top-1 same-action retrieval over raw equal-budget, recency, and random baselines on two of three tight memory budgets.

## Why it stopped

Tier 1 direct trace retrieval test met the useful-signal threshold, but evidence is too small and retrieval-only for paper readiness.

## Recommended next action

Run a bounded deepen follow-up across multiple real agent traces with downstream task-reuse success, not just same-action retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-trace downstream validation of semantic compressed memory for agent task reuse
- Success threshold: Semantic compressed memory improves downstream held-out task success by at least 10% relative over the best non-semantic baseline, or reduces time-to-solution by at least 15%, across at least 5 traces without increasing failure rate.
- Stop condition: Stop as negative if semantic compression fails to beat the best non-semantic baseline on downstream outcomes in at least 4 of 5 traces or if gains disappear after controlling for recency.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-compression-memory-on-real-agent-task-reuse-trace-5fe88edad7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

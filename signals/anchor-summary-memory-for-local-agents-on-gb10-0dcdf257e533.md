# Anchor+Summary Memory for local agents on gb10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-summary-memory-for-local-agents-on-gb10-0dcdf257e533`
Run ID: `anchor-summary-memory-for-local-agents-on-gb10-0dcdf257e533-20260613T164112050795+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e4c4acd0bf0

## What looked useful

Main benchmark over 220 turns, 36 facts, 60 trials: anchor_summary recall was 1.000 at 250/500/900 token budgets, versus summary_only 0.320/0.363/0.440 and recent_window 0.104/0.229/0.432. Capacity sweep over 360 turns, 96 facts, 30 trials showed anchor_summary 0.500 recall at 250 tokens but 1.000 at 500 and 900 tokens.

## Boundaries and scale limits

No LLM-in-the-loop summarization, no real agent traces, no task completion measurement, no long-running GB10 model workload, and no validation beyond synthetic exact-recall queries. Anchor recall degrades when the anchor store cannot fit all facts, demonstrated by 50% recall at 96 facts and a 250-token budget.

## Claim scope

In a deterministic synthetic local-agent memory benchmark, explicit compact key/value anchors plus a rolling summary preserved exact operational facts better than recent-window and summary-only compaction at equal memory budgets when the anchor set fit in the allocated budget.

## Why it stopped

This run produced a synthetic mechanism signal but not direct real-agent or LLM-in-the-loop evidence, so it is no-paper useful evidence rather than a positive result.

## Recommended next action

Run a bounded deepen follow-up using replayed local-agent traces or small LLM-generated summaries, with task-level exact-fact recovery and anchor eviction policies measured against summary-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor+Summary Memory on Replayed Local-Agent Traces
- Success threshold: Anchor+summary improves exact-fact recovery by at least 20 percentage points over summary-only at equal token budget on replayed traces, with no more than 5% relative regression on non-anchor task context queries.
- Stop condition: Stop if anchor+summary fails to beat summary-only by 10 percentage points on exact-fact recovery in the first 100 annotated trace queries, or if annotation/replay data cannot be produced locally.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-summary-memory-for-local-agents-on-gb10-0dcdf257e533`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

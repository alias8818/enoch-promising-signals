# Exact-Anchor Compressed Memory for Multi-Session Agent Runs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-compressed-memory-for-multi-session-agent-runs-e2c85b033684`
Run ID: `exact-anchor-compressed-memory-for-multi-session-agent-runs-e2c85b033684-20260613T182327483522+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d4d69433c599

## What looked useful

Across 50 seeds with 24 sessions and 96 exact-anchor queries per run, exact-anchor memory reached 1.0 recall at 8%, 12%, and 20% memory budgets and 0.7508 recall at 5%; the best baseline ranged from 0.0596 to 0.8302 recall depending on budget.

## Boundaries and scale limits

Synthetic traces only; no LLM-in-the-loop summarization, extraction mistakes, answer generation, real agent logs, concurrency, or production token/latency accounting. The method degrades when anchors alone exceed the memory budget.

## Claim scope

On deterministic synthetic multi-session traces with regex-extractable exact anchors, exact-anchor compressed memory preserved byte-exact anchor recall better than recent truncation, lossy summaries, and session-local keyword windows at equal character budgets.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic mechanism test, not direct multi-session agent validation.

## Recommended next action

Run a bounded LLM-in-the-loop follow-up using realistic multi-session agent traces, real summarization, anchor extraction, and exact answer scoring before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop exact-anchor memory on realistic multi-session agent traces
- Success threshold: At equal token budget, exact-anchor memory improves exact-match answer accuracy by at least 15 percentage points over the best baseline while retaining at least 90% anchor extraction precision on the evaluated traces.
- Stop condition: Stop if automatic anchor extraction precision falls below 80%, if exact-answer accuracy is within 5 percentage points of the best baseline, or if anchor storage consumes the budget before preserving necessary context on most traces.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-compressed-memory-for-multi-session-agent-runs-e2c85b033684`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

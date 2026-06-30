# Anchor-preserving compressed state for long-horizon agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-preserving-compressed-state-for-long-horizon-agents-710df5b169be`
Run ID: `anchor-preserving-compressed-state-for-long-horizon-agents-710df5b169be-20260613T113952079396+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3e5761862387

## What looked useful

Anchor preservation is useful under moderate compression budgets but has a measurable tight-budget overhead failure mode: at 256 tokens it underperformed latest-fact-only summary across all tested horizons because anchor definitions crowded out fact records.

## Boundaries and scale limits

Synthetic event streams only; no LLM semantic extraction, no real tool-use trajectories, no downstream agent task success, one CPU process, 80 seeds per cell, horizons up to 16000 events, budgets up to 1024 synthetic tokens.

## Claim scope

In a synthetic long-horizon state-compression benchmark with parseable anchor-bound facts, explicit anchor preservation plus latest-fact retention improves final-state query accuracy over recent-window and reservoir compression at all tested horizons/budgets, and over latest-fact-only compression when the budget is sufficient for both anchors and facts.

## Why it stopped

Synthetic evidence supports the mechanism only within a proxy benchmark and exposes a tight-budget failure mode; this is not direct publication-grade validation of long-horizon agents.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate adaptive anchor budgeting on generated LLM-agent trajectories with downstream task success.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive anchor budgeting on LLM-agent trajectory summaries
- Success threshold: At 256 and 512 token budgets, adaptive anchor budgeting must match or exceed latest-fact-only accuracy while retaining at least 90 percent of the fixed anchor-preserving advantage over recent-window at horizons of 8000 events or longer.
- Stop condition: Stop if adaptive anchor budgeting still trails latest-fact-only by more than 2 accuracy points at 256 tokens or if downstream task success does not improve over latest-fact-only at any tested budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserving-compressed-state-for-long-horizon-agents-710df5b169be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Operator-doctrine memory: layered semantic compression for home agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operator-doctrine-memory-layered-semantic-compression-for-home-agents-50d5ee397d57`
Run ID: `operator-doctrine-memory-layered-semantic-compression-for-home-agents-50d5ee397d57-20260613T183032115893+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d25e02f83924

## What looked useful

Layered semantic compression should not be assumed superior to flat current-fact summaries under equal token budgets. The observed value is a safety-biased tradeoff: higher hazard recall at 80 and 120 token budgets, but lower preference and routine recall.

## Boundaries and scale limits

Synthetic retrieval-only traces; no real home-agent logs, no LLM summarizer, no embodied planner, no privacy/persistence stress test, and no multi-user operator-doctrine conflicts.

## Claim scope

On a deterministic synthetic home-agent memory retrieval benchmark with 50 seeds, 120 update episodes per seed, and 80-260 token budgets, a layered quota memory is better than recent-only truncation but does not outperform a flat current-fact summary on aggregate recall; it only improves hazard recall at tight budgets.

## Why it stopped

Early synthetic mechanism probe produced a mixed/no-paper result: layered memory failed to beat the relevant flat-summary baseline on aggregate retrieval, although it produced a measurable hazard-recall tradeoff worth one bounded follow-up.

## Recommended next action

Run a bounded risk-weighted planning benchmark where hazard misses carry higher cost than preference/routine misses; stop if layered memory does not reduce weighted action risk by at least 10% versus flat summaries at equal token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Risk-weighted evaluation of layered home-agent memory
- Success threshold: Layered memory reduces weighted action-risk score by at least 10% versus flat summary at 80 and 120 token budgets without reducing aggregate retrieval hit rate by more than 10 percentage points.
- Stop condition: Stop as negative if layered memory fails the weighted-risk threshold on 50 seeds or if its aggregate recall penalty exceeds 10 percentage points at both tight budgets.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-layered-semantic-compression-for-home-agents-50d5ee397d57`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

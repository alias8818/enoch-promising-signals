# Compressed anchor-pointer state for long-horizon home agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-anchor-pointer-state-for-long-horizon-home-agents-7d779ab667e3`
Run ID: `compressed-anchor-pointer-state-for-long-horizon-home-agents-7d779ab667e3-20260610T005621886351+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43b997fa0ab8

## What looked useful

Across 432 paired comparisons per baseline, anchor-pointer memory beat recency by +0.359 mean accuracy (95% CI +0.333 to +0.385) and lossy summary by +0.256 (95% CI +0.237 to +0.275), but trailed full trace by -0.510 while using far fewer prompt-state tokens.

## Boundaries and scale limits

The evidence is synthetic and oracle-evaluated. It does not include embodied perception, navigation, action failures, LLM prompt behavior, learned policy adaptation, realistic household benchmarks, or strong graph/vector/episodic memory baselines.

## Claim scope

In a deterministic synthetic home-memory benchmark, compact object-location anchors with raw-event pointers improve delayed object-location recall over recency-only and fixed-budget lossy-summary memories at comparable prompt-state token budgets.

## Why it stopped

No-paper useful signal: the mechanism is supported by synthetic recall evidence, but the original long-horizon home-agent claim needs direct planner or embodied-task evidence.

## Recommended next action

Stop paper escalation for this run; run a bounded deepen test where an actual text/simulator household planner must use anchor-pointer memory during task execution.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-pointer memory inside a bounded household planner benchmark
- Success threshold: Anchor-pointer improves task completion by at least 10 percentage points over both compressed baselines with non-overlapping bootstrap 95% confidence intervals, while using no more prompt-state tokens than the fixed budget.
- Stop condition: Stop if anchor-pointer fails to beat either compressed baseline by 5 percentage points after 20 seeds, or if gains only appear when the benchmark gives oracle information unavailable to the planner.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-anchor-pointer-state-for-long-horizon-home-agents-7d779ab667e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

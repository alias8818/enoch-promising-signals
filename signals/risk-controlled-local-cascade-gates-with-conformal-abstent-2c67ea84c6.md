# Risk-controlled local cascade gates with conformal abstention

Status: `useful_signal`
Project ID: `risk-controlled-local-cascade-gates-with-conformal-abstent-2c67ea84c6`
Run ID: `risk-controlled-local-cascade-gates-with-conformal-abstent-2c67ea84c6-20260518T163842762474+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Risk-controlled local cascade gates with conformal abstention: internal_generated:risk-controlled-local-cascade-gates-with-conformal-abstent-2c67ea84c6

## What looked useful

Local gates often lowered average selective risk but usually did so by sharply reducing coverage or increasing cost. Empirical-only local gates recovered coverage on the hard heterogeneous stress case but violated the target risk in 96-100% of seeds, showing the mechanism needs stronger pooled or shrinkage calibration before it is paper-ready.

## Boundaries and scale limits

This run used small-to-medium sklearn datasets and split-calibration selective-risk bounds, not large production traces, LLM cascades, or a full conformal prediction-set theorem for adaptive local gating.

## Claim scope

In a bounded sklearn validation over 4 tabular/image datasets, 50 fixed seeds, alpha in {0.05, 0.10}, and cheap/expert classifier cascades, naive independently calibrated local Clopper-Pearson selective-risk gates did not consistently improve practical coverage/cost over a global calibrated cascade.

## Why it stopped

Bounded direct metrics produced a useful negative/mixed result: naive local conformal cascade gates were either over-conservative or lost target-risk control, so the current mechanism is not paper-positive.

## Recommended next action

Run at most one final depth-4 deepen test of hierarchical or shrinkage local risk bounds against the same global CP cascade and empirical ablation; otherwise stop this line as no-paper evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hierarchical shrinkage local cascade gates for selective-risk control
- Success threshold: At alpha=0.10 on synthetic_heterogeneous and at least one real dataset, improve mean coverage by at least 10 percentage points or reduce normalized cost by at least 0.05 versus global CP while keeping violation_rate <= global CP + 0.02 and mean_risk <= alpha.
- Stop condition: Stop if hierarchical/shrinkage local gates still lose more than 5 percentage points of coverage versus global CP or exceed global CP violation_rate by more than 0.02 on the hard stress case.

## Evidence references

- Artifact root: `<local-path>/projects/risk-controlled-local-cascade-gates-with-conformal-abstent-2c67ea84c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

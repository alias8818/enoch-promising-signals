# Real-Data Training-Dynamics Difficulty Selection Check

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-data-training-dynamics-difficulty-selection-check-b3bda4802a`
Run ID: `real-data-training-dynamics-difficulty-selection-check-b3bda4802a-20260522T040635842370+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Training-Dynamics Scoring for Difficulty-Based Data Selection: enoch://control-plane/projects/training-dynamics-scoring-for-difficulty-based-data-selection-4c11de50b342/runs/training-dynamics-scoring-for-difficulty-based-data-selection-4c11de50b342-20260521T212138960486+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a7551cd5ba5c

## What looked useful

TD-middle beat random only clearly at the 20% subset budget (+1.77 pp, 5/5 seed wins), but not at 10% (+0.10 pp) or 40% (+0.25 pp), and it failed to beat the best static baseline by 1 pp at any budget (-1.13, +0.22, -0.23 pp versus static_mid). TD-hard and static-hard both concentrated injected label noise and collapsed, while TD and static hardness were highly correlated (mean r=0.974), suggesting little added value from dynamics in this setup.

## Boundaries and scale limits

Single real tabular dataset; injected random train-label noise rather than natural annotation noise; small MLPs; 5 seeds; short warmup; no text/vision coverage, no large-model pretraining, and no long-horizon dynamics.

## Claim scope

In a Tier 1 real-data Covertype classification test with 15% injected train-label noise, clean held-out labels, 5 seeds, and equal-budget downstream MLP retraining, TD-middle selection did not satisfy the parent threshold of beating random and the strongest static final-loss/confidence baseline by at least 1 percentage point.

## Why it stopped

Direct Tier 1 real-data follow-up failed the stated success threshold: TD-middle did not beat the strongest static baseline by at least 1 percentage point and was unstable across subset budgets.

## Recommended next action

Stop this follow-up as a no-paper useful signal; any next bounded test should specifically target datasets or scoring features where trajectory dynamics are decorrelated from static final loss/confidence.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Trajectory-Only Difficulty Signal Versus Static Loss on Real Data
- Success threshold: Trajectory-only or trajectory-dominant selection beats the strongest static baseline by at least 1 percentage point mean clean-test accuracy at one or more subset budgets, wins at least 4/5 seeds, and has TD-static correlation below 0.8.
- Stop condition: Stop if TD-static correlation remains above 0.9 on candidate real datasets or if trajectory-only selection fails to beat the strongest static baseline by at least 0.5 percentage points on average.

## Evidence references

- Artifact root: `<local-path>/projects/real-data-training-dynamics-difficulty-selection-check-b3bda4802a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

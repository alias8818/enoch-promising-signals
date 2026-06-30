# Reputation-Weighted Aggregation Against Sybil Volunteers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `reputation-weighted-aggregation-against-sybil-volunteers-9d751dbc7ab2`
Run ID: `reputation-weighted-aggregation-against-sybil-volunteers-9d751dbc7ab2-20260628T012525074156+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f232d869c4a5

## What looked useful

Consensus-derived reputation weighting mostly behaved like the plain mean at attack magnitude 2, with 0 wins versus the best baseline across 24 aggregate conditions. At attack magnitude 8, it had 0 wins, 9 neutral conditions, and 15 losses versus the best non-reputation baseline; at 30% direct-bias Sybils, coordinate median RMSE was 0.1359 while reputation RMSE was 0.2972. Majority-Sybil cases assigned high Sybil weight share after burn-in: mean 0.705/max 0.798 at magnitude 2 and mean 0.709/max 0.847 at magnitude 8.

## Boundaries and scale limits

No real volunteer traces, real ML gradients, identity churn, stake/identity-cost model, or fully adaptive adversary were tested. The result does not rule out all reputation-weighted aggregation designs; it rejects this simple consensus-derived reputation mechanism as a standalone Sybil defense in the tested synthetic setting.

## Claim scope

Synthetic IID vector-update aggregation with 101 volunteers, 64-dimensional updates, 120 rounds, 8 seeds per condition, Sybil fractions from 0.0 to 0.7, and coordinated bias attacks at magnitudes 2 and 8. The tested reputation method updates per-identity reputation from agreement with a leave-one-out coordinate-median reference and uses softmax reputation weights for aggregation.

## Why it stopped

Early synthetic falsification: the concrete reputation-weighted aggregation mechanism tested here did not outperform ordinary baselines and can give coordinated Sybils high aggregate weight. This is not a full real-world validation.

## Recommended next action

Stop this mechanism as no-paper evidence; a bounded follow-up should test influence-capped or identity-cost-aware reputation against adaptive minority Sybil attacks before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Influence-Capped Reputation Aggregation Under Adaptive Minority Sybils
- Success threshold: At least 20% lower mean RMSE than the best non-reputation baseline in 75% or more minority-Sybil attack conditions, no more than 5% worse than mean at 0% Sybil, and observed Sybil weight share below population share after burn-in for Sybil fractions up to 0.4.
- Stop condition: Stop as negative if the best tuned influence-capped reputation variant fails to beat the best baseline by 10% in at least half of minority-Sybil conditions or has more than 5% clean-setting RMSE regression.

## Evidence references

- Artifact root: `<local-path>/projects/reputation-weighted-aggregation-against-sybil-volunteers-9d751dbc7ab2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Norm-Bound Commitment for Outlier Rejection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `norm-bound-commitment-for-outlier-rejection-780d039c62b7`
Run ID: `norm-bound-commitment-for-outlier-rejection-780d039c62b7-20260607T213053943141+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/74578bf9a95b

## What looked useful

Precommitted L2 norm rejection reliably removed gross radial outliers but rejected 0% of norm-bounded directional outliers and matched plain-mean error in those attacks; norm commitment alone is therefore insufficient as general outlier rejection.

## Boundaries and scale limits

No real model gradients, no federated protocol implementation, no cryptographic commitment overhead, no non-Gaussian production data, and no multi-round adaptive attacker beyond fixed in-ball directional outliers.

## Claim scope

Synthetic robust mean-estimation probe with 64-dimensional Gaussian inliers, 256 vectors per batch, 5-20% contamination, and an L2 radius committed from clean calibration data.

## Why it stopped

Proxy statistical test supports only a narrow radial-outlier benefit and early-falsifies norm-bound commitment as a standalone general outlier rejection rule.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test norm commitment combined with a directional robust aggregator on synthetic gradient-like updates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Norm commitment plus directional robust aggregation for in-ball attackers
- Success threshold: At 10% and 20% in-ball directional contamination, the combined method must reduce mean L2 error by at least 40% versus norm-only filtering while preserving at least 95% radial outlier rejection.
- Stop condition: Stop if the combined method fails to improve norm-only filtering by 20% on in-ball directional contamination in two independent seeds or if it rejects more than 5% of clean inliers under the committed bound.

## Evidence references

- Artifact root: `<local-path>/projects/norm-bound-commitment-for-outlier-rejection-780d039c62b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

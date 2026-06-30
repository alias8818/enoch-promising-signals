# Learned Residual Scaling for 1-Bit Weight Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `learned-residual-scaling-for-1-bit-weight-training-b145fd1e722f`
Run ID: `learned-residual-scaling-for-1-bit-weight-training-b145fd1e722f-20260603T185846753174+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5bb884061b8a

## What looked useful

Residual scaling drove soft residual-forward validation MSE near zero, but removing the residual path for hard 1-bit inference made validation MSE 86.3% worse than scale-only by median paired relative change.

## Boundaries and scale limits

CPU-only NumPy experiment; 8 seeds; linear regression only; no transformer, language modeling, convolutional, or large-scale validation.

## Claim scope

In a small synthetic teacher-student linear regression probe, learned residual-forward scaling did not improve deployable hard 1-bit weights over a learned scale-only straight-through baseline.

## Why it stopped

Early proxy falsification: the tested learned residual-forward variant appears to rely on dense residual capacity rather than improving the deployable 1-bit model.

## Recommended next action

Stop this variant as a paper direction unless a bounded follow-up constrains or anneals the residual path and demonstrates hard 1-bit gains after residual removal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Annealed or backward-only residual scaling for hard 1-bit transfer
- Success threshold: At least 10% median paired improvement in hard 1-bit validation metric over scale-only, with residual-removed inference matching the reported metric.
- Stop condition: Stop if the hard 1-bit metric is not improved after residual removal or if the method only improves soft residual-forward evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/learned-residual-scaling-for-1-bit-weight-training-b145fd1e722f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

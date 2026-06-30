# Cross-Verification Redundancy Protocol for Volunteer Gradient Integrity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-verification-redundancy-protocol-for-volunteer-gradient-integrity-6a957bd9279a`
Run ID: `cross-verification-redundancy-protocol-for-volunteer-gradient-integrity-6a957bd9279a-20260525T030741444094+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/32a0ed3309c6

## What looked useful

Cross-verification adds explicit malicious-gradient detection and preserves clean-level accuracy for Gaussian corruption through 40% and sign-flip corruption through 20% with redundancy 5, but collapses under stronger coherent sign-flip attacks due to local malicious majorities.

## Boundaries and scale limits

Not validated on real volunteer infrastructure, heterogeneous devices, privacy-preserving data assignment, nondeterministic kernels, stale gradients, large models, or colluding/adaptive adversaries. Sign-flip results show standalone per-batch verification fails at 30-40% coherent corruption.

## Claim scope

Small synthetic logistic-regression volunteer-gradient simulation with deterministic same-batch redundant gradients, redundancy 3 or 5, and controlled sign-flip or Gaussian malicious submissions.

## Why it stopped

No-paper useful signal: the proxy experiment supports the detection mechanism in limited regimes but directly falsifies standalone robustness under coherent 30-40% sign-flip corruption.

## Recommended next action

Do not write a paper from this run; run a bounded deepen follow-up that combines same-batch cross-verification with global robust aggregation or reputation to remove the local-majority failure mode.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Cross-Verification plus Global Robust Aggregation for Volunteer Gradient Integrity
- Success threshold: Hybrid protocol maintains at least 95% of clean-reference accuracy and at least 0.85 malicious-gradient recall at 30% coherent sign-flip corruption across 5 seeds, without more than 10% honest false rejects.
- Stop condition: Stop if the hybrid still collapses below 70% of clean-reference accuracy at 30% coherent sign-flip corruption or if false rejects exceed 20% under honest jitter.

## Evidence references

- Artifact root: `<local-path>/projects/cross-verification-redundancy-protocol-for-volunteer-gradient-integrity-6a957bd9279a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

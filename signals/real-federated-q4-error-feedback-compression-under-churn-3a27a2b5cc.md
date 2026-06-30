# Real federated q4 error-feedback compression under churn

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-federated-q4-error-feedback-compression-under-churn-3a27a2b5cc`
Run ID: `real-federated-q4-error-feedback-compression-under-churn-3a27a2b5cc-20260610T140657386804+0000`

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

- Parent run decision: 4-bit gradient compression for volunteer training: enoch://control-plane/projects/4-bit-gradient-compression-for-volunteer-training-714787c8e376/runs/4-bit-gradient-compression-for-volunteer-training-714787c8e376-20260610T092731836762+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/486752b231db

## What looked useful

Across a 5-seed main run and a harsher churn sensitivity, q4_ef stayed within 0.24 percentage points of fp32 accuracy and preserved a 86.88% payload reduction, but its accuracy gain versus q4_noef was -0.016 percentage points in the main run and -0.144 percentage points in stress, failing the preset >=5 percentage point error-feedback advantage threshold.

## Boundaries and scale limits

Synthetic data and a convex linear model only; no public real federated dataset, nonconvex CNN/transformer, production network behavior, secure aggregation, delayed updates, privacy accounting, or long-horizon/datacenter-scale training was tested.

## Claim scope

In a controlled small federated softmax-classification simulation with 40 non-IID clients, Markov client churn, online-only sampling, q4 per-tensor update compression, and persistent per-client residuals, q4 compression matched fp32 FedAvg within the preset parity thresholds but q4 error feedback did not improve accuracy over q4 without error feedback.

## Why it stopped

Controlled direct Tier 1 tests falsified the q4 error-feedback advantage threshold in this small setting rather than merely failing to run; this is not a full real-world validation.

## Recommended next action

Stop this run as a no-paper useful signal; the bounded next test is a public nonconvex federated benchmark with the same fp32, q4_noef, and q4_ef controls under explicit churn.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public nonconvex federated benchmark for q4 error feedback under churn
- Success threshold: q4_ef final accuracy is within 3 percentage points of fp32 and at least 5 percentage points higher than q4_noef under the same churn schedule, with at least 85% update-payload byte reduction versus fp32.
- Stop condition: Stop if q4_noef remains within 1 percentage point of q4_ef across five seeds or if q4_ef falls more than 3 percentage points below fp32.

## Evidence references

- Artifact root: `<local-path>/projects/real-federated-q4-error-feedback-compression-under-churn-3a27a2b5cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

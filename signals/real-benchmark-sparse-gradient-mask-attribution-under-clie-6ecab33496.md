# Real-benchmark sparse gradient mask attribution under client subsampling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-benchmark-sparse-gradient-mask-attribution-under-clie-6ecab33496`
Run ID: `real-benchmark-sparse-gradient-mask-attribution-under-clie-6ecab33496-20260526T135941073961+0000`

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

- Parent run decision: Sparse-Mask Gradient Fingerprinting for Low-Bandwidth Volunteer Training: enoch://control-plane/projects/sparse-mask-gradient-fingerprinting-for-low-bandwidth-volunteer-training-2b91ec540b68/runs/sparse-mask-gradient-fingerprinting-for-low-bandwidth-volunteer-training-2b91ec540b68-20260526T054210896845+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fcaeefd6eeab

## What looked useful

Sparse masked aggregate gradients leaked above-chance client participation, but 5% top-k masks failed the support threshold on all datasets and were consistently worse than same-density random masks. At 5% top-k density, AP/precision@8 were digits 0.572/0.475, breast_cancer 0.430/0.326, and wine 0.405/0.305.

## Boundaries and scale limits

Small built-in real datasets, small MLPs, known per-client reference gradients, no repeated FL training rounds, no DP/noise, no secure aggregation protocol implementation, and no large client population or production-scale model.

## Claim scope

Controlled Tier-1 benchmark on sklearn digits, breast_cancer, and wine using trained small MLPs, 40 non-IID clients, 8 sampled clients per round, and single-round gradient attribution from sparse aggregate masks.

## Why it stopped

Tier-1 direct small benchmark produced early falsification of the stated top-k sparse-mask attribution threshold: two of three datasets had 5% top-k AP below 0.50 and precision@8 below 2x random participant rate, and top-k did not beat random masks on any dataset.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing locally, run a bounded mask-selection ablation to determine whether attribution leakage comes from retained gradient subspace rather than top-k salience.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mask-selection ablation for sparse gradient attribution under client subsampling
- Success threshold: At equal density, a non-top-k mask beats top-k by at least 0.05 AP on two or more datasets, or top-k beats all alternatives by at least 0.05 AP on two or more datasets, with paired seed-level consistency.
- Stop condition: Stop if all sparse masks remain below AP 0.50 and precision@participants below 2x random rate on two or more datasets, or if pairwise mask differences are below 0.03 AP across datasets.

## Evidence references

- Artifact root: `<local-path>/projects/real-benchmark-sparse-gradient-mask-attribution-under-clie-6ecab33496`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

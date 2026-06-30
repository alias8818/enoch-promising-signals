# Gradient Norm Fingerprinting for Cheap Volunteer Contribution Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-norm-fingerprinting-for-cheap-volunteer-contribution-verification-cbc6febdb2e9`
Run ID: `gradient-norm-fingerprinting-for-cheap-volunteer-contribution-verification-cbc6febdb2e9-20260527T194853413846+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/038bddab746a

## What looked useful

36-value fingerprints achieved AUROC 1.0 and FPR@95TPR 0.0 over 384 honest and 1536 impostor comparisons with 360x payload reduction versus the full gradient vector. Three-value fingerprints across seeds 7, 11, and 19 achieved AUROC 0.9902-0.9967 and FPR@95TPR 0.0065-0.0195 with 4322x payload reduction. Median audit recomputation time was essentially equal to local gradient/update time, so compute-cheap verification was not supported.

## Boundaries and scale limits

Tested only a 12,965-parameter MLP, synthetic data, deterministic CUDA/PyTorch recomputation, 24 clients, 8 rounds, 2 repeats, and three one-step ablation seeds. No real dataset, heterogeneous hardware tolerance, privacy analysis, cryptographic binding, or adaptive attacker evaluation was performed.

## Claim scope

In a small synthetic non-IID volunteer/federated MLP setting, deterministic per-layer gradient norm traces distinguish honest recomputed local-training traces from wrong-client, label-shuffle, random-fake, and replay controls; the evidence supports communication/storage-cheap audit metadata, not compute-cheap verification.

## Why it stopped

Bounded synthetic evidence supports separability and payload reduction but not the stronger claim of compute-cheap volunteer contribution verification; publication-grade validation would require real-task and adversarial evidence.

## Recommended next action

Stop this run as no-paper useful evidence; next run should test randomized partial gradient-norm audits on a real small dataset with adaptive norm-spoofing and heterogeneous tolerance controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Randomized Partial Gradient-Norm Audits on Real Small Datasets
- Success threshold: At least AUROC 0.95 and FPR@95TPR <= 0.05 against all non-adaptive controls, no adaptive control above 0.10 FPR at the selected honest tolerance, and at least 3x verifier compute reduction versus full local-work recomputation.
- Stop condition: Stop as negative if randomized partial audits either fail AUROC 0.90 against simple controls or require verifier compute within 2x of full recomputation to keep FPR@95TPR <= 0.05.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-fingerprinting-for-cheap-volunteer-contribution-verification-cbc6febdb2e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

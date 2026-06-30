# Distributed Commit-Audit Gradient Verification in a Real Training Harness

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `distributed-commit-audit-gradient-verification-in-a-real-t-561cb5a656`
Run ID: `distributed-commit-audit-gradient-verification-in-a-real-t-561cb5a656-20260605T154855117946+0000`

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

- Parent run decision: Distributed Commitment-Audit Gradient Verification with Adaptive Attackers: enoch://control-plane/projects/distributed-commitment-audit-gradient-verification-with-ad-6320e8112b/runs/distributed-commitment-audit-gradient-verification-with-ad-6320e8112b-20260605T094654058738+0000
- Parent run decision: Cheating-Resistant Volunteer Training via Commitment-Based Gradient Verification: enoch://control-plane/projects/cheating-resistant-volunteer-training-via-commitment-based-gradient-verification-0fea379ad0db/runs/cheating-resistant-volunteer-training-via-commitment-based-gradient-verification-0fea379ad0db-20260605T054604023231+0000

## What looked useful

Dense sign-flip corruption reduced unaudited accuracy to 0.104 mean and diverged loss, while commit-audit at 32 sampled coordinates detected 100% of corrupt steps and matched clean accuracy near 0.980. Sparse 1% corruption showed detection rising from 0.269 at 32 coords to 0.928 at 256 and 1.0 at 2048, but had little accuracy impact unaudited. Sparse 10% corruption increased unaudited gradient error/loss, while audit restored clean-range loss with 0.975-1.0 detection.

## Boundaries and scale limits

Synthetic teacher-student classification, small MLP, one local GPU, simulated workers rather than real multi-node DDP/NCCL, post-commit non-adaptive attacks only, and no public benchmark or large-model validation.

## Claim scope

In a single-process PyTorch CUDA training harness with 8 simulated workers, fixed seeds, a clean synchronous-SGD baseline, unaudited attack controls, and coordinate-audit ablations, commit-audit verification preserved clean-training accuracy under dense post-commit sign-flip corruption and detected sparse post-commit corruption according to sampled-coordinate budget.

## Why it stopped

Medium local evidence supports the mechanism but remains bounded to a synthetic single-process harness and mixed sparse-attack practical benefit, so it is not paper-positive.

## Recommended next action

Stop as no-paper useful signal; the next bounded test should move the same protocol into real torch.distributed DDP across local processes with a public dataset and an adaptive sparse attacker before considering scale-only validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real DDP Commit-Audit Verification on Public Data with Adaptive Sparse Corruption
- Success threshold: Commit-audit must recover at least 95% of the clean-vs-attacked accuracy gap for dense and adaptive sparse attacks, keep false positives below 1%, and add less than 15% wall-clock overhead at the smallest audit budget that reaches at least 95% detection.
- Stop condition: Stop negative if DDP implementation overhead exceeds 25% before attack mitigation, if false positives exceed 5%, or if audit fails to recover at least half of the clean-vs-attacked accuracy gap on two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/distributed-commit-audit-gradient-verification-in-a-real-t-561cb5a656`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

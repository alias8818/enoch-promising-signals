# Volunteer Gradient Compression for Distributed Training Bandwidth Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-gradient-compression-for-distributed-training-bandwidth-reduction-618af7ff3ba8`
Run ID: `volunteer-gradient-compression-for-distributed-training-bandwidth-reduction-618af7ff3ba8-20260610T071329622126+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7021e6dc2932

## What looked useful

Across three seeds, q8_ef matched dense mean loss and accuracy while reducing transmitted bytes by 74.95%; sign_1bit_ef increased mean loss by 0.0024 and reduced accuracy by 0.0021 while reducing bytes by 96.83%; randomk_1pct_ef and randomk_5pct_ef collapsed to near-chance accuracy with losses around 8.

## Boundaries and scale limits

No real neural-network model, no true multi-node networking, no secure aggregation overhead, no straggler/latency model, and no large-model optimizer dynamics were tested. Results should not be read as datacenter-scale or publication-grade validation.

## Claim scope

In a local NumPy volunteer-style distributed SGD simulator for logistic regression with non-IID worker shards and stochastic worker availability, q8 error-feedback compression preserved dense convergence at about 4x compression, scaled sign with error feedback had small degradation at about 31.5x compression, top-k was sparsity-sensitive, and the tested random-k error-feedback variants diverged.

## Why it stopped

Closed as no-paper useful signal because the evidence is a proxy simulator, not direct multi-node or neural-network training validation.

## Recommended next action

Run a bounded deepen follow-up on a real small neural model with the same byte accounting and fixed schedules, focusing on q8_ef, sign_1bit_ef, topk_5pct_ef, and a tuned safer random-k control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model validation of q8 and sign compression for volunteer distributed training
- Success threshold: q8_ef must match dense validation accuracy within 0.2 percentage points at about 4x compression; sign_1bit_ef must stay within 1 percentage point of dense while reducing transmitted bytes by at least 90%; no method may show residual norm explosion.
- Stop condition: Stop if q8_ef or sign_1bit_ef loses more than 2 percentage points of validation accuracy on two seeds or if compression overhead exceeds the estimated communication savings in the local network model.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-gradient-compression-for-distributed-training-bandwidth-reduction-618af7ff3ba8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

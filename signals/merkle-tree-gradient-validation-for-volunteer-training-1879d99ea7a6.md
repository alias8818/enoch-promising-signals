# Merkle-Tree Gradient Validation for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-tree-gradient-validation-for-volunteer-training-1879d99ea7a6`
Run ID: `merkle-tree-gradient-validation-for-volunteer-training-1879d99ea7a6-20260601T054713427004+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7c1ce4c99f51

## What looked useful

Merkle trees are a practical integrity/transport primitive for committed gradient shards, but they do not validate correctness. For 121,524 gradient leaves, 1,024 random audits detect a single corrupted leaf only about 0.84% of the time, and 95% detection of one corrupted leaf requires auditing about 95% of all leaves.

## Boundaries and scale limits

Synthetic gradients only; no real volunteer training, no real model loss curves, no adversarially adaptive attacker, no collusion model, no zero-knowledge or trusted-execution validation. Results cover Merkle commitment overhead and random audit detection probability, not end-to-end distributed training.

## Claim scope

Bounded local synthetic evidence for SHA-256 Merkle commitments over GPT-2-small-scale quantized gradient shards: inclusion proofs are cheap, but random spot audits do not make sparse malicious gradient edits practically detectable.

## Why it stopped

Proxy and analytic evidence reject the central correctness claim for Merkle-only validation; this is not a full training validation, but it directly falsifies the assumption that commitments alone or low-rate random audits can validate sparse malicious gradients.

## Recommended next action

Stop Merkle-only gradient validation as non-viable; if continuing, test a distinct audit-plus-recomputation scheme on real gradients with explicit sparse-attack detection thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Structured Gradient Audit Detection on Real Training Gradients
- Success threshold: At least 95% detection of sparse and targeted malicious edits with no more than 1% audited gradient leaves and less than 5% validator false-positive rate.
- Stop condition: Stop if structured audits fail to exceed 80% detection at 1% audit budget on any sparse or targeted attack class.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-tree-gradient-validation-for-volunteer-training-1879d99ea7a6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

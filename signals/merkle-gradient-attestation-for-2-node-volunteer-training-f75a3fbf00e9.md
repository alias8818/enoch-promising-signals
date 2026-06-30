# Merkle Gradient Attestation for 2-Node Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-gradient-attestation-for-2-node-volunteer-training-f75a3fbf00e9`
Run ID: `merkle-gradient-attestation-for-2-node-volunteer-training-f75a3fbf00e9-20260530T020426660611+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/36b9f72c1481

## What looked useful

Merkle gradient commitments are useful for byte integrity and auditability, but alone they do not stop a volunteer from hashing and submitting a maliciously computed gradient; final accuracy fell from 0.9738 baseline/honest Merkle to 0.5050 while all malicious Merkle verifications passed.

## Boundaries and scale limits

Test used one local GB10, two virtual workers, a 395266-parameter MLP, synthetic binary classification, 1000 optimizer steps, and no real network, volunteer churn, Sybil resistance, large language model, or real corpus training.

## Claim scope

In a deterministic synthetic two-node gradient-averaging probe, Merkle roots over serialized gradients detected post-commit byte tampering but did not attest semantic gradient correctness when a malicious node committed to its bad gradient before submission.

## Why it stopped

Proxy-scale direct mechanism test: Merkle hashing alone verified byte commitments but failed to detect pre-commit Byzantine gradients, so the stronger gradient-attestation hypothesis is unsupported without an additional semantic correctness mechanism.

## Recommended next action

Stop this Merkle-only claim as a no-paper useful signal; any next test should add a semantic validation layer such as spot-check recomputation or redundant-worker comparison.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Spot-check semantic validation for Merkle-committed volunteer gradients
- Success threshold: Detect at least 95% of malicious pre-commit gradient attacks at no more than 25% additional wall-clock overhead over Merkle-only on a small real dataset, while honest validation accuracy remains within 1 percentage point of baseline.
- Stop condition: Stop if spot checks detect less than 80% of malicious pre-commit attacks at 25% overhead or if honest training accuracy drops more than 2 percentage points versus baseline.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-gradient-attestation-for-2-node-volunteer-training-f75a3fbf00e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

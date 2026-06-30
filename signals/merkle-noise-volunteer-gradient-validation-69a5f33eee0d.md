# Merkle-Noise Volunteer Gradient Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-noise-volunteer-gradient-validation-69a5f33eee0d`
Run ID: `merkle-noise-volunteer-gradient-validation-69a5f33eee0d-20260607T053025494115+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4d064f2d90ca

## What looked useful

Merkle commitments validated committed tensor integrity and post-commit tamper detection according to audit coverage, but did not validate source correctness. Adaptive attackers that knew the public feature thresholds passed validation at 100% acceptance and reversed aggregate cosine even at 10% malicious clients.

## Boundaries and scale limits

No real volunteer deployment, no full model training, no real privacy accounting, no network adversary, and no production robust-aggregation or attestation protocol were tested.

## Claim scope

Synthetic 512-dimensional federated logistic-gradient simulation with 100 clients, clipped Gaussian-noisy volunteer gradients, Merkle commitments, public feature-envelope validation, and adaptive committed poisoning.

## Why it stopped

Bounded synthetic evidence supports Merkle integrity use but falsifies simple Merkle-plus-noise public-feature validation as sufficient semantic volunteer-gradient validation.

## Recommended next action

Stop this no-paper run; any next work should test source-correctness validation or robust aggregation against adaptive committed attackers, not Merkle commitments alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Committed-Gradient Robust Aggregation Benchmark
- Success threshold: At 20% adaptive malicious clients, the selected robust method keeps filtered aggregate cosine above 0.5 while rejecting or bounding malicious influence and preserving at least 90% honest update acceptance.
- Stop condition: Stop if adaptive attacks reduce aggregate cosine below 0.2 at 10% malicious clients or if the method requires private data, trusted hardware, or external attestations outside the bounded local simulator.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-noise-volunteer-gradient-validation-69a5f33eee0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

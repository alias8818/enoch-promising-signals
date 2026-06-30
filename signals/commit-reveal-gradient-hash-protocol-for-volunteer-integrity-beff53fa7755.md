# Commit-Reveal Gradient Hash Protocol for Volunteer Integrity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-gradient-hash-protocol-for-volunteer-integrity-beff53fa7755`
Run ID: `commit-reveal-gradient-hash-protocol-for-volunteer-integrity-beff53fa7755-20260628T133456799496+0000`

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

- Provider-backed Research Facility batch: z-ai/glm-5.2: enoch://research-facility/provider/z-ai/glm-5.2/65bc9827b977

## What looked useful

Commit-reveal is an immutability and ordering primitive, not a standalone volunteer-integrity protocol. The tested mechanism caught 100% of post-commit mutation attempts and 0% of pre-committed bogus-gradient attacks.

## Boundaries and scale limits

Local CPU-only synthetic experiment: 40 volunteers, 96 examples per volunteer, dimension 128, 2048 validation examples, 50 seeds, 3 malicious fractions, 600 total trials. No real volunteer network, no large model, no repeated training, no private-data attestation, and no robust aggregation.

## Claim scope

In a synthetic one-round federated logistic-regression test, salted SHA-256 commit-reveal over quantized gradient bytes reliably detects after-commit gradient mutation but does not detect zero, random, or label-flipped gradients that are committed up front.

## Why it stopped

Proxy/local early falsification of the broad volunteer-integrity claim: the protocol verifies that a revealed gradient equals the committed bytes, but every tested pre-committed bogus-gradient attack passed verification.

## Recommended next action

Stop this standalone protocol line; only continue if adding a bounded semantic-validity layer such as redundant recomputation, robust aggregation, trusted execution, or proof-of-correct-computation checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Reveal Plus Semantic Gradient Validity Checks
- Success threshold: At 25% malicious volunteers, malicious acceptance below 20%, honest false rejection below 5%, and lower aggregate L2 error than commit-reveal-only for zero, random-noise, and label-flip attacks.
- Stop condition: Stop if semantic checks cannot reduce malicious acceptance below 50% without exceeding 10% honest false rejection, or if they add assumptions equivalent to trusted execution or full recomputation without producing a practical intermediate protocol.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-hash-protocol-for-volunteer-integrity-beff53fa7755`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

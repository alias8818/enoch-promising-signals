# Merkle-committed gradient audit for volunteer training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-committed-gradient-audit-for-volunteer-training-cd1dd987438c`
Run ID: `merkle-committed-gradient-audit-for-volunteer-training-cd1dd987438c-20260610T095630037008+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d02fcf38374a

## What looked useful

Transport tamper detection matched the hypergeometric audit model within 0.0199 max absolute error, but one self-consistent malicious worker caused a 0.2525 final-accuracy drop while producing 0 audit failures over 300 malicious steps.

## Boundaries and scale limits

Synthetic logistic regression only: 8 workers, 4096-dimensional gradients, 128 chunks, 300 steps, 1000 transport-tamper trials per detection cell. No real volunteer network, large model, data provenance proof, secure hardware, or proof-of-correct-computation validation.

## Claim scope

In a deterministic toy volunteer-training simulation, Merkle chunk commitments detect post-commit gradient-byte tampering with the expected random-audit probability, but Merkle-only audits do not detect self-consistent malicious gradients.

## Why it stopped

Proxy early falsification of the broad correctness-audit claim: Merkle commitments bind gradient bytes but do not prove those bytes are a correct gradient.

## Recommended next action

Stop this Merkle-only line as a standalone correctness audit; next test should add replicated spot recomputation or attested/proved gradient computation and compare against this baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Merkle commitments plus replicated spot recomputation for volunteer-gradient correctness
- Success threshold: At least 80% detection of a one-of-eight self-consistent malicious worker over 300 steps at audit budget <= 10% recomputed batches, with honest false-positive rate below 1% and final accuracy within 5 percentage points of honest training.
- Stop condition: Stop if recomputation cannot distinguish malicious from honest gradients in the toy setting or if the overhead exceeds 2x mean training-step time before reaching the detection threshold.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-committed-gradient-audit-for-volunteer-training-cd1dd987438c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

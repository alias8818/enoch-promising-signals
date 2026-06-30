# CPU Re-Derivation Proof for Volunteer Gradients

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-re-derivation-proof-for-volunteer-gradients-43b979e12a1c`
Run ID: `cpu-re-derivation-proof-for-volunteer-gradients-43b979e12a1c-20260620T034402234382+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8af0377f90cd

## What looked useful

Exact re-derivation is a viable bounded integrity check when deterministic replay inputs are available. Naive coordinate sampling is falsified for sparse tamper, missing 246 of 247 sparse-spike corruptions in the medium run.

## Boundaries and scale limits

Synthetic CPU-only NumPy test with 2400 submissions, small MLP tensors, no real volunteers, no large model, no mixed precision, no GPU nondeterminism, no optimizer-state protocol, and no cryptographic or privacy-preserving proof.

## Claim scope

In a deterministic small NumPy MLP, exact CPU re-derivation from committed weights, batch inputs, labels, and submitted gradients detected all tested volunteer-gradient tamper classes with zero false accepts and zero false rejects; a 64-coordinate sampled audit was not reliable against sparse single-coordinate corruption.

## Why it stopped

Closed as no-paper useful signal: the evidence is synthetic and bounded, and it supports exact deterministic re-derivation while falsifying naive sampled-coordinate verification for sparse tamper.

## Recommended next action

Run a bounded PyTorch reproduction test with fixed seeds, explicit dtype policy, optimizer-state commitments, and CPU/GPU gradient comparison before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch Deterministic Replay Audit for Volunteer Gradients
- Success threshold: At least 1000 submissions with honest false reject rate <= 1%, tampered false accept rate <= 1% for both dense and sparse tamper, and verifier overhead reported for each model/batch setting.
- Stop condition: Stop if deterministic replay cannot keep honest CPU/GPU relative gradient error below the verification threshold under documented dtype/seed controls, or if sparse tamper remains accepted above 1%.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-re-derivation-proof-for-volunteer-gradients-43b979e12a1c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

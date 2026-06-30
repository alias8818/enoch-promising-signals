# Verifiable training ledger with cryptographic commitment trees

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `verifiable-training-ledger-with-cryptographic-commitment-trees-b9551a039d7e`
Run ID: `verifiable-training-ledger-with-cryptographic-commitment-trees-b9551a039d7e-20260607T175708537770+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aa85fc0bcc9a

## What looked useful

The prototype verified chain integrity, Merkle inclusion proofs, and tamper detection across smoke, 2000-step small-model, and 500-step wide-model runs. Median minimal-ledger overhead was 112.7% on the tiny 128-feature proxy but 7.6% on the wider 2048-feature proxy; full-batch hashing overhead was 471.3% and 188.4%, respectively.

## Boundaries and scale limits

Synthetic single-process CPU proxy only; no real neural-network trainer, distributed execution, checkpoint signing, trusted timestamping, replayable dataloader audit, or production cryptographic review. Full-batch hashing remained expensive in the tested proxy.

## Claim scope

A local NumPy logistic-regression proxy can attach append-only SHA-256 step records, commit them into a Merkle tree, verify inclusion proofs, and detect post-hoc record tampering; minimal metadata commitments show low overhead only when training compute is large enough relative to hashing.

## Why it stopped

No-paper useful signal: this run supports the local mechanism but only through a synthetic proxy, not direct evidence from a real training stack.

## Recommended next action

Run a bounded PyTorch integration that logs real dataloader seeds, checkpoint hashes, and optimizer-step commitments on a small neural network, with overhead measured against a no-ledger baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch checkpoint-backed training ledger overhead probe
- Success threshold: Minimal ledger mode verifies all integrity checks and has median runtime overhead below 15% versus no-ledger baseline; full-batch hashing may be reported separately but is not required to pass.
- Stop condition: Stop if minimal checkpoint-backed ledger overhead exceeds 50% after three repeated runs or if checkpoint/dataloader replay verification cannot be made deterministic locally.

## Evidence references

- Artifact root: `<local-path>/projects/verifiable-training-ledger-with-cryptographic-commitment-trees-b9551a039d7e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Volunteer Distributed Training: Bounded Proof-of-Concept with Evidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-distributed-training-bounded-proof-of-concept-with-evidence-ledger-0e4d4dbbbebc`
Run ID: `volunteer-distributed-training-bounded-proof-of-concept-with-evidence-ledger-0e4d4dbbbebc-20260608T094135212438+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/51028fbb9717

## What looked useful

Honest volunteer aggregation matched the centralized baseline at 1.0000 accuracy. With 20% dropout, 20% malicious submissions, and 50% random audits, 44/44 audited corrupted submissions were rejected and accuracy remained 1.0000. All original ledgers verified and all tampered ledgers failed verification. A 70% malicious no-audit control fell to 0.2861 accuracy despite a valid ledger, showing validation is required in addition to evidence recording.

## Boundaries and scale limits

Toy synthetic task only; one local process; no real volunteer machines, WAN networking, cryptographic worker identities, privacy constraints, adaptive adversaries, checkpoint restart across hosts, or LLM-scale training.

## Claim scope

Local GPU-assisted emulation of 8 volunteer gradient workers on a synthetic classification task shows that hash-chained evidence ledgers can record assignments/results/audits, detect post-hoc tampering, and support audit-based rejection of corrupted gradients in a bounded proof-of-concept.

## Why it stopped

Closed as no-paper useful signal because the evidence is a local/toy emulation, not a real volunteer distributed training deployment.

## Recommended next action

Run a bounded multi-process or LAN-host follow-up with signed worker identities, induced network failures, and checkpoint restart verification before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-process Volunteer Ledger with Signed Workers and Restart Recovery
- Success threshold: Original ledgers verify, tampered ledgers fail verification, audited corrupted submissions are rejected at the configured audit rate, restart preserves the checkpoint hash, and final accuracy is within 5 percentage points of centralized training under <=20% dropout and <=20% malicious submissions.
- Stop condition: Stop if signed ledger verification fails on untampered events, restart cannot reproduce checkpoint hashes, or audited corrupted gradients are accepted above tolerance.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-distributed-training-bounded-proof-of-concept-with-evidence-ledger-0e4d4dbbbebc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

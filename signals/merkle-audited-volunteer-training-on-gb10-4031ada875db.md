# Merkle-Audited Volunteer Training on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `merkle-audited-volunteer-training-on-gb10-4031ada875db`
Run ID: `merkle-audited-volunteer-training-on-gb10-4031ada875db-20260604T182207942297+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3c542971de2e

## What looked useful

Merkle update commitments are mechanically compatible with a small GB10 volunteer-training loop and provide byte-level tamper evidence with sub-millisecond hashing cost per roughly 543 KB update, but this is not end-to-end decentralized training evidence.

## Boundaries and scale limits

Synthetic data only; small MLP only; one local process; no real volunteer network, remote attestation, identity resistance, reward accounting, public audit log, verifier sampling policy, heterogeneous workers, large-model payloads, or long-duration checkpoint persistence.

## Claim scope

In a single-process GB10 CUDA synthetic volunteer/FedAvg harness, per-update deterministic SHA-256 Merkle commitments over approximately 543 KB model deltas preserved paired training metrics, detected a deliberate tensor modification in all tested audited runs, and cost about 0.784 ms per submitted update across 288 audited updates.

## Why it stopped

No-paper closure: this run produced a useful bounded local mechanism signal, but the evidence is synthetic and local rather than an end-to-end volunteer-training validation.

## Recommended next action

Run a bounded multi-process follow-up with real serialized update transport, verifier recomputation, adversarial update cases, and larger payloads before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-process Merkle-audited volunteer update verification on GB10
- Success threshold: Across at least 1000 submitted updates, audited throughput remains within 5% of baseline, all injected tamper/replay/truncation cases are detected, and restart verification reproduces all accepted roots.
- Stop condition: Stop if audited throughput loss exceeds 15%, deterministic serialization is not reproducible across worker processes, or any injected tamper/replay/truncation case is accepted as valid.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-audited-volunteer-training-on-gb10-4031ada875db`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

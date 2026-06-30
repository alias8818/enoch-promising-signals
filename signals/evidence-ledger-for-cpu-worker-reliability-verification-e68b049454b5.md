# Evidence Ledger for CPU Worker Reliability Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-cpu-worker-reliability-verification-e68b049454b5`
Run ID: `evidence-ledger-for-cpu-worker-reliability-verification-e68b049454b5-20260607T213045242796+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/bf7bbd7d1a18

## What looked useful

The prototype verified 1000 artifact records, detected a modified ledger entry and a modified artifact, and recorded at 7788 artifacts/s after fixing an O(n^2) append bottleneck.

## Boundaries and scale limits

Tested on 1000 generated artifacts totaling 4002273 bytes on one CPU worker. Not tested against rollback, root-level adversaries, concurrent writers, remote attestation, signed checkpoints, controller integration, or real multi-day worker traces.

## Claim scope

A dependency-free local JSONL hash-chain ledger over command metadata and artifact SHA-256 digests can detect ledger-entry mutation and artifact mutation for generated CPU-worker artifacts with practical overhead in a single-process prototype.

## Why it stopped

Prototype and synthetic-artifact evidence supports the local mechanism but is not a full validation of CPU-worker reliability verification.

## Recommended next action

Stop this run as no-paper useful signal; next run should replay real Enoch worker logs through the ledger and require signed checkpoint roots plus rollback detection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Real Enoch Worker Traces Through a Signed Evidence Ledger
- Success threshold: All injected faults are detected and median replay overhead is below 5 percent on at least three real worker traces.
- Stop condition: Stop if any injected fault is not detected or median overhead exceeds 10 percent after the append-cache optimization.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-cpu-worker-reliability-verification-e68b049454b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

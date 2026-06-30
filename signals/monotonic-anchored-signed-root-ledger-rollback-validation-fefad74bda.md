# Monotonic anchored signed-root ledger rollback validation

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `monotonic-anchored-signed-root-ledger-rollback-validation-fefad74bda`
Run ID: `monotonic-anchored-signed-root-ledger-rollback-validation-fefad74bda-20260523T213921220823+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-agent persisted signed-root ledger validation: enoch://control-plane/projects/real-agent-persisted-signed-root-ledger-validation-1edf9d7075/runs/real-agent-persisted-signed-root-ledger-validation-1edf9d7075-20260523T165658261392+0000
- Parent run decision: Live signed-root checksum ledger for agent tool-call traces: enoch://control-plane/projects/live-signed-root-checksum-ledger-for-agent-tool-call-trace-522d69f843/runs/live-signed-root-checksum-ledger-for-agent-tool-call-trace-522d69f843-20260523T164725208271+0000

## What looked useful

Anchored signed roots gave 100% detection for rollback before the latest anchor and anchored same-sequence forks, 0% false positives on honest latest state, and near-zero in-memory verification overhead; however, stateless anchored verification detected 0% of unanchored-tail rollbacks, showing freshness is bounded by anchor cadence.

## Boundaries and scale limits

The validation uses local SHA-256/HMAC simulation with in-memory anchors, ledger length up to 2000, fixed seeded adversarial trials, and no networked transparency service, durable crash recovery, public-key signature cost, multi-writer concurrency, or production timestamping latency.

## Claim scope

In a deterministic signed-root ledger simulator, monotonic external anchors detect stateless rollback to any checkpoint older than the latest anchored sequence and detect same-sequence anchored root equivocation; signed-root-only verification accepts stale signed roots.

## Why it stopped

Mechanism support is clear but not paper-readiness: the result reproduces known freshness behavior of externally anchored signed roots and exposes the expected unanchored-tail limitation.

## Recommended next action

Stop this follow-up line at depth 4: keep the reproducible simulator and metrics as useful no-paper evidence; a paper would require a real networked transparency-log deployment and a stronger novelty claim.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/monotonic-anchored-signed-root-ledger-rollback-validation-fefad74bda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

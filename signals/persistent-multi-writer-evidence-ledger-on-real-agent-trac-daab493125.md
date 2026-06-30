# Persistent Multi-Writer Evidence Ledger on Real Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `persistent-multi-writer-evidence-ledger-on-real-agent-trac-daab493125`
Run ID: `persistent-multi-writer-evidence-ledger-on-real-agent-trac-daab493125-20260613T104239060385+0000`

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

- Parent run decision: Cryptographic Evidence Ledger for Agent Claims: enoch://control-plane/projects/cryptographic-evidence-ledger-for-agent-claims-f2e39ac22977/runs/cryptographic-evidence-ledger-for-agent-claims-f2e39ac22977-20260613T100821989066+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/274266e08693

## What looked useful

The controlled direct test supports the mechanism that serialized append transactions plus WAL can make a persistent multi-writer evidence ledger reliable for small real-agent-trace ingestion, while the unsafe control demonstrates the race prevented by the mechanism. This is useful engineering evidence, not paper-grade validation.

## Boundaries and scale limits

Single host, SQLite-only, one local trace source, 8 writer processes, 8,250 writes, no crash injection, no distributed filesystem, no adversarial tampering, no long-retention or large-artifact workload.

## Claim scope

On one local worker, an SQLite WAL append-only evidence ledger using BEGIN IMMEDIATE around read-tip/insert preserved 8,250 concurrent writes from 8 writer processes over 33 real Codex JSONL trace records with no missing records, duplicate logical IDs, sequence gaps, or hash-chain errors; an unsafe no-transaction control lost 6,419 of 8,250 writes.

## Why it stopped

Tier 1 direct mechanism support was achieved, but the evidence is too narrow for publication readiness because it lacks crash recovery, distributed writers, larger traces, and adversarial integrity tests.

## Recommended next action

Run a bounded crash-injection follow-up that kills and restarts writers mid-ingestion, then verifies exact-once recovery and hash-chain integrity over at least 100,000 writes from multiple real agent trace files.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-Recovering Multi-Writer Evidence Ledger on Real Agent Traces
- Success threshold: Across at least 5 deterministic crash schedules, the safe ledger persists and recovers 100% of expected logical evidence records with 0 duplicates, 0 missing IDs, 0 sequence gaps, and 0 hash-chain errors, while a reduced-safety control fails at least one verification criterion.
- Stop condition: Stop if any safe-ledger crash schedule produces missing records, duplicate logical IDs, a sequence gap, or a hash-chain error after restart, or if the workload cannot complete locally within the controller's bounded runtime.

## Evidence references

- Artifact root: `<local-path>/projects/persistent-multi-writer-evidence-ledger-on-real-agent-trac-daab493125`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

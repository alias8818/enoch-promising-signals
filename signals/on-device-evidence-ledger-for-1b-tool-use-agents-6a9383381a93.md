# On-Device Evidence Ledger for 1B Tool-Use Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `on-device-evidence-ledger-for-1b-tool-use-agents-6a9383381a93`
Run ID: `on-device-evidence-ledger-for-1b-tool-use-agents-6a9383381a93-20260608T053450892532+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/bb579c688b03

## What looked useful

Hash-chain evidence cost was small relative to durable SQLite commit cost, and tamper detection worked on every tested ledger copy. The mechanism looks practical enough for a bounded real-agent integration test, but this run is not paper-ready.

## Boundaries and scale limits

Synthetic events only; no real 1B-class model, no end-to-end agent loop, no real tool traces, no crash-recovery fault injection, no concurrent writers, and no task-quality or prompt-context overhead measurement.

## Claim scope

A standalone SQLite WAL hash-chain ledger can persist synthetic on-device tool-use evidence events with deterministic tamper detection, about 1.33x storage overhead versus plain SQLite, 3.5k events/s with FULL synchronous per-event commits, 25.7k events/s with FULL synchronous 16-event batches, and 382k-602k events/s clean-chain verification on this host.

## Why it stopped

No-paper closure: this is a standalone synthetic systems benchmark, not direct publication-grade evidence for a 1B on-device agent.

## Recommended next action

Run a bounded integration test with an actual local 1B-class tool-use agent, recording real tool traces while measuring end-to-end latency, memory, crash recovery, and task success against no-ledger and plain-SQLite controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real 1B Tool-Use Agent Ledger Integration
- Success threshold: Hash-chain ledger adds less than 5% median end-to-end latency and less than 10% p95 latency versus plain SQLite, records all committed tool events, preserves task success within 2 percentage points of no-ledger, and detects 100% of injected row tampering in the test set.
- Stop condition: Stop if ledger overhead exceeds 15% p95 end-to-end latency, causes missed events or task-success degradation above 5 percentage points, or cannot recover a verifiable committed prefix after crash/restart.

## Evidence references

- Artifact root: `<local-path>/projects/on-device-evidence-ledger-for-1b-tool-use-agents-6a9383381a93`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Local Agent Evidence Ledger with Rollback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-agent-evidence-ledger-with-rollback-c06b3186675f`
Run ID: `local-agent-evidence-ledger-with-rollback-c06b3186675f-20260608T213901738069+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7b7a88ab66bb

## What looked useful

Prototype and tests support the core mechanism: 5/5 tamper mutations detected, rollback to sequence 500 verified, verification averaged 13,722 records/s, rollback averaged 12,994 reverted records/s, and append averaged 484 ops/s versus 3,826 ops/s for direct writes.

## Boundaries and scale limits

Tested only synthetic operations, 5 trials of 1,000 operations, single writer, no crash-kill harness, no concurrent writes, no real agent traces, and no million-record scale. The naive append path rereads the ledger and fsyncs each append, producing about 7.9x overhead versus direct state writes.

## Claim scope

A single-process, file-backed, hash-chained JSONL evidence ledger can provide deterministic rollback, replay verification, and persisted-record tamper detection for 1,000-operation synthetic local-agent key-value workflows.

## Why it stopped

Bounded synthetic evidence supports rollback and tamper-detection mechanics, but it is not publication-grade and the naive implementation has material write overhead.

## Recommended next action

Stop as no-paper useful signal; next bounded work should replace naive append with a tail-metadata or SQLite/WAL-backed design and rerun against real local-agent traces plus a crash-consistency harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-safe and baseline-comparative local agent evidence ledger
- Success threshold: Tamper detection and rollback correctness remain 100%; crash recovery has zero corrupt tips across randomized kills; mean append overhead is below 2x the strongest durable baseline or below 5 ms per operation for real local-agent traces.
- Stop condition: Stop if crash recovery produces unrecoverable corruption, rollback verification fails in any trial, or durable append overhead remains above 5x direct writes after replacing the naive append path.

## Evidence references

- Artifact root: `<local-path>/projects/local-agent-evidence-ledger-with-rollback-c06b3186675f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

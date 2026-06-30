# Durable compact rollback ledger for real tool-wrapper crashes

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `durable-compact-rollback-ledger-for-real-tool-wrapper-cras-3787ec8079`
Run ID: `durable-compact-rollback-ledger-for-real-tool-wrapper-cras-3787ec8079-20260609T103345305082+0000`

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

- Parent run decision: Rollback Ledger: Recovery Logging for Tool Errors: enoch://control-plane/projects/rollback-ledger-recovery-logging-for-tool-errors-f91053ffd9e7/runs/rollback-ledger-recovery-logging-for-tool-errors-f91053ffd9e7-20260609T031113668928+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/480fb0c46c7f

## What looked useful

Across 300 transactions per implementation and 250 SIGKILL crashes per mode, the compact ledger had 0 semantic recovery failures with 226 byte peak metadata before recovery; the append-only event log also had 0 failures but grew to 12508 bytes; the no-rollback control had 150 semantic failures.

## Boundaries and scale limits

Tested only one state file, one counter operation, serialized child processes, local filesystem atomic replace/fsync behavior, and 300 transactions per implementation. Not tested for concurrent wrappers, multi-file state, real tool APIs, power-loss storage faults, or production databases.

## Claim scope

Small direct crash-injection harness for a single-process JSON tool-wrapper state file: compact prepare/commit rollback ledger recovered correctly from SIGKILL at controlled transaction windows and kept metadata bounded relative to an append-only event log.

## Why it stopped

Tier 1 direct evidence supports the mechanism, but the validation is too small and synthetic for publication readiness.

## Recommended next action

Run a deepen follow-up against a realistic multi-file/concurrent tool-wrapper workload with SQLite/WAL and append-log baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent multi-file compact rollback ledger versus SQLite WAL for tool-wrapper crashes
- Success threshold: Zero recovery invariant failures over at least 5000 crash-injected operations, compact metadata remaining bounded by active transaction footprint rather than total event count, and recovery latency not worse than 2x SQLite/WAL on the bounded workload.
- Stop condition: Stop as unsupported if any compact-ledger invariant failure is reproducible after recovery, or if metadata grows linearly with total operation count under the intended compaction policy.

## Evidence references

- Artifact root: `<local-path>/projects/durable-compact-rollback-ledger-for-real-tool-wrapper-cras-3787ec8079`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

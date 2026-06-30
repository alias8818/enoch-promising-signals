# Crash-Safe Multi-Writer Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `crash-safe-multi-writer-agent-evidence-ledger-af35228ffe`
Run ID: `crash-safe-multi-writer-agent-evidence-ledger-af35228ffe-20260602T192800752804+0000`

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

- Parent run decision: Live Agent Evidence Ledger with Signed Root Commitments: enoch://control-plane/projects/live-agent-evidence-ledger-with-signed-root-commitments-3abd9b13cd/runs/live-agent-evidence-ledger-with-signed-root-commitments-3abd9b13cd-20260601T102100952587+0000
- Parent run decision: CPU Agent Evidence Ledger with Deterministic Verifier: enoch://control-plane/projects/cpu-agent-evidence-ledger-with-deterministic-verifier-17e32bf65419/runs/cpu-agent-evidence-ledger-with-deterministic-verifier-17e32bf65419-20260601T044620781565+0000

## What looked useful

Unsafe concurrent JSONL append failed strongly under multi-writer interleaving, losing 1030 acknowledged records at 4 writers and 3493 at 8 writers across five seeds. Framed+fsync, locked JSONL+fsync, no-fsync locked variants under process crashes, and SQLite WAL all had zero missing acknowledged records in this bounded test. Framed recovery detected injected mid-file and tail corruption and truncated to valid prefixes, but the main metric did not show a novelty advantage over locked JSONL+fsync.

## Boundaries and scale limits

Not validated under real power-loss, reboot, storage-controller faults, filesystem mount-option variation, network/shared filesystems, object stores, multi-host writers, file rotation, or production-scale agent traces. A simpler locked JSONL+fsync baseline matched the framed ledger on the main process-crash metric.

## Claim scope

On a local Linux CPU worker with up to 8 concurrent writer processes and deterministic process-exit injection, a framed file-locking evidence ledger with per-record CRC and fsync preserved all acknowledged records across 15/15 medium trials and recovered clean prefixes after deliberate byte and tail corruption.

## Why it stopped

Tier 2 local process-crash evidence supports viability and recovery diagnostics but is not paper-positive because a simple locked JSONL+fsync baseline matched the custom framed ledger on the direct acknowledged-record metric and real power-loss durability was not tested.

## Recommended next action

Run a bounded block-device or VM power-cut fault-injection follow-up comparing framed_fsync, jsonl_locked_fsync, sqlite_wal, and nofsync ablations for acknowledged-record loss after simulated power failure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Power-Cut Fault Injection for Multi-Writer Evidence Ledgers
- Success threshold: Across at least 30 power-cut trials and writer counts 4 and 8, fsync-backed modes must show zero missing acknowledged records after recovery, nofsync ablations must show a measurable failure mode, and framed recovery must correctly localize/truncate injected corruption with no invalid recovered records.
- Stop condition: Stop if fsync-backed framed or locked JSONL loses any acknowledged record under correctly configured local filesystem power-cut recovery, or if nofsync ablations cannot be made to fail under the available fault injector after 30 valid cuts.

## Evidence references

- Artifact root: `<local-path>/projects/crash-safe-multi-writer-agent-evidence-ledger-af35228ffe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

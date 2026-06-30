# Process-kill validation of strict-framed rollback ledger recovery

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `process-kill-validation-of-strict-framed-rollback-ledger-r-9ba167d51d`
Run ID: `process-kill-validation-of-strict-framed-rollback-ledger-r-9ba167d51d-20260520T052743264221+0000`

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

- Parent run decision: Rollback Evidence Ledger for Local Tool Agents: enoch://control-plane/projects/rollback-evidence-ledger-for-local-tool-agents-8d0906640758/runs/rollback-evidence-ledger-for-local-tool-agents-8d0906640758-20260520T051301386101+0000
- Parent run decision: Replay real local-agent traces with crash-injected rollback ledger commits: enoch://control-plane/projects/replay-real-local-agent-traces-with-crash-injected-rollbac-81dbb9f5e9/runs/replay-real-local-agent-traces-with-crash-injected-rollbac-81dbb9f5e9-20260520T052008294008+0000

## What looked useful

Strict framing works for bounded process-kill tail rollback, but a conservative newline-delimited JSONL baseline matched the direct correctness target. The unsafe prefix control accepted 295 partial records, showing that exposing parseable commit tokens before full record boundaries is unsafe.

## Boundaries and scale limits

Tested only local process SIGKILL during single-writer appends; no power-loss durability, filesystem matrix, concurrent writers, application-level transaction replay, large-record stress, or device fault injection.

## Claim scope

In a local CPU-only process-kill harness with fixed seeds, strict-framed rollback recovery preserved every parent-observed committed record and recovered a valid prefix across 360 SIGKILL trials, while detecting incomplete tail frames.

## Why it stopped

Tier 2 process-kill validation supports the mechanism but not a novel strict-framing advantage over a real conservative JSONL baseline.

## Recommended next action

Stop this follow-up as no-paper useful-signal evidence; use conservative complete-record commit boundaries as the practical lesson, and only reopen if testing power-loss or fault-injected torn-write durability against stronger baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fault-injected torn-write validation of strict framing versus checksummed JSONL
- Success threshold: Strict framing must reduce false acceptance or lost committed records versus both JSONL baselines by a practically meaningful margin while preserving 100% of observed committed prefixes across the seeded fault matrix.
- Stop condition: Stop if checksummed JSONL matches strict framing on false acceptance, lost commits, and valid-prefix recovery across the full seeded fault matrix.

## Evidence references

- Artifact root: `<local-path>/projects/process-kill-validation-of-strict-framed-rollback-ledger-r-9ba167d51d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

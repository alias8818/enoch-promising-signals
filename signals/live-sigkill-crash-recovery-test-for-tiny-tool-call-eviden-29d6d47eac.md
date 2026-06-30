# Live SIGKILL Crash-Recovery Test for Tiny Tool-Call Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-sigkill-crash-recovery-test-for-tiny-tool-call-eviden-29d6d47eac`
Run ID: `live-sigkill-crash-recovery-test-for-tiny-tool-call-eviden-29d6d47eac-20260528T231343367586+0000`

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

- Parent run decision: Real Agent Trace and Crash Test for Tiny Tool-Call Evidence Ledger: enoch://control-plane/projects/real-agent-trace-and-crash-test-for-tiny-tool-call-evidenc-9c95dffea8/runs/real-agent-trace-and-crash-test-for-tiny-tool-call-evidenc-9c95dffea8-20260528T200344160080+0000
- Parent run decision: Tiny Agent Evidence Ledger for Tool Calls: enoch://control-plane/projects/tiny-agent-evidence-ledger-for-tool-calls-06c77b526a27/runs/tiny-agent-evidence-ledger-for-tool-calls-06c77b526a27-20260528T162823992974+0000

## What looked useful

Across 4,813 acknowledged SIGKILL records per safe variant, flush and fsync recovered 100% with zero corrupt lines; the buffered baseline recovered 0 of 4,813 acknowledged SIGKILL records while graceful controls recovered all records.

## Boundaries and scale limits

Tested 50 SIGKILL trials and 10 graceful controls per variant on a local filesystem with small JSONL records. Not tested: power loss, kernel panic, network filesystems, concurrent writers, disk-full behavior, full LangGraph recovery replay, or semantic idempotency of real tools.

## Claim scope

In a local single-writer Python JSONL evidence ledger, externally acknowledged tool-call records survived live process SIGKILL when acknowledgement occurred after flush or fsync; an acknowledge-before-flush buffered baseline lost acknowledged records.

## Why it stopped

No-paper useful signal: the scoped Tier-2 SIGKILL mechanism was supported, but the experiment only validates local JSONL sequence recovery and is not paper-positive systems evidence.

## Recommended next action

Run a bounded LangGraph/tool-call integration test that verifies recovered ledger entries can drive correct replay after SIGKILL, including duplicate suppression and partial transaction handling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LangGraph Tool-Call Ledger Replay Under SIGKILL
- Success threshold: At least 100 fixed-seed SIGKILL trials with 100% recovered acknowledged tool outputs, zero duplicate side effects after replay, and final recovered state matching graceful controls; baseline must show nonzero missing or duplicate acknowledged outputs.
- Stop condition: Stop if any safe variant loses or duplicates acknowledged tool outputs in two or more reproduced trials, or if integration cannot distinguish replay correctness from raw JSONL recovery.

## Evidence references

- Artifact root: `<local-path>/projects/live-sigkill-crash-recovery-test-for-tiny-tool-call-eviden-29d6d47eac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

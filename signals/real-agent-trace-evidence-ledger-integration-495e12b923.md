# Real Agent Trace Evidence-Ledger Integration

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-trace-evidence-ledger-integration-495e12b923`
Run ID: `real-agent-trace-evidence-ledger-integration-495e12b923-20260528T150914016428+0000`

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

- Parent run decision: Evidence-Ledger for Tiny Agent Tool Calls: enoch://control-plane/projects/evidence-ledger-for-tiny-agent-tool-calls-51678a3e6e58/runs/evidence-ledger-for-tiny-agent-tool-calls-51678a3e6e58-20260528T012513536322+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/125b33f851bb

## What looked useful

A deterministic harness converted a real agent trace into one ledger record per source event. Clean verification passed with 0 errors; a mutated source event failed with source_sha256 mismatch; a mutated ledger record failed with record_hash mismatch. Median build overhead was 0.0765 ms/event and median verify overhead was 0.0623 ms/event across 100 repeats.

## Boundaries and scale limits

Tested on a single 25-event local trace after events existed on disk. Did not test online streaming append, crash recovery, multi-agent ordering, concurrent writers, remote notarization, signing/key management, long traces, schema drift, or adversarial insertion/deletion/reordering/truncation campaigns.

## Claim scope

Offline ingestion of one real Codex/Enoch worker JSONL trace into a SHA-256 hash-chained evidence ledger, with exact event coverage for the observed trace, clean verification, single-source-record tamper detection, single-ledger-record tamper detection, and sub-1 ms/event median local build+verify overhead.

## Why it stopped

Mechanism support was obtained in a small direct offline trace test, but publication-grade claims require live streaming, recovery, concurrency, and broader adversarial validation.

## Recommended next action

Run a bounded streaming follow-up that attaches the ledger writer to multiple live agent runs, checkpoints during execution, forces crash/restart, and verifies no dropped events plus tamper detection under insertion, deletion, reordering, and truncation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Streaming Agent Trace Evidence-Ledger Recovery Test
- Success threshold: Pass if all live runs have zero dropped and zero duplicated events after restart, every adversarial mutation class is detected, and p95 append+verify overhead remains below 5 ms/event on traces of at least 100 events per run.
- Stop condition: Stop as unsupported if any live run loses or duplicates events after restart, if any adversarial mutation class verifies cleanly, or if p95 append+verify overhead exceeds 5 ms/event on the bounded traces.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-trace-evidence-ledger-integration-495e12b923`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

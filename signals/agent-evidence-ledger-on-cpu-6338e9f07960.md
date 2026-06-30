# Agent Evidence Ledger on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-evidence-ledger-on-cpu-6338e9f07960`
Run ID: `agent-evidence-ledger-on-cpu-6338e9f07960-20260609T032712209715+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0b02e3d6188e

## What looked useful

The mechanism is practical but costly relative to plain JSONL: median append overhead was 5.48x and storage overhead was 1.55x for 50k-event, 256-byte-payload trials. Tamper scenarios confirmed edit/middle-delete/reorder detection and exposed the need for external anchoring to catch suffix deletion.

## Boundaries and scale limits

Synthetic events only; single writer; local filesystem; no fsync/WAL durability tuning; no production agent traces; no concurrent writers; no privileged adversary, key theft, or filesystem rollback testing. Suffix truncation is not detected unless final event count and final hash are anchored outside the mutable ledger.

## Claim scope

A single-process CPU-local JSONL evidence ledger using canonical records, SHA-256 hash chaining, HMACs, and Merkle checkpoints can detect in-place edits, middle deletions, and record reorders on synthetic agent events while sustaining about 17.3k appends/s and 36.7k verified events/s on the tested CPU worker.

## Why it stopped

No-paper useful signal: evidence is synthetic and local, and the suffix-truncation limitation means the broad evidence-ledger claim is not closed without an anchoring design.

## Recommended next action

Run a bounded follow-up that adds an external final-hash/count anchor and replays real or realistic multi-agent traces against JSONL, SQLite WAL, and the current ledger.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored CPU Evidence Ledger on Realistic Agent Trace Replay
- Success threshold: Anchored ledger detects all tested tamper scenarios including suffix truncation, verifies clean traces without false failures, and stays below 3x append overhead versus the strongest durable baseline at 100k or more events.
- Stop condition: Stop if anchoring fails to detect suffix truncation, if clean trace verification is unreliable, or if append overhead exceeds 5x the durable baseline after straightforward batching.

## Evidence references

- Artifact root: `<local-path>/projects/agent-evidence-ledger-on-cpu-6338e9f07960`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

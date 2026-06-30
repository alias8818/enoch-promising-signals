# Append-Only Evidence Ledger for CPU Tool Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `append-only-evidence-ledger-for-cpu-tool-agents-ef81f599a0b2`
Run ID: `append-only-evidence-ledger-for-cpu-tool-agents-ef81f599a0b2-20260604T094355480569+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/45c91285252e

## What looked useful

The ledger mechanism is practical as low-overhead local tamper evidence for ordered CPU tool events, but append-only assurance requires external tail-hash anchoring. Buffered append reached 10766 events/s for 10000 events; fsync append on a 2500-event subset reached 696 events/s.

## Boundaries and scale limits

Synthetic events only; no real agent traces, no concurrent writers, no crash/power-loss validation, no OS-level append-lock study, and no external transparency/timestamp anchor. Tail truncation is not detectable by the internal chain alone.

## Claim scope

Single-writer local Python prototype for synthetic CPU tool-agent events: hash/HMAC-chained JSONL evidence records append at about 78.8 us/event buffered and detect tested edit, delete, reorder, and one-record rehash tampering.

## Why it stopped

Synthetic single-writer evidence supports the mechanism but also shows a standalone ledger cannot detect valid-prefix tail truncation without an external anchor.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should integrate external tail anchoring and replay real concurrent CPU-agent traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored Concurrent Evidence Ledger on Real CPU-Agent Traces
- Success threshold: All tested tamper classes including truncation are detected when anchors are present, with p95 buffered append latency below 1 ms and no lost or reordered records in concurrent replay.
- Stop condition: Stop if anchored truncation is not detected, concurrent writers corrupt ordering, or p95 append latency exceeds 1 ms for realistic traces after one implementation pass.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-evidence-ledger-for-cpu-tool-agents-ef81f599a0b2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

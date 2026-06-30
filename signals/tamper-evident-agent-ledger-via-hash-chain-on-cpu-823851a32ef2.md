# Tamper-Evident Agent Ledger via Hash Chain on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tamper-evident-agent-ledger-via-hash-chain-on-cpu-823851a32ef2`
Run ID: `tamper-evident-agent-ledger-via-hash-chain-on-cpu-823851a32ef2-20260531T143626231331+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b744dcbcced0

## What looked useful

Anchored hash-chain ledgers are practical on CPU for bounded agent logs: median write throughput was about 25k-62k events/s depending on payload size, verification scanned 50k events in 0.61-1.57s, and storage overhead was about 1.74x for 128-byte payloads and 1.07x for 2048-byte payloads. Unanchored verification missed suffix truncation and full-chain rewrite attacks.

## Boundaries and scale limits

Benchmarked locally up to 50,000 events, 2,048-byte payloads, and 108.7 MiB hash-chain files. Did not test real agent framework integration, concurrent writers, crash durability, signed/remote anchors, privileged host compromise, or long-running production traces.

## Claim scope

A single-process CPU Python prototype of a canonical JSONL agent-event ledger using per-record SHA-256 hash chaining detects local event edits, deletion, and reordering, and detects suffix truncation or full-chain rewrite only when verification includes a trusted final head/checkpoint anchor.

## Why it stopped

The bounded mechanism worked, but evidence is limited to a local Python prototype and shows that trusted anchoring is mandatory; this is useful engineering evidence but not publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test anchored checkpoints under concurrent append and crash injection rather than claiming broad tamper-evident agent provenance from this prototype alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-safe anchored hash-chain checkpoints for concurrent agent ledgers
- Success threshold: Across at least 100 crash-injection trials and 4 concurrent writers, no acknowledged event may disappear silently; all tamper/truncation/rewrite cases must either verify cleanly with preserved acknowledged events or fail verification, with median sustained throughput at or above 10k 2KiB events/s on CPU.
- Stop condition: Stop as negative if any acknowledged event can be silently lost or rewritten while anchored verification still passes, or if checkpointing drops median 2KiB-event throughput below 2k events/s in the bounded CPU test.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-agent-ledger-via-hash-chain-on-cpu-823851a32ef2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

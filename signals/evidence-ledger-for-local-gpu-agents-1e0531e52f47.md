# Evidence Ledger for Local GPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-local-gpu-agents-1e0531e52f47`
Run ID: `evidence-ledger-for-local-gpu-agents-1e0531e52f47-20260629T224531940425+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f57ede06da9f

## What looked useful

Clean ledgers verified for all tested payload sizes, three tamper probes were detected, and durable ledger throughput exceeded the fsync-per-line durable JSONL baseline by 1.63x-1.85x in this local benchmark.

## Boundaries and scale limits

Synthetic single-process benchmark only; no live GPU-agent integration, no concurrent writers, no crash/power-loss fault injection, no external anchoring, and no validation against adversaries able to rewrite the entire local database and verifier state.

## Claim scope

A local SQLite-backed SHA-256 hash-chain ledger can detect simple post-hoc tampering of synthetic local-agent evidence records while sustaining roughly 4200-4700 durable events/s for 128-8192 byte payloads on this GB10 worker filesystem.

## Why it stopped

Synthetic local benchmark supports the mechanism but does not provide direct production or adversarial evidence needed for a paper.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to integrate the ledger with one real local GPU-agent trace and add crash-injection plus concurrent-writer tests.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live GPU-Agent Evidence Ledger With Crash and Concurrency Checks
- Success threshold: Ledger-enabled live run completes with less than 5 percent end-to-end overhead, verifier passes after normal completion and crash recovery, and all post-hoc tamper probes are detected.
- Stop condition: Stop if ledger overhead exceeds 20 percent on the live run, verification fails on untampered data, or crash recovery produces an unverifiable committed prefix.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-local-gpu-agents-1e0531e52f47`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

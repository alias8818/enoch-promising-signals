# Evidence-Ledger for Tiny Agent Tool Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-tiny-agent-tool-calls-540e8b1c2c2b`
Run ID: `evidence-ledger-for-tiny-agent-tool-calls-540e8b1c2c2b-20260531T141221163027+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a7e78c6c302c

## What looked useful

A minimal standard-library evidence ledger verified clean traces and detected payload mutation, record deletion, and record reordering in all 9 benchmark cases. Median extra write latency was 12.13 microseconds per record, max extra latency was 25.59 microseconds per record, minimum ledger throughput was 27,094 records/second, and storage overhead was about 264 to 266 bytes per record.

## Boundaries and scale limits

Synthetic payloads only; local filesystem only; single process; maximum tested size was 100,000 records per payload-size case; no real agent integration, concurrent writers, crash recovery, signatures, remote anchoring, object-store durability, or adversarial key custody tests.

## Claim scope

Canonical JSONL records with payload SHA-256 hashes and a per-record hash chain can provide deterministic tamper detection for synthetic single-process tiny agent tool-call traces with about 9 to 26 microseconds extra write latency per record versus plain JSONL on the tested local worker.

## Why it stopped

The run produced a supported bounded mechanism result, but the evidence is synthetic and local-only, so it is not publication-grade validation.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should integrate the ledger into a real agent runtime and add crash/concurrency fault injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Agent-runtime ledger integration with crash and concurrency fault injection
- Success threshold: For at least 50,000 real or replayed tool calls, ledger overhead stays below 5 percent wall-clock versus baseline logging and every injected mutation, deletion, reorder, partial-write, and rotation fault is detected or explicitly quarantined.
- Stop condition: Stop if real-runtime overhead exceeds 10 percent after straightforward batching/checkpoint tuning, or if partial-write/log-rotation faults cannot be detected or quarantined deterministically.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tiny-agent-tool-calls-540e8b1c2c2b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

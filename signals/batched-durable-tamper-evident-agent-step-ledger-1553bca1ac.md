# Batched durable tamper-evident agent-step ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `batched-durable-tamper-evident-agent-step-ledger-1553bca1ac`
Run ID: `batched-durable-tamper-evident-agent-step-ledger-1553bca1ac-20260604T024715670797+0000`

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

- Parent run decision: Tamper-Evident KV Ledger for Agent Steps: enoch://control-plane/projects/tamper-evident-kv-ledger-for-agent-steps-1cb4fdaf8de7/runs/tamper-evident-kv-ledger-for-agent-steps-1cb4fdaf8de7-20260603T165953705206+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/788c4883ed21

## What looked useful

Batching fsync every 128 records reduced fsync calls from 2,000 to 16 and improved append throughput from 831.49 to 22,363.91 records/s (26.90x) while completed ledgers verified, an in-place mutation was detected at line 10, and SIGKILL recovery produced a valid 896-record prefix.

## Boundaries and scale limits

Small controlled local test only; no real power-loss test, no real agent traces, no concurrent writers, no distributed replication, no external rollback anchor, and no cross-filesystem/device robustness.

## Claim scope

Single-writer local JSONL agent-step ledger with per-record SHA-256 hash chaining and fsync batching over 2,000 synthetic 512-byte records on this CPU worker/filesystem.

## Why it stopped

Tier 1 direct mechanism test passed, but the evidence is small controlled local evidence and is not paper-positive.

## Recommended next action

Run a bounded deepen follow-up with real agent traces, latency percentiles, concurrent writer ordering, and fault-injection or power-loss simulation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium durability and latency validation for batched hash-chain agent ledgers
- Success threshold: At least 5x throughput over per-step fsync, completed-ledger verification success, tamper and truncation detection, valid prefix recovery after injected write faults, and p99 append latency under 100 ms on a replayed agent trace.
- Stop condition: Stop if batching cannot keep p99 append latency under 100 ms, recovery fails to produce a valid prefix after injected faults, or rollback/truncation remains undetectable without an impractical external anchor.

## Evidence references

- Artifact root: `<local-path>/projects/batched-durable-tamper-evident-agent-step-ledger-1553bca1ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

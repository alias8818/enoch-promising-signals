# Real agent runtime batched signed provenance ledger integration

Status: `useful_signal`
Project ID: `real-agent-runtime-batched-signed-provenance-ledger-integr-7e80aea690`
Run ID: `real-agent-runtime-batched-signed-provenance-ledger-integr-7e80aea690-20260516T023023047225+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Real agent runtime batched signed provenance ledger integration: internal_generated:real-agent-runtime-batched-signed-provenance-ledger-integr-7e80aea690

## What looked useful

Across 42 bounded-full cases and three fixed seeds, all ledgers verified and all tampered payloads were rejected. Batch sizes 32-128 captured most of the throughput benefit; batch size 128 achieved 639,767 events/s signing for 256-byte payloads and 699,054 events/s for 4096-byte payloads versus about 72,500 events/s for per-event Ed25519, while keeping p95 logical commit latency at 24.2 ms.

## Boundaries and scale limits

Evidence is bounded to single-process CPU execution on one ARM/GB10-class host, 32 simulated agents, 200,000 events per case, payloads up to 4096 bytes, and in-memory JSON ledger structures. It does not include production agent runtime integration, concurrent writers, fsync/database/object-storage persistence, crash recovery, network audit service behavior, or external verifier interoperability.

## Claim scope

In a deterministic local agent-runtime simulator with real SHA-256 hash chaining, Merkle batching, and Ed25519 signatures, batched Merkle-root signing preserved verification and tamper detection while improving signing throughput by about 8.8x to 9.6x at batch size 128 versus per-event Ed25519, with p95 logical commit latency of 24.2 ms at a 5,000 events/sec synthetic arrival rate.

## Why it stopped

No-paper useful signal: the bounded local evidence supports the cryptographic batching mechanism, but the real-runtime integration claim remains proxied by a deterministic simulator.

## Recommended next action

Run a bounded deepen follow-up that instruments a real LangGraph or comparable agent runtime with concurrent event emission, durable append-only persistence, crash/replay verification, and the same per-event versus batched-signing baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Durable concurrent agent-runtime provenance ledger integration
- Success threshold: All replay and tamper checks pass; batch sizes 32-128 provide at least 5x signing-throughput improvement versus per-event Ed25519, no more than 5% event loss or replay mismatch under crash testing, and p95 added commit latency remains below 50 ms.
- Stop condition: Stop as negative if durable runtime integration fails replay/tamper checks, loses events under crash/restart, or cannot sustain at least 2x signing-throughput improvement over per-event Ed25519 while keeping p95 added commit latency below 100 ms.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-runtime-batched-signed-provenance-ledger-integr-7e80aea690`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

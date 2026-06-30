# Medium durability and latency validation for batched hash-chain agent ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-durability-and-latency-validation-for-batched-hash-e83ea8f6e5`
Run ID: `medium-durability-and-latency-validation-for-batched-hash-e83ea8f6e5-20260604T050121356884+0000`

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
- Parent run decision: Batched durable tamper-evident agent-step ledger: enoch://control-plane/projects/batched-durable-tamper-evident-agent-step-ledger-1553bca1ac/runs/batched-durable-tamper-evident-agent-step-ledger-1553bca1ac-20260604T024715670797+0000

## What looked useful

At batch size 64 over 5 fixed seeds and 12,000 records per seed, batched hash-chain throughput averaged 34,614.9 records/s, 1.316x SQLite WAL FULL and 38.22x per-record fsync; p95/p99 latency averaged 2.783/5.070 ms; hash-chain corruption detection was 100% while the no-hash ablation detected 0% of single-byte corruptions.

## Boundaries and scale limits

Synthetic payloads only; no real agent traces, no concurrent writers, no process-kill crash injection during unflushed batches, no network filesystem, no torn-sector or power-loss device testing, and no production append-only log baseline beyond SQLite WAL.

## Claim scope

On a local single-process filesystem benchmark with fixed synthetic payload seeds, a batched hash-chain ledger with acknowledgement after batch fsync achieved verifiable prefix recovery and higher throughput than SQLite WAL synchronous=FULL at the same batch size and a per-record fsync hash-chain control.

## Why it stopped

Tier-2 local validation supports the mechanism but is synthetic and single-process, so it is not publication-grade durability evidence.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should add a real agent-trace replay plus randomized process-kill crash injection before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-injected agent-trace replay for batched hash-chain ledgers
- Success threshold: Across at least 100 injected crashes and fixed replay seeds, recover 100% of acknowledged records with no hash-chain verification failures, lose no acknowledged records, and sustain at least 1.2x SQLite WAL FULL throughput with p99 latency no worse than 2x SQLite.
- Stop condition: Stop if any acknowledged record is lost or verifies incorrectly, or if throughput falls below SQLite WAL FULL on all replay workloads.

## Evidence references

- Artifact root: `<local-path>/projects/medium-durability-and-latency-validation-for-batched-hash-e83ea8f6e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

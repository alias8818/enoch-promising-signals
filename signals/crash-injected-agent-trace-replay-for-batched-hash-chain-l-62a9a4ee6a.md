# Crash-injected agent-trace replay for batched hash-chain ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `crash-injected-agent-trace-replay-for-batched-hash-chain-l-62a9a4ee6a`
Run ID: `crash-injected-agent-trace-replay-for-batched-hash-chain-l-62a9a4ee6a-20260604T083914953364+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Batched durable tamper-evident agent-step ledger: enoch://control-plane/projects/batched-durable-tamper-evident-agent-step-ledger-1553bca1ac/runs/batched-durable-tamper-evident-agent-step-ledger-1553bca1ac-20260604T024715670797+0000
- Parent run decision: Medium durability and latency validation for batched hash-chain agent ledgers: enoch://control-plane/projects/medium-durability-and-latency-validation-for-batched-hash-e83ea8f6e5/runs/medium-durability-and-latency-validation-for-batched-hash-e83ea8f6e5-20260604T050121356884+0000

## What looked useful

Hash-chain batching preserved exact-prefix crash replay and tamper detection in all bounded trials. JSONL baselines recovered newline-complete prefixes but detected 0% of valid semantic tampering. Batching improved durable hash-chain write throughput from 283 events/s at batch 1 to 21,275 events/s at batch 64 and 25,470 events/s at batch 256, with an at-risk commit window bounded by batch size.

## Boundaries and scale limits

Tested 10,000 events per seed, five fixed seeds, six methods, 6,090 crash replay checks, and 750 tamper trials on local files only. Did not test real agent trace corpora, concurrent writers, production tracing stores, SQLite/WAL baselines, network filesystems, or multi-GB ledgers.

## Claim scope

For deterministic synthetic agent traces on a local filesystem, framed batched hash-chain ledgers recovered exactly the committed prefix under byte-level crash cuts and detected same-length semantic tampering, while batch sizes 64 and 256 delivered much higher write throughput than per-event durable hash-chain records.

## Why it stopped

Mechanism supported in a bounded synthetic local-filesystem validation, but evidence is not publication-grade because real traces, production baselines, concurrency, and larger ledgers were not tested.

## Recommended next action

Stop this run as no-paper useful evidence; the concrete next deepen test is to replay real agent trace corpora against SQLite WAL and an existing trace backend under the same crash/tamper harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace crash replay comparison for batched hash-chain ledgers
- Success threshold: Across at least five fixed seeds and at least 50,000 total real trace events, batch-64 hash-chain replay has prefix_ok_rate 1.0, tamper_detect_rate 1.0, p95 commit window <= 64 events, and write throughput >= 5x per-event durable hash-chain without losing replay correctness relative to SQLite WAL.
- Stop condition: Stop if any hash-chain batch-64 run violates exact committed-prefix replay, if tamper detection falls below 1.0 on valid committed-history modifications, or if throughput is not at least 2x per-event durable integrity logging on real traces.

## Evidence references

- Artifact root: `<local-path>/projects/crash-injected-agent-trace-replay-for-batched-hash-chain-l-62a9a4ee6a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

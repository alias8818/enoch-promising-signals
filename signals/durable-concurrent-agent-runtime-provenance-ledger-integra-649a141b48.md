# Durable concurrent agent-runtime provenance ledger integration

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `durable-concurrent-agent-runtime-provenance-ledger-integra-649a141b48`
Run ID: `durable-concurrent-agent-runtime-provenance-ledger-integra-649a141b48-20260516T034102937850+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Durable concurrent agent-runtime provenance ledger integration: internal_generated:durable-concurrent-agent-runtime-provenance-ledger-integra-649a141b48

## What looked useful

Across 5 fixed-seed concurrent trials, sqlite_hash_wal had 5/5 integrity passes with 0 missing events, 0 duplicates, 0 corrupt rows, and 0 hash failures at 2006 unique events/s mean throughput and 54.07 ms mean p95 latency. Across 5 crash-after-ack trials it had 5/5 recovery passes with 0 missing acknowledged keys. The unsafe no-lock control failed all trials.

## Boundaries and scale limits

Not integrated into LangGraph or a production runtime; no multi-host writers, no long-running operational workload, no realistic provenance query/replay benchmark, and no comparison against established tracing systems beyond local JSONL controls.

## Claim scope

In a local synthetic single-node agent-runtime simulation, a SQLite WAL provenance ledger with synchronous commits, idempotency keys, and hash-chain verification preserved all expected concurrent retry events and all acknowledged events after forced writer death.

## Why it stopped

Mechanism support was reproduced under local synthetic concurrency and crash-recovery tests, but Tier 4 paper-readiness was not met because the result lacks real runtime integration, representative workloads, broader baselines, and long-run robustness.

## Recommended next action

Stop this follow-up as no-paper useful evidence; controller follow-up depth is already 4, so do not recommend another autonomous deepen/retry branch.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/durable-concurrent-agent-runtime-provenance-ledger-integra-649a141b48`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

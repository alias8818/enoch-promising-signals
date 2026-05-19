# Incremental Merkle KV Ledger on Real Agent Traces

Status: `useful_signal`
Project ID: `incremental-merkle-kv-ledger-on-real-agent-traces-663a492842`
Run ID: `incremental-merkle-kv-ledger-on-real-agent-traces-663a492842-20260518T002312606692+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bc7881660028

## What looked useful

Tier 1 direct replay produced 0 root mismatches across 828 checked updates, 0 sparse-index collisions, 99.48% measured hash-work reduction, and 268.75x median update speedup versus full sparse recomputation.

## Boundaries and scale limits

Validated on 828 events and 489 unique keys from 8 local real agent trace files with a 40-bit sparse index. No adversarial mutation suite, persistence/crash recovery, proof API, concurrency, database backend, independent corpus, or million-event production-scale run was tested.

## Claim scope

A deterministic incremental sparse Merkle KV ledger can replay small real Codex/Enoch agent JSONL traces with roots identical to from-scratch recomputation after every event, while reducing local per-update hash work substantially.

## Why it stopped

Mechanism support was demonstrated on a controlled small direct test, but evidence is not paper-ready because robustness, persistence, proof APIs, and larger trace scale remain untested.

## Recommended next action

Run a bounded deepen test with adversarial trace mutation/replay cases plus durable persistence/crash-recovery checks before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adversarial Persistence Test for Incremental Merkle KV Agent Trace Ledger
- Success threshold: Clean replay has 0 root mismatches; every adversarial mutation in the suite is detected; recovered checkpoint roots match uninterrupted replay for all tested checkpoints; median incremental update time remains at least 10x faster than full recomputation.
- Stop condition: Stop as unsupported if any clean replay root mismatch occurs, any mutation class is not detected, or persisted recovery cannot reproduce uninterrupted roots.

## Evidence references

- Artifact root: `<local-path>/projects/incremental-merkle-kv-ledger-on-real-agent-traces-663a492842`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

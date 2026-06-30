# Deterministic Replay Ledger on Home Nodes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deterministic-replay-ledger-on-home-nodes-de26cb287084`
Run ID: `deterministic-replay-ledger-on-home-nodes-de26cb287084-20260526T040041019480+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/32cdf8380d92

## What looked useful

The ledger mechanism caught all injected tampering and nondeterminism, with replay around 9390 ops/s at 512 keys and 2427 ops/s at 2048 keys. Compressed ledger size was 2.9x to 3.4x larger than compressed full snapshots at 512 keys, but 0.75x the snapshot size at 2048 keys, showing a workload-dependent storage crossover rather than a universal low-overhead win.

## Boundaries and scale limits

Tested only Python stdlib synthetic traces up to 100000 operations at 512 keys plus one 10000-operation sensitivity run at 2048 keys. No real home-node software, distributed peers, crash recovery, fsync durability, adversarial network, or long-running hardware fault evidence was produced.

## Claim scope

In a synthetic single-process key-value state-machine harness, a hash-chained deterministic replay ledger detected clean replay success, local ledger tampering, and unlogged ambient nondeterminism; storage efficiency depended on state size.

## Why it stopped

Closed as no-paper useful signal: the synthetic mechanism works, but the evidence is not direct enough for a publication-grade home-node claim and storage overhead is mixed.

## Recommended next action

Run a bounded SQLite-backed crash-injection follow-up comparing replay-ledger append/recovery against incremental snapshot checkpoints on realistic home-service traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Durable SQLite Replay Ledger With Crash Injection
- Success threshold: All crash-injection recoveries preserve the last committed state; all tampering and nondeterminism injections are detected; median bytes/op is no worse than 1.25x incremental snapshots and p95 append latency overhead is below 2x baseline on at least two of three workloads.
- Stop condition: Stop if crash recovery loses committed state, if nondeterminism/tampering is not detected, or if median bytes/op exceeds 2x incremental snapshots on all workloads.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-replay-ledger-on-home-nodes-de26cb287084`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

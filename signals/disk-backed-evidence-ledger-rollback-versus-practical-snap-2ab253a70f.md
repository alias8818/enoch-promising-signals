# Disk-backed evidence-ledger rollback versus practical snapshot baselines

Status: `useful_signal`
Project ID: `disk-backed-evidence-ledger-rollback-versus-practical-snap-2ab253a70f`
Run ID: `disk-backed-evidence-ledger-rollback-versus-practical-snap-2ab253a70f-20260516T013702987292+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/40feb6f09d0c

## What looked useful

Mechanism correctness is supported and the storage/write-cost advantage is strong, but practical rollback latency is mixed and depends on rollback depth and changed-key count.

## Boundaries and scale limits

Single-host small direct benchmark only; single timing run per configuration; no crash-injection, concurrent workload, realistic locality distribution, periodic snapshot baseline, copy-on-write filesystem baseline, or confidence intervals.

## Claim scope

In a controlled SQLite key/value microbenchmark with 20,000 keys, 256-byte values, 80 mutation steps, and deterministic traces, a disk-backed inverse evidence ledger produced exact rollback and used far less storage and write overhead than per-step full database snapshots, but rollback latency was only favorable for shallow low-change rollback and was slower for ten-step or high-change rollback.

## Why it stopped

Tier 1 direct evidence is useful but not paper-ready: correctness and write/storage advantages were shown, while rollback latency was mixed and practical baselines remain incomplete.

## Recommended next action

Run a replicated medium deepen test comparing ledger-only, periodic-snapshot-plus-ledger, filesystem reflink snapshots, and full snapshots under an explicit rollback-frequency cost model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replicated hybrid snapshot versus evidence-ledger rollback cost model
- Success threshold: Hybrid ledger snapshot strategy must preserve exact rollback correctness and reduce expected total cost by at least 30% versus the best practical snapshot baseline in at least two realistic rollback-frequency regimes without increasing p95 rollback latency by more than 2x.
- Stop condition: Stop if correctness fails under crash injection, if the best practical snapshot baseline dominates expected total cost in all regimes, or if confidence intervals overlap enough that no 20% effect can be resolved.

## Evidence references

- Artifact root: `<local-path>/projects/disk-backed-evidence-ledger-rollback-versus-practical-snap-2ab253a70f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

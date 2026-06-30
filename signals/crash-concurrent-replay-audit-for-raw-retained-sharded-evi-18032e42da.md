# Crash-concurrent replay audit for raw-retained sharded evidence ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `crash-concurrent-replay-audit-for-raw-retained-sharded-evi-18032e42da`
Run ID: `crash-concurrent-replay-audit-for-raw-retained-sharded-evi-18032e42da-20260530T054003396753+0000`

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

- Parent run decision: Sharded evidence ledger with raw blob retention and replay audit: enoch://control-plane/projects/sharded-evidence-ledger-with-raw-blob-retention-and-replay-ddc426cffa/runs/sharded-evidence-ledger-with-raw-blob-retention-and-replay-ddc426cffa-20260530T015913334912+0000
- Parent run decision: Evidence ledger for 100M-agent tool-use cascade: enoch://control-plane/projects/evidence-ledger-for-100m-agent-tool-use-cascade-e0175498bcda/runs/evidence-ledger-for-100m-agent-tool-use-cascade-e0175498bcda-20260529T224504311518+0000

## What looked useful

Raw retention is strongly supported as necessary for raw evidence replay. Sharding showed a bounded average recovery advantage under the injected fault model (0.82961 mean raw recovery versus 0.76857 for monolithic raw) but the effect is seed-dependent and trades off replay throughput.

## Boundaries and scale limits

Synthetic post-write truncation/corruption rather than actual process kill, power loss, filesystem journal, or production storage behavior; Python JSONL implementation; 300,000 total written records in the faulted medium run plus a no-fault control; not a full durability or distributed-systems validation.

## Claim scope

In a deterministic local Python JSONL crash/truncation replay harness with 5 fixed seeds, 8 writers, and 20,000 acknowledged records per seed/variant, raw-retained ledgers replay surviving raw evidence while digest-only ledgers cannot; sharding improved mean raw recovery over a monolithic raw baseline but not on every seed.

## Why it stopped

Tier-2 local evidence produced a useful mixed signal but not direct publication-grade crash-concurrency evidence; the sharded variant did not consistently dominate the monolithic raw baseline across fixed seeds.

## Recommended next action

Stop paper escalation here; run a bounded direct crash follow-up with real writer processes, durable ack/fsync policies, and a fair loss-budget fault model before making any sharded-ledger durability claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct process-kill replay audit with fair loss-budget faults
- Success threshold: Across at least 10 fixed seeds, raw_sharded mean raw recovery exceeds monolith_raw by >=5 percentage points with no more than one seed worse by >2 percentage points, and both raw variants retain 100% no-fault recovery.
- Stop condition: Stop if no-fault controls show any unexplained raw replay/audit error, or if raw_sharded fails to beat monolith_raw by the threshold after the fixed-seed crash suite.

## Evidence references

- Artifact root: `<local-path>/projects/crash-concurrent-replay-audit-for-raw-retained-sharded-evi-18032e42da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

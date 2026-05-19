# Home Quorum Ledger for Small Agent Swarms

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `home-quorum-ledger-for-small-agent-swarms-16bf644875c9`
Run ID: `home-quorum-ledger-for-small-agent-swarms-16bf644875c9-20260517T211417098903+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bc7881660028

## What looked useful

Across 9 scenarios with 100 trials and 2,000 writes per trial, quorum averaged 0.862 read completeness and 0.896 alive-node durability versus baseline averages of 0.346 and 0.653, while mean write latency rose from 1.026 ms to 2.299 ms. Heavy churn showed the main failure mode: quorum commit rate fell as low as 0.140 for 7 nodes when majority availability was poor.

## Boundaries and scale limits

Synthetic only: no real network, disk fsync, recovery protocol, membership changes, concurrent process implementation, real agent traces, Byzantine faults, or adversarial partitions were tested.

## Claim scope

In a deterministic synthetic 3-7 node home-swarm model with 1% message loss and churn, majority quorum replication improves committed-entry read completeness and alive-node durability over local-only and single-hub logging, at higher latency and reduced write availability under heavy churn.

## Why it stopped

No-paper closure: this is a reproducible synthetic useful signal, not a direct systems validation.

## Recommended next action

Build a real-process localhost prototype with SQLite/WAL and quorum RPC, then replay the same churn schedule to measure fsync latency, recovery correctness, and read completeness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SQLite/WAL Local Quorum Ledger Prototype
- Success threshold: Under mild and moderate churn, quorum must reach read completeness >= 0.95 and alive-node durability >= 0.98 with mean committed-write latency < 25 ms and no committed-entry loss after crash/restart.
- Stop condition: Stop as negative if real fsync/RPC overhead exceeds 100 ms mean latency, committed entries are lost after restart, or read completeness remains below 0.90 under moderate churn.

## Evidence references

- Artifact root: `<local-path>/projects/home-quorum-ledger-for-small-agent-swarms-16bf644875c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

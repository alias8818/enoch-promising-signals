# Multi-Agent Consensus Ledger on Home Network

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-agent-consensus-ledger-on-home-network-1affaf48522d`
Run ID: `multi-agent-consensus-ledger-on-home-network-1affaf48522d-20260520T082913280651+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d99004ef738a

## What looked useful

Across 200 simulated main runs, all quorum scenarios preserved prefix safety. Good 5-node quorum consensus committed 100% of requested transactions with mean p95 latency 11.75 ms and 106.80 modeled tx/s versus centralized 7.18 ms and 196.50 tx/s. Noisy 5-node quorum consensus committed 99.998% with p95 62.51 ms and 21.67 tx/s versus centralized 39.50 ms and 39.07 tx/s. A 5-node majority partition committed 0% while remaining prefix-safe.

## Boundaries and scale limits

No physical home-network devices, real router/Wi-Fi behavior, durable fsync persistence, leader election, membership changes, Byzantine agents, NAT discovery, or long recovery tests were run. Results are simulation-only and should not be treated as full system validation.

## Claim scope

A deterministic proxy simulation supports that a 3-7 node crash-fault quorum hash-chain ledger can preserve a single committed prefix under modeled home-network latency, loss, crashes, and majority partitions, with material latency and throughput overhead versus centralized append.

## Why it stopped

Simulation-only proxy result is useful for scoping but not direct/full validation of a deployable home-network consensus ledger.

## Recommended next action

Stop this run as no-paper useful proxy evidence; the next concrete action is a bounded physical LAN validation with 5-7 devices, durable storage, and router-level fault injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Physical 5-Device Home LAN Consensus Ledger Validation
- Success threshold: For 5 nodes, all committed prefix hashes match after recovery, one follower crash does not stop progress, majority partition makes progress unavailable without divergence, sustained throughput is at least 10 tx/s, and p95 commit latency remains below 250 ms under noisy LAN conditions.
- Stop condition: Stop as negative if committed prefixes diverge, crash recovery loses committed entries, or noisy LAN throughput remains below 10 tx/s or p95 latency exceeds 250 ms in two independent runs.

## Evidence references

- Artifact root: `<local-path>/projects/multi-agent-consensus-ledger-on-home-network-1affaf48522d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

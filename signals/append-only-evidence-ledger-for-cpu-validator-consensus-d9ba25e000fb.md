# Append-Only Evidence Ledger for CPU Validator Consensus

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `append-only-evidence-ledger-for-cpu-validator-consensus-d9ba25e000fb`
Run ID: `append-only-evidence-ledger-for-cpu-validator-consensus-d9ba25e000fb-20260604T091417183286+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a224e97984d2

## What looked useful

The evidence-ledger mechanism worked for the targeted fault classes, but median overhead versus ephemeral signature verification was 16.52x. Absolute throughput remained about 8340 ledger events/s median and peak memory stayed under 95 MiB at 300 validators.

## Boundaries and scale limits

Not a full BFT consensus implementation; no real network, disk fsync durability, production key management, evidence gossip latency, commit latency, or liveness/safety proof was tested. The benchmark is CPU-only and local.

## Claim scope

In a deterministic Python toy evidence model, a signed append-only hash-chain ledger detected injected validator equivocation, rejected forged evidence and replay, and verified chain integrity for up to 300 validators and 267000 total benchmark events.

## Why it stopped

Bounded local simulation supports the evidence mechanism but does not provide direct production-consensus evidence, and the observed ledger overhead is material.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a small Tendermint/HotStuff-style simulator that measures disk-backed append/fsync, partition reconciliation latency, and finality impact.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Disk-backed evidence ledger in a partitioned BFT simulator
- Success threshold: Detect all injected equivocations after reconciliation, preserve expected safety behavior in within-threshold runs, and keep p95 commit latency overhead below 25 percent for disk-backed ledger mode at 31 validators.
- Stop condition: Stop if disk-backed ledger mode misses any injected equivocation after reconciliation, corrupts/reorders the append chain, or exceeds 2x p95 commit latency overhead at 31 validators.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-evidence-ledger-for-cpu-validator-consensus-d9ba25e000fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

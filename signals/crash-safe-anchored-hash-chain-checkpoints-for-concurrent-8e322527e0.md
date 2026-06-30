# Crash-safe anchored hash-chain checkpoints for concurrent agent ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `crash-safe-anchored-hash-chain-checkpoints-for-concurrent-8e322527e0`
Run ID: `crash-safe-anchored-hash-chain-checkpoints-for-concurrent-8e322527e0-20260601T043610962529+0000`

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

- Parent run decision: Tamper-Evident Agent Ledger via Hash Chain on CPU: enoch://control-plane/projects/tamper-evident-agent-ledger-via-hash-chain-on-cpu-823851a32ef2/runs/tamper-evident-agent-ledger-via-hash-chain-on-cpu-823851a32ef2-20260531T143626231331+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b744dcbcced0

## What looked useful

The anchored hash-chain checkpoint mechanism passed 50/50 readiness-gated crash trials with 0 recovery failures, min 55 and median 170 valid records per trial, and 37 detected torn/corrupt unanchored tails. A preceding 100-trial batch also had 0 failures but included some no-op startup kills.

## Boundaries and scale limits

Short single-machine filesystem test only; no real power-loss rig, no multi-host or network filesystem writers, no storage-controller reordering study, no high-throughput benchmark, no Byzantine-writer model, and no long-running production agent ledger trace.

## Claim scope

In a local Python harness with four concurrent writer processes, advisory file locking, SHA-256 hash-chain records, and fsynced atomic checkpoint anchors every 8 records, recovery after SIGKILL plus unanchored tail damage accepted only hash-consistent prefixes covering the latest durable anchor across 50 readiness-gated Tier 1 trials.

## Why it stopped

Tier 1 mechanism support is useful but not paper-ready; this run used a controlled local harness and artificial unanchored tail mutation rather than real power-loss or broader storage/concurrency validation.

## Recommended next action

Run a bounded deepen test on a real crash/power-fault or filesystem fault-injection setup comparing anchored recovery against a baseline ledger without hash-chain anchors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Filesystem fault-injection comparison for anchored hash-chain ledger recovery
- Success threshold: Anchored design has 0 unrecoverable latest-anchor violations and detects all injected tail corruptions, while the baseline shows either undetected corruption or a larger ambiguous recovery window under the same faults.
- Stop condition: Stop if any anchored trial cannot recover a prefix covering the latest durable anchor under the documented durability assumptions, or if the baseline and anchored design are indistinguishable on corruption detection and recovery ambiguity.

## Evidence references

- Artifact root: `<local-path>/projects/crash-safe-anchored-hash-chain-checkpoints-for-concurrent-8e322527e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

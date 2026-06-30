# Fault-injected torn-write validation of strict framing versus checksummed JSONL

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `fault-injected-torn-write-validation-of-strict-framing-ver-29b0877aab`
Run ID: `fault-injected-torn-write-validation-of-strict-framing-ver-29b0877aab-20260520T053509281245+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Replay real local-agent traces with crash-injected rollback ledger commits: enoch://control-plane/projects/replay-real-local-agent-traces-with-crash-injected-rollbac-81dbb9f5e9/runs/replay-real-local-agent-traces-with-crash-injected-rollbac-81dbb9f5e9-20260520T052008294008+0000
- Parent run decision: Process-kill validation of strict-framed rollback ledger recovery: enoch://control-plane/projects/process-kill-validation-of-strict-framed-rollback-ledger-r-9ba167d51d/runs/process-kill-validation-of-strict-framed-rollback-ledger-r-9ba167d51d-20260520T052743264221+0000

## What looked useful

The integrity benefit comes from per-record checksumming and valid-prefix recovery semantics, not from binary strict framing alone. Naive JSONL silently accepted corrupted payloads under bit flips and stale splices, while both checksummed formats did not in the observed trials.

## Boundaries and scale limits

This did not test real filesystem power-loss traces, fsync policies, concurrent writers, device sector atomicity, or production recovery integration. The result is bounded local fault-injection evidence, not publication-grade operational validation.

## Claim scope

In a deterministic local append-only log harness with truncation, zero-tail, stale-splice, and single-bit-flip faults, strict binary framing and correctly checksummed JSONL both produced zero accepted corrupt payloads; strict framing was smaller and about 2x faster to scan.

## Why it stopped

Bounded direct fault injection found no corruption-detection advantage for strict framing over checksummed JSONL, only size and throughput advantages; the remaining stronger claim would require real filesystem/power-loss validation rather than another synthetic local proxy at follow-up depth 3.

## Recommended next action

Stop this follow-up: the bounded local evidence does not support a paper claim that strict framing materially improves torn-write integrity over correctly checksummed JSONL; use strict framing only for space/scan-speed reasons unless real crash-trace evidence shows a new gap.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/fault-injected-torn-write-validation-of-strict-framing-ver-29b0877aab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

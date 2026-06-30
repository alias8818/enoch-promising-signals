# Real-harness Merkle evidence ledger durability and verifier benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-harness-merkle-evidence-ledger-durability-and-verifie-0a17c8c23b`
Run ID: `real-harness-merkle-evidence-ledger-durability-and-verifie-0a17c8c23b-20260605T190538505054+0000`

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

- Parent run decision: CPU-bound evidence ledger with append-only merkle trees for agent reliability: enoch://control-plane/projects/cpu-bound-evidence-ledger-with-append-only-merkle-trees-for-agent-reliability-ececf8f8d6bc/runs/cpu-bound-evidence-ledger-with-append-only-merkle-trees-for-agent-reliability-ececf8f8d6bc-20260605T140438459761+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/205a2aa29d04

## What looked useful

Tier 1 direct harness met the threshold: per-entry fsync append throughput was 756.29 entries/s, recovery reproduced the snapshot root at 70,515.68 entries/s, corruption was detected at line 2501, and proof verification succeeded for 1,000/1,000 samples at 35,291.38 proofs/s. Batched fsync every 100 records improved append throughput to 11,987.38 entries/s with the same root and correctness checks.

## Boundaries and scale limits

Single-process CPU-only local filesystem harness; 5,000 records of 512 bytes; no true power-loss crash injection, concurrent writers, external anti-rollback anchor, remote storage, or long-duration scale test.

## Claim scope

A small local filesystem-backed Merkle evidence ledger can append and fsync 5,000 deterministic evidence records, recover the committed root after process restart, detect one byte-level log mutation, and verify 1,000 sampled inclusion proofs with zero failures.

## Why it stopped

No-paper useful signal: the scoped Tier 1 direct harness supports the mechanism, but publication-grade durability needs crash-injection, rollback, concurrency, and longer-scale validation.

## Recommended next action

Run a bounded crash-injection follow-up that kills the ledger during append and snapshot phases across many trials, then verifies prefix recovery, committed-root consistency, and anti-rollback behavior with an external root anchor.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-injected Merkle evidence ledger recovery and anti-rollback test
- Success threshold: 100/100 crash-injection trials recover to a valid prefix or fail closed with an explicit corruption error; 100% rollback detection against the anchor; 0/1,000 proof verification failures.
- Stop condition: Stop on any silent divergent recovered root, any accepted rollback against the anchor, or more than one unexplained recovery failure after reproducing with saved logs.

## Evidence references

- Artifact root: `<local-path>/projects/real-harness-merkle-evidence-ledger-durability-and-verifie-0a17c8c23b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

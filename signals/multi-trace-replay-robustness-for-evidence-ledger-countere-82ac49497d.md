# Multi-trace replay robustness for evidence ledger counterexample logging

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-trace-replay-robustness-for-evidence-ledger-countere-82ac49497d`
Run ID: `multi-trace-replay-robustness-for-evidence-ledger-countere-82ac49497d-20260607T070239383007+0000`

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

- Parent run decision: Agent reliability via evidence ledger and counterexample logging: enoch://control-plane/projects/agent-reliability-via-evidence-ledger-and-counterexample-logging-d150c89c3693/runs/agent-reliability-via-evidence-ledger-and-counterexample-logging-d150c89c3693-20260605T161915922832+0000
- Parent run decision: Real trace replay for evidence ledger and counterexample logging: enoch://control-plane/projects/real-trace-replay-for-evidence-ledger-and-counterexample-l-23a59b1dc1/runs/real-trace-replay-for-evidence-ledger-and-counterexample-l-23a59b1dc1-20260605T195848357432+0000

## What looked useful

Full trace-bound hash-chain dedupe reduced corrupt acceptance from 69.54% in the append-log baseline to 0.36% and improved exact replay from 37.98% to 42.48%, but counterexample recall fell from 97.45% to 65.40%. Removing trace binding degraded relabel robustness, while removing chain continuity preserved recall, pointing to chain-continuity handling as the main failure mode.

## Boundaries and scale limits

20 fixed seeds, 250 traces per seed, 40 events per trace, synthetic fault injection only. No production ledger traces, distributed writers, crash recovery, real database compaction, or adversarial cryptographic audit were tested.

## Claim scope

Synthetic medium-scale multi-trace replay benchmark with fixed seeds, append-log baseline, and ablations for trace binding, chain checking, and dedupe. The result supports trace-bound hashing for corrupt-record detection but does not support the tested full-chain ledger as a high-recall counterexample logger under upstream faults.

## Why it stopped

Medium fixed-seed evidence is mixed: the mechanism strongly detects corrupt records, but the tested full-chain ledger loses too much counterexample recall to support the original robustness claim.

## Recommended next action

Stop this run as no-paper useful signal; test a segmented or checkpointed chain replay variant that can resume validation after invalid spans without accepting corrupt records.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Segmented chain recovery for high-recall evidence-ledger counterexample replay
- Success threshold: Invalid detection >= 0.98, corrupt accept <= 0.01, counterexample precision >= 0.99, and counterexample recall within 2 percentage points of baseline_append_jsonl on the mixed-fault benchmark.
- Stop condition: Stop as negative if segmented replay still loses more than 10 percentage points of counterexample recall versus baseline or if corrupt accept rises above 1%.

## Evidence references

- Artifact root: `<local-path>/projects/multi-trace-replay-robustness-for-evidence-ledger-countere-82ac49497d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

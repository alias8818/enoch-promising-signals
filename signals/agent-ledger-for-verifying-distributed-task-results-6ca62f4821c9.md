# Agent ledger for verifying distributed task results

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-ledger-for-verifying-distributed-task-results-6ca62f4821c9`
Run ID: `agent-ledger-for-verifying-distributed-task-results-6ca62f4821c9-20260527T161543864987+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/05d9de47723a

## What looked useful

Ledger integrity and tamper detection passed in every run, but ledger-only single-result acceptance allowed wrong results at approximately the faulty-worker rate: 20.89% wrong acceptance at 20% random faulty workers and 38.89-38.99% at 40%. Redundant quorum eliminated wrong majorities under independent random faults in these seeds but failed under systematic/colluding faults, accepting wrong majorities at 10.93% for 3 replicas and 6.12% for 5 replicas with 20% faulty workers.

## Boundaries and scale limits

Synthetic CPU-only simulator; no real distributed executor, network faults, public-key identity, key compromise, adaptive adversary, model/tool workload, or production verifier cost. Quorum results depend strongly on independent versus systematic/colluding fault assumptions.

## Claim scope

In a deterministic synthetic distributed-task simulator with 30 seeded runs per condition, 2,000 tasks per run, 50 workers, HMAC-signed hash-chain ledger entries, and injected faulty workers, a ledger verifies provenance/tamper evidence but does not verify semantic task correctness when accepting a single signed result.

## Why it stopped

Synthetic evidence early-falsifies the standalone ledger-as-correctness-verifier claim; it supports only the narrower provenance/tamper-evidence role without direct real-system validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should implement ledger-backed challenge tasks in a real local distributed executor and compare against quorum-only and audit-only baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ledger-backed challenge tasks in a real distributed executor
- Success threshold: Across at least 30 seeded runs of 1,000 or more tasks, ledger-backed challenge tasks keep wrong accepted results below 1% under 20% faulty workers and reduce wrong acceptance by at least 5x versus the best non-ledger baseline without more than 2x verification overhead.
- Stop condition: Stop if challenge-task ledger policy cannot beat quorum-only or audit-only baselines on wrong accepted result rate at comparable overhead, or if real executor overhead dominates task runtime by more than 2x.

## Evidence references

- Artifact root: `<local-path>/projects/agent-ledger-for-verifying-distributed-task-results-6ca62f4821c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

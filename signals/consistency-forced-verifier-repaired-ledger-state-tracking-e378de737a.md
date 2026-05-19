# Consistency-forced verifier-repaired ledger state tracking

Status: `useful_signal`
Project ID: `consistency-forced-verifier-repaired-ledger-state-tracking-e378de737a`
Run ID: `consistency-forced-verifier-repaired-ledger-state-tracking-e378de737a-20260518T172536057060+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Consistency-forced verifier-repaired ledger state tracking: internal_generated:consistency-forced-verifier-repaired-ledger-state-tracking-e378de737a

## What looked useful

Verifier repair is valuable when exact transaction deltas are available, but consistency-forced learned repair is insufficient by itself for exact ledger state tracking in this benchmark.

## Boundaries and scale limits

Five fixed seeds, 6000 synthetic training sequences per seed, 1200 test sequences per length, six accounts, train length 24, test lengths 24/48/72. No natural-language ledger traces, no noisy parser, no LLM agent outputs, and no production-scale ledger workload.

## Claim scope

On a synthetic structured multi-account transfer ledger, exact transaction-verifier repair perfectly recovers ledger state from known transaction deltas, while learned delta-based repair only reduces MAE and invariant residuals versus a learned GRU state baseline and does not achieve exact final ledger recovery.

## Why it stopped

No-paper mixed result: oracle verifier repair succeeds on structured synthetic records, but the model-in-the-loop repair path does not meet exact ledger tracking thresholds.

## Recommended next action

Run one bounded deepen test with noisy or natural-language transaction extraction before considering any paper claim; stop this run because the current evidence is synthetic and the learned repair path failed exact recovery.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy transaction extraction for verifier-repaired ledger state tracking
- Success threshold: At least 50 percentage-point improvement in final exact ledger accuracy over direct learned state tracking at length 24, positive improvement at length 48, and transaction extraction F1 >= 0.98.
- Stop condition: Stop if extraction F1 is below 0.95 or verifier repair fails to improve final exact accuracy over the direct baseline on at least 4 of 5 fixed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/consistency-forced-verifier-repaired-ledger-state-tracking-e378de737a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

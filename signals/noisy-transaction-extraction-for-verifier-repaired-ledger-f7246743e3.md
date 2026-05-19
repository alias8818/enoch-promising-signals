# Noisy transaction extraction for verifier-repaired ledger state tracking

Status: `useful_signal`
Project ID: `noisy-transaction-extraction-for-verifier-repaired-ledger-f7246743e3`
Run ID: `noisy-transaction-extraction-for-verifier-repaired-ledger-f7246743e3-20260518T173036351660+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Noisy transaction extraction for verifier-repaired ledger state tracking: internal_generated:noisy-transaction-extraction-for-verifier-repaired-ledger-f7246743e3

## What looked useful

Verifier state consistency is useful for repairing ledger state but creates a tradeoff against exact transaction extraction, especially amount recovery. Default verifier repair reduced final balance L1 by about 3749.8 versus no-state ablation but reduced exact accuracy by about 8.2 percentage points.

## Boundaries and scale limits

No real ledger corpus, no LLM/OCR extraction model, no adversarial noise, no multi-transaction snapshot batching, and no learned adaptive verifier. Authoritative corrected runs cover about 16,960 synthetic transactions plus additional logged exploratory runs.

## Claim scope

Synthetic 24-account ledger streams with 200 transactions per seed, noisy transaction fields, and partial noisy state snapshots. Verifier repair improves final ledger-state tracking and sometimes endpoints, but does not reliably improve exact transaction recovery over a no-state extraction ablation.

## Why it stopped

Bounded synthetic validation directly tested exact transaction recovery and found that verifier-repaired state scoring improves state tracking but fails to beat the no-state extraction ablation on exact transactions.

## Recommended next action

Stop this line as a positive transaction-extraction claim; only pursue a bounded adaptive-gating follow-up if the target is to preserve exact extraction while selectively using verifier state evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive verifier gating for exact transaction recovery
- Success threshold: Adaptive verifier exact_acc exceeds verifier_no_state_ablation by at least 0.02 absolute with a 95% paired CI excluding zero, while final_balance_l1 remains at least 20% lower than the no-state ablation.
- Stop condition: Stop if exact_acc fails to beat no-state by 0.01 absolute on a 10-seed medium probe or if amount MAE worsens by more than 10% while state error improves.

## Evidence references

- Artifact root: `<local-path>/projects/noisy-transaction-extraction-for-verifier-repaired-ledger-f7246743e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

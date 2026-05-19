# Hard Unsupported-Claim Ledger Audit Across Models

Status: `useful_signal`
Project ID: `hard-unsupported-claim-ledger-audit-across-models-bac6248a0f`
Run ID: `hard-unsupported-claim-ledger-audit-across-models-bac6248a0f-20260519T134832740838+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Hard Unsupported-Claim Ledger Audit Across Models: internal_generated:hard-unsupported-claim-ledger-audit-across-models-bac6248a0f

## What looked useful

The ledger reached F1 1.000 on scored slot-valued claims, while answer-level baseline F1 was 0.570, lexical baseline F1 was 0.190, and shuffled-context control F1 was 0.406. The controlled mixed ablation showed the localization advantage: ledger F1 1.000 vs answer-level F1 0.500.

## Boundaries and scale limits

36 synthetic source items, 972 generations, 1,823 scored slot-valued claims; small cached models only; labels and ledger rely on a controlled value universe, not independent open-domain semantic adjudication.

## Claim scope

In a deterministic synthetic slot-valued factual QA audit, a claim-level unsupported-claim ledger localized unsupported slot-value claims across three small models and three fixed seeds better than answer-level and lexical baselines.

## Why it stopped

No-paper closure: medium synthetic evidence supports the mechanism, but the verifier is not independent of the controlled slot-value labeling and does not validate open-domain unsupported claims.

## Recommended next action

Run a natural-claim follow-up on FEVER/SciFact-style evidence with an independent verifier or human-labeled claim support labels; stop here for paper gating because this run is synthetic slot-oracle evidence only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural Evidence Claim-Ledger Audit with Independent Verification
- Success threshold: Claim-ledger unsupported/localization F1 exceeds both answer-level and lexical baselines by >=0.10 absolute on each dataset, with bootstrap 95% CI lower bound above the best baseline on pooled claims.
- Stop condition: Stop negative if the ledger fails to beat the best baseline by 0.10 absolute F1 on either dataset or if independent verification shows precision below 0.75.

## Evidence references

- Artifact root: `<local-path>/projects/hard-unsupported-claim-ledger-audit-across-models-bac6248a0f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Bounded ablation of verifier-repaired ledgers on small-model state tracking

Status: `useful_signal`
Project ID: `bounded-ablation-of-verifier-repaired-ledgers-on-small-mod-3dfb92907f`
Run ID: `bounded-ablation-of-verifier-repaired-ledgers-on-small-mod-3dfb92907f-20260518T172032969612+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3a12a50e16d3

## What looked useful

Verifier-repaired ledgers matched clean-ledger IID exact accuracy within 0.002 and beat unrepaired noisy ledgers by 0.679 exact accuracy, but long-length OOD exact accuracy remained near 0.05 for all ledger conditions.

## Boundaries and scale limits

Only 3 seeds, synthetic symbolic data, deterministic repair from the operation stream, small Transformer, train lengths 8-16, OOD lengths 32-48, no natural-language ledgers, no learned verifier, and no large-model evaluation.

## Claim scope

A tiny causal Transformer on a synthetic 4-slot modulo-3 state-tracking task benefits strongly from deterministic verifier repair of corrupted ledger tokens on in-distribution sequence lengths.

## Why it stopped

No-paper closure: this Tier 1 direct test supports an in-distribution repair mechanism but fails the stronger length-generalization criterion needed for a bounded paper claim.

## Recommended next action

Run a bounded deepen test that prevents trivial final-ledger copying and requires consistency use across time, then require repaired-ledger OOD exact accuracy >=0.80 and >=0.25 above noisy-ledger control before further escalation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Consistency-forced verifier-repaired ledger state tracking
- Success threshold: Repaired-ledger OOD exact accuracy >=0.80, repaired minus noisy OOD exact accuracy >=0.25, and repaired IID exact accuracy within 0.05 of clean ledger across 3 seeds.
- Stop condition: Stop as unsupported if repaired-ledger OOD exact accuracy remains below 0.50 or the repaired-minus-noisy OOD exact gain is below 0.10 across 3 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-ablation-of-verifier-repaired-ledgers-on-small-mod-3dfb92907f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

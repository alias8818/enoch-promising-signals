# Pointer-head small transformer test for exact anchor-ledger retrieval

Status: `useful_signal`
Project ID: `pointer-head-small-transformer-test-for-exact-anchor-ledge-306a5a9bd4`
Run ID: `pointer-head-small-transformer-test-for-exact-anchor-ledge-306a5a9bd4-20260517T035823312246+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Pointer-head small transformer test for exact anchor-ledger retrieval: internal_generated:pointer-head-small-transformer-test-for-exact-anchor-ledge-306a5a9bd4

## What looked useful

The shifted pointer-copy mechanism is strongly useful for trained-length exact anchor-ledger retrieval and the no-shift ablation collapses, but the same setup does not learn length-robust retrieval.

## Boundaries and scale limits

Evidence is synthetic-only, small-model only, and length-limited. The pointer model failed extrapolation to unseen 32- and 64-pair ledgers, so this does not support a broad long-context or natural-document retrieval claim.

## Claim scope

On fresh synthetic 16-pair anchor-ledger sequences, a 628k-parameter transformer with a shifted pointer-copy head reached 100% exact value retrieval across seeds 11, 22, and 33 after 2,200 steps, while a 595k-parameter dense transformer baseline reached 6.26% at 2,200 steps and 7.56% after a 10,000-step baseline check.

## Why it stopped

Tier 2 evidence supports the trained-length mechanism but directly falsifies a broader length-general retrieval claim in this setup.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should test variable-length training with relative or rotary positions before any paper gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Variable-length pointer-copy transformer for length-robust anchor-ledger retrieval
- Success threshold: Pointer-copy model achieves at least 95% mean exact accuracy and at least 95% mean pointer-position accuracy on held-out 16, 32, and 64 pair ledgers across three fixed seeds, with at least a 20 percentage point gap over dense and no-shift baselines.
- Stop condition: Stop if the pointer-copy model remains below 80% exact accuracy on 32-pair held-out ledgers after the planned mixed-length training budget or if the no-shift ablation matches the full pointer model within 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/pointer-head-small-transformer-test-for-exact-anchor-ledge-306a5a9bd4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

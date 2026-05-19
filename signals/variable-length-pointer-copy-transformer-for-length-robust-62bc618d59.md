# Variable-length pointer-copy transformer for length-robust anchor-ledger retrieval

Status: `useful_signal`
Project ID: `variable-length-pointer-copy-transformer-for-length-robust-62bc618d59`
Run ID: `variable-length-pointer-copy-transformer-for-length-robust-62bc618d59-20260517T041433323304+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Variable-length pointer-copy transformer for length-robust anchor-ledger retrieval: internal_generated:variable-length-pointer-copy-transformer-for-length-robust-62bc618d59

## What looked useful

Across 3 seeds, pointer-copy exact accuracy was 100% at 32 and 64 entries after training on 8-32 entries, versus 5.9-6.0% for standard baselines at 32 entries and 3.7-4.0% at 64 entries. The no-match pointer ablation stayed near baseline, supporting the query-key pointer mechanism. Robustness failed at 128 and 192 entries.

## Boundaries and scale limits

Validation is synthetic, uses 0.6-0.7M-parameter models, trains for 1200 steps over generated ledgers, and does not test natural-language retrieval, pretrained LMs, or datacenter-scale training. The pointer-copy model drops to 43.9% mean exact accuracy at 4x length and 32.2% at 6x length.

## Claim scope

On a synthetic anchor-ledger retrieval task with 8-32 training entries, a 0.66M-parameter pointer-copy transformer achieves reproducible exact retrieval in-range and at 2x train length, outperforming standard transformer baselines and a no-match pointer ablation.

## Why it stopped

No-paper closure: direct seeded validation supports the pointer-copy mechanism but falsifies the stronger length-robust claim at 4x-6x extrapolation under the tested setup.

## Recommended next action

Run one bounded deepen test of a length curriculum or pointer normalization change, requiring at least 90% exact accuracy at 4x train length across 3 seeds against the same baselines and no-match ablation; otherwise stop the line as not length-robust.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length-curriculum pointer-copy anchor-ledger retrieval at 4x extrapolation
- Success threshold: Mean exact accuracy at 128 entries is at least 90% across 3 seeds, 32-entry in-range accuracy remains at least 99%, and the full pointer model beats the no-match ablation by at least 50 percentage points at 128 entries.
- Stop condition: Stop if the curriculum or normalization variant is below 90% mean exact accuracy at 128 entries after the same 1200-step budget, or if gains are not specific to the query-key pointer path.

## Evidence references

- Artifact root: `<local-path>/projects/variable-length-pointer-copy-transformer-for-length-robust-62bc618d59`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

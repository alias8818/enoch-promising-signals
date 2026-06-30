# Real-Corpus Curation Ladder for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-corpus-curation-ladder-for-tiny-pretraining-9b0786d575`
Run ID: `real-corpus-curation-ladder-for-tiny-pretraining-9b0786d575-20260613T133121915063+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Curation Ladder for 50M-Token Tiny Pretraining: enoch://control-plane/projects/curation-ladder-for-50m-token-tiny-pretraining-4d95feb1799f/runs/curation-ladder-for-50m-token-tiny-pretraining-4d95feb1799f-20260613T130700601117+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3c2469b6e979

## What looked useful

Cleaner-looking top-quality selections were less representative of validation/test byte distributions and produced 6.58% worse validation loss and 7.17% worse test loss than random selection in the longer confirmation.

## Boundaries and scale limits

Test used WikiText-2 only, byte-level tokenization, a tiny 3-layer Transformer, 350k training bytes per condition, 2000 training steps, and three random seeds; it does not settle larger subword-tokenized or web-scale pretraining.

## Claim scope

In a controlled tiny next-byte Transformer pretraining test on WikiText-2, a naive real-corpus curation ladder based on length, lexical quality, and exact dedup did not improve held-out loss over equal-token random selection.

## Why it stopped

Tier 1 direct test falsified the stated useful-signal threshold rather than validating the naive curation ladder.

## Recommended next action

Stop this simple-ladder hypothesis; if continuing locally, test a representativeness-constrained curation rule against the same random baseline and threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Representativeness-Constrained Curation for Tiny WikiText Pretraining
- Success threshold: Representativeness-constrained curation improves mean validation loss by at least 1.5% versus random and has mean test loss no worse than random.
- Stop condition: Stop if the constrained curation condition is not better than random on validation or is worse than random on test after the same 2000-step budget.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-curation-ladder-for-tiny-pretraining-9b0786d575`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

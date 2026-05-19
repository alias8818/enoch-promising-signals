# Real-Dataset Small-Model Evidence-Ledger Jury Benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-dataset-small-model-evidence-ledger-jury-benchmark-4e95f7d83d`
Run ID: `real-dataset-small-model-evidence-ledger-jury-benchmark-4e95f7d83d-20260514T192756759078+0000`

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

- Internal Enoch project: Real-Dataset Small-Model Evidence-Ledger Jury Benchmark: internal_generated:real-dataset-small-model-evidence-ledger-jury-benchmark-4e95f7d83d

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct Tier 2 validation on real 20 Newsgroups tasks found mechanism support but failed the paper gate: ledger jury macro-F1 0.8575 versus baseline 0.8808, 0/9 paired wins over baseline, and ECE 0.1293 versus baseline 0.0665.

## Recommended next action

Stop paper preparation for this run; the Tier 2 real-data benchmark supports the ledger mechanism but is a no-paper result because the ledger jury trails the full-feature baseline by 2.33 macro-F1 points and has worse calibration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Evidence-Ledger Jury With Larger Real-Data Coverage
- Success threshold: Ledger jury mean macro-F1 within 0.01 of the strong baseline or better, ECE no more than 0.02 worse than baseline, positive paired wins over uniform and permuted-ledger controls on at least 80% of runs, and ledger-erasure confidence drop at least 0.10 above random-token erasure.
- Stop condition: Stop as negative if the calibrated ledger jury remains more than 0.01 macro-F1 below the strong baseline or has ECE more than 0.02 worse after 5 datasets and 5 fixed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-dataset-small-model-evidence-ledger-jury-benchmark-4e95f7d83d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

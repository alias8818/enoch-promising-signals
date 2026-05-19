# Real Small-Model Evidence-Ledger Jury Benchmark

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `real-small-model-evidence-ledger-jury-benchmark-0ba0c258c3`
Run ID: `real-small-model-evidence-ledger-jury-benchmark-0ba0c258c3-20260514T192236774233+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/13c56c7c9b90

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Controlled small-model evidence was mechanism-supportive but failed the preregistered replicate/aggregate threshold: seed 7 passed, seed 11 failed, and aggregate ledger_jury gain was +0.09375 versus the required +0.10. This is not full validation.

## Recommended next action

Stop this run as a no-paper mixed Tier 1 result; run one bounded deepen follow-up on a real evidence-grounded benchmark with direct, ledger, and ledger-jury protocols.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Dataset Small-Model Evidence-Ledger Jury Benchmark
- Success threshold: ledger_jury must exceed direct accuracy by >= 0.10 on aggregate and on a held-out replicate/fold, with parse rate >= 0.95 and ledger_jury outperforming ledger-only by >= 0.02 or showing lower variance.
- Stop condition: Stop if the real-dataset aggregate gain is below +0.05, parse rate is below 0.95 after prompt repair, or ledger_jury does not improve over ledger-only.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-model-evidence-ledger-jury-benchmark-0ba0c258c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

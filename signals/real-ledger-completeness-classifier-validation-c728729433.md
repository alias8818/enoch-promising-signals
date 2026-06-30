# Real-Ledger Completeness Classifier Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-ledger-completeness-classifier-validation-c728729433`
Run ID: `real-ledger-completeness-classifier-validation-c728729433-20260610T232531561216+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence-Ledger Completeness Classifier on CPU: enoch://control-plane/projects/evidence-ledger-completeness-classifier-on-cpu-e3e8b452fd07/runs/evidence-ledger-completeness-classifier-on-cpu-e3e8b452fd07-20260610T193030310119+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc2b9d07cee3

## What looked useful

On public Ledger-format files, formal structural completeness checks caught missing date, missing payee, dropped posting, missing account, over-missing-amount, and explicit single-commodity imbalance corruptions with 0 FP and 0 FN over 7,014 final test cases.

## Boundaries and scale limits

Single plaintext-accounting ecosystem, mutation-derived incomplete cases, no proprietary ERP exports, no independent human labels, no noisy CSV/OCR ingestion, and limited multi-commodity balance handling.

## Claim scope

A dependency-free structural classifier correctly separated complete Ledger-format transactions from controlled completeness-breaking corruptions on 1,377 eligible complete transactions parsed from public Ledger project inputs.

## Why it stopped

Tier 1 direct controlled test supports the mechanism for Ledger-format structural completeness, but evidence remains mutation-derived and too narrow for publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up on heterogeneous CSV/ERP-style ledger exports with independent labels or format-specific controlled corruptions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Heterogeneous Ledger Completeness Classifier Validation
- Success threshold: Macro-F1 >= 0.95, false-negative rate <= 1%, and no corruption family with recall below 0.90 on at least 500 complete originals or all available records if fewer exist.
- Stop condition: Stop if any format has false-negative rate > 5% after one rule clarification pass, or if available public data cannot support at least two non-Ledger schemas.

## Evidence references

- Artifact root: `<local-path>/projects/real-ledger-completeness-classifier-validation-c728729433`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

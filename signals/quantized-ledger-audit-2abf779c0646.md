# Quantized Ledger Audit

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `quantized-ledger-audit-2abf779c0646`
Run ID: `quantized-ledger-audit-2abf779c0646-20260521T230421054891+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2eeb37ddb77e

## What looked useful

Exact-cent audit recall averaged 0.924. Best quantized recall was log 8-bit at 0.496, and small imbalance flag rate dropped from 1.000 exact to 0.046 for log 8-bit and 0.009 for uniform 8-bit. Duplicate detection survived quantization, and log 8-bit preserved balanced outlier detection, but amount-only quantization failed the core ledger-balance audit mechanism.

## Boundaries and scale limits

20 trials of 50,000 synthetic transactions each, 500 accounts, four injected anomaly classes, CPU-only NumPy implementation. No real ledger data, production audit controls, adversarial data, or storage-system benchmark was tested.

## Claim scope

On a reproducible synthetic double-entry ledger benchmark, replacing exact-cent signed amounts with 8-bit or 4-bit reconstructed quantized amounts is not sufficient for basic audit anomaly detection, mainly because quantization tolerance masks transaction imbalances.

## Why it stopped

Proxy synthetic evidence, not full real-ledger validation, showed that low-bit reconstructed amounts erase most imbalance detections under the tested audit rules.

## Recommended next action

Stop this amount-only quantized ledger audit line as an early synthetic falsification; a bounded follow-up should test a hybrid design that keeps quantized analytic features but adds exact balance residuals or commitments.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Quantized Ledger Audit With Exact Balance Residuals
- Success threshold: Hybrid method recall >= 0.90 overall, small imbalance flag rate >= 0.90, false-positive rate no worse than exact-cent baseline by more than 2 percentage points, and at least 2x nominal amount-storage reduction versus int64 cents.
- Stop condition: Stop if hybrid recall remains below 0.80 or if residual/checksum overhead removes the nominal compression advantage below 2x.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-ledger-audit-2abf779c0646`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

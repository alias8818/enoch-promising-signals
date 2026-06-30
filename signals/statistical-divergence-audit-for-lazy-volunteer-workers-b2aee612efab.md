# Statistical divergence audit for lazy volunteer workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `statistical-divergence-audit-for-lazy-volunteer-workers-b2aee612efab`
Run ID: `statistical-divergence-audit-for-lazy-volunteer-workers-b2aee612efab-20260630T155843643264+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c910545da46

## What looked useful

Distributional audits can flag several simple lazy-worker shortcuts, especially with larger windows, but an OR-combined detector exceeded the nominal 1% false-positive target and was weak against noise-preserving lazy approximations.

## Boundaries and scale limits

No real volunteer-computing traces, no real model/task outputs, no adaptive adversary, and no full family-wise false-positive recalibration. CPU-only run with 600 honest calibration windows and 400 evaluation trials per condition.

## Claim scope

Synthetic residual-stream audit for volunteer workers over windows of 64, 128, and 256 tasks. The audit detects stale replay, partial skipping, and quantized submissions in this toy model, but not low-effort noise that preserves the broad residual distribution.

## Why it stopped

Synthetic mechanism probe was mixed: strong detection for stale replay, partial skip, and quantization, but weak low-effort-noise detection and above-target combined false positives prevent a paper-positive claim.

## Recommended next action

Stop as no-paper useful signal; run a bounded deepen test with family-wise threshold calibration and either real volunteer traces or an adaptive synthetic lazy worker that matches marginal residual statistics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Family-wise calibrated divergence audit against adaptive lazy workers
- Success threshold: False-positive rate <= 1.5% on held-out honest workers and detection >= 80% for at least two adaptive lazy modes at n <= 256.
- Stop condition: Stop if family-wise calibration pushes adaptive-lazy detection below 50% at n=256 or if no real/adaptive trace source can be constructed without private external evidence.

## Evidence references

- Artifact root: `<local-path>/projects/statistical-divergence-audit-for-lazy-volunteer-workers-b2aee612efab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

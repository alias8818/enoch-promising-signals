# Calibrated confidence gates for stable local cascade routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `calibrated-confidence-gates-for-stable-local-cascade-routi-4973719f64`
Run ID: `calibrated-confidence-gates-for-stable-local-cascade-routi-4973719f64-20260518T163004164115+0000`

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

- Internal Enoch project: Calibrated confidence gates for stable local cascade routing: internal_generated:calibrated-confidence-gates-for-stable-local-cascade-routi-4973719f64

## What looked useful

Calibration improved probability semantics on some datasets and reduced strong-call rate for fixed semantic thresholds, but retuned monotone calibration often produced the same routing as raw confidence and the clearest hierarchy, digits, still breached the target in most seeds.

## Boundaries and scale limits

Classical sklearn classifiers were used as a local cascade proxy, not LLM small/large routing. Datasets are small to medium; breast_cancer has a confounded strong baseline where the cheap model often wins. No production latency, API fallback, or large language model benchmark was measured.

## Claim scope

On three real sklearn classification datasets with fixed seeds, local cheap-to-strong cascades, validation-tuned and fixed 0.95 confidence gates, calibration alone did not reliably preserve strong-model accuracy or improve route stability. It did show limited fixed-threshold cost savings versus naive raw 0.95 confidence.

## Why it stopped

Tier 2 fixed-seed validation produced a useful mixed signal but not a paper-positive result: calibration alone failed to deliver stable target preservation on the strongest real baseline and did not improve route stability under perturbation.

## Recommended next action

Stop this calibrated-confidence-only paper path; the next bounded test should evaluate conformal or upper-confidence risk-controlled gates on the same cascade harness before any LLM-scale escalation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Risk-controlled local cascade gates with conformal abstention
- Success threshold: On datasets with a real cheap < strong hierarchy, target breach rate <= 0.2 across seeds while preserving at least half of the strong-call reduction achieved by the best calibrated confidence gate.
- Stop condition: Stop if conformal/UCB gates still breach the strong-accuracy tolerance in more than 20% of seeds or require strong-call rates within 10 percentage points of always-strong.

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-confidence-gates-for-stable-local-cascade-routi-4973719f64`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Static parameter-matched residual adapters for 1-bit recovery

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `static-parameter-matched-residual-adapters-for-1-bit-recov-8ee68488ea`
Run ID: `static-parameter-matched-residual-adapters-for-1-bit-recov-8ee68488ea-20260519T030504964652+0000`

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

- Internal Enoch project: Static parameter-matched residual adapters for 1-bit recovery: internal_generated:static-parameter-matched-residual-adapters-for-1-bit-recov-8ee68488ea

## What looked useful

Static residual adapters are not random: they improve mean test accuracy by 0.64 percentage points over 1-bit and reduce loss substantially, while random static residuals hurt. However, the parameter-matched trained adapter improves accuracy by 3.04 points and recovers 81.5% of the dense-minus-1-bit accuracy gap, versus 16.3% for static SVD.

## Boundaries and scale limits

Single small vision classifier, MNIST only, 20,000 train examples per seed, 3 fixed seeds, no transformer/language-model validation, no larger dataset, and no activation-aware static calibration.

## Claim scope

On MNIST with a 535,818-parameter MLP quantized to per-row scaled 1-bit weights, rank-8 static SVD residual adapters provide a small but consistent recovery signal over the bare 1-bit model, but they are far weaker than a parameter-matched trained low-rank adapter baseline.

## Why it stopped

Medium direct validation found only weak static recovery and a much stronger parameter-matched trained-adapter baseline, so the static residual method is not paper-ready.

## Recommended next action

Stop this line as no-paper evidence unless running a bounded activation-aware static calibration follow-up; the current medium confirmation is a direct local negative against competitive static parameter-matched recovery.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware calibration for static residual adapters
- Success threshold: The calibrated static residual must recover at least 50% of the dense-minus-1-bit accuracy gap and close at least half of the remaining gap to the parameter-matched trained adapter on the same seeds.
- Stop condition: Stop if calibrated static residual recovery remains below 30% of the dense-minus-1-bit gap or is unstable across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/static-parameter-matched-residual-adapters-for-1-bit-recov-8ee68488ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

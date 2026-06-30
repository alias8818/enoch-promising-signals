# Medium multi-dataset CPU validation for confidence-threshold cascades

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-multi-dataset-cpu-validation-for-confidence-thresho-7c5d3ec130`
Run ID: `medium-multi-dataset-cpu-validation-for-confidence-thresho-7c5d3ec130-20260523T113010252534+0000`

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

- Parent run decision: Real CPU inference validation for confidence-threshold early-exit cascades: enoch://control-plane/projects/real-cpu-inference-validation-for-confidence-threshold-ear-793b8965e7/runs/real-cpu-inference-validation-for-confidence-threshold-ear-793b8965e7-20260523T111602758948+0000
- Parent run decision: Early-exit cascade router for CPU serving: enoch://control-plane/projects/early-exit-cascade-router-for-cpu-serving-545c67795e74/runs/early-exit-cascade-router-for-cpu-serving-545c67795e74-20260523T110636121032+0000

## What looked useful

Direct fixed-seed metrics met the practical speed/accuracy threshold on 4 of 4 datasets, but matched-rate random/inverted controls show mixed evidence for confidence ordering as the causal mechanism. The result is useful no-paper evidence for cheap-model-first CPU cascades, not a paper-positive cross-dataset mechanism claim.

## Boundaries and scale limits

Small local datasets only; batch predict_proba timing rather than deployed serving latency; strong baselines were real but not exhaustively tuned; mechanism controls only clearly favored confidence gating on digits.

## Claim scope

On four small real sklearn datasets with five fixed seeds, a validation-tuned two-stage CPU cascade using standardized logistic regression plus a tree-ensemble fallback preserved median held-out accuracy within 1 percentage point of the always-on tree baseline and reduced estimated batch CPU inference latency by more than 13x at low escalation rates.

## Why it stopped

Tier 2 direct metrics were positive, but ablations and baseline strength caveats make the mechanism support mixed rather than paper-ready.

## Recommended next action

Stop as no-paper useful signal; a future deepen run should use stronger/tuned baselines and larger real datasets where the cheap model is not already competitive with the fallback.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Strict-baseline confidence cascade validation on larger real datasets
- Success threshold: On at least 3 datasets, confidence cascade accuracy within 1 point of tuned fallback baseline, measured end-to-end latency speedup at least 1.5x, and confidence gate accuracy strictly above both matched-rate controls on at least 4 of 5 seeds.
- Stop condition: Stop negative if the fallback is not consistently stronger than the cheap model, if speedup falls below 1.2x after end-to-end measurement, or if confidence gating fails to beat matched-rate controls on most seeds.

## Evidence references

- Artifact root: `<local-path>/projects/medium-multi-dataset-cpu-validation-for-confidence-thresho-7c5d3ec130`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

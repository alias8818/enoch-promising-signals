# Strict-baseline confidence cascade validation on larger real datasets

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `88`
Project ID: `strict-baseline-confidence-cascade-validation-on-larger-re-1d9308b110`
Run ID: `strict-baseline-confidence-cascade-validation-on-larger-re-1d9308b110-20260523T121144949435+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `88`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Medium multi-dataset CPU validation for confidence-threshold cascades: enoch://control-plane/projects/medium-multi-dataset-cpu-validation-for-confidence-thresho-7c5d3ec130/runs/medium-multi-dataset-cpu-validation-for-confidence-thresho-7c5d3ec130-20260523T113010252534+0000
- Parent run decision: Real CPU inference validation for confidence-threshold early-exit cascades: enoch://control-plane/projects/real-cpu-inference-validation-for-confidence-threshold-ear-793b8965e7/runs/real-cpu-inference-validation-for-confidence-threshold-ear-793b8965e7-20260523T111602758948+0000

## What looked useful

Confidence gating beat both random and inverted matched-rate controls on 5/5 larger UCI datasets, but only 2/5 datasets met the strict speed/accuracy threshold of <=1 percentage point accuracy loss and >=1.2x speedup versus the strong baseline.

## Boundaries and scale limits

Validated on local CPU sklearn tabular classifiers, not transformer serving or production request traces; latency is vectorized predict_proba timing recombined by escalation rate; categorical variables use ordinal encoding; model families were not exhaustively tuned.

## Claim scope

On five public UCI tabular classification datasets with three fixed seeds, held-out threshold tuning, measured CPU predict_proba latency, and matched-rate random/inverted controls, confidence ordering reliably beats matched-rate controls but does not reliably preserve a strict strong-baseline accuracy margin while speeding inference.

## Why it stopped

Strict Tier 3 success threshold was not met: mechanism controls passed on 5/5 datasets, but speed/accuracy preservation passed on only 2/5 datasets.

## Recommended next action

Stop this Tier 3 branch as no-paper useful signal; if continuing within the lineage, test calibrated or selective-prediction gates on the same five-dataset protocol with a pre-registered 4/5 speed-accuracy pass threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated confidence gates for strict-baseline cascades on larger UCI datasets
- Success threshold: At least 4 of 5 datasets must have median cascade accuracy no worse than 1 percentage point below the strong baseline, median speedup at least 1.2x, and median accuracy above both matched-rate controls.
- Stop condition: Stop as negative if calibrated/selective gates still pass speed/accuracy on fewer than 4 of 5 datasets or lose the matched-rate control advantage on more than one dataset.

## Evidence references

- Artifact root: `<local-path>/projects/strict-baseline-confidence-cascade-validation-on-larger-re-1d9308b110`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

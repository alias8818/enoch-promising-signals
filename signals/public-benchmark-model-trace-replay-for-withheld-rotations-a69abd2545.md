# Public Benchmark Model-Trace Replay for Withheld Rotations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `88`
Project ID: `public-benchmark-model-trace-replay-for-withheld-rotations-a69abd2545`
Run ID: `public-benchmark-model-trace-replay-for-withheld-rotations-a69abd2545-20260530T003943406960+0000`

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

- Parent run decision: Trace Replay Validation of Rotating Private Challenge Banks: enoch://control-plane/projects/trace-replay-validation-of-rotating-private-challenge-bank-1dc87ee4fc/runs/trace-replay-validation-of-rotating-private-challenge-bank-1dc87ee4fc-20260529T163552340268+0000
- Parent run decision: Real-Trace Replay Screen for Withheld Benchmark Rotations: enoch://control-plane/projects/real-trace-replay-screen-for-withheld-benchmark-rotations-19cec89958/runs/real-trace-replay-screen-for-withheld-benchmark-rotations-19cec89958-20260529T203313353078+0000

## What looked useful

Trace interpolation improved final accuracy error by 13.8% and curve accuracy MAE by 12.2% versus nearest-angle replay, but missed the predeclared 15% threshold and lost to the global public mean baseline on all target metrics. The shuffled-angle control also beat trace interpolation on final accuracy error, indicating weak angular trace structure on this benchmark.

## Boundaries and scale limits

This bounded validation covers MNIST rotations only, one CNN architecture, 8-epoch traces, midpoint withheld rotations, and accuracy/loss trace prediction. It does not test harder image benchmarks, larger architectures, non-midpoint shifts, language models, or private benchmark traces.

## Claim scope

On full MNIST train/test with a small CNN, 5 fixed seeds, 24 public rotation angles, 24 withheld midpoint rotations, and 8 training epochs per model, linear replay/interpolation of public model traces does not provide a useful withheld-rotation prediction advantage over simple non-trace baselines.

## Why it stopped

Direct bounded validation completed 240 model trainings and 120 withheld seed-angle evaluations; the trace replay method failed the predeclared success threshold and failed to beat a real non-trace global-mean baseline/control.

## Recommended next action

Stop the current MNIST withheld-rotation line as no-paper evidence; only pursue a bounded deepen test on a harder public benchmark where rotation sensitivity is materially larger.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder Public Rotation Benchmark for Trace Replay
- Success threshold: Trace interpolation must reduce final accuracy absolute error and curve accuracy MAE by at least 15% versus nearest public and must also beat global public mean and shuffled-angle controls on the same metrics across at least 100 withheld seed-angle pairs.
- Stop condition: Stop if the dataset's actual withheld final accuracy range is below 1 percentage point after calibration, or if trace interpolation fails to beat global mean and shuffled controls after the first complete fixed-seed matrix.

## Evidence references

- Artifact root: `<local-path>/projects/public-benchmark-model-trace-replay-for-withheld-rotations-a69abd2545`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

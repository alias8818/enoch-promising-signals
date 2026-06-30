# Bounded transformer validation of INT8 fake-quantized training with per-channel smoothing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-transformer-validation-of-int8-fake-quantized-trai-0183d2a5fc`
Run ID: `bounded-transformer-validation-of-int8-fake-quantized-trai-0183d2a5fc-20260609T131611911056+0000`

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

- Parent run decision: INT8 quantized training with per-channel smoothing: enoch://control-plane/projects/int8-quantized-training-with-per-channel-smoothing-4993d2442ea2/runs/int8-quantized-training-with-per-channel-smoothing-4993d2442ea2-20260609T081940735847+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/eca178203750

## What looked useful

Per-channel smoothing appears useful when activation channel outliers create a real fake-quantization error: stressed naive INT8 final val loss was 4.080359 versus FP32 4.054102, while smoothed INT8 was 4.054378; sampled relative output RMSE dropped from 0.371386 to 0.011957 and activation p99/median dropped from 17.655 to 1.288.

## Boundaries and scale limits

Three seeds per condition, 400 training steps, synthetic structured data, fake quantization only, no real text corpus, no GPT-2-small-class scale, no true INT8 training kernels, and no long-horizon stability validation.

## Claim scope

In a 4-layer 128-dimensional causal transformer trained on a deterministic synthetic token-language task with INT8 fake quantization in all linear layers, SmoothQuant-style per-input-channel smoothing recovered 98.95% of the naive INT8 validation-loss gap to FP32 under a controlled FP32-equivalent activation-channel outlier stressor. Without the stressor, naive INT8 was already nearly lossless and smoothing gave only a tiny diagnostic improvement.

## Why it stopped

Tier 1 controlled direct test completed with mechanism support but only synthetic small-transformer evidence; this is useful no-paper evidence, not paper-positive validation.

## Recommended next action

Run a bounded medium confirmation on a real text corpus with a GPT-2-small-class or locally feasible parameter-matched transformer, measuring natural activation outliers, training loss recovery, and smoothing-alpha sensitivity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-text validation of INT8 fake-quantized transformer training with per-channel smoothing
- Success threshold: Smoothed INT8 recovers at least 50% of the naive INT8 validation-loss gap to FP32 and reduces sampled relative quantized-linear output RMSE by at least 25% versus naive INT8 under natural, unstressed training.
- Stop condition: Stop if naive INT8 has less than a 0.5% validation-loss gap to FP32 after a calibrated run, or if smoothing fails to recover at least 25% of the observed naive gap in two independent seeds.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-transformer-validation-of-int8-fake-quantized-trai-0183d2a5fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

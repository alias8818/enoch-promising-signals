# Gradient Compression with CPU Spillover for Tiny Model Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-compression-with-cpu-spillover-for-tiny-model-training-41ee1d4c70d7`
Run ID: `gradient-compression-with-cpu-spillover-for-tiny-model-training-41ee1d4c70d7-20260609T110603202899+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/befa06f93b7e

## What looked useful

Dense quantized gradient spillover is a plausible bounded mechanism for tiny training because FP16 kept accuracy unchanged at 2x byte reduction and INT8 kept accuracy essentially unchanged at about 4x byte reduction. Very aggressive naive 1% top-k spillover reached about 50x byte reduction but lost about 5.5 validation accuracy points.

## Boundaries and scale limits

No GPU-to-CPU DMA, UMA pressure, asynchronous overlap, PyTorch/autograd integration, transformer/GPT-2-small-class model, Adam/momentum optimizer state, real dataset, or long schedule was tested.

## Claim scope

CPU NumPy tiny-MLP optimizer-boundary probe: FP16 and symmetric INT8 gradient compression preserved validation accuracy and loss while reducing spillover payload bytes; naive 1% top-k sparse compression did not preserve quality.

## Why it stopped

Bounded CPU evidence supports part of the mechanism but is not publication-grade direct spillover evidence, and naive aggressive sparse compression is early-falsified in this proxy setup rather than fully validated or fully refuted at scale.

## Recommended next action

Stop this run as no-paper useful signal; next run should test residual/error-feedback top-k gradient spillover on the same tiny benchmark before any framework or GPU spillover implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Error-feedback sparse gradient spillover for tiny training
- Success threshold: At least one sparse error-feedback variant achieves 10x or greater gradient payload reduction with mean validation accuracy within 1 percentage point of FP32 baseline and no more than 10% worse validation loss across 5 seeds.
- Stop condition: Stop if all error-feedback sparse variants are more than 2 validation accuracy points below baseline or require residual memory/step overhead that removes the practical benefit versus INT8 dense spillover.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-compression-with-cpu-spillover-for-tiny-model-training-41ee1d4c70d7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Minimal Calibration Dataset Selection for Stable INT4 Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `minimal-calibration-dataset-selection-for-stable-int4-quantization-df58e7a9b9b4`
Run ID: `minimal-calibration-dataset-selection-for-stable-int4-quantization-df58e7a9b9b4-20260609T062440513022+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b4f39773704c

## What looked useful

Activation coverage may modestly reduce seed-to-seed variance versus random subsets, but it was inconsistent across candidate pools and weaker than a simple token-diversity heuristic on mean and median loss degradation.

## Boundaries and scale limits

Tested one small language model, one dataset, calibration k<=16, four candidate pools, and a proxy quantizer rather than production GPTQ/AWQ kernels or 1B+/7B+ models.

## Claim scope

On distilgpt2 with WikiText-2 and a transparent activation-weighted INT4 clipping proxy, activation-signature coverage selection for k=4/8/16 produced only a tiny aggregate loss-degradation improvement over random calibration subsets and did not beat a cheap token-diversity control.

## Why it stopped

No-paper useful signal: the local proxy experiment did not show a robust advantage for activation-coverage minimal calibration selection over cheap controls.

## Recommended next action

Do not write a paper from this run; run a bounded follow-up using a real GPTQ/AWQ implementation on OPT-125M or GPT-2-small-class models with paired random and token-diversity controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-quantizer validation of coverage-plus-diversity calibration selection
- Success threshold: Combined coverage-plus-diversity must beat both random and diversity-only controls by at least 0.02 validation loss or 10% relative degradation reduction and reduce random-like standard deviation by at least 25% on both tested models.
- Stop condition: Stop if the combined selector fails to beat the diversity-only control on either model or if real GPTQ/AWQ results match the proxy result's tiny, inconsistent effect.

## Evidence references

- Artifact root: `<local-path>/projects/minimal-calibration-dataset-selection-for-stable-int4-quantization-df58e7a9b9b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

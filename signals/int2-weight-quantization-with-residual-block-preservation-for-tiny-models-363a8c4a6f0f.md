# INT2 Weight Quantization with Residual Block Preservation for Tiny Models

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `int2-weight-quantization-with-residual-block-preservation-for-tiny-models-363a8c4a6f0f`
Run ID: `int2-weight-quantization-with-residual-block-preservation-for-tiny-models-363a8c4a6f0f-20260608T074542045378+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7841a987ac2c

## What looked useful

Residual block preservation reduced blanket INT2 damage but quantized only about 9% of weights. Quantizing residual blocks only covered about 91% of weights and had the smallest mean degradation: accuracy drop 0.000098 and NLL delta 0.000462 versus FP32, compared with blanket INT2 accuracy drop 0.001563 and NLL delta 0.005795.

## Boundaries and scale limits

Synthetic data only; residual MLP only; post-training symmetric 2-bit proxy levels only; no real vision/language dataset, no CNN/Transformer residual stream, no quantization-aware training, and no packed INT2 deployment kernel.

## Claim scope

On a five-seed synthetic 10-class tiny residual MLP proxy, preserving residual block weights during post-training symmetric INT2 weight quantization did not outperform quantizing residual blocks only; endpoint/input-head weights were more fragile than residual block weights.

## Why it stopped

Proxy evidence does not support the proposed residual-block-preservation heuristic as paper-worthy; this is not a full validation, but it directly falsifies the heuristic on the tested tiny residual MLP setup.

## Recommended next action

Stop this run as an early proxy falsification; the next bounded test should evaluate endpoint-preservation versus residual-preservation on a real tiny CNN or Transformer dataset before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Endpoint-preservation versus residual-preservation for real tiny INT2 models
- Success threshold: Endpoint-preserved or residual-block-only INT2 achieves lower accuracy drop and lower loss delta than residual-block-preserved INT2 while quantizing at least 50% more weights.
- Stop condition: Stop if residual-block preservation wins on both accuracy/loss and quantized-weight fraction across two real tiny-model tasks, or if all INT2 variants lose more than 2 percentage points accuracy versus FP32.

## Evidence references

- Artifact root: `<local-path>/projects/int2-weight-quantization-with-residual-block-preservation-for-tiny-models-363a8c4a6f0f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

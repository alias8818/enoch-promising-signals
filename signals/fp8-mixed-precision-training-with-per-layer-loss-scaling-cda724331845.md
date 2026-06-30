# FP8 Mixed Precision Training with Per-Layer Loss Scaling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fp8-mixed-precision-training-with-per-layer-loss-scaling-cda724331845`
Run ID: `fp8-mixed-precision-training-with-per-layer-loss-scaling-cda724331845-20260605T140725215818+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4368a712410f

## What looked useful

Per-layer scaling reduced medium-run small-branch gradient relative error from 0.054675 to 0.019486 and gradient zero fraction from 0.045006 to 0.000015; in a 100x stronger heterogeneity stress run it reduced small-branch error from 0.266050 to 0.019670 and zero fraction from 0.115483 to 0.000741. End-to-end final loss improvement was modest, so this is mechanism evidence rather than paper-grade validation.

## Boundaries and scale limits

Synthetic MLP regression only; no transformer, no real corpus, no activation FP8/GEMM coverage, no distributed optimizer, no long-horizon pretraining, and no production throughput claim.

## Claim scope

On a controlled CUDA FP8 synthetic two-branch regression task with heterogeneous per-parameter gradient magnitudes, per-layer FP8 gradient scaling substantially reduced small-layer gradient quantization error and zeroing versus one global scale, and matched FP32 final loss in the medium setting.

## Why it stopped

Proxy CUDA FP8 experiment supports the mechanism but does not directly validate full FP8 mixed-precision transformer training, so it is insufficient for a paper-positive decision.

## Recommended next action

Stop this run as a useful no-paper signal; next concrete step is a bounded GPT-2-small-class or small transformer training confirmation with real validation loss, activation/gradient FP8 coverage, and BF16/global-FP8/per-layer-FP8 controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer FP8 Per-Layer Scaling Confirmation
- Success threshold: Per-layer FP8 must reduce mean small/low-magnitude-layer gradient relative error by at least 2x versus global FP8 and achieve validation loss no worse than 1% above BF16 while outperforming global FP8 validation loss or stability on at least two of three seeds.
- Stop condition: Stop if per-layer FP8 does not improve gradient diagnostics by 2x, if validation loss is worse than global FP8 on two or more seeds, or if the implementation cannot run a fair transformer control within the local bounded budget.

## Evidence references

- Artifact root: `<local-path>/projects/fp8-mixed-precision-training-with-per-layer-loss-scaling-cda724331845`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Low-Rank Residual Correction to 2-bit Quantization (LoRC)

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `low-rank-residual-correction-to-2-bit-quantization-lorc-c323cc6b4fc2`
Run ID: `low-rank-residual-correction-to-2-bit-quantization-lorc-c323cc6b4fc2-20260601T003220788834+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/03d2b34b4c60

## What looked useful

Under the 3-bit effective budget, LoRC beat 3-bit quantization on 0/20 matrices; the best LoRC candidate was median 4.98x worse in output NMSE than 3-bit. Under the 4-bit effective budget, LoRC beat 4-bit on 0/20 matrices and was median 20.78x worse. The naive residual-SVD formulation appears storage-inefficient versus simply using more quantization levels.

## Boundaries and scale limits

This is matrix-level and proxy output-distortion evidence only. It does not include trained large-model weights, real activation calibration, perplexity/task accuracy, latency, quantized residual factors, or end-to-end inference.

## Claim scope

Naive LoRC defined as per-row affine 2-bit quantization plus unweighted fp16 SVD residual factors was tested on 20 matrices: 4 synthetic probes and 16 tiny-random-GPT2 transformer-shaped weights. Metrics were normalized weight MSE and random-activation output NMSE at comparable effective storage budgets.

## Why it stopped

Early proxy falsification: matrix/output-distortion tests consistently showed naive fp16 SVD residual correction is much worse than plain 3-bit or 4-bit quantization at comparable storage.

## Recommended next action

Stop this naive LoRC variant as a no-paper proxy negative; only revisit with an activation-aware or quantized-factor residual method evaluated on trained model perplexity against equal-budget 3-bit and 4-bit baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware LoRC on trained GPT-2-small weights
- Success threshold: At equal effective storage, activation-aware LoRC must beat the 3-bit baseline on validation perplexity degradation and layer-output NMSE for at least 80% of tested linear layers, without worse measured inference latency than the matched baseline by more than 25%.
- Stop condition: Stop if activation-aware LoRC still fails to beat 3-bit on validation perplexity or if residual-factor storage/latency erases the accuracy gain on most layers.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-residual-correction-to-2-bit-quantization-lorc-c323cc6b4fc2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# 2-bit Weights + Low-Rank Residual Channels for Sub-4-bit Inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `2-bit-weights-low-rank-residual-channels-for-sub-4-bit-inference-79ec0ca26402`
Run ID: `2-bit-weights-low-rank-residual-channels-for-sub-4-bit-inference-79ec0ca26402-20260621T023912060351+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc4ce748255b

## What looked useful

Low-rank residuals improve plain 2-bit quantization, but even rank 64 at 3.94 effective bits/weight failed to beat uniform 3-bit weight error on any of 48 GPT-2 layers and had 3.91x worse median activation-output error than uniform 3-bit.

## Boundaries and scale limits

No end-to-end perplexity replacement, fused inference kernel, metadata overhead accounting, activation-aware residual learning, or larger-model validation was run. Results cover the naive SVD residual mechanism on GPT-2-class weights only.

## Claim scope

Post-training per-row affine quantization of pretrained GPT-2 Conv1D weights with FP16 SVD low-rank residual factors at ranks 4, 8, 16, 32, 48, and 64; evaluated by weight relative MSE and layer output relative MSE on captured GPT-2 activations.

## Why it stopped

Early direct post-training falsification on GPT-2 weights: the simple 2-bit plus FP16 SVD residual scheme is consistently weaker than ordinary 3-bit quantization under paired layer metrics, so it is not paper-positive.

## Recommended next action

Stop this naive SVD residual variant as no-paper evidence; a bounded follow-up should test activation-aware low-rank residual fitting at the same bit budgets before any larger model or kernel work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware low-rank residual fitting for 2-bit GPT-2 projections
- Success threshold: At less than 3.0 effective bits/weight, activation-aware 2-bit plus residual must beat uniform 3-bit activation-output error on at least 30 of 48 layers and reduce median activation-output error by at least 10%; then the end-to-end perplexity delta should be no worse than uniform 3-bit on the same slice.
- Stop condition: Stop if the activation-aware residual fails to beat uniform 3-bit on at least 24 of 48 layers or has median activation-output error worse than uniform 3-bit after the bounded GPT-2 pass.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-weights-low-rank-residual-channels-for-sub-4-bit-inference-79ec0ca26402`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

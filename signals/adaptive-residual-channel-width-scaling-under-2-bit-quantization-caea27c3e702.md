# Adaptive Residual Channel Width Scaling Under 2-bit Quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `adaptive-residual-channel-width-scaling-under-2-bit-quantization-caea27c3e702`
Run ID: `adaptive-residual-channel-width-scaling-under-2-bit-quantization-caea27c3e702-20260529T105504000671+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/730f4b282d3d

## What looked useful

The sensitivity-adaptive schedule [8, 12, 16, 28] lost to uniform [16, 16, 16, 16] on all 3 seeds and had 113.5% higher mean all-weight 2-bit MSE. A reverse/front-loaded control [28, 16, 12, 8] was slightly better than uniform on mean, suggesting the measured sensitivity signal may point to blocks that should be narrowed rather than widened under 2-bit PTQ.

## Boundaries and scale limits

CPU-only NumPy probe; synthetic regression data; residual MLP rather than transformer/GPT; 3 seeds; post-training weight quantization only; no activation quantization, QAT, real token data, hardware kernels, or GPT-2-small-class baseline.

## Claim scope

In a small synthetic 4-block residual MLP teacher/student regression task with equal total residual branch width and 2-bit post-training weight quantization, allocating more residual channels to blocks with higher one-block quantization sensitivity did not improve quantized loss versus uniform width.

## Why it stopped

Proxy/local early falsification: the proposed sensitivity-directed adaptive residual width rule failed the direct synthetic residual-network test and is not a full validation or paper-ready result.

## Recommended next action

Stop this hypothesis as a proxy early falsification; if continuing, run a bounded transformer follow-up that tests inverse/front-loaded residual width schedules against uniform under 2-bit PTQ on real token loss.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Inverse Sensitivity Residual Width Allocation for 2-bit Quantized Transformers
- Success threshold: Inverse/front-loaded schedule reduces mean 2-bit token loss by at least 5% versus uniform and beats uniform on at least 2 of 3 seeds/checkpoints without increasing float loss by more than 2%.
- Stop condition: Stop if inverse/front-loaded fails to beat uniform on at least 2 of 3 seeds/checkpoints or if gains disappear after matching parameter count and training budget.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-residual-channel-width-scaling-under-2-bit-quantization-caea27c3e702`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Cheap Residual Coding for Error-Selected 2-bit Channels

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cheap-residual-coding-for-error-selected-2-bit-channels-8c70450907`
Run ID: `cheap-residual-coding-for-error-selected-2-bit-channels-8c70450907-20260520T093559429310+0000`

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

- Parent run decision: Principled Residual Channels for 2-bit Weight Quantization with Iso-Budget Baseline: enoch://control-plane/projects/principled-residual-channels-for-2-bit-weight-quantization-with-iso-budget-baseline-8b9a61126ad6/runs/principled-residual-channels-for-2-bit-weight-quantization-with-iso-budget-baseline-8b9a61126ad6-20260520T092209492583+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/0ab4599540f4

## What looked useful

At 10% residual-coded channels and about 2.10 effective bits/value, error-selected residuals reduced MSE vs plain 2-bit by 47.7%, 84.8%, and 32.5% on three heterogeneous channel-error cases, and beat random residual allocation by 42.7%, 83.1%, and 27.2%. A five-seed replication kept all heterogeneous minima above the 20% vs plain and 10% vs random threshold. The homogeneous control showed only a 2.16% selection advantage over random.

## Boundaries and scale limits

Evidence is limited to synthetic 8192 x 512 channel matrices and reconstruction MSE. It does not include real transformer checkpoints, downstream perplexity or task accuracy, learned residual codes, entropy coding, or inference-kernel latency.

## Claim scope

Controlled NumPy channel-tensor reconstruction tests show that adding a one-bit sign residual to the 10% highest-error channels after per-channel 2-bit quantization reduces MSE substantially more than equal-budget random or uniform residual allocation when channel quantization error is heterogeneous.

## Why it stopped

Tier 1 controlled direct test met its mechanism threshold, but the evidence is synthetic reconstruction-only and therefore insufficient for publication readiness.

## Recommended next action

Run a bounded deepen test on real transformer weight or activation tensors, preserving the same equal-rate baselines and adding downstream perplexity or task-loss measurement; do not write a paper from the synthetic-only result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transformer Tensor Test for Error-Selected 2-bit Residual Channels
- Success threshold: At 10% residual-coded channels, pass if real model tensors show at least 20% MSE reduction vs plain 2-bit, at least 10% MSE reduction vs random equal-rate residual allocation, and no downstream metric regression relative to the best equal-rate control.
- Stop condition: Stop as unsupported if real tensor reconstruction gains fall below either threshold on most layers or if downstream loss/perplexity regresses relative to equal-rate baselines despite reconstruction gains.

## Evidence references

- Artifact root: `<local-path>/projects/cheap-residual-coding-for-error-selected-2-bit-channels-8c70450907`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Sparse-Update Optimizer With Momentum Accumulation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sparse-update-optimizer-with-momentum-accumulation-6d26d6646d20`
Run ID: `sparse-update-optimizer-with-momentum-accumulation-6d26d6646d20-20260531T111213457416+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/95f52623c2d6

## What looked useful

Residual/momentum accumulation is the mechanism that made sparse coordinate application preserve dense-like loss in this benchmark. Naive sparse top-k updates that drop non-selected deltas were consistently worse.

## Boundaries and scale limits

Evidence is limited to CPU NumPy convex regression. It does not test neural-network validation metrics, GPT-style training, fused sparse optimizer kernels, GPU memory traffic, distributed communication, or large-scale hyperparameter robustness.

## Claim scope

On synthetic minibatch linear regression with 2048-4096 features and 3 seeds, top-k sparse parameter application with momentum/residual accumulation matched dense momentum final MSE while applying only 2-10% of coordinate writes; dropping skipped updates at the same density degraded MSE.

## Why it stopped

No-paper closure: bounded synthetic evidence supports the mechanism but does not provide direct model-training or systems evidence.

## Recommended next action

Run a bounded PyTorch follow-up on a small real neural-network task with validation loss/accuracy and optimizer-time instrumentation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch neural-network validation of sparse momentum accumulation
- Success threshold: Across at least 3 seeds, sparse accumulation reaches within 1% relative validation loss or accuracy of the dense optimizer while applying no more than 10% of coordinate updates and outperforming the no-accumulation sparse control.
- Stop condition: Stop if sparse accumulation misses the dense validation metric by more than 5% relative after reasonable learning-rate tuning, or if optimizer bookkeeping makes wall-clock more than 25% slower without a plausible systems path to recover the cost.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-update-optimizer-with-momentum-accumulation-6d26d6646d20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

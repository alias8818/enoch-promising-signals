# Hessian-Trace Residual Channel Preservation for Sub-2bit Quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `hessian-trace-residual-channel-preservation-for-sub-2bit-quantization-3664c59792af`
Run ID: `hessian-trace-residual-channel-preservation-for-sub-2bit-quantization-3664c59792af-20260516T082145575876+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/86fcadeec75f

## What looked useful

Hessian-trace residual channel preservation was slightly negative on average at 5%, 10%, and 20% preserved channels. Activation-magnitude preservation showed a small noisy positive signal, suggesting forward contribution may be a better bounded follow-up heuristic than Hessian trace in this setup.

## Boundaries and scale limits

Small residual MLP and image-classification digits data only; not transformer language modeling, not production packed sub-2-bit kernels, and not a full parameter-Hessian LLM study.

## Claim scope

On a 5-seed sklearn digits residual-MLP experiment with row-wise ternary quantization and fp32 residual output-row preservation, selecting preserved channels by Hutchinson Hessian-trace estimates did not improve quantized accuracy over no preservation or simple controls.

## Why it stopped

Proxy/small-model evidence did not support the named Hessian-trace mechanism: Hessian-selected preservation averaged -0.0005, -0.0016, and -0.0016 accuracy improvement versus no preservation at 5%, 10%, and 20% preserved channels.

## Recommended next action

Stop this Hessian-trace run as a bounded early falsification; if continuing locally, branch to a separate activation-magnitude residual preservation test on a GPT-2-small-class language-model quantization benchmark.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Activation-Magnitude Residual Channel Preservation for Sub-2bit Transformer Quantization
- Success threshold: Activation-magnitude preservation beats all listed controls by at least 10% relative reduction in quantization-induced perplexity degradation at one or more preservation budgets, with no worse result at the other budgets.
- Stop condition: Stop if activation-magnitude preservation fails to beat random and no-preservation baselines on mean held-out perplexity degradation across 3 seeds/checkpoints.

## Evidence references

- Artifact root: `<local-path>/projects/hessian-trace-residual-channel-preservation-for-sub-2bit-quantization-3664c59792af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

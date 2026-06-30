# Micro-Batch Gradient Accumulation with Activation Buffer Reuse

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `micro-batch-gradient-accumulation-with-activation-buffer-reuse-56349164ad09`
Run ID: `micro-batch-gradient-accumulation-with-activation-buffer-reuse-56349164ad09-20260603T161233166969+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/534646c74c6b

## What looked useful

Activation buffer reuse is implementable and gradient-correct in this scoped custom-autograd form, but PyTorch allocator reuse already handles the standard immediate accumulation case well. The buffer bank reduced some CUDA malloc calls in deferred accumulation while increasing peak allocated/reserved memory and lowering throughput by about 14-23% on larger BF16 runs.

## Boundaries and scale limits

Synthetic MLP proxy only; no attention layers, no real dataset convergence, no optimizer-state pressure beyond SGD, no compiler or fused-kernel integration, no distributed training, and runtime was seconds rather than long training.

## Claim scope

On a GB10 PyTorch CUDA transformer-MLP-like proxy, a custom autograd GELU that reuses preallocated activation buffers during micro-batch gradient accumulation preserved gradients but did not reduce peak memory and reduced throughput versus standard PyTorch autograd.

## Why it stopped

Early bounded proxy falsification: the direct reusable activation-bank implementation increased peak memory and reduced throughput despite preserving gradients and slightly reducing allocator calls.

## Recommended next action

Stop this simple buffer-bank path; only revisit with a fused-kernel or compiler-integrated design that can avoid the extra activation copy and prove memory savings on a GPT-2-small-class workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused activation-save buffer reuse for transformer MLP training
- Success threshold: At least 10% lower peak allocated memory than standard PyTorch immediate gradient accumulation with no more than 5% throughput loss and matched loss trajectory over the measured segment.
- Stop condition: Stop if the fused path cannot avoid duplicate live activations or if the first GPT-2-small-class segment shows less than 5% peak-memory reduction or more than 10% throughput loss.

## Evidence references

- Artifact root: `<local-path>/projects/micro-batch-gradient-accumulation-with-activation-buffer-reuse-56349164ad09`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

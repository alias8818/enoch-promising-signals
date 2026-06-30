# Activation buffer sharing across gradient accumulation micro-batches

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `activation-buffer-sharing-across-gradient-accumulation-micro-batches-3cce9c12bd90`
Run ID: `activation-buffer-sharing-across-gradient-accumulation-micro-batches-3cce9c12bd90-20260527T192813355633+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7f28bed917fe

## What looked useful

For 8 micro-batches, delayed backward used exactly 8.0x the saved-tensor peak residency of streaming gradient accumulation and 3.91x CUDA peak allocation; checkpointing reduced delayed saved residency to 26.6% and CUDA peak to 45.3% but required recomputation and 1.64x delayed-backward wall time. Gradients matched streaming within 5.59e-09.

## Boundaries and scale limits

Not validated on production LLM stacks, fused attention kernels, distributed training, ZeRO/FSDP, pipeline parallelism, or full GPT-2-small training. Evidence is local and mechanistic, not publication-grade broad training evidence.

## Claim scope

A single-GPU PyTorch mechanism probe on a toy transformer-like stack shows that ordinary streaming gradient accumulation already releases activation graphs between micro-batches, while delayed-backward accumulation keeps distinct saved tensors for every live micro-batch and cannot safely alias them into one buffer without recomputation.

## Why it stopped

Early/local falsification: streaming gradient accumulation already reuses activation memory across micro-batches, and delayed backward requires distinct saved activations unless using recomputation such as checkpointing.

## Recommended next action

Stop this project as a no-paper useful negative signal unless a distinct exact-training schedule is proposed that aliases live micro-batch activations without recomputation and still matches gradients.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/activation-buffer-sharing-across-gradient-accumulation-micro-batches-3cce9c12bd90`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

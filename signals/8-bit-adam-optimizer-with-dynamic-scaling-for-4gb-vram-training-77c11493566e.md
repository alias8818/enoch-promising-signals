# 8-bit Adam optimizer with dynamic scaling for <4GB VRAM training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adam-optimizer-with-dynamic-scaling-for-4gb-vram-training-77c11493566e`
Run ID: `8-bit-adam-optimizer-with-dynamic-scaling-for-4gb-vram-training-77c11493566e-20260619T071102016257+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/698232ea40db

## What looked useful

Persistent optimizer state fell from 128,000,004 bytes for PyTorch fp16 AdamW to 64,062,504 bytes for dynamic int8 m+v at 32M parameters, but the trace ablation showed second-moment quantization creates large outlier updates; keeping v fp32 while quantizing m stayed close to fp32 AdamW on the trace.

## Boundaries and scale limits

Evidence is limited to synthetic tensors, a deterministic gradient trace, and a short synthetic classifier run on a GB10 with large unified memory. It does not directly validate real transformer training on a physically constrained <4GB GPU or a fused production optimizer.

## Claim scope

On GB10 CUDA proxy tests, a reference dynamic blockwise int8 AdamW implementation reduces persistent optimizer-state memory for Adam moments, but linear int8 quantization of both first and second moments is not robust on a fixed gradient trace.

## Why it stopped

Proxy evidence early-falsified the stronger naive full-int8 dynamic-scaling claim: linear int8 second-moment storage produced trace outliers by step 2, so broader training claims would be unsupported.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is a stabilized second-moment encoding under an enforced 4GB CUDA memory cap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized second-moment encoding for sub-4GB AdamW
- Success threshold: No NaNs, trace max absolute error below 1e-2, final validation loss within 5% of fp32 AdamW on the bounded model, and persistent optimizer-state memory at least 35% lower than PyTorch fp16 AdamW.
- Stop condition: Stop if stabilized second-moment variants still produce outlier updates above 1e-1 on the trace or fail to reduce persistent state by at least 25% versus PyTorch fp16 AdamW.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adam-optimizer-with-dynamic-scaling-for-4gb-vram-training-77c11493566e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

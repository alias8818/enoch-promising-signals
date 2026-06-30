# LoRA with 2-bit quantization for ultra-low VRAM fine-tuning on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lora-with-2-bit-quantization-for-ultra-low-vram-fine-tuning-on-gb10-ac91090513da`
Run ID: `lora-with-2-bit-quantization-for-ultra-low-vram-fine-tuning-on-gb10-ac91090513da-20260619T072115481976+0000`

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

Packed 2-bit storage reduced persistent base bytes to about 12.5% of FP16, but the non-fused PyTorch implementation increased peak CUDA allocation to 3.30x FP16 at d=4096 and produced 111.95x higher final MSE with 0.758 relative base quantization RMSE.

## Boundaries and scale limits

This is not a transformer, real dataset, 7B model, PEFT/bitsandbytes run, or fused int2 matmul kernel validation. It is an early mechanism probe for storage, peak CUDA allocation, and adaptation error.

## Claim scope

Self-contained PyTorch 2.12 packed 2-bit frozen linear base plus FP32 LoRA adapters on NVIDIA GB10, tested on synthetic low-rank adaptation at dimensions 1024 and 4096. The tested path stores base weights compactly but dequantizes to FP16 during forward.

## Why it stopped

Early bounded falsification of the non-fused packed-2-bit LoRA path: it saves persistent weight storage but does not deliver ultra-low peak CUDA allocation or comparable adaptation quality in the tested setup.

## Recommended next action

Do not pursue paper writing from this run; only continue if implementing a fused/groupwise 2-bit LoRA layer and rerunning this harness against the same FP16 baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused groupwise 2-bit LoRA linear on GB10
- Success threshold: At d=4096, fused/groupwise q2 LoRA peak CUDA allocation must be below the FP16 LoRA baseline and final MSE must be no more than 2x the FP16 LoRA final MSE.
- Stop condition: Stop if the fused path still materializes full dequantized weights, exceeds FP16 peak CUDA allocation, or final MSE remains above 2x the FP16 baseline after matching rank and steps.

## Evidence references

- Artifact root: `<local-path>/projects/lora-with-2-bit-quantization-for-ultra-low-vram-fine-tuning-on-gb10-ac91090513da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

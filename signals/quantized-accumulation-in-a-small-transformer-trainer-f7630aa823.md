# Quantized accumulation in a small transformer trainer

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-accumulation-in-a-small-transformer-trainer-f7630aa823`
Run ID: `quantized-accumulation-in-a-small-transformer-trainer-f7630aa823-20260611T025531956922+0000`

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

- Parent run decision: Quantized gradient accumulation for home training: enoch://control-plane/projects/quantized-gradient-accumulation-for-home-training-5a10341ce073/runs/quantized-gradient-accumulation-for-home-training-5a10341ce073-20260611T024142834994+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/79b0409ff79c

## What looked useful

q8 final eval loss mean was 0.460341 versus FP32 0.460326, a +0.000015 delta with 0 NaN/Inf runs and mean accumulator relative error 0.032856. q4 final eval loss mean was 0.462448, a +0.002122 delta, with mean accumulator relative error 0.557938. This supports q8 as viable in the small direct test and identifies q4 as a degradation boundary.

## Boundaries and scale limits

Synthetic task only; tiny transformer only; 1000-step runs only; simulated quantize/dequantize accumulator in PyTorch rather than a fused low-bit kernel; no GPT-2-small-class, real text corpus, long-run convergence, optimizer-state quantization, distributed training, or production throughput validation.

## Claim scope

In a controlled small 2-layer transformer trainer on a synthetic repeated-motif language-modeling task, simulated 8-bit per-tensor quantized gradient accumulation across 8 microbatches preserved final eval loss versus FP32 accumulation over 1000 optimizer steps and 3 seeds; 4-bit accumulation remained stable but showed a small repeatable loss penalty.

## Why it stopped

Tier 1 direct evidence produced a useful mechanism signal, but the evidence is synthetic, small-scale, short-run, and prototype-level, so it is not paper-positive.

## Recommended next action

Run a bounded deepen follow-up on a GPT-2-small-class or at least larger decoder-only transformer using a real tokenized text corpus, with q8 final validation loss required to stay within 0.1% of FP32 across at least 3 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: q8 gradient accumulation in a larger text-trained transformer
- Success threshold: q8 final validation loss within 0.1% of FP32 mean across at least 3 seeds, no NaN/Inf runs, and no persistent divergence in loss trajectory after warmup.
- Stop condition: Stop if q8 exceeds FP32 validation loss by more than 0.5% on two or more seeds, shows NaN/Inf instability, or the larger run cannot fit within the local calibrated compute budget.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-accumulation-in-a-small-transformer-trainer-f7630aa823`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

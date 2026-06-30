# 8-bit AdamW optimizer state quantization for CPU training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adamw-optimizer-state-quantization-for-cpu-training-594d5fe1a231`
Run ID: `8-bit-adamw-optimizer-state-quantization-for-cpu-training-594d5fe1a231-20260607T204843656901+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/69fa459122a8

## What looked useful

The memory target was achieved mechanically, but loss diverged or degraded by orders of magnitude. Diagnostics show 96-98% of quantized second-moment entries were zero at the end of failed 8-bit runs, while float32 AdamW had no zero second moments, identifying linear uint8 second-moment quantization as the likely instability source.

## Boundaries and scale limits

Local CPU-only NumPy experiments: 2M-parameter quadratic proxy for 40 steps and a 296k-parameter dense teacher-student MLP for 50 steps. This does not test PyTorch allocator behavior, fused kernels, large language models, long training, or stabilized 8-bit Adam variants.

## Claim scope

Naive blockwise linear 8-bit persistent AdamW moment state in a NumPy CPU implementation reduces optimizer-state memory to about 25% of float32 AdamW but fails stability on the tested quadratic and dense MLP CPU training tasks.

## Why it stopped

Proxy/local CPU experiments are sufficient to early-falsify the naive blockwise linear 8-bit AdamW state design, but they are not a full validation of all possible 8-bit AdamW implementations.

## Recommended next action

Stop this naive design; a bounded follow-up should test stabilized second-moment encodings before any larger CPU training validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized second-moment quantization for CPU AdamW
- Success threshold: Pass all required evidence criteria with saved JSON metrics and logs.
- Stop condition: Stop if the stabilized design still exceeds 1.2x float32 final loss on either task or requires more than 35% of float32 optimizer-state memory.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-optimizer-state-quantization-for-cpu-training-594d5fe1a231`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

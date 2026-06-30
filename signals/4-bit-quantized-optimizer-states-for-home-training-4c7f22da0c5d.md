# 4-bit quantized optimizer states for home training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `4-bit-quantized-optimizer-states-for-home-training-4c7f22da0c5d`
Run ID: `4-bit-quantized-optimizer-states-for-home-training-4c7f22da0c5d-20260530T071441017157+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/561ff17d42d8

## What looked useful

Corrected 8-bit optimizer states nearly matched FP32 validation loss (+0.0110) at 25.4% of FP32 optimizer-state memory, while the best stable 4-bit variant used 12.9% memory but lagged by +0.3247 validation loss. The main 4-bit failure mechanism was second-moment quantization: zeroing small nonzero v_t values can destabilize Adam, and minimum-code preservation stabilizes but distorts updates.

## Boundaries and scale limits

This is a bounded home-scale result on a synthetic token stream, not a GPT-2-small-class or real-corpus validation. Runtime uses Python-level quantize/dequantize rather than fused optimizer kernels, so speed is not a systems-performance claim.

## Claim scope

On a GB10 local PyTorch small-Transformer language-model task with three seeds and 250 training steps, blockwise 4-bit AdamW optimizer states either diverged under naive quantization or trained materially worse than FP32 even after preserving nonzero second-moment entries.

## Why it stopped

Proxy-scale but direct optimizer-training evidence falsified the simple 4-bit blockwise AdamW-state hypothesis for this local task; broader real-corpus validation would be needed to overturn it.

## Recommended next action

Stop this run as a bounded negative/useful-signal result; the next bounded test should evaluate a log-domain or error-feedback 4-bit second-moment quantizer against the corrected 8-bit control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Log-domain 4-bit Adam second-moment states for stable home training
- Success threshold: Mean final validation loss within 0.03 of FP32 across three seeds while using no more than 15% of FP32 optimizer-state memory and no NaNs/divergence.
- Stop condition: Stop if any candidate diverges in two seeds or if the three-seed mean validation-loss gap remains above 0.10 after 250 steps.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-quantized-optimizer-states-for-home-training-4c7f22da0c5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

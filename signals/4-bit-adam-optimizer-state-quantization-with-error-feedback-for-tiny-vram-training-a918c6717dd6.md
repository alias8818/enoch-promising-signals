# 4-bit Adam Optimizer State Quantization with Error Feedback for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-adam-optimizer-state-quantization-with-error-feedback-for-tiny-vram-training-a918c6717dd6`
Run ID: `4-bit-adam-optimizer-state-quantization-with-error-feedback-for-tiny-vram-training-a918c6717dd6-20260529T002213370981+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b40ae817e9c8

## What looked useful

Error feedback materially improved 4-bit Adam-state convergence under a damped denominator, but fp16 residuals reduced the practical state-memory saving to about 1.6x versus AdamW fp32 states. Without denominator stabilization, quantized second moments produced early NaNs even at 10x lower LR.

## Boundaries and scale limits

Only synthetic proxy training was run: 240 steps, small MLP, no real LM/vision dataset, no optimizer-state-dominated VRAM pressure, no fused kernel, no long-horizon convergence, and no comparison to production 8-bit/offloaded/low-rank optimizer baselines.

## Claim scope

On a small CUDA teacher-student regression proxy, packed 4-bit Adam moments with fp16 error-feedback residuals and stabilized epsilon (1e-4) matched or beat AdamW final loss over three seeds while using 62.5% of AdamW optimizer-state bytes; standard Adam epsilon (1e-8) diverged for both 4-bit variants.

## Why it stopped

No-paper closure: this is a proxy useful signal with an early standard-epsilon failure and a stabilized small-task success, not direct full validation of tiny-VRAM model training.

## Recommended next action

Run a bounded GPT-2-small-class or transformer block training follow-up with quantized-v flooring/epsilon ablations and baselines against 8-bit Adam and Adafactor before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-scale QAdam4 error-feedback stability and memory-pressure ablation
- Success threshold: Across at least three seeds, QAdam4+EF final validation/train loss is within 5% of AdamW and no worse than 8-bit Adam, while optimizer-state GPU bytes are at least 30% lower than AdamW fp32 states and the run fits a batch/model setting that AdamW cannot fit or cannot match at equal VRAM.
- Stop condition: Stop if standard stabilized variants still produce NaNs, if loss exceeds AdamW by more than 10% after the planned budget, or if residual/flooring overhead leaves less than 20% optimizer-state memory reduction versus AdamW.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-adam-optimizer-state-quantization-with-error-feedback-for-tiny-vram-training-a918c6717dd6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

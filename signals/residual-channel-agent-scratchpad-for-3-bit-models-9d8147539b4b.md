# Residual Channel Agent Scratchpad for 3-Bit Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-agent-scratchpad-for-3-bit-models-9d8147539b4b`
Run ID: `residual-channel-agent-scratchpad-for-3-bit-models-9d8147539b4b-20260601T063751314077+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8740107b585d

## What looked useful

Across three seeds at 5,000 steps, all-quantized 3-bit residuals stayed near chance at 0.0699 validation accuracy, 8 FP residual scratchpad channels improved to 0.1003, and 16 channels improved to 0.1153; the FP32 reference reached 0.8876, showing the task is learnable but the tested 3-bit recipe remains badly degraded.

## Boundaries and scale limits

Synthetic task only; tiny 64-hidden, 3-layer transformer; fake 3-bit quantization rather than production kernels; no pretrained LLM, natural-language agent scratchpad, or GPT-2-small-class validation.

## Claim scope

On a tiny causal transformer trained on a synthetic running modular-sum task, reserving 8 or 16 unquantized residual channels inside an otherwise fake-3-bit residual path improves validation accuracy versus quantizing all residual channels, but does not make the quantized model competent.

## Why it stopped

Bounded local evidence supports a small residual scratchpad benefit but also shows the tested mechanism does not rescue 3-bit training degradation; this is a proxy/synthetic result, not full validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should use a stronger quantization baseline with per-channel activation scaling and scratch-channel state diagnostics before attempting larger LLM validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Per-channel 3-bit quantization plus residual scratchpad diagnostics
- Success threshold: Scratchpad variant improves mean validation accuracy by at least 0.05 absolute over the per-channel 3-bit baseline and a linear probe decodes prefix-sum state from scratch channels at least 0.10 accuracy above quantized channels.
- Stop condition: Stop if the stronger all-quantized baseline matches scratchpad accuracy within 0.02 absolute or if scratch-channel state probes do not exceed quantized-channel probes by 0.05 absolute.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-agent-scratchpad-for-3-bit-models-9d8147539b4b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# 2-bit Activation-Weight Co-quantization with Residual Information Highways

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `2-bit-activation-weight-co-quantization-with-residual-information-highways-1e0954144146`
Run ID: `2-bit-activation-weight-co-quantization-with-residual-information-highways-1e0954144146-20260531T213951072976+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/290050cb2943

## What looked useful

The run measured a real 2-bit quantization gap versus float, but the tested full-precision residual information highway did not improve validation-selected test accuracy over plain 2-bit and underperformed a quantized residual skip control.

## Boundaries and scale limits

Small vision dataset only; fake quantization rather than packed integer kernels; MLP only; no CNN, transformer, language-model, energy, or hardware-throughput validation.

## Claim scope

A NumPy QAT probe on sklearn digits with a two-hidden-layer 128-wide MLP found no accuracy benefit from a same-width full-precision residual information highway in a 2-bit weight and 2-bit activation model.

## Why it stopped

Bounded local evidence does not support the tested residual information highway; this is an early scoped falsification, not a full-scale rejection of all residual quantized architectures.

## Recommended next action

Stop this mechanism as no-paper evidence unless a future project proposes a materially different, hardware-efficient residual encoding with a direct success threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-activation-weight-co-quantization-with-residual-information-highways-1e0954144146`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

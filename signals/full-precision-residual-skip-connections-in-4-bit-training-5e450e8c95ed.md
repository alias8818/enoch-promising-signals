# Full-Precision Residual Skip Connections in 4-bit Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `full-precision-residual-skip-connections-in-4-bit-training-5e450e8c95ed`
Run ID: `full-precision-residual-skip-connections-in-4-bit-training-5e450e8c95ed-20260602T183711278919+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/878afbbb9b2b

## What looked useful

Full-precision residual stream improved mean best validation loss from 4.1430 to 4.0695 versus quantized residual stream, a paired mean gain of 0.0735 nats across 3 seeds, with zero nonfinite steps. FP32 remained better at 3.9926.

## Boundaries and scale limits

Synthetic sequence task only; 350 training steps; 3 seeds; no real text corpus; no GPT-2-small-class scale; no true integer 4-bit kernels; no optimizer-state quantization; no production memory or wall-clock efficiency claim.

## Claim scope

In a 4-layer, width-128 synthetic autoregressive transformer trained with PyTorch straight-through fake 4-bit weights and activations, keeping the residual stream full precision improved best validation loss versus fake-quantizing the residual stream after each residual add across 3 matched seeds.

## Why it stopped

No-paper useful signal: this was a synthetic fake-quant proxy that supports the residual-precision mechanism but does not provide full validation of 4-bit training.

## Recommended next action

Run a bounded direct follow-up on a real text corpus with a GPT-2-small-class or parameter-matched small transformer, true or production-relevant 4-bit QAT kernels, and ablations for residual stream, LayerNorm, and branch-output precision.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus 4-bit QAT residual precision ablation
- Success threshold: Full-precision residual stream improves mean validation loss versus quantized residual stream by at least 0.03 nats or eliminates reproducible instability across at least 3 matched seeds without erasing the intended memory/training efficiency rationale.
- Stop condition: Stop if the full-precision residual condition does not beat quantized residual stream on mean validation loss or stability after the planned real-corpus budget, or if its memory/throughput overhead makes the 4-bit training setup practically unattractive.

## Evidence references

- Artifact root: `<local-path>/projects/full-precision-residual-skip-connections-in-4-bit-training-5e450e8c95ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

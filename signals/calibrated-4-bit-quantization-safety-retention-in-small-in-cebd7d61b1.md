# Calibrated 4-bit quantization safety retention in small instruction LMs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `calibrated-4-bit-quantization-safety-retention-in-small-in-cebd7d61b1`
Run ID: `calibrated-4-bit-quantization-safety-retention-in-small-in-cebd7d61b1-20260522T050850964261+0000`

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

- Parent run decision: Small-LM residual safety under low-bit quantization: enoch://control-plane/projects/small-lm-residual-safety-under-low-bit-quantization-84f4915740/runs/small-lm-residual-safety-under-low-bit-quantization-84f4915740-20260522T043802355610+0000
- Parent run decision: Quantized Agent Residual Safety: enoch://control-plane/projects/quantized-agent-residual-safety-ffb017ce72fb/runs/quantized-agent-residual-safety-ffb017ce72fb-20260521T200443227399+0000

## What looked useful

Activation-aware int4 clipping reduced mean layer reconstruction MSE versus naive int4 but reduced harmful refusal rates: harmful+benign calibrated int4 was -15.3 percentage points versus fp16 and -12.5 points versus naive int4 on paired reclassified refusal metrics.

## Boundaries and scale limits

Single 0.5B instruction model, local prompt set, heuristic refusal classifier, sampled generations, fake dequantized int4 weights rather than packed production kernels; not evidence about 7B+ models or broad safety benchmarks.

## Claim scope

On Qwen/Qwen2.5-0.5B-Instruct with 24 harmful and 16 benign local prompts over fixed seeds 11,22,33, activation-calibrated fake weight-only int4 quantization did not retain harmful-prompt refusal behavior better than fp16 or naive int4.

## Why it stopped

Tier 2 local evidence directly falsified the calibrated-retention threshold: calibrated int4 failed to stay within 5 percentage points of fp16 harmful refusal and was worse than naive int4, despite using fixed seeds, ablations, and a real baseline.

## Recommended next action

Stop this follow-up as a no-paper negative useful signal; do not scale this calibration objective without replacing the MSE-only clipping criterion with a safety-behavior-aware objective and revalidating against fp16 and naive int4.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-4-bit-quantization-safety-retention-in-small-in-cebd7d61b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

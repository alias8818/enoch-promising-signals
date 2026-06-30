# Per-Layer 4-bit Adam with Fisher-Scaled Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `per-layer-4-bit-adam-with-fisher-scaled-quantization-a48f75a269a3`
Run ID: `per-layer-4-bit-adam-with-fisher-scaled-quantization-a48f75a269a3-20260527T190713536424+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b00ef2eaaae5

## What looked useful

Fisher normalization of the first moment by sqrt(v) plus log2 quantization of the second moment rescued 4-bit Adam state training on bounded GPU tests where naive linear 4-bit moment quantization failed in every seed.

## Boundaries and scale limits

Evidence is limited to small synthetic tasks, 450-step runs, un-packed Python quantize/dequantize code, and estimated optimizer-state memory. It does not validate language-model training, long schedules, packed 4-bit kernels, or production throughput.

## Claim scope

On two deterministic small MLP synthetic classification tasks, a Fisher-scaled 4-bit AdamW state quantizer preserved validation accuracy close to fp32 AdamW while naive per-tensor 4-bit state quantization collapsed to NaN loss.

## Why it stopped

No-paper useful signal: the current result is a small synthetic proxy that supports the mechanism but is not direct/full validation for large-model optimizer training.

## Recommended next action

Run a bounded small-transformer language-model follow-up comparing fp32 AdamW, naive4, and fisher4 under equal tokens and learning-rate schedule, with packed-state memory accounting if available.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer validation of Fisher-scaled 4-bit Adam state quantization
- Success threshold: fisher4 completes all runs without NaNs, stays within 2% relative validation loss of fp32 AdamW, beats naive4 by at least 10% relative validation loss or avoids naive4 divergence, and shows at least 6x packed-equivalent optimizer-state memory reduction.
- Stop condition: Stop if fisher4 diverges or exceeds fp32 AdamW validation loss by more than 5% relative in two matched runs, or if Python optimizer overhead prevents completing the bounded token budget within the local run budget.

## Evidence references

- Artifact root: `<local-path>/projects/per-layer-4-bit-adam-with-fisher-scaled-quantization-a48f75a269a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Residual-Preserved 1.58-bit Quantization with Full-Precision Skip Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-preserved-1-58-bit-quantization-with-full-precision-skip-channels-be770d9d7365`
Run ID: `residual-preserved-1-58-bit-quantization-with-full-precision-skip-channels-be770d9d7365-20260528T165401028529+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a4ad4d2c21be

## What looked useful

Selected skip channels consistently improved residual reconstruction over plain ternary quantization, with strongest gains on heavy-tailed weights, but bit-budget-matched controls were mixed and gaussian cases favored ordinary 3-bit quantization.

## Boundaries and scale limits

No trained language model, perplexity, downstream task, hardware kernel, or full-scale memory/throughput validation was run. Effective bit cost was estimated analytically rather than implemented in a packed format.

## Claim scope

Synthetic residual-block reconstruction with d_model=256, 1024 samples, 6 seeds, and gaussian/heavy-tailed/low-rank weight distributions shows selected full-precision skip channels reduce residual error versus plain 1.58-bit ternary quantization.

## Why it stopped

Proxy evidence supports the residual-preservation mechanism but does not validate the model-quality or hardware-efficiency claim, and the bit-budget comparison is mixed.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should quantize a small trained transformer checkpoint with activation-calibrated skip-channel selection and compare perplexity against bit-budget-matched 2/3/4-bit baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-Calibrated Skip Channels on a Small Trained Transformer
- Success threshold: At 1-2% full-precision channels, skip-channel ternary recovers at least 50% of the perplexity degradation from plain ternary and matches or beats the nearest effective-bit low-bit baseline on a majority of evaluated layers/models.
- Stop condition: Stop if skip-channel ternary fails to beat random channel preservation or fails to recover at least 25% of ternary perplexity degradation on the first trained-checkpoint evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/residual-preserved-1-58-bit-quantization-with-full-precision-skip-channels-be770d9d7365`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

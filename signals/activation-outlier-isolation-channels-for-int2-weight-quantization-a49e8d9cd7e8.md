# Activation Outlier Isolation Channels for INT2 Weight Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `activation-outlier-isolation-channels-for-int2-weight-quantization-a49e8d9cd7e8`
Run ID: `activation-outlier-isolation-channels-for-int2-weight-quantization-a49e8d9cd7e8-20260628T115456475280+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.2: enoch://research-facility/provider/hf:zai-org/GLM-5.2/c4557f400578

## What looked useful

Across 216 synthetic trials, activation-selected isolation reduced mean relative MSE from 0.398894 to 0.241061 and beat random and weight-norm isolation in every trial; a no-outlier control removed the activation-selection advantage over random.

## Boundaries and scale limits

No real transformer, perplexity, downstream task, kernel packing, throughput, or equal-production-implementation validation was run. Isolated columns were counted as 16-bit and tested only in NumPy synthetic matrices.

## Claim scope

Synthetic linear-layer probe: activation second-moment channel selection can reduce output reconstruction error for INT2 weight quantization when activations contain outlier input channels.

## Why it stopped

Synthetic evidence is a useful mechanism signal but not direct paper-grade validation for INT2 transformer weight quantization.

## Recommended next action

Run a bounded real-model follow-up on transformer projection layers using calibration activations, perplexity/task metrics, random and equal-bit-budget controls, and an AWQ/GPTQ-style baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real transformer activation-outlier channel isolation for INT2 projection weights
- Success threshold: Activation-isolated INT2 must improve perplexity or task accuracy over all-INT2 and both random and weight-norm mixed-precision controls at matched effective bits on at least two model layers or one end-to-end small model.
- Stop condition: Stop if activation-selected columns do not beat random mixed-precision columns under matched effective bits, or if real activation outliers are not stable across calibration/evaluation samples.

## Evidence references

- Artifact root: `<local-path>/projects/activation-outlier-isolation-channels-for-int2-weight-quantization-a49e8d9cd7e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

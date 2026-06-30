# Progressive Residual Refinement: Multi-Rate 2-bit+Residual vs 4-bit Uniform

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `progressive-residual-refinement-multi-rate-2-bit-residual-vs-4-bit-uniform-7cf9101fb08e`
Run ID: `progressive-residual-refinement-multi-rate-2-bit-residual-vs-4-bit-uniform-7cf9101fb08e-20260521T194904562950+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2a296f7a6b8d

## What looked useful

Across 75 full-rate distribution/seed/block comparisons, 2+2 PRR had mean MSE 2.65x, median 2.72x, and best case 2.27x versus direct 4-bit uniform. Multi-rate partial refinement was worse, from 5.00x MSE at 3.5 avg bits/value to 14.77x at 2.5 avg bits/value.

## Boundaries and scale limits

No real transformer weights, activations, perplexity, task accuracy, entropy coding, or hardware kernel measurements were run. The result is a direct mechanism-level rate-distortion proxy, not a full model validation.

## Claim scope

For simple per-block min/max affine quantization on synthetic weight-like scalar distributions, 2-bit base plus 2-bit residual refinement is worse than direct 4-bit uniform quantization at equal nominal 4 data bits/value.

## Why it stopped

Proxy early falsification: direct quantization distortion shows the tested 2-bit base plus 2-bit residual scheme is consistently worse than 4-bit uniform, so a larger model run would not be a justified next step for this exact mechanism.

## Recommended next action

Stop this simple 2+2 affine PRR path; only revisit with a changed residual codebook design that can produce at least 16 useful reconstruction levels at the same data-bit budget, then test on real model weights and activations.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/progressive-residual-refinement-multi-rate-2-bit-residual-vs-4-bit-uniform-7cf9101fb08e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

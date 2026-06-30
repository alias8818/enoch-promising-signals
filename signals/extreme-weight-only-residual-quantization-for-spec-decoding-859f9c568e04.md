# Extreme Weight-Only Residual Quantization for Spec-Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `extreme-weight-only-residual-quantization-for-spec-decoding-859f9c568e04`
Run ID: `extreme-weight-only-residual-quantization-for-spec-decoding-859f9c568e04-20260619T091252213536+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/38be93e803b3

## What looked useful

Across 5 calibrated seeds, residual_2x_int2 at 4 bpw achieved 0.5805 expected speculative acceptance versus 0.8496 for direct_int4; residual_3x_int2 at 6 bpw achieved 0.7738 versus 0.9629 for direct_int6; residual_4x_int2 at 8 bpw achieved 0.8787 versus 0.9912 for direct_int8. The simple extreme residual-int2 stack is not a promising draft-weight representation without a stronger codebook or a separate kernel advantage.

## Boundaries and scale limits

Does not test real transformer layers, real token streams, multi-token speculative decoding chains, learned or activation-aware residual codebooks, quantized GPU kernels, or accepted tokens per second in production serving.

## Claim scope

Projection-level synthetic next-token distribution proxy: stacked signed int2 residual weight-only quantizers were worse than direct int4/int6/int8 quantizers at matched nominal bit budgets for speculative acceptance, top-1 agreement, KL, and logit RMSE.

## Why it stopped

Moderate proxy evidence consistently rejects the tested mechanism at matched nominal bit budgets; direct quantization preserves the speculative-decoding target distribution much better.

## Recommended next action

Stop this formulation as no-paper early falsification; only revisit if proposing a learned/non-uniform residual codebook or an optimized kernel with a concrete accepted-tokens-per-second threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/extreme-weight-only-residual-quantization-for-spec-decoding-859f9c568e04`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

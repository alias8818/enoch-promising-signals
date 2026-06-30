# Entropy-Bounded Residual Channels for 1-bit Weight Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-bounded-residual-channels-for-1-bit-weight-quantization-d0a8a8ed3ee8`
Run ID: `entropy-bounded-residual-channels-for-1-bit-weight-quantization-d0a8a8ed3ee8-20260521T205623080509+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2a296f7a6b8d

## What looked useful

Across 160 medium-sweep comparisons, entropy-bounded top-residual correction beat the matched random residual control every time. Mean weight-MSE reductions at 1.10 bpw were 13.03% for gaussian, 22.51% for laplace, 17.24% for lowrank_noisy, and 66.01% for outlier_sparse matrices. The sparse-outlier family also exposed a limitation: a single shared residual amplitude was best at 1.10 bpw and degraded at larger overheads.

## Boundaries and scale limits

No real pretrained model layers, no task accuracy or perplexity, no established PTQ/QAT baseline comparison, no entropy-coder implementation, no metadata/throughput measurement, and no GPU/kernel validation were tested.

## Claim scope

Synthetic matrix and random linear-output probes show that magnitude-selected sparse ternary residual streams can reduce 1-bit per-row quantization error under empirical entropy budgets from 1.05 to 1.50 bits per weight, compared with binary-only quantization and matched random residual controls.

## Why it stopped

This run is a synthetic/proxy mechanism validation only, not a full model-quality or systems validation, so it should close as no-paper useful signal rather than a positive paper result.

## Recommended next action

Run a bounded direct follow-up on real pretrained transformer linear-layer weights, comparing binary-only, EBR with per-row or multi-code residual amplitudes, and a standard low-bit PTQ baseline on layer reconstruction and small calibration perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transformer Layer EBR Probe with Per-Row Residual Amplitudes
- Success threshold: At <=1.15 effective bits per weight including residual entropy and metadata, EBR reduces layer output MSE by at least 10% versus binary-only on most tested layers and improves small calibration perplexity versus binary-only without losing to the low-bit PTQ control by an impractical margin.
- Stop condition: Stop as negative if real transformer layers show less than 5% median output-MSE reduction versus binary-only at <=1.15 effective bits per weight, or if metadata/coding overhead pushes the practical budget above the target.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-bounded-residual-channels-for-1-bit-weight-quantization-d0a8a8ed3ee8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

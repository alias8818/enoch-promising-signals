# Benchmark-scale activation-outlier residual KV-cache ablation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `benchmark-scale-activation-outlier-residual-kv-cache-ablat-1a62aa546e`
Run ID: `benchmark-scale-activation-outlier-residual-kv-cache-ablat-1a62aa546e-20260522T075854519621+0000`

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

- Parent run decision: Activation-Outlier Residual Channels for KV-Cache Compression: enoch://control-plane/projects/activation-outlier-residual-channels-for-kv-cache-compression-670d1fe086f0/runs/activation-outlier-residual-channels-for-kv-cache-compression-670d1fe086f0-20260522T005226764313+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/130c0d3912f4

## What looked useful

The 1% outlier cutoff increased loss by 0.0402 nats/token versus baseline, compared with random-control mean 0.0179 and std 0.0102, giving z=2.18 but missing the >0.05 nats/token absolute threshold. Nearby 0.5% and 2% cutoffs did not support a robust disproportionate effect.

## Boundaries and scale limits

Single GPT-2-class pretrained model, 32 calibration windows, 32 evaluation windows, sequence length 96, suffix length 48, 8 random controls per cutoff. Not tested on larger models, long-context serving, quantized KV caches, per-layer outlier selection, or separated key-only/value-only interventions.

## Claim scope

On distilgpt2 cached next-token evaluation over 32 WikiText-2 windows, zeroing KV-cache channels corresponding to residual activation-outlier dimensions produced at most a weak cutoff-sensitive loss increase versus random channel controls; it did not meet the predeclared practical threshold.

## Why it stopped

Tier 1 direct test completed but failed the predeclared robust practical threshold; result is a useful no-paper signal, not full validation.

## Recommended next action

Run one bounded deepen test that selects activation outliers per layer and separates key-only from value-only cache ablations; stop if no condition exceeds random controls by 2 std and 0.05 nats/token across at least two seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layerwise key-versus-value activation-outlier KV-cache ablation
- Success threshold: At least one predeclared layer/tensor condition exceeds its random-control mean by 2 standard deviations and by more than 0.05 nats/token in both seeds, without being contradicted by neighboring outlier fractions.
- Stop condition: Stop as negative/no-paper if no layer/tensor condition meets both the statistical and absolute thresholds across two seeds, or if the apparent effect appears only in one cutoff without seed replication.

## Evidence references

- Artifact root: `<local-path>/projects/benchmark-scale-activation-outlier-residual-kv-cache-ablat-1a62aa546e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

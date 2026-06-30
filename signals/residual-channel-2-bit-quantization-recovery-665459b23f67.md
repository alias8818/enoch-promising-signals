# Residual-Channel 2-bit Quantization Recovery

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-2-bit-quantization-recovery-665459b23f67`
Run ID: `residual-channel-2-bit-quantization-recovery-665459b23f67-20260528T043213393778+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4a9b5300cb31

## What looked useful

Per-layer signed int2 over 20 seeds dropped mean accuracy from 97.76% fp32 to 97.17%; activation-weighted residual retention at 10% channels raised it to 97.44% and recovered about 57.7% of the small drop (paired p=0.0247 vs plain). Raw residual-norm retention did not help, and per-row int2 showed no statistically clear residual-channel gain.

## Boundaries and scale limits

Toy-to-small classifier only; no transformer, CNN, language model, activation quantization, quantization-aware training, real int2 kernel, latency benchmark, or large pretrained model evidence.

## Claim scope

On sklearn digits with a small CUDA MLP and post-training signed int2 weight quantization, activation-weighted residual/full-precision channel rows can recover a small accuracy drop under per-layer scaling, but raw residual-norm channel selection is not supported and per-row scaling shows no clear benefit.

## Why it stopped

No-paper useful signal: the local evidence is small-model and partly synthetic/toy-scale, with a modest effect that does not consistently beat random retention; it is not publication-grade validation.

## Recommended next action

Run a bounded deepen test on a transformer or CNN where 2-bit PTQ causes at least a 1-2 point metric drop, comparing activation-weighted residual rows against random rows, raw residual rows, and matched int3/int4 or calibration baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-weighted residual channels for 2-bit PTQ on a bounded transformer or CNN
- Success threshold: Activation-weighted residual channels recover at least 40% of the plain 2-bit metric drop and beat the best random/matched-storage baseline by at least 0.5 metric points or a predeclared statistically meaningful margin.
- Stop condition: Stop if plain 2-bit degradation is below 1 point, activation-weighted retention fails to beat random or matched higher-bit baselines, or residual-channel storage overhead eliminates practical compression benefit.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-2-bit-quantization-recovery-665459b23f67`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Residual Channel Extreme Quantization: 1.5-bit Weights with Learned Error Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-extreme-quantization-1-5-bit-weights-with-learned-error-channels-2a8545eb7366`
Run ID: `residual-channel-extreme-quantization-1-5-bit-weights-with-learned-error-channels-2a8545eb7366-20260522T000045109137+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e11337304f75

## What looked useful

Residual error channels directionally reduce ternary quantization error, but near 2.0 fp16-accounted bits/weight they recover only about 4-14% of output MSE, and near 3.1 bits/weight only about 16-27%, making the broad 1.5-bit-weight claim unsupported in this proxy.

## Boundaries and scale limits

No end-to-end neural training, no real language data, no transformer layers, no inference-kernel benchmark, and no learned-SGD residual channels. The residual correction is an optimistic SVD upper bound.

## Claim scope

Post-training synthetic 256x256 and 512x512 linear maps with column-wise ternary weights and optimal low-rank residual-channel repair under fp16/fp32 side-parameter accounting.

## Why it stopped

Proxy/early falsification: an optimistic low-rank residual repair did not recover enough ternary quantization error under honest bit accounting to support the broad claim.

## Recommended next action

Stop the paper path for this run; only continue with a bounded QAT follow-up if it can show at least 50% recovery of a ternary model quality gap below about 2.0 effective bits/weight.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware residual channels on a small real model
- Success threshold: Recover at least 50% of the ternary-only quality gap versus dense while keeping total effective storage at or below about 2.0 bits/weight.
- Stop condition: Stop if recovery is below 25% at 2.0 bits/weight or if matching 50% recovery requires more than 3.0 effective bits/weight.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-extreme-quantization-1-5-bit-weights-with-learned-error-channels-2a8545eb7366`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# 1-Bit Activation Forward with Narrow FP32 Residual Stream

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `1-bit-activation-forward-with-narrow-fp32-residual-stream-7c913d485c66`
Run ID: `1-bit-activation-forward-with-narrow-fp32-residual-stream-7c913d485c66-20260602T223730995605+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5bfc35e4763c

## What looked useful

The dense FP32 baseline reached 0.7726 mean test accuracy. Pure 1-bit hidden activations dropped 9.84 percentage points. A 6.25% exact-FP32 residual stream still dropped 9.37 percentage points, far outside the predeclared 1 percentage point success threshold, although normalized logit MSE improved slightly and wider residual streams recovered monotonically.

## Boundaries and scale limits

Toy MLP only; synthetic labels only; inference-only activation compression only; no transformer blocks, language-model perplexity, quantized training, learned residual routing, custom kernels, or hardware bandwidth measurements.

## Claim scope

In a 5-seed NumPy toy dense tanh MLP forward-inference proxy on synthetic teacher classification data, fixed calibrated exact-FP32 residual channels of 6.25% or less did not preserve dense FP32 accuracy when the remaining hidden activations were replaced by 1-bit sign values.

## Why it stopped

Proxy/toy forward experiment falsified the declared narrow fixed-FP32 residual success threshold; this is not a full transformer-scale validation or disproof.

## Recommended next action

Stop this fixed-channel narrow-residual variant as an early proxy negative; only pursue a bounded follow-up if it changes the mechanism to learned or per-token residual routing and tests against the same <=6.25% residual-width threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned per-token residual routing for 1-bit activation forward passes
- Success threshold: <=1 percentage point mean accuracy drop from dense FP32 and normalized logit MSE <0.10 at <=6.25% exact-FP32 residual values, with residual-index overhead included in the effective storage accounting.
- Stop condition: Stop if learned/per-token routing still loses >3 percentage points at <=6.25% residual width or if routing metadata/compute removes the claimed bandwidth or memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-activation-forward-with-narrow-fp32-residual-stream-7c913d485c66`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Real-model activation-aware INT8 CPU linear-layer validation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-model-activation-aware-int8-cpu-linear-layer-validati-074b85f784`
Run ID: `real-model-activation-aware-int8-cpu-linear-layer-validati-074b85f784-20260614T112852960516+0000`

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

- Parent run decision: Activation-Aware INT8 Quantization for CPU Inference: enoch://control-plane/projects/activation-aware-int8-quantization-for-cpu-inference-0bb49e5fb4aa/runs/activation-aware-int8-quantization-for-cpu-inference-0bb49e5fb4aa-20260614T102556583517+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/293290b77429

## What looked useful

Plain dynamic W8A8 normalized RMSE was 0.0018236475. The best activation-aware variant, alpha 0.75, reached 0.0017962945, only a 1.4999% error reduction versus the predeclared 10% threshold. The scoped mechanism threshold was not met, although artifacts make the small direct test reproducible.

## Boundaries and scale limits

One small pretrained model, one first-block QKV linear layer, 113 calibration tokens, 112 evaluation tokens, NumPy int8/int32 simulation timing rather than optimized CPU INT8 kernels, no end-to-end perplexity or generation-quality evaluation.

## Claim scope

Tier 1 controlled small direct test of activation-aware SmoothQuant-style W8A8 scaling on the first-block QKV linear layer of cached EleutherAI/pythia-14m, using held-out real token activations and float32 layer output as reference.

## Why it stopped

Early direct falsification of the Tier 1 first-layer QKV threshold: activation-aware scaling improved normalized RMSE by only 1.4999%, below the required 10%, so this run is no-paper useful evidence rather than a full validation.

## Recommended next action

Run one bounded direct follow-up that sweeps MLP and attention projection layers in a small real model with an optimized CPU INT8 backend; stop if activation-aware scaling again fails to reduce layer-output error by at least 10% on held-out activations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layer-sweep activation-aware INT8 CPU validation on outlier-prone real-model projections
- Success threshold: At least two outlier-prone real-model linear layers must show >=10% normalized RMSE reduction versus plain dynamic W8A8 on held-out activations with <=25% optimized CPU INT8 median latency overhead, and no tested layer may show a severe error regression above 10% relative normalized RMSE.
- Stop condition: Stop and finalize negative if MLP and attention projection layer sweep repeats the <10% error-reduction result or if optimized CPU INT8 timing shows activation-aware scaling adds >25% median latency overhead.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-activation-aware-int8-cpu-linear-layer-validati-074b85f784`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

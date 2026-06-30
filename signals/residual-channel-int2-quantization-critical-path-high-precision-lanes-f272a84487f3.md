# Residual-Channel INT2 Quantization: Critical-Path High-Precision Lanes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-int2-quantization-critical-path-high-precision-lanes-f272a84487f3`
Run ID: `residual-channel-int2-quantization-critical-path-high-precision-lanes-f272a84487f3-20260531T230100860001+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/fa735c67db63

## What looked useful

Residual high-precision lanes are useful for reducing INT2 activation projection error, but channel selection should benchmark against simple weight-norm and activation-RMS controls; the tested critical-path heuristic lost to the best simple control in 21 of 24 real-model layer/budget comparisons.

## Boundaries and scale limits

No end-to-end perplexity, generation-quality, latency, kernel-overhead, or large-checkpoint validation; real-model evidence is limited to distilgpt2, six MLP c_fc layers, 800 prompt tokens per layer, and forward projection error metrics.

## Claim scope

Bounded projection-level evidence on synthetic heavy-tail dense projections and distilgpt2 MLP c_fc activations: preserving 1-10% high-precision activation channels reduces INT2 projection error, but the calibrated critical-path selector does not beat simple controls on real-model layers.

## Why it stopped

Proxy projection evidence is useful but mixed: residual lanes help, while the specific critical-path selector is not competitive with simple controls on direct distilgpt2 layer evidence.

## Recommended next action

Stop this critical-path selector as a paper candidate; run a bounded follow-up that tests simpler weight-norm residual lanes end-to-end against all-INT2 and activation-RMS controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Weight-Norm Residual Lanes for INT2 Transformer Inference
- Success threshold: Weight-norm residual lanes reduce perplexity degradation versus all-INT2 by at least 20% relative and beat every matched selector control at 5% or lower lane budget on the primary checkpoint.
- Stop condition: Stop if weight-norm lanes fail to beat activation-RMS or critical-path controls on perplexity at 5% lane budget, or if overhead estimates remove the practical benefit.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-int2-quantization-critical-path-high-precision-lanes-f272a84487f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

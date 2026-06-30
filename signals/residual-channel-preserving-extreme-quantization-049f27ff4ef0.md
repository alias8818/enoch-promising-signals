# Residual-Channel Preserving Extreme Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-channel-preserving-extreme-quantization-049f27ff4ef0`
Run ID: `residual-channel-preserving-extreme-quantization-049f27ff4ef0-20260601T025441178977+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4ec8f6b79033

## What looked useful

Top-RMS channel preservation produced a consistent bounded mechanism signal: at 6.25% preserved channels, 2-bit delta loss fell from 7.293 all-quantized to 1.820, and 3-bit delta loss fell from 5.778 all-quantized to 0.212. Random preservation at the same budget remained poor, with 2-bit delta loss 8.197 and 3-bit delta loss 5.525.

## Boundaries and scale limits

Small pretrained model, small token slice, one calibration seed, activation-only hooks, no packed integer kernel, no weight quantization, no end-to-end memory or latency validation, and no larger-model or downstream-task robustness evidence.

## Claim scope

On distilgpt2 with forward-hook activation-only residual block output quantization over an 11,008-token WikiText-2 test slice, preserving top-RMS residual channels reduces 2-bit and 3-bit loss degradation far more than all-channel quantization or same-budget random channel preservation.

## Why it stopped

The local activation-only proxy supports the mechanism but is not a full validation of residual-channel preserving extreme quantization as a deployable compression method.

## Recommended next action

Stop this run as a no-paper useful signal; next, run a bounded deepen study on GPT-2-small-class models with full WikiText-2 validation, multiple random seeds, and layerwise/channel-budget ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small residual-channel preservation ablation under extreme activation quantization
- Success threshold: 3-bit top-RMS preservation at no more than 6.25% channels has mean delta loss <= 0.3 and beats random preservation by >= 2.0 delta-loss points; 2-bit top-RMS preservation beats all-quantized and random controls by >= 3.0 delta-loss points.
- Stop condition: Stop if the effect disappears on GPT-2-small, if random preservation matches top-RMS within 0.5 delta loss, or if 3-bit top-RMS preservation exceeds 0.8 mean delta loss at 6.25% preserved channels.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-preserving-extreme-quantization-049f27ff4ef0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

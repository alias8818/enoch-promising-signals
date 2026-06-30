# Asymmetric Quantization Cascade: INT4 Small + INT8 Large

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `asymmetric-quantization-cascade-int4-small-int8-large-92f40564b7b5`
Run ID: `asymmetric-quantization-cascade-int4-small-int8-large-92f40564b7b5-20260523T041434995303+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2d6e729e5612

## What looked useful

The cascade mechanism is plausible when the small model is capacity-limited but calibrated: it accepted 19.5% of held-out examples on average and lost 0.0035 absolute accuracy versus the INT8 large baseline. Earlier runs also showed a failure mode where poor benchmark construction makes the cascade degenerate into small-only routing.

## Boundaries and scale limits

Proxy-only evidence: dequantized PyTorch affine quantization, synthetic data, estimated MACs rather than hardware-native INT4/INT8 latency or energy, and no real LLM/vision/recommender benchmark.

## Claim scope

On a self-contained structured synthetic classification benchmark over 5 seeds, a validation-thresholded affine INT4 small model plus affine INT8 large fallback preserved large-only accuracy within 0.35 percentage points on average while reducing estimated linear-layer MACs to 80.6% of INT8-large-only.

## Why it stopped

Stopped after proxy evidence: the local mechanism is supported, but the result is not direct production-model evidence and should not be treated as full validation.

## Recommended next action

Run a bounded direct follow-up on a real benchmark with hardware-native INT4/INT8 inference and measured latency/energy before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hardware-native INT4-small/INT8-large cascade on a real benchmark
- Success threshold: Cascade accepts at least 15% of examples, test quality drops by no more than 0.5 percentage points versus INT8-large-only, and measured latency or energy improves by at least 10%.
- Stop condition: Stop if the real INT8 large baseline is not stronger than INT4 small-only, if thresholded routing cannot meet the 0.5 percentage-point quality target, or if measured routing/kernel overhead eliminates latency and energy savings.

## Evidence references

- Artifact root: `<local-path>/projects/asymmetric-quantization-cascade-int4-small-int8-large-92f40564b7b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

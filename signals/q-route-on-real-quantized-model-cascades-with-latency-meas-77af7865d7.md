# Q-Route on Real Quantized Model Cascades with Latency Measurement

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `q-route-on-real-quantized-model-cascades-with-latency-meas-77af7865d7`
Run ID: `q-route-on-real-quantized-model-cascades-with-latency-meas-77af7865d7-20260524T221121682966+0000`

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

- Parent run decision: Q-Route: Quantization-Aware Routing in Model Cascades: enoch://control-plane/projects/q-route-quantization-aware-routing-in-model-cascades-e2c498ca23dc/runs/q-route-quantization-aware-routing-in-model-cascades-e2c498ca23dc-20260524T200640351436+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b5ed284b6fb1

## What looked useful

Before testing routing algorithms, quantized cascades must verify fallback dominance or complementary errors. In this direct run, the larger fallback was about 2x slower and less accurate on held-out examples, so selective routing collapsed to small-only and fixed thresholds worsened latency/accuracy.

## Boundaries and scale limits

Single task, one completed model pair, 80/80 calibration/test split, CPU int8 dynamic quantization on GB10 ARM, per-example unbatched latency, simple confidence-threshold Q-route approximation rather than a learned Q-function router.

## Claim scope

On a 160-example GLUE SST-2 dev split, a CPU int8 qnnpack dynamic-quantized DistilBERT to BERT-base cascade did not produce a non-trivial Q-route benefit; the calibrated route selected the cheap DistilBERT stage for every held-out example because the fallback was slower and not more accurate.

## Why it stopped

Controlled Tier 1 direct test found no non-trivial cascade mechanism support for the completed real quantized model pair; the apparent speedup is the small-only baseline, not selective routing.

## Recommended next action

Stop this run as no-paper useful evidence; a next bounded test should first require a verified weak/strong quantized pair before evaluating nonzero Q-route behavior.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Q-route on verified weak/strong quantized SST-2 cascades
- Success threshold: Held-out Q-route has nonzero route rate, mean latency at least 1.3x faster than large-only, and accuracy no worse than 1 percentage point below large-only while beating small-only accuracy.
- Stop condition: Stop if no candidate pair has a stronger/complementary fallback on calibration or if every nonzero-route policy is slower without improving held-out accuracy over small-only.

## Evidence references

- Artifact root: `<local-path>/projects/q-route-on-real-quantized-model-cascades-with-latency-meas-77af7865d7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

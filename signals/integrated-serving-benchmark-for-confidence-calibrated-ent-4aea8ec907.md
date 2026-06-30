# Integrated serving benchmark for confidence-calibrated entropy cascades

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `integrated-serving-benchmark-for-confidence-calibrated-ent-4aea8ec907`
Run ID: `integrated-serving-benchmark-for-confidence-calibrated-ent-4aea8ec907-20260526T184421423242+0000`

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

- Parent run decision: Entropy-Gated Model Cascade for Local Inference: enoch://control-plane/projects/entropy-gated-model-cascade-for-local-inference-ce8f6933e1a0/runs/entropy-gated-model-cascade-for-local-inference-ce8f6933e1a0-20260525T171041427494+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/aef8ea46c8ed

## What looked useful

At a 1 pp accuracy budget the calibrated cascade accepted only about 7.7% of requests locally and reduced p95 latency by about 13.5%, below the 25% target. A risk sweep showed the latency target becomes reachable near a 2 pp quality budget, implying the main bottleneck is insufficient safe small-stage acceptance under saturated large-stage load.

## Boundaries and scale limits

Synthetic logits, simulated large-model predictions, and modeled service times; no real model trace, no production scheduler, and no measured GPU inference runtime.

## Claim scope

Controlled synthetic online-serving benchmark with 20,000 calibration requests and 50,000 test requests: temperature-calibrated entropy cascading preserved accuracy within 1 pp of the large-only baseline but did not achieve the required 25% p95 latency reduction.

## Why it stopped

Tier 1 controlled direct test failed the pre-registered 1 pp accuracy / 25% p95 latency success threshold; this is a useful no-paper early falsification under synthetic serving assumptions, not a full production validation.

## Recommended next action

Run the same benchmark on real small/large model logits or traces and stop unless calibrated local acceptance reaches at least 18% while maintaining a <=1 pp accuracy gap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-logit acceptance-rate test for calibrated entropy cascades
- Success threshold: Accept >=18% of requests locally, keep final accuracy within <=1 pp of large-only, and reduce p95 latency by >=25% on held-out traffic.
- Stop condition: Stop if calibrated local acceptance remains below 18% at <=1 pp accuracy gap or if p95 latency reduction remains below 25%.

## Evidence references

- Artifact root: `<local-path>/projects/integrated-serving-benchmark-for-confidence-calibrated-ent-4aea8ec907`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

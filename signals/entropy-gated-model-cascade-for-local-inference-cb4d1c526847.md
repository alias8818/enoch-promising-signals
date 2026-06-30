# Entropy-Gated Model Cascade for Local Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-gated-model-cascade-for-local-inference-cb4d1c526847`
Run ID: `entropy-gated-model-cascade-for-local-inference-cb4d1c526847-20260522T014345450682+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4f687c69d27f

## What looked useful

Entropy routing sent about 10.69% of samples to the larger model, recovered 1.72 percentage points over small-only, beat random same-fraction routing by 1.47 points, and cost about 53.35% of large-only latency. Max-confidence risk matched entropy at a lower route fraction, so entropy should be benchmarked as one uncertainty baseline rather than treated as uniquely validated.

## Boundaries and scale limits

Four synthetic seeds with tiny MLP classifiers on GB10 CUDA; no real LLM prompts, quantized runtimes, serving queues, KV-cache behavior, energy measurement, or production local inference stack.

## Claim scope

On a controlled synthetic local classification proxy, uncertainty-gated routing from a small model to a larger model improves the accuracy/cost tradeoff over small-only and random routing; entropy itself was not better than max-confidence risk.

## Why it stopped

No-paper useful signal: the mechanism is supported only on a synthetic proxy and entropy did not outperform a simpler confidence baseline.

## Recommended next action

Run a bounded real local-prompt benchmark with two resident local models and compare entropy, max-confidence risk, margin, random routing, small-only, and large-only on task quality plus wall-clock latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Local Prompt Benchmark for Uncertainty-Gated Cascades
- Success threshold: A gating method reaches at least 95% of large-only quality with at least 30% lower median wall-clock latency than large-only and beats random same-fraction routing by at least 2 absolute quality points on the held-out test split.
- Stop condition: Stop if no uncertainty score beats random same-fraction routing or if routing overhead/model residency removes the latency advantage below 10%.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-gated-model-cascade-for-local-inference-cb4d1c526847`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

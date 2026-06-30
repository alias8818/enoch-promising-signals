# Latency-Quality Router for CPU Model Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `latency-quality-router-for-cpu-model-cascade-c1e5574a1b19`
Run ID: `latency-quality-router-for-cpu-model-cascade-c1e5574a1b19-20260528T195651031771+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8fda443b78db

## What looked useful

The uncertainty signal works for quality triage, but latency savings require the expensive tier to be substantially slower than the cheap tier. In this run, direct expensive latency averaged 0.03555 ms, cheap latency averaged 0.02250 ms, router escalation averaged 56.545%, and the router needed expensive latency around 0.05176 ms to break even. Observed router latency was 19.32% slower than direct expensive serving.

## Boundaries and scale limits

Synthetic bag-of-words workload only; tiny Naive Bayes CPU models; sequential per-request timing only; no real transformer/LLM, tokenizer, batching, queueing, production traffic, or datacenter-scale serving validation.

## Claim scope

On a NumPy-only synthetic CPU text-classification cascade, confidence-margin routing preserved expensive-model quality within 1 percentage point and beat random same-rate escalation, but failed to reduce latency versus direct expensive-model serving because cheap-tier overhead exceeded the break-even budget.

## Why it stopped

Proxy/local evidence does not support the latency-reduction claim against the correct direct-expensive baseline, although it supports the quality-routing mechanism.

## Recommended next action

Stop this run as a proxy negative/useful-signal result; the next bounded test should use an actual slower CPU model pair and keep direct expensive serving as the primary latency baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU Cascade Router Test with a Real Slower Expensive Tier
- Success threshold: Router accuracy within 1 percentage point of direct expensive serving, at least 10% lower mean latency and no p95 regression versus direct expensive serving, and at least 5 percentage points higher accuracy than random same-rate routing.
- Stop condition: Stop if the direct expensive/cheap latency ratio is below the measured break-even ratio or if confidence routing cannot meet the 1 percentage point quality budget on calibration and heldout splits.

## Evidence references

- Artifact root: `<local-path>/projects/latency-quality-router-for-cpu-model-cascade-c1e5574a1b19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

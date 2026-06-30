# Adaptive Cascade Router with Latency SLO Enforcement

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-cascade-router-with-latency-slo-enforcement-60ba774f5af9`
Run ID: `adaptive-cascade-router-with-latency-slo-enforcement-60ba774f5af9-20260528T052911129378+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b47b93fd62bd

## What looked useful

SLO-aware routing produced positive paired SLO-violation reductions for every seed and load. At 10 rps, violations dropped from 27.63% for the accuracy-only cascade to 9.28%, with a 1.58 percentage point accuracy loss and lower mean cost.

## Boundaries and scale limits

Synthetic requests and difficulty scores only; no real LLM outputs, no measured semantic quality, no batching, no production traces, no accelerator serving kernels, and no multi-tenant interference. Medium run covered 30 seeds, 6 loads, and 5000 requests per policy/load/seed.

## Claim scope

In a bounded synthetic discrete-event serving simulator with three inference tiers, queue-state- and deadline-aware cascade routing reduced latency-SLO violation rates versus an accuracy-only cascade across 2-12 rps while losing at most 2.19 percentage points of accuracy.

## Why it stopped

No-paper closure: the local synthetic evidence supports the mechanism but is not direct production or model-serving evidence.

## Recommended next action

Run a bounded deepen test on a real or trace-driven LLM serving stack with measured quality, batching, queue telemetry, and the same accuracy-only versus SLO-aware policy comparison.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-driven LLM serving validation for SLO-aware cascade routing
- Success threshold: At least 30% relative SLO-violation reduction versus accuracy-only routing at matched load with <=2 percentage point quality loss and no higher mean cost.
- Stop condition: Stop if the SLO-aware router cannot reduce SLO violations by 10% relative at any tested load without more than 3 percentage points quality loss, or if trace/serving artifacts needed for direct evidence are unavailable.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-cascade-router-with-latency-slo-enforcement-60ba774f5af9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

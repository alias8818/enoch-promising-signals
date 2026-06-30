# CPU Cascade Router for Latency-Quality Pareto

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-cascade-router-for-latency-quality-pareto-ce95602c60fa`
Run ID: `cpu-cascade-router-for-latency-quality-pareto-ce95602c60fa-20260607T094609166605+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/536a305805e4

## What looked useful

Confidence-gated CPU cascades can produce a latency-quality Pareto benefit when the large model is much slower and small-model confidence identifies easy cases; the digits result shows the benefit can disappear when the large model is only modestly slower because every query pays the small-model cost.

## Boundaries and scale limits

Proxy-scale only: built-in sklearn datasets, CPU classifiers, single-query predict_proba latency, no LLM serving, no production batching, no task-quality metrics beyond classification accuracy, and small test sets for wine and breast_cancer.

## Claim scope

On three local sklearn CPU classification benchmarks, a small-model confidence router improved accuracy by 3.9 to 7.2 percentage points over random same-fraction routing and could match or nearly match large-model accuracy with fewer large-model calls when the large model was substantially slower.

## Why it stopped

Closed as no-paper useful signal because this run produced reproducible classifier-proxy evidence but not direct CPU LLM/router serving evidence.

## Recommended next action

Run a bounded direct CPU LLM cascade benchmark with two local language models, held-out routing thresholds, and end-to-end latency plus task-quality metrics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM Cascade Router Benchmark
- Success threshold: At least one held-out task suite shows >=95% of large-model quality with >=25% lower p50 or p95 latency than large-only and statistically clear improvement over random same-fraction routing.
- Stop condition: Stop if the cascade cannot beat random same-fraction routing or if small-model overhead makes every quality-preserving threshold no faster than large-only.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-cascade-router-for-latency-quality-pareto-ce95602c60fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

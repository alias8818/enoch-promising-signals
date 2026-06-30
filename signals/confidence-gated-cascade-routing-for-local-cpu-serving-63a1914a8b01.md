# Confidence-Gated Cascade Routing for Local CPU Serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-gated-cascade-routing-for-local-cpu-serving-63a1914a8b01`
Run ID: `confidence-gated-cascade-routing-for-local-cpu-serving-63a1914a8b01-20260621T181243236249+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.2: enoch://research-facility/provider/hf:zai-org/GLM-5.2/8c31183a0892

## What looked useful

At threshold 0.90 over 8 seeds, the cascade reached 0.8895 accuracy versus 0.8956 for expensive-only while reducing mean latency from 0.9706 ms to 0.6763 ms, a 30.3% mean latency reduction.

## Boundaries and scale limits

Not direct LLM serving evidence; no real request trace, no generation quality metric, no production serving stack, and no broad dataset robustness. Tail latency did not improve at the viable threshold.

## Claim scope

Synthetic NumPy local CPU classification cascade: a cheap probabilistic tier can confidence-gate escalation to a slower exact kNN fallback and reduce mean latency while staying within 1 percentage point of fallback-only accuracy.

## Why it stopped

No-paper closure: useful synthetic/proxy mechanism evidence, but not direct local LLM CPU serving validation.

## Recommended next action

Run a bounded direct local-serving follow-up on a real workload with a cheap confidence estimator, fallback model, quality metric, and mean plus p95 latency thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU serving cascade on real text classification or short-form generation requests
- Success threshold: Quality at least 98% of fallback-only, mean latency at least 20% lower than fallback-only, and p95 latency no more than 5% worse than fallback-only.
- Stop condition: Stop if no threshold satisfies the quality/mean/p95 criteria on the direct workload or if the cheap confidence score is not monotonic with accepted-case error.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-cascade-routing-for-local-cpu-serving-63a1914a8b01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

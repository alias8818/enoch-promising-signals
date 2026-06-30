# Direct CPU serving cascade on real text classification or short-form generation requests

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-cpu-serving-cascade-on-real-text-classification-or-b9a876e6f4`
Run ID: `direct-cpu-serving-cascade-on-real-text-classification-or-b9a876e6f4-20260621T193135404120+0000`

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

- Parent run decision: Confidence-Gated Cascade Routing for Local CPU Serving: enoch://control-plane/projects/confidence-gated-cascade-routing-for-local-cpu-serving-63a1914a8b01/runs/confidence-gated-cascade-routing-for-local-cpu-serving-63a1914a8b01-20260621T181243236249+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.2: enoch://research-facility/provider/hf:zai-org/GLM-5.2/8c31183a0892

## What looked useful

The nondegenerate cascade used a 0.975 validation-selected confidence threshold, routed 6.8% of held-out requests to fallback, achieved 0.9857 accuracy versus 0.9833 for strong-only, and reduced mean latency from 0.2464 ms to 0.0284 ms with p95 latency from 0.5593 ms to 0.0848 ms.

## Boundaries and scale limits

Single public dataset, one deterministic split/seed, simple NB models, no short-form generation, no LLM backend, no calibrated uncertainty study, no concurrent serving/load test, and no multi-dataset or multi-seed robustness.

## Claim scope

On one real SMS spam classification dataset, a CPU confidence-routed cascade from a cheap word-unigram Naive Bayes classifier to a slower character n-gram Naive Bayes fallback preserved strong-baseline accuracy while reducing per-request latency.

## Why it stopped

Tier 1 direct test produced a useful mechanism signal, but evidence is too narrow for publication-grade closure.

## Recommended next action

Run a bounded deepen follow-up on at least two additional real text classification datasets or one short-form generation routing task using calibrated confidence and the same nondegenerate cascade success criteria.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replicate CPU text-serving cascade across multiple real tasks with calibrated confidence
- Success threshold: For every tested workload, fallback rate is at least 5%, quality is no more than 1 percentage point below the strong-only baseline, and cascade mean and p95 latency are each at least 2x faster than strong-only.
- Stop condition: Stop if the cascade degenerates to cheap-only or strong-only routing, loses more than 1 percentage point quality on any workload, or fails to reach 2x mean and p95 latency speedup on any workload.

## Evidence references

- Artifact root: `<local-path>/projects/direct-cpu-serving-cascade-on-real-text-classification-or-b9a876e6f4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

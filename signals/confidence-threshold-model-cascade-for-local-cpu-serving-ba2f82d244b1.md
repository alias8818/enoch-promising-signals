# Confidence-threshold model cascade for local CPU serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-threshold-model-cascade-for-local-cpu-serving-ba2f82d244b1`
Run ID: `confidence-threshold-model-cascade-for-local-cpu-serving-ba2f82d244b1-20260529T103341055423+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/630e55275c8c

## What looked useful

The mechanism works when cheap-model confidence reliably identifies easy requests: the primary run matched big-only accuracy at 0.9975 while routing 31.3% of requests and improving latency from 2.076 ms/request to 0.684 ms/request; an independent seed stayed within 0.15 percentage points of big-only accuracy with 28.0% routed and 3.41x speedup.

## Boundaries and scale limits

Proxy-only evidence: synthetic data, centroid classifiers, mean latency only, no real production traces, no p95/p99 latency, no LLM or deployed local CPU model, and no threshold-transfer validation beyond two random seeds.

## Claim scope

On a controlled synthetic CPU classification workload with easy requests separable by a cheap 32-feature model and hard requests requiring a larger 256-feature model, confidence-threshold cascading preserved big-model accuracy or stayed within 1 percentage point while reducing measured mean latency by about 3.0x to 3.4x.

## Why it stopped

Stopped after bounded proxy confirmation because the result is useful but synthetic and not publication-grade direct evidence.

## Recommended next action

Run the same threshold-sweep protocol on a real local CPU task with an actual cheap model and larger fallback, collecting accuracy, p50/p95/p99 latency, calibration, and threshold stability.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real local CPU workload validation for confidence-threshold cascades
- Success threshold: At least 1.5x p95 latency speedup versus always-large while preserving accuracy within 1 percentage point and accepting at least 50% of requests on held-out data.
- Stop condition: Stop as negative if no threshold accepts at least 30% of requests while staying within 2 percentage points of always-large accuracy, or if p95 latency speedup is below 1.2x after accounting for routing overhead.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-threshold-model-cascade-for-local-cpu-serving-ba2f82d244b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

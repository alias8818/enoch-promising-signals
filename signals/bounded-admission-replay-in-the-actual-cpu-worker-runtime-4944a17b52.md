# Bounded admission replay in the actual CPU worker runtime

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-admission-replay-in-the-actual-cpu-worker-runtime-4944a17b52`
Run ID: `bounded-admission-replay-in-the-actual-cpu-worker-runtime-4944a17b52-20260621T063806149032+0000`

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

- Parent run decision: Bounded Queue Backpressure for CPU Worker Reliability: enoch://control-plane/projects/bounded-queue-backpressure-for-cpu-worker-reliability-3be8504e0f2c/runs/bounded-queue-backpressure-for-cpu-worker-reliability-3be8504e0f2c-20260621T062202040799+0000
- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/7933f37160e7

## What looked useful

Layered bounded admission reached 11/11 accuracy with zero unsafe leakage; transcript search reached 9/11 with one unsafe leakage; flat retrieval reached 6/11 with five unsafe leakage/noise failures.

## Boundaries and scale limits

Small deterministic suite with explicit admission labels; no real LLM summarization, production Enoch controller state, multi-job persistence, broad private corpus, or noisy learned admission classifier was tested.

## Claim scope

In an 8-episode, 11-query controlled replay suite run in the local CPU worker runtime, bounded layered admission retained durable worker/doctrine/run-state facts, rejected noisy/private events, handled latest corrections, and outperformed transcript and flat retrieval baselines.

## Why it stopped

Tier 1 direct threshold passed, but evidence remains controlled and small; this is no-paper mechanism support rather than publication-grade validation.

## Recommended next action

Run one bounded deepen follow-up using a larger replay set with unlabeled/noisy candidate events and persistence across separate process invocations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded admission with unlabeled replay events and cross-process persistence
- Success threshold: Layered admission accuracy >= 0.85, unsafe leakage count == 0, stale/noise error rate at least 50% lower than flat_retrieval, and no regression after save/reload.
- Stop condition: Stop if layered admission leaks any raw sensitive value, fails to beat flat_retrieval by 0.10 accuracy, or persistence changes any held-out answer.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-admission-replay-in-the-actual-cpu-worker-runtime-4944a17b52`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

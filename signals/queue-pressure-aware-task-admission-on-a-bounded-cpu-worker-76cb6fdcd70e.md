# Queue-Pressure-Aware Task Admission on a Bounded CPU Worker

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-pressure-aware-task-admission-on-a-bounded-cpu-worker-76cb6fdcd70e`
Run ID: `queue-pressure-aware-task-admission-on-a-bounded-cpu-worker-76cb6fdcd70e-20260611T105951878713+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfc61bad5e15

## What looked useful

Across 12 medium-sweep overload cells, naive bounded admission averaged 7.63 on-time completions/s, 8.6% deadline success, 93.2% wasted CPU, and 0.559 s p95 latency. Pressure-deadline admission averaged 95.22 on-time completions/s, 89.1% deadline success, 2.0% wasted CPU, and 0.177 s p95 latency. Pressure-safety admission averaged 94.89 on-time completions/s, 88.7% deadline success, 0.5% wasted CPU, and 0.158 s p95 latency. Underload goodput was not uniformly improved, with worst medium-sweep losses of -0.27% and -1.76% for the two pressure policies.

## Boundaries and scale limits

Evidence is synthetic and local: no production traces, live RPC stack, OS scheduling effects, client retry feedback, heterogeneous service classes, or multi-host admission control were tested. The high-noise sensitivity was shorter than the primary medium sweep.

## Claim scope

In a deterministic discrete-event model of a 4-slot bounded CPU worker with a 32-job FIFO queue, bursty synthetic arrivals, lognormal service times, deadline SLOs, and noisy service estimates, queue-pressure/deadline-aware admission substantially improves on-time completion goodput and reduces late-work CPU waste under overload compared with naive accept-until-full admission.

## Why it stopped

Synthetic/local evidence is useful but insufficient for a paper-ready systems claim; the result should stop here as no-paper evidence and feed a direct live-worker validation.

## Recommended next action

Run a bounded live-worker or trace-replay follow-up that preserves the same metrics and tests whether estimator noise, OS/process overhead, and client retry behavior preserve the overload goodput benefit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live bounded CPU worker validation of pressure-aware admission
- Success threshold: Pressure-aware admission achieves at least 25% higher on-time goodput and at least 50% lower wasted CPU fraction than naive bounded admission in overload cells, while losing no more than 5% on-time goodput in underload cells.
- Stop condition: Stop if live-worker overhead, estimator noise, or retry feedback reduces overload on-time goodput improvement below 10% in repeated cells or causes underload goodput loss above 10%.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-aware-task-admission-on-a-bounded-cpu-worker-76cb6fdcd70e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

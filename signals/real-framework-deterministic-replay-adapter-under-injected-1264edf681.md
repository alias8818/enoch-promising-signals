# Real-framework deterministic replay adapter under injected dropout

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-framework-deterministic-replay-adapter-under-injected-1264edf681`
Run ID: `real-framework-deterministic-replay-adapter-under-injected-1264edf681-20260620T135713005236+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Framework-level deterministic replay for non-IID federated gradient validation: enoch://control-plane/projects/framework-level-deterministic-replay-for-non-iid-federated-6ff8b31f2a/runs/framework-level-deterministic-replay-for-non-iid-federated-6ff8b31f2a-20260620T131632459404+0000
- Parent run decision: Framework-integrated deterministic replay under partial participation and dropout: enoch://control-plane/projects/framework-integrated-deterministic-replay-under-partial-pa-5ca6301c29/runs/framework-integrated-deterministic-replay-under-partial-pa-5ca6301c29-20260620T133321992044+0000

## What looked useful

Across 50,000 comparisons per strategy, event_log_adapter achieved 1.0 exact state/answer/trace match with Wilson 95% state-match CI [0.999923, 1.0]. Seed-only replay under jitter had 0.0 exact state match, fresh RNG had 0.0, and dropout-only logging had 0.00264 exact state match. This supports the mechanism that labelled event logs, not seed control alone, are required for deterministic replay under injected dropout and perturbation.

## Boundaries and scale limits

Validated on one local CPU worker, one LangGraph workflow, synthetic tasks, 10,000 tasks x 5 seed blocks x 4 strategies. Not validated on real LLM/tool traces, asynchronous/concurrent graphs, process crash recovery, checkpoint-store persistence, or production workloads.

## Claim scope

A labelled event-log deterministic replay adapter produced exact state, answer, and trace replay for a synthetic but real LangGraph StateGraph workflow with injected observation dropout, conditional routing, stochastic repair, fixed seeds, and scheduler-like RNG jitter.

## Why it stopped

Not paper-ready despite strong scoped mechanism support: the validation used a synthetic workload and did not test production-like LLM/tool nondeterminism, crash persistence, or concurrent framework execution.

## Recommended next action

Stop this run as no-paper useful signal; next bounded evidence should validate the adapter on real or benchmark agent traces with LangGraph checkpoint crash/resume and asynchronous event ordering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LangGraph checkpoint crash/resume replay under real agent trace perturbations
- Success threshold: Across at least 1000 replay episodes, integrated event-log replay achieves >=0.99 exact state and trace match after crash/resume and async perturbation, and improves exact state match by >=0.50 absolute over seed-only and checkpoint-only baselines.
- Stop condition: Stop if event-log replay exact state match falls below 0.95 on two fixed-seed trace suites or if checkpoint integration cannot reproduce event order after three bounded implementation attempts.

## Evidence references

- Artifact root: `<local-path>/projects/real-framework-deterministic-replay-adapter-under-injected-1264edf681`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

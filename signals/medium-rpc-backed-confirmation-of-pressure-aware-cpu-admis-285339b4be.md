# Medium RPC-backed confirmation of pressure-aware CPU admission

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-rpc-backed-confirmation-of-pressure-aware-cpu-admis-285339b4be`
Run ID: `medium-rpc-backed-confirmation-of-pressure-aware-cpu-admis-285339b4be-20260611T124530373782+0000`

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

- Parent run decision: Queue-Pressure-Aware Task Admission on a Bounded CPU Worker: enoch://control-plane/projects/queue-pressure-aware-task-admission-on-a-bounded-cpu-worker-76cb6fdcd70e/runs/queue-pressure-aware-task-admission-on-a-bounded-cpu-worker-76cb6fdcd70e-20260611T105951878713+0000
- Parent run decision: Live bounded CPU worker validation of pressure-aware admission: enoch://control-plane/projects/live-bounded-cpu-worker-validation-of-pressure-aware-admis-c095d4dda6/runs/live-bounded-cpu-worker-validation-of-pressure-aware-admis-c095d4dda6-20260611T121428440053+0000

## What looked useful

Under explicit CPU PSI pressure, pressure-aware admission reduced accepted p95 latency from 121.0 ms to 73.4 ms and accepted SLO violations from 4.8% to 0.48%, comparable to a static cap but with slightly higher rejection and lower goodput. Under no external pressure, PSI stayed low while RPC queueing was severe, so PSI-only admission did not engage and performed worse than both accept-all and the static cap. The mechanism is useful but incomplete as a standalone RPC admission rule.

## Boundaries and scale limits

Single-machine Python ThreadingHTTPServer, loopback clients, synthetic CPU work, short 15 s conditions, no production RPC framework, no cgroups or CPU quotas, no networked clients, no realistic trace mix, and no datacenter-scale contention. The Python GIL and process scheduler likely affect the pressure dynamics.

## Claim scope

Local loopback HTTP RPC service on an 8-logical-CPU worker, fixed 25,000-iteration CPU-bound Python work units, 30 rps seeded Poisson arrivals, three fixed seeds, accept-all baseline, static concurrency-cap ablation, and Linux CPU PSI-triggered admission. Evidence supports PSI-triggered admission only when the measured CPU PSI signal is elevated.

## Why it stopped

Tier 2 medium evidence supports the CPU-PSI mechanism only in the explicit pressure scenario and falsifies PSI-only admission as a sufficient standalone rule under self-induced RPC queueing.

## Recommended next action

Stop this run as no-paper mixed evidence; if continuing, test a hybrid PSI plus queue/backlog admission controller against static cap on the same fixed-seed RPC harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid PSI and queue-backed RPC admission versus static caps
- Success threshold: Hybrid policy reduces accepted p95 by at least 75% versus accept-all in no-pressure self-overload and at least 35% under explicit CPU pressure, while keeping rejection rate at or below the static cap and accepted SLO violation at or below 2% in both scenarios.
- Stop condition: Stop if the hybrid policy either fails to beat static cap on rejection-adjusted latency/goodput in both scenarios or still misses no-pressure self-overload because its non-PSI signal does not engage reliably.

## Evidence references

- Artifact root: `<local-path>/projects/medium-rpc-backed-confirmation-of-pressure-aware-cpu-admis-285339b4be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Live bounded CPU worker validation of pressure-aware admission

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-bounded-cpu-worker-validation-of-pressure-aware-admis-c095d4dda6`
Run ID: `live-bounded-cpu-worker-validation-of-pressure-aware-admis-c095d4dda6-20260611T121428440053+0000`

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

- Parent run decision: Queue-Pressure-Aware Task Admission on a Bounded CPU Worker: enoch://control-plane/projects/queue-pressure-aware-task-admission-on-a-bounded-cpu-worker-76cb6fdcd70e/runs/queue-pressure-aware-task-admission-on-a-bounded-cpu-worker-76cb6fdcd70e-20260611T105951878713+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfc61bad5e15

## What looked useful

The Tier 1 direct test supports the mechanism: rejecting before deep queueing preserved worker saturation while converting most completed CPU work from deadline-missing to on-time. This is useful engineering evidence but not paper-ready.

## Boundaries and scale limits

Single CPU host, one Python ProcessPool worker implementation, synthetic Poisson/log-normal workload, one deadline setting, three paired seeds, no real HTTP/RPC ingress, no production trace, no multi-tenant or multi-node validation.

## Claim scope

On a single local 4-process bounded CPU worker with synthetic but live CPU-bound requests, pressure-aware online admission using backlog, EWMA service time, and CPU pressure/load signals reduced completed-request deadline misses by about 99.9% versus blind bounded-queue admission while increasing useful on-time completions by about 1127 requests per paired 24 s trace.

## Why it stopped

Tier 1 direct local validation threshold passed, but evidence is limited to one host and synthetic workload, so this run should close as no-paper useful signal rather than publication readiness.

## Recommended next action

Run a medium confirmation with real RPC ingress, bursty arrivals, multiple request deadlines/classes, and ablations for backlog-only, EWMA-only, load-only, and PSI-aware admission.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium RPC-backed confirmation of pressure-aware CPU admission
- Success threshold: Pressure-aware admission must reduce completed-request deadline miss fraction by >=50%, keep useful on-time completions >= blind baseline, and maintain >=80% CPU utilization proxy across all paired trace windows.
- Stop condition: Stop if pressure-aware admission fails the deadline-miss or useful-throughput threshold in two or more paired trace windows, or if the real ingress overhead removes the useful-completion advantage.

## Evidence references

- Artifact root: `<local-path>/projects/live-bounded-cpu-worker-validation-of-pressure-aware-admis-c095d4dda6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

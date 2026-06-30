# CPU Speculative Cascade Routing Under Queue Pressure

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `cpu-speculative-cascade-routing-under-queue-pressure-0eae9891258f`
Run ID: `cpu-speculative-cascade-routing-under-queue-pressure-0eae9891258f-20260620T070353442478+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ce09d176aa68

## What looked useful

Cheap-tier queue pressure alone was not a useful speculation signal. After guarding on predicted mid-tier benefit, speculation almost never fired, and the few speculative launches increased cost/work while p95 latency was worse at every tested arrival rate.

## Boundaries and scale limits

No production traces, real model inference, CPU kernel batching, preemptive cancellation, multi-host routing, or datacenter-scale serving were tested. Direct evidence is limited to the local deterministic simulator.

## Claim scope

Synthetic three-tier CPU FCFS queue simulation with Poisson arrivals, tier-dependent service times, tier-dependent success probabilities, five seeds, ten arrival rates, and a guarded pressure-speculative cascade policy.

## Why it stopped

Proxy/local simulation early falsification: the tested pressure-speculative cascade did not improve deadline hit rate or p95 latency over cheapest-first and added cost/work.

## Recommended next action

Stop this run as a scoped negative simulation result; only revisit with a direct serving trace where fallback-tier spare capacity and cancellation semantics can be measured.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/cpu-speculative-cascade-routing-under-queue-pressure-0eae9891258f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Local cascade router reduces p99 latency under queue pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-cascade-router-reduces-p99-latency-under-queue-pressure-81a549181ca8`
Run ID: `local-cascade-router-reduces-p99-latency-under-queue-pressure-81a549181ca8-20260629T133721998116+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/218ac87ce6e2

## What looked useful

Local cascade cut p99 latency by about 99.3% versus sticky/random baselines and by 20.7% to 37.0% versus power-of-two at loads 0.86 and 0.94, but was 64.6% to 79.3% worse than the full-information shortest-queue reference.

## Boundaries and scale limits

Synthetic-only evidence; no production traces, real router overhead, stale telemetry, network locality costs, multi-core contention, or fleet topology constraints were measured. Global shortest-queue routing remained substantially lower p99 than local cascade.

## Claim scope

In a bounded synthetic bursty M/M/1-style simulation with 32 heterogeneous queues, 4096 request keys, five seeds, and load points 0.72, 0.86, and 0.94, a deterministic four-candidate local cascade router reduced p99 latency versus sticky-primary and random routing, and beat power-of-two routing at higher simulated load.

## Why it stopped

No-paper useful signal: the current evidence is a bounded synthetic mechanism test, not a production-grade validation of the routing claim.

## Recommended next action

Run the same policy matrix against a trace-driven or live local load-generator setup with measured router overhead and queue-telemetry staleness; stop here for paper purposes until that direct evidence exists.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-driven local cascade routing under measured telemetry staleness
- Success threshold: Local cascade reduces p99 latency by at least 15% versus power-of-two at high load while adding less than 5% mean router overhead, and the result is consistent across at least three seeds or replay windows.
- Stop condition: Stop if local cascade fails to beat power-of-two p99 by 10% in two high-load trace windows or router overhead exceeds the measured p99 benefit.

## Evidence references

- Artifact root: `<local-path>/projects/local-cascade-router-reduces-p99-latency-under-queue-pressure-81a549181ca8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

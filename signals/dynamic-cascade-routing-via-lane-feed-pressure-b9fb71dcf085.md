# Dynamic Cascade Routing via Lane Feed Pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-cascade-routing-via-lane-feed-pressure-b9fb71dcf085`
Run ID: `dynamic-cascade-routing-via-lane-feed-pressure-b9fb71dcf085-20260523T155135486752+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/72c532193db4

## What looked useful

Across 64 seeds and three synthetic cascade scenarios, lane_feed_pressure tied shortest_queue_pending exactly on primary metrics, while feed_pressure_ema_only worsened p95 latency by 2-3 ticks and increased mean queue size by 8.8-11.9 jobs versus the pending-aware baseline. The useful mechanism appears to be pending-assignment accounting, not the feed-pressure EMA term.

## Boundaries and scale limits

No real model training, MoE dispatch, GPU kernel scheduling, production serving traces, delayed-observability routing, or large-scale distributed validation was run. Results are local synthetic evidence only.

## Claim scope

Synthetic discrete-time 3-stage, 4-lane queueing cascades with bursty/skewed arrivals and finite lane queues. Dynamic pending-aware routing reduces latency versus weak baselines, but adding lane-feed-pressure EMA provides no measurable benefit over shortest_queue_pending in this setting.

## Why it stopped

No-paper useful signal: bounded synthetic evidence does not support lane feed pressure as a distinct improvement over a strong pending-aware shortest-queue control.

## Recommended next action

Stop this paper path; if continuing, run a bounded delayed-observability cascade test where pending assignments are hidden or stale to see whether feed-pressure prediction has value when the winning baseline cannot observe current pending load.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Delayed-Observability Lane Feed Pressure
- Success threshold: At least 10% lower p95 latency than the best stale-load baseline in two of three scenarios, with no higher drop rate and no more than 5% worse mean queue size.
- Stop condition: Stop if feed-pressure EMA fails to beat the best stale-load baseline by 10% p95 latency in at least two scenarios or if gains disappear after matching drop rate and queue capacity.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-cascade-routing-via-lane-feed-pressure-b9fb71dcf085`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

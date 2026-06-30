# Priority-Lane Admission Control Under Saturation on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `priority-lane-admission-control-under-saturation-on-gb10-7f2085fd62c5`
Run ID: `priority-lane-admission-control-under-saturation-on-gb10-7f2085fd62c5-20260621T033402531774+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/60b7c27a2283

## What looked useful

Under measured GB10 saturation, FIFO high-priority p95 latency was 5.50 s in the main run and 2.94 s in replication; priority-lane p95 was 3.09 ms and 3.24 ms at roughly the same completed throughput. Admission control preserved high-priority latency and bounded completed low-priority latency near 214 ms by dropping low-priority arrivals.

## Boundaries and scale limits

Synthetic homogeneous matmul jobs only; one process; no real LLM serving stack, CUDA stream-priority preemption, multi-tenant isolation, networking, batching, KV-cache pressure, or datacenter-scale validation.

## Claim scope

On a single NVIDIA GB10 running a deterministic PyTorch CUDA matrix-multiply saturation proxy, application-level priority-lane dispatch reduced high-priority p95 latency from multi-second FIFO backlog to about 3 ms while preserving similar completed throughput; adding low-priority admission caps bounded completed low-priority latency by dropping excess low-priority work.

## Why it stopped

The current evidence is a direct GB10 CUDA saturation proxy with replication, not a full production-serving validation, so it supports the mechanism but is insufficient for a paper.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement the same policies in a real GB10 inference server and measure TTFT/TPOT under mixed-priority request traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Priority-lane admission control in a real GB10 inference server
- Success threshold: High-priority TTFT p95 improves by at least 10x over FIFO in every trace, accepted-token throughput remains at least 95% of FIFO for non-dropping priority-lane mode, and any admission-control drops are fully accounted.
- Stop condition: Stop if priority mode fails to improve high-priority TTFT p95 by 2x on the first two saturated traces, reduces accepted-token throughput below 90% without an SLO benefit, or GB10 memory pressure prevents a valid serving run.

## Evidence references

- Artifact root: `<local-path>/projects/priority-lane-admission-control-under-saturation-on-gb10-7f2085fd62c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

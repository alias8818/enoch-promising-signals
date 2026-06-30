# Agent Reliability Under Cascade Routing Pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-reliability-under-cascade-routing-pressure-25a259729a87`
Run ID: `agent-reliability-under-cascade-routing-pressure-25a259729a87-20260601T013320843838+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/02a91e825c70

## What looked useful

Cascade pressure behaved as a threshold effect rather than a monotonic failure mode: naive cascade success dropped from 88.69% at arrival rate 4 to 18.01% at arrival rate 22, while pressure-aware routing beat naive only at rate 22 by 13.52 success percentage points on average.

## Boundaries and scale limits

Synthetic proxy only; no real LLM/agent traffic, real answer correctness, tool-use traces, production latency curves, or datacenter-scale serving system was tested. Full sweep was 384 local CPU trials and 2,304,000 synthetic tasks.

## Claim scope

In a deterministic synthetic queueing simulator with probabilistic task success, naive cheap-to-strong cascade routing is reliable at low and medium load but shows a severe timeout cliff at the highest tested arrival rate; pressure-aware routing only improves success in that extreme overload regime.

## Why it stopped

Closed as no-paper useful signal because the evidence is reproducible but proxy-only and mixed; it supports an overload-threshold mechanism, not a broad claim that cascade routing generally reduces agent reliability under pressure.

## Recommended next action

Run a bounded deepen follow-up using trace-derived or measured model latency/success curves plus bursty arrivals to test whether the observed overload crossover persists outside the synthetic simulator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Calibrated Cascade Routing Overload Crossover
- Success threshold: Show a reproducible crossover where pressure-aware or adaptive routing improves success by at least 5 percentage points over naive cascade in overload while losing no more than 3 percentage points at moderate load.
- Stop condition: Stop if trace-calibrated runs show no overload crossover or if pressure-aware/adaptive routing is dominated by naive cascade across all arrival regimes.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-under-cascade-routing-pressure-25a259729a87`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

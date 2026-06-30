# Trace replay validation of queue-depth-gated lane work generation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-replay-validation-of-queue-depth-gated-lane-work-gen-2b4c194da5`
Run ID: `trace-replay-validation-of-queue-depth-gated-lane-work-gen-2b4c194da5-20260525T080210970855+0000`

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

- Parent run decision: Queue-depth-gated work generation for lane feed pressure stability: enoch://control-plane/projects/queue-depth-gated-work-generation-for-lane-feed-pressure-stability-0b72dde5f7ae/runs/queue-depth-gated-work-generation-for-lane-feed-pressure-stability-0b72dde5f7ae-20260525T074150938866+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/48e5caa5378f

## What looked useful

Queue-depth gating showed a real waste-reduction mechanism, with median waste reduction of 96.0% overall and 96.7% in overload, while completions stayed at parity. The same fixed gate raised p95 latency substantially: median 1.33x overall and 4.03x in overload, causing only 26/120 trials to pass the combined threshold.

## Boundaries and scale limits

Synthetic simulator only; no real production traces, no GPU scheduler integration, no real serving stack, and only fixed depth-4 gating versus fixed depth-24 deep prefill.

## Claim scope

In a deterministic small trace-replay simulator with 8 lanes, 1200 ticks, three synthetic arrival/service scenarios, and 40 seeds per scenario, a fixed low queue-depth gate preserved completions and reduced stale generated work but failed the p95 latency preservation threshold.

## Why it stopped

Direct Tier 1 replay failed the latency-preservation threshold: p95 latency ratio median was 1.33x overall and 4.03x under overload, above the allowed 1.10x, even though stale-work waste fell sharply.

## Recommended next action

Stop this fixed-gate claim as no-paper evidence; run a bounded adaptive-gate follow-up that increases lane depth when backlog age or p95 latency risk rises.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive queue-depth gating with latency guard under trace replay
- Success threshold: Across the same three scenarios with at least 40 seeds each, adaptive gating must complete at least 95% of baseline work, keep p95 latency ratio <= 1.10 in at least 80% of trials, and preserve median stale-work waste reduction >= 70% of the fixed-gate reduction.
- Stop condition: Stop if adaptive gating cannot achieve p95 latency ratio <= 1.10 in at least 50% of bursty_tight_ttl and overload trials, because the latency tradeoff would remain unresolved.

## Evidence references

- Artifact root: `<local-path>/projects/trace-replay-validation-of-queue-depth-gated-lane-work-gen-2b4c194da5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

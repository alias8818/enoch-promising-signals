# VRAM-Headroom Cascade Abort: Reroute When KV Pressure >85%

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `vram-headroom-cascade-abort-reroute-when-kv-pressure-85-c183de79cafb`
Run ID: `vram-headroom-cascade-abort-reroute-when-kv-pressure-85-c183de79cafb-20260620T040422222769+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c1d9a11bb32e

## What looked useful

Stress workload: no-reroute abort rate 1.57% versus 85% threshold abort rate 0.00%, success 98.43% versus 99.99%. Overload workload: no-reroute abort rate 4.25% versus 85% threshold abort rate 0.00%, success 95.75% versus 99.99%. Overflow-only routing still had aborts and worse tail latency. Thresholds from 80% to 90% performed similarly, so 85% is plausible but not uniquely supported.

## Boundaries and scale limits

Synthetic scheduler-level evidence only; no real serving stack, model weights, allocator telemetry, network transfer, heterogeneous worker fleet, or production request trace was tested. The result supports an 80-90% threshold band rather than a uniquely optimal 85% constant.

## Claim scope

In a deterministic two-worker KV-cache pressure simulator with Llama-class bf16 KV bytes per token, 24 GiB KV budget per worker, heavy-tailed request traces, and pressure-dependent decode slowdown, preemptive reroute when primary KV pressure would exceed 85% eliminated modeled cascade aborts under stress and overload workloads.

## Why it stopped

Bounded simulator supports the mechanism but does not provide production-serving or publication-grade evidence; 85% is not uniquely optimal in the threshold sweep.

## Recommended next action

Stop as no-paper useful signal; next direct evidence should implement the threshold router in a real serving stack and replay comparable pressure traces with allocator and latency telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-serving KV pressure reroute threshold sweep
- Success threshold: Across at least two nontrivial pressure traces, a threshold in the 80-90% band reduces abort rate by at least 90% versus no-reroute and improves or does not degrade p95 latency by more than 5% while keeping reject rate below 0.5%.
- Stop condition: Stop if real serving telemetry shows threshold reroute mostly converts aborts into rejects, increases p95 latency by more than 10%, or cannot reduce aborts by at least 50% versus overflow-only routing.

## Evidence references

- Artifact root: `<local-path>/projects/vram-headroom-cascade-abort-reroute-when-kv-pressure-85-c183de79cafb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

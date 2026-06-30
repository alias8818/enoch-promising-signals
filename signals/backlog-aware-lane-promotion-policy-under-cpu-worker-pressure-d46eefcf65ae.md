# Backlog-Aware Lane Promotion Policy Under CPU Worker Pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `backlog-aware-lane-promotion-policy-under-cpu-worker-pressure-d46eefcf65ae`
Run ID: `backlog-aware-lane-promotion-policy-under-cpu-worker-pressure-d46eefcf65ae-20260613T121020013599+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8f60b319249d

## What looked useful

Backlog-aware promotion reduced backlog p95 by 1.22% to 1.62% and backlog starvation by 1.35 to 2.92 percentage points versus no promotion, with urgent SLA miss deltas of 0.003 to 0.204 percentage points. Static age-only promotion improved backlog p95 much more but caused 53.88% to 68.40% urgent SLA misses, showing that promotion requires urgent-depth/backlog guardrails.

## Boundaries and scale limits

Synthetic model only; no real worker traces, OS scheduler contention, container pressure, or control-plane dispatch latency. Full validation requires trace replay or an instrumented worker harness under observed CPU load.

## Claim scope

In a deterministic synthetic CPU-worker queue simulator with 3 pressure scenarios and 20 seeds per policy/scenario, a backlog-aware guarded promotion rule modestly reduced backlog starvation versus no promotion while keeping urgent SLA misses near zero.

## Why it stopped

No-paper useful signal from bounded synthetic evidence; result is not publication-grade because the mechanism was not validated on real worker traces or an instrumented production-like harness.

## Recommended next action

Run a bounded trace-replay follow-up using real or instrumented worker arrival/service traces to test whether the guarded promotion signal survives non-synthetic CPU pressure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace Replay for Guarded Backlog-Aware Lane Promotion
- Success threshold: Backlog-aware promotion improves backlog starvation by >=2 percentage points versus no promotion with urgent SLA miss increase <1 percentage point across at least two pressure scenarios or trace slices.
- Stop condition: Stop if guarded promotion improves backlog starvation by <1 percentage point or urgent SLA misses increase by >=1 percentage point on the primary trace replay.

## Evidence references

- Artifact root: `<local-path>/projects/backlog-aware-lane-promotion-policy-under-cpu-worker-pressure-d46eefcf65ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

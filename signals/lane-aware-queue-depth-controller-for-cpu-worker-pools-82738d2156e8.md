# Lane-aware queue depth controller for CPU worker pools

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lane-aware-queue-depth-controller-for-cpu-worker-pools-82738d2156e8`
Run ID: `lane-aware-queue-depth-controller-for-cpu-worker-pools-82738d2156e8-20260613T162051927855+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9bb53858795a

## What looked useful

Lane separation prevents global FIFO head-of-line blocking, but the adaptive depth rule tested here over-backpressures. Normal load useful completion: static_lane 99.67%, adaptive_lane 96.37%, global_fifo 83.20%. At 1.5x load: static_lane 85.40%, adaptive_lane 67.13%, global_fifo 16.44%.

## Boundaries and scale limits

Synthetic simulator only; no production traces, no real executor/runtime overheads, no caller retry/backoff feedback, no multi-host effects, and no datacenter-scale validation.

## Claim scope

Local deterministic simulator of an 8-worker CPU worker pool with interactive, standard, and bulk lanes under bursty synthetic arrivals. The tested adaptive per-lane queue-depth controller improves admitted latency relative to global FIFO but is worse than a simple static lane baseline on useful completion rate because it drops too much work.

## Why it stopped

Proxy/local simulation produced a useful early falsification of the adaptive depth rule versus a static lane baseline; this is not full production validation.

## Recommended next action

Stop this controller variant as no-paper evidence; if continuing, redesign admission control to optimize useful completion with anti-windup and validate against real CPU worker traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-driven lane admission controller with retry-aware useful-completion objective
- Success threshold: Beat static_lane by at least 3% relative overall useful completion at equal or better interactive p95 latency, without increasing interactive drop rate above 1% under normal load or 5% under overload.
- Stop condition: Stop if the redesigned controller still loses to static_lane on useful completion or exceeds the drop-rate thresholds in two independent trace families.

## Evidence references

- Artifact root: `<local-path>/projects/lane-aware-queue-depth-controller-for-cpu-worker-pools-82738d2156e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

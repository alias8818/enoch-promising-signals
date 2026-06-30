# QueuePressureCascade: SLO-Aware Router Under Lane Feed Pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queuepressurecascade-slo-aware-router-under-lane-feed-pressure-8b87346222e4`
Run ID: `queuepressurecascade-slo-aware-router-under-lane-feed-pressure-8b87346222e4-20260628T180717563027+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f09155c847f9

## What looked useful

The SLO pressure cascade reduced p95 latency versus preferred-static routing, but it increased deadline miss rate versus preferred-static in all scenarios; best threshold-swept cascade miss rates remained 10 to 40 percentage points worse than static.

## Boundaries and scale limits

No real serving traces, model inference kernels, network effects, autoscaling, retries, or production scheduler behavior. Results should be read as mechanism evidence only, not production SLO validation.

## Claim scope

Synthetic discrete-event proxy with three lanes, three request classes, bursty lane feed pressure, 30 seeds per scenario, and comparison against preferred-static, round-robin, and least-queue-delay routing.

## Why it stopped

Proxy result is mixed and no-paper: the tested cascade mechanism improves latency but fails the primary SLO-miss objective against the strongest simple baseline.

## Recommended next action

Run a bounded follow-up that adds class protection or lane reservation to the cascade policy and require it to beat preferred-static miss rate while preserving at least half of the observed p95 latency reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Class-Protected SLO Cascade Router Under Lane Feed Pressure
- Success threshold: Across all three scenarios, dynamic protected cascade has lower mean miss rate than preferred-static and at least 50% of the naive cascade p95 latency improvement versus preferred-static.
- Stop condition: Stop if protected cascade cannot beat preferred-static miss rate in at least two of three scenarios after a 30-seed sweep and one sensitivity sweep.

## Evidence references

- Artifact root: `<local-path>/projects/queuepressurecascade-slo-aware-router-under-lane-feed-pressure-8b87346222e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

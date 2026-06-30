# CPU cascade router for lane feed admission

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-cascade-router-for-lane-feed-admission-27fcbc67136a`
Run ID: `cpu-cascade-router-for-lane-feed-admission-27fcbc67136a-20260628T032535838583+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/426e03455cca

## What looked useful

The cascade reduced expensive-stage scoring to a mean 69.6% of held-out candidates and improved throughput by a mean 1.41x versus full expensive scoring, but lost about 16.0 percentage points of utility capture relative to the full expensive baseline.

## Boundaries and scale limits

No production traces, no real labels, no online serving latency, no per-lane fairness or starvation constraints, no multi-day drift, and no datacenter-scale replay.

## Claim scope

Synthetic local-CPU lane-feed admission simulation with 120000 events per run, 5 seeds, 1024-hidden-unit expensive scorer, and fixed cheap-score cascade thresholds.

## Why it stopped

Proxy synthetic result only: useful mechanism signal, but the measured utility loss is too large and the evidence is not direct production validation.

## Recommended next action

Run a bounded real-trace replay with per-lane budget-aware thresholds and stop unless utility loss is under 5 percentage points at at least 1.3x throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace budget-aware cascade replay for lane-feed admission
- Success threshold: At least 1.3x throughput versus full expensive scoring, expensive-stage fraction at or below 70%, utility capture no more than 5 percentage points below full expensive, and no severe per-lane starvation regression.
- Stop condition: Stop if held-out utility loss remains above 10 percentage points at 70% expensive-stage fraction or if per-lane starvation materially worsens versus full expensive scoring.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-cascade-router-for-lane-feed-admission-27fcbc67136a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

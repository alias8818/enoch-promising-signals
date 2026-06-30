# Bounded CPU Worker Lane: Queue-Aware Contribution Protocol

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-cpu-worker-lane-queue-aware-contribution-protocol-50901878ec28`
Run ID: `bounded-cpu-worker-lane-queue-aware-contribution-protocol-50901878ec28-20260613T135218100084+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f83ebaa4f43d

## What looked useful

Queue-aware bounded scheduling achieved 2409.570 mean useful value versus 807.967 for the best baseline, a 198.226% lift, while using 29.787% less work and eliminating stale/duplicate completions in the synthetic replay.

## Boundaries and scale limits

Only three synthetic scenario families, 30 seeds per strategy, one worker lane, generated task qualities, no live Enoch controller traces, no multi-worker contention, and no production overhead measurement.

## Claim scope

In a deterministic synthetic replay of one bounded non-preemptive CPU worker lane, stale filtering, duplicate/conflict avoidance, value-density scoring, and queue bounding improved useful contribution value versus FIFO and priority-only baselines.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy only, despite meeting the predefined local replay threshold.

## Recommended next action

Run a bounded deepen follow-up with controller-faithful trace replay and ablations for stale filtering, duplicate avoidance, value-density scoring, and queue bounds before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Controller-faithful queue-aware worker-lane replay with ablations
- Success threshold: Queue-aware bounded policy improves useful value by at least 15% versus the best baseline, uses no more total work, has stale+duplicate completions at least 50% lower than the best baseline, and shows no task class with more than 2x baseline starvation.
- Stop condition: Stop as negative if the ablated or full protocol fails the useful-value threshold in any two scenario families or if queue bounds introduce unacceptable starvation.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-cpu-worker-lane-queue-aware-contribution-protocol-50901878ec28`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Promotable Work Detection for GPU Worker Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `promotable-work-detection-for-gpu-worker-reliability-cb4ab0625261`
Run ID: `promotable-work-detection-for-gpu-worker-reliability-cb4ab0625261-20260612T052635487375+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/998410ae075f

## What looked useful

Across 86,400 synthetic jobs, the composite gate retained 88.1% recall, reduced promoted failure rate by 52.5%, reduced wasted projected GPU-hours by 61.4%, and improved utility versus promoting every smoke-passing job.

## Boundaries and scale limits

No production worker traces, real long GPU jobs, cross-host deployment, or online scheduler integration were tested; labels and job distributions are simulated.

## Claim scope

In a deterministic synthetic GPU-worker promotion model with smoke-window telemetry, a composite promotability gate reduced promoted failure rate and wasted projected GPU-hours versus promote-all and single-signal controls while retaining more than 80% recall.

## Why it stopped

Closed as a no-paper useful signal because the positive result is synthetic/proxy rather than direct production evidence.

## Recommended next action

Run a bounded deepen follow-up that replays the composite gate and controls against real historical GPU-worker telemetry with known final outcomes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay promotable-work gates on real GPU worker traces
- Success threshold: At least 80% recall of useful completions plus at least 30% reduction in promoted failures and wasted GPU-hours versus promote-all on held-out real traces.
- Stop condition: Stop if real trace replay shows less than 15% waste reduction at 80% recall or if telemetry fields needed by the gate are absent for most jobs.

## Evidence references

- Artifact root: `<local-path>/projects/promotable-work-detection-for-gpu-worker-reliability-cb4ab0625261`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

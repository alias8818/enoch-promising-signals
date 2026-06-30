# Pareto-Calibrated Escalation Threshold for 2-Tier Home Cascade

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pareto-calibrated-escalation-threshold-for-2-tier-home-cascade-7246a4bc6628`
Run ID: `pareto-calibrated-escalation-threshold-for-2-tier-home-cascade-7246a4bc6628-20260609T105405241748+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/153d62b5b21c

## What looked useful

Across 256 synthetic homes, 5,000 requests per home, 20 seeds, and 101 thresholds, the population-tuned global threshold had 0.00703 mean utility regret versus per-home Pareto-calibrated selection; common fixed thresholds at 0.50, 0.70, and 0.90 had mean regrets of 0.06536, 0.02371, and 0.00955 respectively.

## Boundaries and scale limits

Synthetic traces only: no real model confidence traces, user labels, home network latency, energy measurements, privacy costs, or deployed home hardware were tested.

## Claim scope

In a reproducible synthetic two-tier home cascade with heterogeneous homes, selecting escalation thresholds from each home's accuracy/cost/p95-latency Pareto frontier eliminates per-home threshold regret by construction and exposes consistent regret from a single global threshold.

## Why it stopped

Proxy simulation supports the mechanism but does not provide direct deployment evidence or paper-grade validation.

## Recommended next action

Stop this run as a no-paper proxy useful signal; next, test the same Pareto-calibrated threshold selection on real local/remote model trace data with correctness labels and observed latency/cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Based Pareto Threshold Calibration for Local-to-Remote Assistant Cascades
- Success threshold: At least 20% lower mean utility regret than the best population-tuned global threshold on held-out traces, with no statistically meaningful accuracy decrease.
- Stop condition: Stop if trace-based Pareto calibration improves mean utility regret by less than 5% or requires utility weights that cannot be justified from measurable deployment constraints.

## Evidence references

- Artifact root: `<local-path>/projects/pareto-calibrated-escalation-threshold-for-2-tier-home-cascade-7246a4bc6628`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

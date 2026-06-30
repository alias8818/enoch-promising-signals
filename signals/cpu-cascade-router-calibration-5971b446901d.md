# CPU Cascade Router Calibration

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-cascade-router-calibration-5971b446901d`
Run ID: `cpu-cascade-router-calibration-5971b446901d-20260614T052629816931+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a505c71cd74a

## What looked useful

The calibrated fallback router reached 91.1% holdout accuracy versus 92.5% for always-on layered memory and reduced modeled latency by 27.9%, but no grid setting met the 1.5pp calibration tolerance and the latency reduction missed the 30% bar.

## Boundaries and scale limits

720 synthetic tasks, 360 calibration and 360 holdout, modeled latency and probabilistic correctness only; no real replay corpus, no LLM answer scoring, and no actual retrieval implementation timing.

## Claim scope

Synthetic CPU-only repeated-agent memory routing proxy: a simple threshold cascade router over generated task features did not meet the combined calibration and latency success threshold.

## Why it stopped

Proxy early falsification of the simple threshold router under the predefined 1.5pp accuracy tolerance and 30% latency-reduction success threshold, not a full validation or rejection of cascade routing in general.

## Recommended next action

Stop this run as a proxy negative; next bounded test should use real replay labels and compare a learned router against the same always-on strategy baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned CPU cascade router on labeled replay tasks
- Success threshold: On real or semi-real replay holdout data, learned router accuracy within 1.5 percentage points of always-on layered memory and measured mean CPU latency at least 30% lower.
- Stop condition: Stop if the learned router cannot beat the simple threshold router frontier or if measured latency savings above 30% require more than a 1.5 percentage point accuracy loss.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-cascade-router-calibration-5971b446901d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

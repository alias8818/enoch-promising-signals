# Replay promotable-work gates on real GPU worker traces

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `replay-promotable-work-gates-on-real-gpu-worker-traces-b0803734ee`
Run ID: `replay-promotable-work-gates-on-real-gpu-worker-traces-b0803734ee-20260612T060332926754+0000`

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

- Parent run decision: Promotable Work Detection for GPU Worker Reliability: enoch://control-plane/projects/promotable-work-detection-for-gpu-worker-reliability-cb4ab0625261/runs/promotable-work-detection-for-gpu-worker-reliability-cb4ab0625261-20260612T052635487375+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/998410ae075f

## What looked useful

No replayed gate met the selectivity threshold of promoting at most 80% of traces while retaining at least 90% recall. The recorded follow-up gate promoted 95.19% of traces; artifact gates promoted 82.88-92.92%; stricter decision gates became selective only by losing most recall.

## Boundaries and scale limits

Local historical trace corpus only; labels are controller-consumed decision fields rather than independent human-review or downstream follow-up-success labels. No private queue state, paper-writing outcomes, or future project-success labels were tested.

## Claim scope

Tier 1 replay over 2161 local completed GB10/GPU-worker Enoch traces using serialized project metadata, decisions, run notes, logs, and result-file footprints. Simple recorded, decision-derived, and artifact-derived promotable-work gates were evaluated for selectivity and recall.

## Why it stopped

Tier 1 direct trace replay falsified the simple promotable-work gate threshold on real local GPU-worker traces: broad gates were near-pass-throughs and selective gates lost recall.

## Recommended next action

Stop this run as no-paper useful evidence; only continue with a bounded deepen test if independent downstream success or reviewer promotion labels can be attached to the same GPU-worker traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay promotable-work gates with independent downstream success labels
- Success threshold: On a held-out split with independent labels, promote <=50% of traces with >=80% recall and >=2x precision lift over the base success rate.
- Stop condition: Stop if independent labels are unavailable, if the positive label base rate remains above 80%, or if the best held-out gate cannot beat the base-rate baseline by at least 2x precision lift.

## Evidence references

- Artifact root: `<local-path>/projects/replay-promotable-work-gates-on-real-gpu-worker-traces-b0803734ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

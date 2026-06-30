# DFlash checkpoint trace replay with measured branch latency

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dflash-checkpoint-trace-replay-with-measured-branch-latenc-0947164db6`
Run ID: `dflash-checkpoint-trace-replay-with-measured-branch-latenc-0947164db6-20260520T002107041353+0000`

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

- Parent run decision: Spec Trace Oracle v0 for DFlash Branch Selection: enoch://control-plane/projects/spec-trace-oracle-v0-dflash-branch-selection/runs/spec-trace-oracle-v0-dflash-branch-selection-20260519T235017287435+0000
- Parent run decision: Real DFlash Trace Replay for Spec Trace Oracle Branch Selection: enoch://control-plane/projects/real-dflash-trace-replay-for-spec-trace-oracle-branch-sele-6f670f66bf/runs/real-dflash-trace-replay-for-spec-trace-oracle-branch-sele-6f670f66bf-20260519T235546563709+0000

## What looked useful

Across five fixed seeds, DFlash averaged 0.3406 ms mean replay latency and 0.4808 ms p95 latency, compared with 3.9409/4.2290 ms for full replay and 1.7355/2.0210 ms for trunk-only periodic checkpoints. It reduced mean replay operations by 94.4% versus periodic baseline, but used 21.5 MiB checkpoint memory versus 0.28 MiB for periodic trunk checkpoints.

## Boundaries and scale limits

Synthetic traces only; no production DFlash traces, disk-backed checkpoint serialization costs, concurrent replay, storage hierarchy behavior, GPU/model-serving interaction, or large-scale deployment evidence. DFlash used materially more checkpoint memory than the baselines.

## Claim scope

On deterministic synthetic branch traces with mixed interior and leaf replay targets, branch-aware DFlash checkpoint placement reduced measured single-process branch-target reconstruction latency versus full replay, trunk-only periodic checkpointing, and two checkpoint-placement ablations while preserving checksum correctness.

## Why it stopped

Medium fixed-seed synthetic evidence supports the checkpoint-placement mechanism, but publication readiness requires real traces and measured checkpoint load/store costs.

## Recommended next action

Stop this run as a no-paper useful signal; the next concrete test is to replay real disk-backed checkpoint traces with the same baselines, checksums, and latency/storage metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: DFlash real-trace disk-backed checkpoint replay latency
- Success threshold: DFlash achieves at least 2x lower p95 branch-target replay latency than trunk-only periodic checkpointing on real disk-backed traces while preserving checksum correctness and using no more than 4x checkpoint storage versus the strongest practical baseline.
- Stop condition: Stop if DFlash fails checksum correctness, fails to beat trunk-only periodic p95 latency by 2x, or requires more than 4x checkpoint storage after reasonable checkpoint interval tuning.

## Evidence references

- Artifact root: `<local-path>/projects/dflash-checkpoint-trace-replay-with-measured-branch-latenc-0947164db6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

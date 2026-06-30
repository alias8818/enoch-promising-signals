# Adaptive micro-batch sizing in a small real training loop

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `adaptive-micro-batch-sizing-in-a-small-real-training-loop-a2f995ffd6`
Run ID: `adaptive-micro-batch-sizing-in-a-small-real-training-loop-a2f995ffd6-20260602T213534698333+0000`

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

- Parent run decision: Adaptive Micro-batch Sizing Under Memory Pressure: enoch://control-plane/projects/adaptive-micro-batch-sizing-under-memory-pressure-cc63b80a16e1/runs/adaptive-micro-batch-sizing-under-memory-pressure-cc63b80a16e1-20260602T172038157511+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f49c5798ed28

## What looked useful

Two controlled online adaptive policies preserved accuracy but failed throughput criteria. The robust controller reached 0.938x conservative fixed micro-batch 16 throughput and 0.709x best fixed micro-batch 32 throughput, with no accuracy loss. Timing noise caused selection of large micro-batch 256 even when fixed 32 was best.

## Boundaries and scale limits

Small dataset, small MLP, CPU/NumPy runtime, estimator-only memory budget, five seeds, no real GPU OOM or accelerator memory-pressure telemetry; results should not be generalized to transformer-scale or GPU training without direct validation.

## Claim scope

In a small CPU NumPy MLP training loop on UCI optdigits with fixed effective batch size 256, online adaptive micro-batch sizing policies tested here did not meet throughput thresholds versus fixed micro-batch baselines, although they preserved validation accuracy.

## Why it stopped

Controlled small direct test failed both predeclared throughput thresholds; this is no-paper evidence, not full-scale validation.

## Recommended next action

Stop this branch as a negative Tier 1 useful signal; only revisit with a bounded direct test that uses randomized replicated calibration and real memory-pressure telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replicated calibrated adaptive micro-batch sizing under real memory telemetry
- Success threshold: Adaptive throughput >=1.10x conservative fixed micro-batch, >=0.90x best fixed feasible micro-batch, and validation accuracy no more than 1 percentage point below best fixed.
- Stop condition: Stop as negative if adaptive fails either throughput threshold or selects a consistently worse micro-batch despite replicated calibration.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-micro-batch-sizing-in-a-small-real-training-loop-a2f995ffd6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

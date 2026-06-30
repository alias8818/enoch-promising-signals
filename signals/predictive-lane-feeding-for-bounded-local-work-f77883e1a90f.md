# Predictive Lane Feeding for Bounded Local Work

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `predictive-lane-feeding-for-bounded-local-work-f77883e1a90f`
Run ID: `predictive-lane-feeding-for-bounded-local-work-f77883e1a90f-20260523T161154608731+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/72c532193db4

## What looked useful

Prediction consistently improved makespan versus naive prefill FIFO by a mean 7.27% across scenario means, but it did not generally beat reactive FIFO feeding: mean improvement versus reactive was -2.25%, with only 20 of 54 scenarios positive and gains mainly when feed latency was high and prediction noise was low.

## Boundaries and scale limits

No real GPU kernel, accelerator lane, online predictor, dynamic arrival, memory hierarchy, contention, or production worker implementation was tested. The result is a local scheduling proxy and cannot support a broad systems or model-training paper claim.

## Claim scope

Synthetic bounded local work scheduling with ready-at-time-zero tasks, 32 lanes, 4096 tasks per trial, 54 scenario cells, and 200 trials per cell. Predictive longest-predicted-time lane assignment was compared against reactive FIFO feeding, naive prefill FIFO, and oracle longest-processing-time scheduling.

## Why it stopped

Moderate synthetic proxy evidence is mixed: prediction helps over naive prefill but often loses to a reactive baseline, so the practical hypothesis is not validated and the result is not paper-ready.

## Recommended next action

Stop this run as no-paper useful evidence; any next direct test should implement predictive feeding in a real worker or GPU-lane benchmark and compare against reactive work stealing plus naive prefill under measured feeder latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Worker-Lane Predictive Feeding Benchmark
- Success threshold: Predictive feeding must beat both reactive and naive prefill by at least 5% on makespan or throughput in at least two non-adversarial regimes without regressing p95 completion time by more than 1%.
- Stop condition: Stop if measured handoff latency is too small for reactive feeding gaps to matter, if online prediction error exceeds the synthetic noise-0.80 regime, or if predictive feeding fails to beat both baselines by 5% in the first two direct regimes.

## Evidence references

- Artifact root: `<local-path>/projects/predictive-lane-feeding-for-bounded-local-work-f77883e1a90f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

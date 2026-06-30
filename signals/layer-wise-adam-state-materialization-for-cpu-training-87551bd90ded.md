# Layer-wise Adam state materialization for CPU training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-wise-adam-state-materialization-for-cpu-training-87551bd90ded`
Run ID: `layer-wise-adam-state-materialization-for-cpu-training-87551bd90ded-20260525T085301066917+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/de2d5cca39c6

## What looked useful

Layer-wise Adam state materialization only reduced process RSS when each layer's state was flushed and advised out of residency. Across 128 MB and 256 MB logical Adam-state tests, explicit drop reduced peak RSS to 61.5% and 58.3% of resident Adam, but slowed the optimizer update path by about 4.3x. Cached memmap state had essentially no RSS benefit and was 2.8-4.1x slower.

## Boundaries and scale limits

No real model training, no autograd forward/backward memory, no convergence evidence, no GPT-2-small-class baseline, no larger-than-RAM state, and no multi-run robustness beyond two local tensor sizes.

## Claim scope

Bounded CPU NumPy Adam-update microbenchmark on 16 layer-shaped float32 tensors. Explicit per-layer file-backed state eviction reduced peak RSS versus resident Adam state, while cached file-backed materialization did not.

## Why it stopped

Bounded microbenchmark supports the memory mechanism only with explicit eviction and exposes a large throughput penalty; this is not full validation or paper-ready evidence.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded action is a framework-integrated CPU training test that measures loss parity, peak RSS, wall-clock, and page faults under memory pressure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Framework-integrated layer-wise Adam materialization under CPU memory pressure
- Success threshold: Materialized Adam completes a memory-pressure run that resident Adam cannot complete or cannot keep below a predeclared RSS ceiling, with loss parity within 1% and less than 5x end-to-end step-time slowdown.
- Stop condition: Stop if materialized Adam fails loss parity, does not reduce peak RSS by at least 25% in the integrated run, or exceeds 5x end-to-end step-time slowdown without enabling a larger feasible configuration.

## Evidence references

- Artifact root: `<local-path>/projects/layer-wise-adam-state-materialization-for-cpu-training-87551bd90ded`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

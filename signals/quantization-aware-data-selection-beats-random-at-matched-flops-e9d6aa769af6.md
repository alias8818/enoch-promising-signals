# Quantization-Aware Data Selection Beats Random at Matched FLOPs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `quantization-aware-data-selection-beats-random-at-matched-flops-e9d6aa769af6`
Run ID: `quantization-aware-data-selection-beats-random-at-matched-flops-e9d6aa769af6-20260628T105646416418+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/92970d39d153

## What looked useful

Balanced random sampling beat quantization-regret-top selection on all 10 seeds by 9.20 percentage points mean quantized test accuracy. Low-regret and absolute-regret quantization-aware variants also lost all 10 seeds; the best variant still trailed random by 4.37 percentage points.

## Boundaries and scale limits

Synthetic classification only; not a real LM/vision workload; no production int4 kernels, activation quantization, QAT, per-channel/groupwise quantization, or full end-to-end selection FLOP accounting. The matched-FLOP claim applies only to final training, not pilot/scoring overhead.

## Claim scope

In a 10-seed synthetic teacher-labeled classification probe with small MLPs, 25% training subsets, matched final-training epochs/batch/model/optimizer, and 4-bit symmetric per-tensor fake weight quantization, naive quantization-regret data selection did not beat balanced random sampling.

## Why it stopped

Proxy/early falsification: the directly tested synthetic setup consistently contradicted the hypothesis, but this is not a full validation or impossibility proof for all quantization-aware data selection methods.

## Recommended next action

Stop this worker run as an early synthetic falsification of naive quantization-regret selection; a new bounded follow-up should test diversity-constrained quantization-aware selection on a real small LM or vision dataset with selection overhead included.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-Constrained Quantization-Aware Selection on a Real Small Dataset
- Success threshold: Diversity-constrained quantization-aware selection improves quantized validation/test metric over random by at least 1 percentage point or equivalent loss reduction on at least 4 of 5 seeds without a worse fp32 metric.
- Stop condition: Stop if quantization-aware variants fail to beat random on at least 3 of the first 5 seeds or if selection overhead dominates any final-training FLOP savings.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-aware-data-selection-beats-random-at-matched-flops-e9d6aa769af6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

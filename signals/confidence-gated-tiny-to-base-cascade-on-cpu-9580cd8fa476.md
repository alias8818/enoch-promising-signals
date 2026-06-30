# Confidence-Gated Tiny-to-Base Cascade on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `confidence-gated-tiny-to-base-cascade-on-cpu-9580cd8fa476`
Run ID: `confidence-gated-tiny-to-base-cascade-on-cpu-9580cd8fa476-20260620T011142243287+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/17cd328b4fe6

## What looked useful

Across seeds 9580-9583, the validation-selected threshold was 1.0 every time, causing a 100% base call rate. Mean tiny accuracy was 0.7579, mean base accuracy was 0.9738, and mean cascade accuracy matched base only because all examples routed to base. The tiny confidence signal was non-monotone and overconfident on hard contrast cases.

## Boundaries and scale limits

Synthetic classifier proxy only; no LLM generation, no real query distribution, no optimized inference runtime, and no full-scale serving workload. The result falsifies only raw monotone confidence gating in this bounded proxy.

## Claim scope

Raw max-probability confidence thresholding for a tiny-to-base CPU cascade was tested on a deterministic synthetic text-classification proxy with four seeds and did not reduce base-model calls while preserving base accuracy.

## Why it stopped

Proxy early falsification: under the stated validation accuracy constraint, raw monotone confidence gating accepted no tiny outputs on any tested seed, so it added overhead without saving base-model work.

## Recommended next action

Stop this raw-confidence proxy path; a useful next local test would replace raw max-probability gating with a calibrated router or selective classifier on a real answer-keyed small query set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Router for Tiny-to-Base CPU Cascade on Answer-Keyed Queries
- Success threshold: On held-out test data, calibrated cascade accuracy is within 1 percentage point of base-only accuracy while base_call_rate <= 0.75 and expected latency is lower than base-only after tiny/router overhead.
- Stop condition: Stop if the calibrated router cannot beat raw thresholding on validation, or if test base_call_rate remains above 0.90 at the accuracy tolerance.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-tiny-to-base-cascade-on-cpu-9580cd8fa476`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

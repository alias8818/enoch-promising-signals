# Confidence-gated CPU model cascade for local serving

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `confidence-gated-cpu-model-cascade-for-local-serving-a75a9c96699a`
Run ID: `confidence-gated-cpu-model-cascade-for-local-serving-a75a9c96699a-20260608T081553137573+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/97e96394eeb2

## What looked useful

The small model was faster but much less accurate. Across three seeds, preserving large-model accuracy within 1 percentage point required about 75.6% deferral, above the about 37.1% average defer-rate break-even estimate, so the cascade was slower than always-large.

## Boundaries and scale limits

Synthetic classification only; NumPy classifiers only; no transformer, LLM, quantized runtime, production request trace, or real calibration workload was tested. Runs were bounded to three seeds and completed in seconds on a CPU worker.

## Claim scope

In a pure-NumPy synthetic nonlinear multiclass CPU batch-1 serving benchmark, a max-confidence small-first cascade did not improve latency while preserving large-model accuracy within 1 percentage point.

## Why it stopped

Proxy early falsification: the bounded local CPU benchmark showed the naive confidence cascade missed the latency-preserving-accuracy target because required defer rates were too high.

## Recommended next action

Stop this run as a proxy early falsification of the naive max-confidence gate; a bounded follow-up should test calibrated routing on a real local CPU model pair and require defer rate below measured break-even.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated router for real CPU local-serving model cascade
- Success threshold: Within 1 percentage point of always-large quality and at least 1.2x mean-latency speedup, with defer rate below the measured break-even point.
- Stop condition: Stop if the calibrated router cannot keep defer rate below break-even while staying within 1 percentage point of always-large quality on the real workload.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-cpu-model-cascade-for-local-serving-a75a9c96699a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Quantization-Aware Training for 4-bit Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantization-aware-training-for-4-bit-inference-7e69c96c0295`
Run ID: `quantization-aware-training-for-4-bit-inference-7e69c96c0295-20260605T084344134083+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/d8e1b158b562

## What looked useful

Across five seeds at 128 hidden units, QAT improved mean simulated int4 test accuracy by 0.37 percentage points and beat PTQ on 4/5 seeds. At 32 hidden units, where PTQ incurred a 2.10 point dense-to-int4 drop, QAT improved simulated int4 accuracy by 1.25 points and beat PTQ on 5/5 seeds.

## Boundaries and scale limits

Small real dataset only; MLP only; simulated fake quantization only; dynamic scales; no transformer, convolutional, static-calibration, hardware int4 kernel, latency, energy, or memory validation.

## Claim scope

On UCI Optdigits with a NumPy MLP and simulated dynamic int4 fake quantization, QAT preserves or improves 4-bit inference accuracy relative to dense training followed by PTQ, with the clearest gain in the lower-capacity 32-hidden-unit setting.

## Why it stopped

No-paper closure: the result is a useful small-scale simulated-quantization signal, not direct publication-grade validation of 4-bit QAT for modern inference.

## Recommended next action

Run a bounded deepen test with static or learned activation scales and a bit-exact int4 inference path on at least one larger real model family before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Static-scale int4 QAT validation beyond Optdigits MLP
- Success threshold: QAT improves mean bit-exact int4 test accuracy by at least 1.0 percentage point over PTQ and reduces dense-to-int4 accuracy drop by at least 50% on the selected larger workload without a material dense-accuracy regression.
- Stop condition: Stop if PTQ has less than 0.5 percentage point quantization drop on the chosen workload or if QAT fails to beat PTQ mean int4 accuracy across matched seeds.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-aware-training-for-4-bit-inference-7e69c96c0295`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Coverage-Maximizing Calibration Data for INT8

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `coverage-maximizing-calibration-data-for-int8-e0dc05fc7146`
Run ID: `coverage-maximizing-calibration-data-for-int8-e0dc05fc7146-20260525T203350882344+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c88017cb2969

## What looked useful

Coverage-maximizing calibration can improve numeric fidelity metrics under very small calibration budgets, but this did not translate into accuracy gains when the baseline INT8 model already preserved MNIST accuracy.

## Boundaries and scale limits

Small MNIST MLP only; simulated PTQ rather than framework/hardware INT8; three model seeds; calibration budgets 4-64; no CNNs, Transformers, language models, production quantizers, or hardware latency/throughput validation.

## Claim scope

On a pure-NumPy MNIST 784-128-10 ReLU MLP with simulated static INT8 weights and activations, activation-space k-center calibration subsets reduced worst-case activation coverage radius, hidden activation clipping, and logit MSE versus random calibration, but did not improve quantized accuracy.

## Why it stopped

No-paper closure: direct small-scale evidence is mixed and does not support the practical INT8 accuracy-improvement claim; it only supports a mechanism-level numeric-fidelity signal.

## Recommended next action

Run a bounded deepen test on a more calibration-sensitive model where random static INT8 calibration causes at least a 1 percentage point accuracy drop before claiming practical value.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Coverage calibration on a calibration-sensitive INT8 benchmark
- Success threshold: Activation coverage selection improves quantized accuracy by at least 0.5 percentage points absolute over the best non-coverage calibration baseline at equal calibration budget, while maintaining lower clipping or logit MSE.
- Stop condition: Stop if the chosen benchmark does not produce at least a 1 percentage point random-calibration INT8 drop, or if coverage selection fails to beat the best baseline by 0.5 percentage points on two independent seeds.

## Evidence references

- Artifact root: `<local-path>/projects/coverage-maximizing-calibration-data-for-int8-e0dc05fc7146`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

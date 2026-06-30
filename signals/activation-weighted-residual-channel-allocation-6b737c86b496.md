# Activation-Weighted Residual Channel Allocation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-weighted-residual-channel-allocation-6b737c86b496`
Run ID: `activation-weighted-residual-channel-allocation-6b737c86b496-20260527T040855304721+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/06b896041af3

## What looked useful

Across 256-trial confirmation runs with 12 layers and 256 channels, activation-weighted allocation improved retained held-out update energy over uniform by 3.1-4.1 percentage points at 5-40% budgets in the stationary predictive setting, but had no advantage in isotropic or shifted nonpredictive controls. A rho sweep showed the advantage rising with calibration/test energy correlation.

## Boundaries and scale limits

No trained transformer, no language-model loss, no convergence measurement, no kernel or throughput measurement, and no real activation traces from GPT-2-class models. Results are synthetic/proxy evidence only.

## Claim scope

Trace-level NumPy simulation of fixed residual layer-channel budgets: activation-weighted global allocation preserves more held-out residual-update energy than uniform per-layer allocation only when calibration activation energy is anisotropic and predictive of held-out update energy.

## Why it stopped

Useful proxy mechanism signal, but not full validation: the result depends on synthetic calibration/update predictiveness and does not test trained model quality or efficiency.

## Recommended next action

Stop this proxy run; next run should implement a small parameter-matched transformer or residual MLP with real activation-weighted channel allocation and compare validation loss against dense and uniform-allocation baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer Validation of Activation-Weighted Residual Channel Allocation
- Success threshold: Activation-weighted allocation beats uniform allocation by at least 1% relative validation loss or at least 3 percentage points retained residual-update energy without worse throughput by more than 10%, with the effect present in at least two of three seeds.
- Stop condition: Stop if activation/update energy correlation stays below 0.25 after warmup or if activation-weighted allocation fails to beat uniform on both validation loss and retained-update metrics after the planned training budget.

## Evidence references

- Artifact root: `<local-path>/projects/activation-weighted-residual-channel-allocation-6b737c86b496`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Independent-calibration undertrained proxy gradient verifier

Status: `useful_signal`
Project ID: `independent-calibration-undertrained-proxy-gradient-verifi-1c467e6bea`
Run ID: `independent-calibration-undertrained-proxy-gradient-verifi-1c467e6bea-20260517T191114107824+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2d019a3fa381

## What looked useful

The calibrated undertrained proxy met the predefined Tier 1 threshold: calibrated AUROC >= 0.75, ECE_10 <= 0.10, and AUROC lift over random >= 0.05. This supports the independent-calibration mechanism in a narrow shared-gradient setting but is not paper-ready.

## Boundaries and scale limits

Small real dataset, linear models only, five seeds, generated candidate update families, and short local runtime; no nonlinear hidden-layer, language-model, adversarial-gradient, or large-scale training validation.

## Claim scope

On sklearn digits with linear softmax target/proxy models sharing a parameter-gradient coordinate system, an independently trained 2-epoch proxy plus independent logistic calibration verified held-out-loss-improving target gradient updates with mean AUROC 0.7666 and mean ECE_10 0.0689 across five seeds.

## Why it stopped

Tier 1 direct small test produced useful mechanism support, but the evidence remains too narrow for publication-grade validation.

## Recommended next action

Run one bounded deepen test on a nonlinear or last-layer shared-gradient model using the same independent calibration protocol and a medium dataset before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Nonlinear shared-gradient proxy verifier confirmation
- Success threshold: Mean calibrated AUROC >= 0.75, mean ECE_10 <= 0.10, AUROC lift over random >= 0.05, and no more than one of five seeds below AUROC 0.70.
- Stop condition: Stop as unsupported if calibrated AUROC is below 0.70 mean, ECE_10 exceeds 0.15, or performance collapses on candidate families not seen in calibration.

## Evidence references

- Artifact root: `<local-path>/projects/independent-calibration-undertrained-proxy-gradient-verifi-1c467e6bea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

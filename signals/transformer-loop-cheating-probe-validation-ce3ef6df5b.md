# Transformer-Loop Cheating Probe Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `transformer-loop-cheating-probe-validation-ce3ef6df5b`
Run ID: `transformer-loop-cheating-probe-validation-ce3ef6df5b-20260531T100901839636+0000`

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

- Parent run decision: Micro-Sharded Gradient Accumulation with On-Device Cheating Probes: enoch://control-plane/projects/micro-sharded-gradient-accumulation-with-on-device-cheating-probes-a0c0499425fd/runs/micro-sharded-gradient-accumulation-with-on-device-cheating-probes-a0c0499425fd-20260530T051240898620+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12c22dd7eb68

## What looked useful

The loop-step probe is valid in a controlled setting: learned recurrent hidden-state trajectories can carry a strong step signal and can support a shortcut that collapses under reversed counterfactual labels. Untrained looped dynamics showed only partial step recoverability below the success threshold.

## Boundaries and scale limits

Synthetic random-token task; tiny transformer; shortcut objective explicitly rewards loop-parity encoding; three seeds; no real algorithmic task, no GPT-2-scale baseline, and no deployment-scale evidence.

## Claim scope

In a tiny synthetic Tier 1 controlled test, a weight-tied looped transformer trained on a loop-parity shortcut without explicit step embeddings produced hidden states from which a linear probe recovered loop step at 0.990 mean test accuracy across three seeds; static, Gaussian, and shuffled-label controls stayed near chance.

## Why it stopped

Tier 1 controlled validation produced a useful mechanism signal but not publication-grade evidence; closing as no-paper useful_signal rather than continuing to broader validation in this run.

## Recommended next action

Run a bounded deepen follow-up on a real iterative synthetic algorithm task with a parameter-matched non-looped baseline and train/test shortcut decorrelation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Loop-Step Probe Predicts Shortcut Failure on Iterative Algorithm Tasks
- Success threshold: Looped model has probe accuracy >= 0.80, in-distribution task accuracy >= 0.90, counterfactual accuracy at least 20 percentage points below a decorrelated-control model, and negative/shuffled controls within chance + 0.10.
- Stop condition: Stop if the looped model cannot learn the base task to >= 0.90 in-distribution accuracy, if probe accuracy remains below 0.80, or if counterfactual accuracy does not degrade relative to the control.

## Evidence references

- Artifact root: `<local-path>/projects/transformer-loop-cheating-probe-validation-ce3ef6df5b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

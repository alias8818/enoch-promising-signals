# Real-Task Severe-Scarcity Nonlinear Adapter Validation

Status: `useful_signal`
Project ID: `real-task-severe-scarcity-nonlinear-adapter-validation-2e407b5048`
Run ID: `real-task-severe-scarcity-nonlinear-adapter-validation-2e407b5048-20260518T054356271257+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Real-Task Severe-Scarcity Nonlinear Adapter Validation: internal_generated:real-task-severe-scarcity-nonlinear-adapter-validation-2e407b5048

## What looked useful

Main rank-32 run: nonlinear_adapter beat linear_probe by +0.0073 mean accuracy over 90 task/k/seed cells and beat linear_low_rank by +0.0089; rank-8 and rank-64 robustness runs showed similar +0.0072 to +0.0113 gains for the simple nonlinear adapter. Shuffled-label controls were lower on average, supporting that the benchmark was learning signal rather than pure noise.

## Boundaries and scale limits

This did not validate transformer/LLM adapters, end-to-end pretrained-model fine-tuning, larger datasets, or a broad task suite. The effect is small, many severe-scarcity splits remain near chance, and residual nonlinear-vs-residual-linear evidence is inconsistent except at rank 64.

## Claim scope

On three 20 Newsgroups real text classification tasks using frozen TF-IDF/SVD features, severe k-shot training, fixed seeds, and held-out accuracy, a simple nonlinear MLP adapter gives a small average gain over linear probe and same-rank linear bottleneck baselines.

## Why it stopped

Evidence supports a small bounded mechanism signal on frozen TF-IDF/SVD real-text features, but it is not publication-grade nonlinear adapter validation for pretrained transformer or LLM settings.

## Recommended next action

Stop this follow-up at depth 4; preserve the artifacts as a useful no-paper signal and do not chain another follow-up from this worker result.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-task-severe-scarcity-nonlinear-adapter-validation-2e407b5048`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

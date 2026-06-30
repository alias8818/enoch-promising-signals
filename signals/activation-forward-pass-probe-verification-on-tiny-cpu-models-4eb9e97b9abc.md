# Activation Forward-Pass Probe Verification on Tiny CPU Models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `activation-forward-pass-probe-verification-on-tiny-cpu-models-4eb9e97b9abc`
Run ID: `activation-forward-pass-probe-verification-on-tiny-cpu-models-4eb9e97b9abc-20260620T232602550089+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dd37f5976891

## What looked useful

Across three seeds, final tiny models reached 100% held-out task accuracy. Prefix and suffix latent-feature probes reached 1.000 mean best balanced accuracy versus 0.589 and 0.536 best-control means; h2 feature probes were about 0.959 balanced accuracy.

## Boundaries and scale limits

Synthetic data only; tiny MLP architecture only; no transformer, pretrained language model, natural-language corpus, large-model, or robustness validation. Task-label controls were less clean than latent-feature controls.

## Claim scope

Tiny CPU NumPy MLP sequence classifiers trained on a controlled synthetic XOR task expose known prefix/suffix latent features in frozen forward-pass activations to linear probes above shuffled-label and random-activation controls.

## Why it stopped

Evidence supports the scoped synthetic mechanism but is not publication-grade because it is small, synthetic, MLP-only, and not validated on transformer or real language activations.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should repeat the protocol on a tiny transformer or GPT-2-small-class model with real or semi-synthetic language features and stricter controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Forward-Activation Probe Controls
- Success threshold: At least two hidden layers show target-feature probe balanced accuracy >= 0.80 with >= 0.20 absolute gap over every control across three seeds while task accuracy exceeds a majority baseline by >= 0.20.
- Stop condition: Stop if the tiny transformer fails to learn the task above baseline after bounded tuning or if probe-control gaps stay below 0.10 across all layers and seeds.

## Evidence references

- Artifact root: `<local-path>/projects/activation-forward-pass-probe-verification-on-tiny-cpu-models-4eb9e97b9abc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

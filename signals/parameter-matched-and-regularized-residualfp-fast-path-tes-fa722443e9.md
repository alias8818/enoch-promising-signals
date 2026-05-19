# Parameter-matched and regularized ResidualFP fast-path test

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `parameter-matched-and-regularized-residualfp-fast-path-tes-fa722443e9`
Run ID: `parameter-matched-and-regularized-residualfp-fast-path-tes-fa722443e9-20260517T151432715891+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Parameter-matched and regularized ResidualFP fast-path test: internal_generated:parameter-matched-and-regularized-residualfp-fast-path-tes-fa722443e9

## What looked useful

ResidualFP fast-path gains become load-bearing under exact parameter matching: full masking raises validation loss by about 0.069 nats, and 50% train-time masking roughly halves both gain magnitude and ablation damage. The practical target fails: mean validation-loss gains versus dense are only about 0.0002-0.0003 nats, inconsistent by seed, and forward latency is about 4.7-5.0% slower than dense.

## Boundaries and scale limits

The evidence is limited to a 466,176-parameter character-level model, 8,000 training steps, three seeds, one dataset, one fast-path definition, and one L2 regularization setting; it does not cover GPT-2-small scale, subword corpora, broader hyperparameter sweeps, or fused custom kernels.

## Claim scope

Exact-parameter tiny character-level Transformer validation on Tiny Shakespeare with a ResidualFP MLP fast path, L2 gain regularization, fixed seeds, ablation controls, and local GB10 forward-latency benchmarking.

## Why it stopped

Tier 3 local validation directly tested the parameter-matched and regularized ResidualFP hypothesis and found only seed-noise-scale validation differences plus a measured latency penalty.

## Recommended next action

Stop this follow-up line as no-paper useful signal: the bounded direct test supports the mechanism but not a meaningful accuracy or fast-path speed claim.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/parameter-matched-and-regularized-residualfp-fast-path-tes-fa722443e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

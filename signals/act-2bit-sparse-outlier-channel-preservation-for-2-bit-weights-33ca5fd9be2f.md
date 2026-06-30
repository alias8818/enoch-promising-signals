# ACT-2bit: Sparse Outlier Channel Preservation for 2-bit Weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `act-2bit-sparse-outlier-channel-preservation-for-2-bit-weights-33ca5fd9be2f`
Run ID: `act-2bit-sparse-outlier-channel-preservation-for-2-bit-weights-33ca5fd9be2f-20260621T201407632407+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/934896233762

## What looked useful

Sparse full-precision channel preservation strongly reduced relative MSE in synthetic heavy-tail matrices and many DistilGPT2 attention layers, but naive activation-weight channel selection substantially worsened several MLP projection layers, so the mechanism needs layer gating or error-aware selection before model-level use.

## Boundaries and scale limits

No perplexity/task evaluation, no 7B-scale model, no overnight training, and no kernel or serving benchmark. DistilGPT2 calibration used a short prompt batch and matrix-output reconstruction only.

## Claim scope

Bounded CPU reconstruction probe for per-row affine 2-bit weight quantization on synthetic heavy-tail matrices and hooked DistilGPT2 layer inputs; not an end-task or large-model validation.

## Why it stopped

Mixed bounded reconstruction evidence: mechanism is useful in heavy-tail and attention cases, but naive sparse preservation is not reliably safe on real transformer MLP projection layers.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded test should add a calibration-error gate and evaluate perplexity on a small causal LM.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gated sparse channel preservation for 2-bit causal LM perplexity
- Success threshold: At the same preserved-channel overhead, gated activation-aware preservation must improve held-out perplexity over plain 2-bit and random preservation, while avoiding calibration reconstruction regressions larger than 1% on gated-in layers.
- Stop condition: Stop if the gated scheme fails to beat plain 2-bit perplexity or if more than 25% of gated-in layers show worse calibration reconstruction than plain 2-bit.

## Evidence references

- Artifact root: `<local-path>/projects/act-2bit-sparse-outlier-channel-preservation-for-2-bit-weights-33ca5fd9be2f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

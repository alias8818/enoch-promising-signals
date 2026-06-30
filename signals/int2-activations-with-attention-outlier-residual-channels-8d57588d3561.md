# INT2 activations with attention-outlier residual channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-activations-with-attention-outlier-residual-channels-8d57588d3561`
Run ID: `int2-activations-with-attention-outlier-residual-channels-8d57588d3561-20260621T225729302150+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5d3a42f703b2

## What looked useful

INT2-all activation quantization increased GPT-2-small loss from 4.1236 to 12.3231. Preserving 3.125% calibrated outlier channels per attention/residual module reduced loss to 7.6979, and 6.25% reduced it to 7.5202. Random same-budget channel preservation was far weaker, and residual outlier preservation carried most of the benefit.

## Boundaries and scale limits

Single GPT-2-small model, 64 calibration windows, 128 validation windows, sequence length 128, one seed, forward-hook dequantized activation simulation only; no packed kernels, training, QAT, larger models, or multi-dataset robustness.

## Claim scope

On GPT-2-small WikiText-2 inference probes, preserving calibrated residual-stream and attention-output outlier channels substantially reduces loss damage from INT2 affine activation quantization, but does not make the method viable by itself.

## Why it stopped

Bounded local evidence supports the outlier-channel mitigation mechanism, but best tested INT2 hybrid remains far from FP baseline loss, so this is not a viable or paper-ready result.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should combine residual-outlier preservation with a stronger activation quantization recipe such as per-group scaling, smoothing, or short QAT on GPT-2-small/medium.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-outlier INT2 activations with smoothing or short QAT
- Success threshold: At a preserved-channel budget no larger than 6.25% per affected module, held-out loss is within 10% of FP baseline and improves over INT4-all or a matched mixed-precision baseline on at least two model/dataset settings.
- Stop condition: Stop if GPT-2-small remains more than 25% worse than FP loss after smoothing/QAT, or if matched random/mixed-precision controls erase the calibrated-outlier advantage.

## Evidence references

- Artifact root: `<local-path>/projects/int2-activations-with-attention-outlier-residual-channels-8d57588d3561`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

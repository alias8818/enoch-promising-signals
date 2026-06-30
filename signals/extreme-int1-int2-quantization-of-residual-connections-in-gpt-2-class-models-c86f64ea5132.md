# Extreme INT1/INT2 Quantization of Residual Connections in GPT-2 class models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-int1-int2-quantization-of-residual-connections-in-gpt-2-class-models-c86f64ea5132`
Run ID: `extreme-int1-int2-quantization-of-residual-connections-in-gpt-2-class-models-c86f64ea5132-20260605T114214529254+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/386df4290840

## What looked useful

Extreme residual-stream quantization is not viable as a simple post-training insertion in this probe, but QAT can adapt a small transformer to INT1/INT2 residual streams with a moderate remaining loss gap. Activation statistics suggest the model may compensate through residual scale inflation.

## Boundaries and scale limits

818k-parameter character-level model, context length 64, one seed, short training and QAT schedule, fake activation quantization only, no packed INT1/INT2 kernels, no GPT-2-small/WebText-scale validation.

## Claim scope

Small GPT-style character language model on Tiny Shakespeare: post-training INT1/INT2 residual-stream quantization after every residual add is damaging, while 180-step quantization-aware fine-tuning recovers most but not all of the loss and remains about +0.25 nats above the FP residual baseline.

## Why it stopped

Bounded direct small-model evidence is mixed: post-training INT1/INT2 residual quantization fails badly, and QAT recovery remains outside the predeclared INT2 support threshold with signs of activation scale inflation.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test from-scratch or longer QAT with residual scale regularization and at least three seeds before considering larger GPT-2-small-class validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual INT1/INT2 QAT with scale control across seeds
- Success threshold: Mean INT2 validation loss delta <= 0.10 nats versus FP residual baseline and residual signal power less than 3x the FP/post-training reference, with no seed exceeding +0.15 nats.
- Stop condition: Stop as negative if mean INT2 loss delta remains > 0.20 nats after the bounded QAT schedule or if scale-control prevents adaptation while unrestricted QAT only succeeds through >3x residual signal-power growth.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int1-int2-quantization-of-residual-connections-in-gpt-2-class-models-c86f64ea5132`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

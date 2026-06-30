# Standard-Corpus Residual-Channel Packed INT4 Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `standard-corpus-residual-channel-packed-int4-validation-5d793976c8`
Run ID: `standard-corpus-residual-channel-packed-int4-validation-5d793976c8-20260605T231658381301+0000`

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

- Parent run decision: Packed INT4 Residual-Channel Validation Across Seeds and Models: enoch://control-plane/projects/packed-int4-residual-channel-validation-across-seeds-and-m-84f85c6d3d/runs/packed-int4-residual-channel-validation-across-seeds-and-m-84f85c6d3d-20260605T220335951521+0000
- Parent run decision: Extreme INT4 Quantization with Principled Residual Channels: enoch://control-plane/projects/extreme-int4-quantization-with-principled-residual-channels-5fe8780180e7/runs/extreme-int4-quantization-with-principled-residual-channels-5fe8780180e7-20260605T210208292221+0000

## What looked useful

Error-selected residual channels are a real mechanism signal: at 6.25% dense residual channels they reduced WikiText PPL from 462570.65 for ordinary INT4 to 8792.31 and beat a random-channel control at equal storage. However dense GPT-2 was PPL 36.88, and increasing residual budget to 12.5% and 25% only reached PPL 7403.92 and 7366.12, so the tested scheme is not viable as a practical packed INT4 validation.

## Boundaries and scale limits

One GPT-2-small-class model, WikiText held-out text only because PTB loading failed under the installed datasets version, simulated packed storage rather than custom INT4 kernels, no calibrated GPTQ/AWQ-style baseline, no larger models, and no throughput claim.

## Claim scope

On GPT-2-small pretrained inference over held-out WikiText text, error-selected dense residual channels in a simulated packed INT4 weight-only quantization scheme consistently outperform ordinary INT4 and random residual-channel controls, but remain far from dense-model perplexity even at 25% dense residual-channel budget.

## Why it stopped

Medium direct perplexity validation found mechanism support but practical failure: residual-channel packed INT4 remained orders of magnitude worse than dense perplexity, and a 25% residual budget barely improved over 12.5%.

## Recommended next action

Stop this branch as no-paper useful evidence; any next bounded test should replace naive per-channel INT4 with a calibrated GPTQ/AWQ-style packed INT4 baseline plus the same residual-channel selection on multiple independent corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Residual-Channel Packed INT4 Against GPTQ/AWQ Baselines
- Success threshold: Calibrated residual-channel INT4 beats the calibrated INT4 baseline and random residual control at equal storage, and reaches within 20% relative perplexity of dense GPT-2 on both corpora at no more than 55% of fp16 weight storage.
- Stop condition: Stop as negative if calibrated residual-channel INT4 remains more than 2x dense perplexity on either corpus or fails to beat the calibrated INT4 baseline at equal storage.

## Evidence references

- Artifact root: `<local-path>/projects/standard-corpus-residual-channel-packed-int4-validation-5d793976c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

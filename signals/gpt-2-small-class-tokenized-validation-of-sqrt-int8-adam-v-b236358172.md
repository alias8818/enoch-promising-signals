# GPT-2-small-class tokenized validation of sqrt-int8 Adam v states

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `gpt-2-small-class-tokenized-validation-of-sqrt-int8-adam-v-b236358172`
Run ID: `gpt-2-small-class-tokenized-validation-of-sqrt-int8-adam-v-b236358172-20260516T052823353758+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: GPT-2-small-class tokenized validation of sqrt-int8 Adam v states: internal_generated:gpt-2-small-class-tokenized-validation-of-sqrt-int8-adam-v-b236358172

## What looked useful

sqrt-space int8 quantization is materially better than raw-v int8, which diverged even at 1e-4, and it can train GPT-2-small-class models with retuning while saving optimizer-state memory. However, it diverged at baseline AdamW hyperparameters and trailed AdamW by about 0.094 to 0.097 validation-loss points at matched lower-rate token counts.

## Boundaries and scale limits

Validation used WikiText-2, 128-token contexts, batch size 16, up to 4.096M tokens for the baseline-rate run and 2.048M tokens for the stable lower-rate run. It did not test long-horizon convergence, larger corpora, pretrained fine-tuning, multi-node scale, or fused optimizer kernels.

## Claim scope

On a local 123.8M-parameter GPT-2-small-class model trained on GPT-2-tokenized WikiText-2, blockwise sqrt-int8 AdamW v-state storage reduced estimated optimizer-state memory by about 37.5% and trained stably only after lowering the learning rate to 1e-4, but it failed as a drop-in replacement at the AdamW baseline learning rate of 3e-4.

## Why it stopped

Direct GPT-2-small-class validation produced mixed evidence: stable retuned training and memory savings, but failure at baseline AdamW learning rate and no publication-grade parity.

## Recommended next action

Stop this run as no-paper evidence; a final depth-4 deepen follow-up should test a less lossy sqrt-state quantizer such as percentile-scaled or zero-floor blockwise int8 against the same GPT-2-small AdamW parity threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Zero-floor or percentile-scaled sqrt-int8 Adam v-state parity test
- Success threshold: Modified sqrt-int8 completes at least 2M tokens at 3e-4 on two seeds with no divergence, validation loss within 0.03 of AdamW at matched tokens, and at least 35% estimated optimizer-state memory reduction.
- Stop condition: Stop early if either seed exceeds AdamW validation loss by more than 0.15 after 512k tokens or shows validation loss above 20 after warmup, because that would falsify baseline-rate parity.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-tokenized-validation-of-sqrt-int8-adam-v-b236358172`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

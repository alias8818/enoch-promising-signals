# Blockwise 8-bit AdamW for tiny transformer pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `blockwise-8-bit-adamw-for-tiny-transformer-pretraining-0c17243ed43d`
Run ID: `blockwise-8-bit-adamw-for-tiny-transformer-pretraining-0c17243ed43d-20260605T011614325627+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/053a5e17c8ff

## What looked useful

Small quantization blocks appear necessary for stable blockwise 8-bit AdamW in this tiny transformer setting. Block-64 matched AdamW validation loss in two seeds with 505,336 optimizer-state bytes versus AdamW's 1,898,612 bytes. Block-2048 passed a 3-step smoke test but later diverged to validation loss 13,800.57.

## Boundaries and scale limits

Test used a repeated small text corpus, 80 CPU steps, no GPU, no fused kernels, no real tokenizer, no long schedule, and no medium or GPT-2-small-class model. Throughput reflects a Python/PyTorch dequantize-update-requantize implementation, not production optimizer performance.

## Claim scope

On a 237,312-parameter char-level tiny causal transformer trained for 80 CPU steps, blockwise int8 AdamW with 64-element quantization blocks preserved short-run training behavior across two seeds while reducing optimizer-state tensor bytes by 73.4%; coarse 2048-element blocks diverged catastrophically by step 80.

## Why it stopped

No-paper closure: this run produced bounded useful signal and an early falsification of coarse blockwise quantization, but it is too small and proxy-limited for publication-grade validation.

## Recommended next action

Run a bounded medium follow-up on a real corpus with a larger transformer and explicit second-moment quantization diagnostics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium-scale stability test for small-block 8-bit AdamW
- Success threshold: Across at least three seeds, small/adaptive-block 8-bit AdamW finishes within 2% relative validation loss of AdamW while reducing optimizer-state tensor bytes by at least 60% and without delayed divergence.
- Stop condition: Stop if validation loss diverges or exceeds AdamW by more than 10% after the warmup phase in two seeds, or if quantization diagnostics show persistent second-moment collapse that is not fixed by block-size reduction.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-8-bit-adamw-for-tiny-transformer-pretraining-0c17243ed43d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

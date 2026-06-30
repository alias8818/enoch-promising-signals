# 8-bit AdamW with calibrated error feedback: VRAM savings vs final loss on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adamw-with-calibrated-error-feedback-vram-savings-vs-final-loss-on-gpt-2-small-19cec702dce2`
Run ID: `8-bit-adamw-with-calibrated-error-feedback-vram-savings-vs-final-loss-on-gpt-2-small-19cec702dce2-20260630T112603149895+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/091de4528619

## What looked useful

Naive calibrated error feedback can erase practical VRAM savings: fp16 residual buffers plus fp32 dequantized moment temporaries outweighed the 8-bit state reduction in measured peak CUDA allocation.

## Boundaries and scale limits

Short-run GPT-2-small-class evidence only; no full pretraining, no convergence-scale final loss, and no fused production optimizer kernel. The result evaluates this local implementation, not all possible 8-bit AdamW error-feedback designs.

## Claim scope

On a 12-step GPT-2-small WikiText-2 local run, the tested blockwise 8-bit AdamW with fp16 calibrated residual error feedback reduced stored optimizer state by about 25% and matched AdamW loss only at a 10x lower learning rate, but it increased peak CUDA allocation by about 38% and ran at about 38% of AdamW throughput.

## Why it stopped

Direct short GPT-2-small evidence did not support the practical VRAM-saving claim: stored optimizer state shrank, but peak CUDA allocation and throughput were worse, and the normal learning rate diverged.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should redesign the optimizer to use fused/blockwise updates without full fp32 moment materialization or full fp16 residual buffers, then repeat the same GPT-2-small memory/loss comparison.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused blockwise 8-bit AdamW CEF without full residual buffers
- Success threshold: Peak CUDA allocated at least 20% lower than AdamW and validation loss within 1% of AdamW at the same learning rate over a 100-step GPT-2-small WikiText-2 run.
- Stop condition: Stop if peak CUDA allocation is not lower than AdamW after optimizer-state initialization and 20 measured steps, or if validation loss diverges by more than 10% at matched learning rate.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-with-calibrated-error-feedback-vram-savings-vs-final-loss-on-gpt-2-small-19cec702dce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

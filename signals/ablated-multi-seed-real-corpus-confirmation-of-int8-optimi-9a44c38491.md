# Ablated multi-seed real-corpus confirmation of int8 optimizer and FP8 saved-tensor memory savings

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ablated-multi-seed-real-corpus-confirmation-of-int8-optimi-9a44c38491`
Run ID: `ablated-multi-seed-real-corpus-confirmation-of-int8-optimi-9a44c38491-20260610T134953151888+0000`

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

- Parent run decision: Real-data confirmation of blockwise int8 optimizer plus checkpointed FP8 saved tensors: enoch://control-plane/projects/real-data-confirmation-of-blockwise-int8-optimizer-plus-ch-c952c77982/runs/real-data-confirmation-of-blockwise-int8-optimizer-plus-ch-c952c77982-20260610T090711845310+0000
- Parent run decision: implementation_gap: Unified Tiny-VRAM Training Framework Combining Checkpointing, FP8, and Int8 Optimizer: enoch://control-plane/projects/implementation-gap-unified-tiny-vram-training-framework-combining-checkpointing-fp8-and-int8-opt-9cf530452b37/runs/implementation-gap-unified-tiny-vram-training-framework-combining-checkpointing-fp8-and-int8-opt-9cf530452b37-20260610T051005835068+0000

## What looked useful

FP8 saved-tensor compression is a reproducible bounded memory-saving mechanism here; the combined int8 optimizer plus FP8 claim is not supported because the int8 optimizer destabilized under the main learning rate and a lower-learning-rate diagnostic.

## Boundaries and scale limits

Only Wikitext-2, byte-level tokenization, 80 training steps, one small Transformer size, one GPU host, and a custom blockwise int8 optimizer were tested. No large-model, long-horizon, distributed, or production optimizer validation was performed.

## Claim scope

On a GB10 GPU, a 19.18M-parameter byte-level causal Transformer trained for 80 steps on Wikitext-2 across seeds 11, 17, and 23 showed FP8 saved-tensor hooks reducing peak CUDA allocated memory by 30.8% versus AdamW without short-run loss regression; the tested blockwise int8 AdamW moment storage reduced optimizer state by about 75% but produced non-finite training in all medium-run seeds.

## Why it stopped

Tier-2 fixed-seed real-corpus evidence is mixed: FP8 memory savings are supported, but the int8 optimizer component fails numerically, so the combined hypothesis is not viable as tested.

## Recommended next action

Stop paper escalation for this branch; if continuing, test FP8 saved-tensor hooks separately with longer training and replace the custom int8 optimizer with a production-grade blockwise or error-feedback implementation before re-evaluating the combined claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer FP8 saved-tensor validation with production int8 optimizer control
- Success threshold: FP8-only must retain at least 25% peak allocated memory reduction with final loss within 5% of AdamW over the longer run; any int8 optimizer claim must complete all seeds without non-finite losses and retain at least 60% optimizer-state reduction.
- Stop condition: Stop if the production int8 optimizer produces non-finite losses in two or more seeds, or if FP8-only loses its memory advantage below 15% peak allocated reduction or shows more than 10% final-loss regression versus AdamW.

## Evidence references

- Artifact root: `<local-path>/projects/ablated-multi-seed-real-corpus-confirmation-of-int8-optimi-9a44c38491`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

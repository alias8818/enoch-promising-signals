# Transformer validation of dynamically scaled 8-bit AdamW state on real token data

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `transformer-validation-of-dynamically-scaled-8-bit-adamw-s-a61c6b40fc`
Run ID: `transformer-validation-of-dynamically-scaled-8-bit-adamw-s-a61c6b40fc-20260612T110844186375+0000`

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

- Parent run decision: 8-bit optimizer state quantization with dynamic scaling for tiny model training: enoch://control-plane/projects/8-bit-optimizer-state-quantization-with-dynamic-scaling-for-tiny-model-training-83b33a417cb4/runs/8-bit-optimizer-state-quantization-with-dynamic-scaling-for-tiny-model-training-83b33a417cb4-20260611T135329835104+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/329924fa12c8

## What looked useful

The exact per-tensor dynamic int8-state mechanism is not viable in this direct small Transformer test: at lr=1e-4 FP32 AdamW reached best validation loss 2.6772 while dynamic int8-state AdamW reached 5.3969 and ended with train loss 126.4640. Diagnostic state inspection found 92.5% of int8 second-moment entries zero after 100 steps, explaining unstable Adam denominators. Optimizer-state memory dropped by about 75%.

## Boundaries and scale limits

Single small Transformer, one real text corpus, byte-level tokens, one seed, up to 300 training steps. This does not test GPT-2-scale models, longer convergence, blockwise scaling, percentile clipping, error feedback, fused kernels, or established 8-bit optimizer implementations.

## Claim scope

A per-tensor absmax dynamically scaled int8 AdamW-state optimizer was tested during small decoder-only Transformer language-model training on Tiny Shakespeare UTF-8 byte tokens. It reduced optimizer-state memory to about 25% of FP32 AdamW state, but failed the Tier 1 stability/non-inferiority threshold versus FP32 AdamW.

## Why it stopped

Direct Tier 1 validation on real token data failed the stated non-inferiority threshold despite a conservative learning rate; this is an early direct falsification of the tested per-tensor mechanism, not a full-scale rejection of all 8-bit AdamW designs.

## Recommended next action

Stop this per-tensor variant as no-paper evidence; run one bounded deepen follow-up that replaces per-tensor absmax scaling with blockwise or percentile-clipped scaling and must meet the same direct Transformer validation threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise dynamic int8 AdamW-state validation on the same tiny Transformer token task
- Success threshold: Best validation loss no worse than 1.2x FP32 AdamW, final train loss finite and not explosively divergent, v_q zero fraction below 50%, and optimizer-state memory below 40% of FP32 AdamW state.
- Stop condition: Stop as negative if blockwise/percentile scaling still exceeds 1.2x FP32 best validation loss or shows loss explosion/NaN within 300 steps on this harness.

## Evidence references

- Artifact root: `<local-path>/projects/transformer-validation-of-dynamically-scaled-8-bit-adamw-s-a61c6b40fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

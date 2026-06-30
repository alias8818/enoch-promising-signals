# C8bit-AdamW: Chunked Error-Feedback 8-bit AdamW for GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `c8bit-adamw-chunked-error-feedback-8-bit-adamw-for-gb10-adaa21bdf433`
Run ID: `c8bit-adamw-chunked-error-feedback-8-bit-adamw-for-gb10-adaa21bdf433-20260621T005454749010+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f5234f46f3f8

## What looked useful

Unguarded linear 8-bit chunk quantization of AdamW second moments catastrophically zeroed small v entries and diverged. A half-scale v dequantization floor stabilized training. Full per-parameter error feedback improved state fidelity but consumed about 10 bytes/parameter for two moments plus residuals, 25% more than FP32 AdamW state. A cheap scalar-per-chunk residual preserved about 75% state-memory savings and improved the noisy quadratic proxy versus no error feedback, but did not materially improve heavy-tailed trace update error.

## Boundaries and scale limits

262,144-parameter synthetic CUDA tensors, 120 optimizer steps, three seeds, no real transformer/CV model, no datacenter-scale run, no custom fused kernel, and no comparison to production 8-bit optimizers beyond theoretical state-memory accounting.

## Claim scope

Bounded CUDA synthetic optimizer-state probe for chunked 8-bit AdamW variants on GB10. The tested mechanism was state/update fidelity and noisy quadratic optimization behavior versus FP32 AdamW, not real model training or a production fused optimizer.

## Why it stopped

No-paper useful signal: proxy evidence found a required stability guard and a memory/fidelity tradeoff, but full error feedback removes the memory benefit and cheap chunk-scalar feedback remains too weakly validated for a publication claim.

## Recommended next action

Do not write a paper from this run; run one bounded direct follow-up with v-floor plus scalar chunk residual inside a tiny transformer or GPT-2-small-class training loop before considering any scale-out.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer validation of v-floored chunk-scalar 8-bit AdamW
- Success threshold: Across three seeds, v-floored scalar chunk EF reaches final validation loss within 1% of FP32 AdamW and better than no-EF int8, while retaining at least 70% optimizer-state memory savings and avoiding divergence.
- Stop condition: Stop if any seed diverges from second-moment zeroing/instability, if validation loss is more than 3% worse than FP32 AdamW, or if implementation overhead removes the memory or runtime advantage.

## Evidence references

- Artifact root: `<local-path>/projects/c8bit-adamw-chunked-error-feedback-8-bit-adamw-for-gb10-adaa21bdf433`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

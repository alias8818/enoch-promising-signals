# Block-wise 8-bit AdamW with error feedback on GPT-2-small (GB10)

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `block-wise-8-bit-adamw-with-error-feedback-on-gpt-2-small-gb10-6ab75df42445`
Run ID: `block-wise-8-bit-adamw-with-error-feedback-on-gpt-2-small-gb10-6ab75df42445-20260630T030622933043+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4a963e195773

## What looked useful

Coarse 2048-element blocks diverged to NaN by step 4. Smaller 256-element blocks trained for 20 WikiText-2 steps with similar loss to AdamW, but used 1.258x AdamW optimizer-state bytes and reached only 0.387x AdamW throughput in this implementation, so the tested EF formulation did not deliver the intended practical memory benefit.

## Boundaries and scale limits

Not full GPT-2-small pretraining, not validation perplexity, not a production fused 8-bit optimizer kernel, and not a long-horizon stability result. The finding applies to this explicit EF-residual formulation and short-run behavior.

## Claim scope

Early GPT-2-small-shaped CUDA training probe on GB10 comparing PyTorch AdamW to a local block-wise uint8 AdamW with explicit full-precision error-feedback residuals, including 5-step synthetic checks and a 20-step WikiText-2 raw run at sequence length 64 and batch size 1.

## Why it stopped

Early bounded falsification: stable 256-block runs did not reduce optimizer memory and were slower than AdamW, while coarse 2048-block runs diverged almost immediately; this is not a full validation but is enough to reject the tested practical formulation.

## Recommended next action

Stop this formulation as no-paper useful signal; only revisit with a residual-compressed or residual-free compensated 8-bit design that can show actual optimizer-state memory reduction before longer GPT-2-small training.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Compressed-residual 8-bit AdamW on GPT-2-small
- Success threshold: At least 20 percent lower optimizer-state bytes than AdamW, no divergence over 100 WikiText-2 GPT-2-small-shaped steps, final loss within 2 percent of AdamW, and throughput at least 50 percent of AdamW in a non-fused reference implementation.
- Stop condition: Stop if the compressed-residual design cannot reduce optimizer-state bytes below AdamW or diverges/NaNs before 100 steps at GPT-2-small shape.

## Evidence references

- Artifact root: `<local-path>/projects/block-wise-8-bit-adamw-with-error-feedback-on-gpt-2-small-gb10-6ab75df42445`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

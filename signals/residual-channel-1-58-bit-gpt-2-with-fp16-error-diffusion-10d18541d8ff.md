# Residual-Channel 1.58-bit GPT-2 with FP16 Error Diffusion

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-1-58-bit-gpt-2-with-fp16-error-diffusion-10d18541d8ff`
Run ID: `residual-channel-1-58-bit-gpt-2-with-fp16-error-diffusion-10d18541d8ff-20260519T143511738409+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b8ef7195f471

## What looked useful

Residual channel improved validation loss versus ternary-only in both 1000-step seeds: -0.012985 and -0.022039 loss, with mean residual validation loss 2.442505 vs ternary 2.460017. Dense remained clearly better at mean validation loss 2.331531. Residual linear-weight storage was estimated at 0.213x dense FP16 vs 0.099x for ternary-only.

## Boundaries and scale limits

CPU-only tiny character-level model, 2 seeds, 1000 steps, 65-character vocabulary, not GPT-2-small, not tokenized WebText/OpenWebText, and FP16 error diffusion is represented by FP16 storage accounting for a low-rank residual channel rather than a fused hardware/kernel implementation.

## Claim scope

Tiny GPT-style character language model on Tiny Shakespeare: a trainable low-rank residual channel added to 1.58-bit ternary linear weights reproducibly improves validation loss over ternary-only, but remains worse than dense.

## Why it stopped

Proxy-scale evidence supports a small residual-over-ternary mechanism but does not validate the GPT-2-class hypothesis or close the dense baseline gap.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded action is a small GPT-2-tokenizer follow-up with residual-rank and initialization ablations before any large-scale claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual rank and initialization ablation for ternary GPT-style language models
- Success threshold: Residual model recovers at least 50% of the ternary-to-dense validation-loss gap at no more than 0.30x dense FP16 linear-weight storage, with the result holding across at least 3 seeds or a clearly stable long run.
- Stop condition: Stop if residual fails to beat ternary-only by at least 0.02 validation loss or if the required residual storage exceeds 0.30x dense FP16 linear-weight storage before recovering 50% of the dense gap.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-1-58-bit-gpt-2-with-fp16-error-diffusion-10d18541d8ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

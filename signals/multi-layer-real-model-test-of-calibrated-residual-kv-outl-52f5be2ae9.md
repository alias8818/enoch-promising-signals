# Multi-layer real-model test of calibrated residual KV outlier selectors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-layer-real-model-test-of-calibrated-residual-kv-outl-52f5be2ae9`
Run ID: `multi-layer-real-model-test-of-calibrated-residual-kv-outl-52f5be2ae9-20260523T131838140283+0000`

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

- Parent run decision: Residual-KV: 2-bit cache with FP16 outlier channels: enoch://control-plane/projects/residual-kv-2-bit-cache-with-fp16-outlier-channels-9aa9954bacd3/runs/residual-kv-2-bit-cache-with-fp16-outlier-channels-9aa9954bacd3-20260523T111544425674+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aaff3ccd450d

## What looked useful

Calibrated residual z-norm averaged 0.134 recall at a 5% selection budget across three seeds, versus random around 0.048 and the 0.35 success threshold. It beat raw residual norm in 7-9 of 12 layers but consistently lost to a position prior at 0.178-0.211 recall.

## Boundaries and scale limits

Single GPT-2-small-class model, short contexts, small real-text prompt set, KV outlier identification only; no downstream KV cache compression, quantization, eviction, perplexity, long-context, larger-model, or broad-corpus validation.

## Claim scope

On GPT-2 small with 24 calibration and 48 evaluation real-text sequences at length 96, calibrated residual z-norm weakly predicts top-5% per-layer KV-norm outlier tokens above random but fails the preset Tier 1 recall threshold and is weaker than a simple position-prior baseline.

## Why it stopped

Controlled small direct test falsified the stated Tier 1 threshold for calibrated residual z-norm KV outlier selection; this is an early direct falsification of the threshold, not a full validation of all residual/KV selector variants.

## Recommended next action

Stop this selector variant as no-paper evidence; a bounded branch should test position-aware residual selectors against position-prior and random baselines with downstream cache-quality metrics.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Position-aware residual selectors for KV outlier prediction
- Success threshold: Mean top-5% KV-outlier recall >= 0.25 and >= 20% relative improvement over position-prior-only, plus lower downstream perplexity degradation than position-prior-only at matched budget.
- Stop condition: Stop if the combined selector fails to beat position-prior-only by 10% relative on held-out KV-outlier recall or fails to improve downstream cache-quality metrics at matched budget.

## Evidence references

- Artifact root: `<local-path>/projects/multi-layer-real-model-test-of-calibrated-residual-kv-outl-52f5be2ae9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

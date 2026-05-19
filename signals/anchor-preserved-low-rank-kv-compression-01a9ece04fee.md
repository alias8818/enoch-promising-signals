# Anchor-Preserved Low-Rank KV Compression

Status: `useful_signal`
Project ID: `anchor-preserved-low-rank-kv-compression-01a9ece04fee`
Run ID: `anchor-preserved-low-rank-kv-compression-01a9ece04fee-20260517T220902477622+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/979f0a9871af

## What looked useful

A 3.125% anchor fraction was neutral at 12.5% cache budget, improved mean attention-output error by 7.7% at 25% budget, and improved it by 23.6% at 50% budget versus pure low-rank. Larger anchor fractions hurt at low budgets but still helped at 50%, indicating a real budget tradeoff rather than universal superiority.

## Boundaries and scale limits

Single GPT-2 model, four repeated text prompts, 384-token prefixes, post-hoc compression only, attention-output reconstruction metric only; no downstream perplexity, generation quality, optimized decode latency, quantization interaction, modern model family, or long-context validation.

## Claim scope

On GPT-2 post-hoc KV cache tensors at sequence length 384, preserving a small fraction of prefix/high-norm anchors exactly can reduce suffix attention-output reconstruction error versus pure low-rank compression at moderate-to-high element budgets, but the advantage disappears or reverses when anchors consume too much of a very low budget.

## Why it stopped

This run produced a bounded useful signal but not publication-grade evidence: it is a post-hoc attention reconstruction benchmark, not downstream or serving validation.

## Recommended next action

Run a medium direct confirmation with incremental decoding on GPT-2-small-class plus one modern small decoder at 1k-2k context, measuring perplexity/logit KL and attention-output error at matched element budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium decode-quality validation for anchor-preserved low-rank KV compression
- Success threshold: Anchor-preserved low-rank must improve matched-budget logit KL or attention-output error by at least 5% relative to pure low-rank and avoid worse perplexity degradation across both tested models.
- Stop condition: Stop if the tuned anchor-preserved method fails to beat pure low-rank on either model at 25% or 50% element budget, or if compression/update overhead eliminates any practical memory benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserved-low-rank-kv-compression-01a9ece04fee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

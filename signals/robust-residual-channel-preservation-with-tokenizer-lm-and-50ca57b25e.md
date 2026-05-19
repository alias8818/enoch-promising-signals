# Robust residual-channel preservation with tokenizer LM and recovery fine-tuning

Status: `useful_signal`
Project ID: `robust-residual-channel-preservation-with-tokenizer-lm-and-50ca57b25e`
Run ID: `robust-residual-channel-preservation-with-tokenizer-lm-and-50ca57b25e-20260516T202932536601+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Robust residual-channel preservation with tokenizer LM and recovery fine-tuning: internal_generated:robust-residual-channel-preservation-with-tokenizer-lm-and-50ca57b25e

## What looked useful

Across seeds 11/17/23, dense and content-only controls stayed at chance residual-bit recovery (0.5095 and 0.5058), while weak preservation, full preservation, preservation after LM-only drift, and recovery fine-tuning all reached 1.0000 residual-bit and sequence-exact recovery. Content loss and accuracy remained within noise of controls.

## Boundaries and scale limits

Small synthetic Markov-token task only: 3 seeds, 96-dim 3-layer Transformer, sequence length 32, content vocab 64, surface vocab 128. No real BPE/Unigram tokenizer, natural-language corpus, GPT-2-small-class model, compression, quantization, distillation, or long forgetting stress test was run.

## Claim scope

In a fixed-seed synthetic tokenizer-LM task where surface token parity carries independent residual payload bits, explicit residual-channel preservation and short recovery fine-tuning recover payload bits perfectly without measurable content-LM degradation relative to content-only and dense baselines.

## Why it stopped

No-paper useful signal: Tier 2 synthetic medium confirmation supports the mechanism but does not provide real-tokenizer or real-corpus evidence required for a paper-positive claim.

## Recommended next action

Run the same preservation/recovery objectives on a real tokenizer and held-out natural-language corpus with payload-bearing alternate tokenizations before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-channel preservation on real BPE tokenizations
- Success threshold: Across at least 3 fixed seeds, preservation and recovery variants achieve at least 95% residual-bit accuracy and at least 80% residual-sequence exact recovery on held-out text, while validation perplexity is no worse than 2% relative to the content-only/dense baseline.
- Stop condition: Stop as negative if residual-bit recovery remains below 80% on held-out text, if sequence-exact recovery is near zero after recovery fine-tuning, or if preservation increases validation perplexity by more than 5% relative to baseline.

## Evidence references

- Artifact root: `<local-path>/projects/robust-residual-channel-preservation-with-tokenizer-lm-and-50ca57b25e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# End-to-end GPT-2-small self-speculative decoding with trained early-exit heads

Status: `useful_signal`
Project ID: `end-to-end-gpt-2-small-self-speculative-decoding-with-trai-f29c835448`
Run ID: `end-to-end-gpt-2-small-self-speculative-decoding-with-trai-f29c835448-20260516T123253081416+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: End-to-end GPT-2-small self-speculative decoding with trained early-exit heads: internal_generated:end-to-end-gpt-2-small-self-speculative-decoding-with-trai-f29c835448

## What looked useful

Training layer-norm-plus-vocab early heads raised final-argmax agreement to about 0.275 at layer 4 and 0.375-0.382 at layer 8, with layer-8 draft-2 acceptance about 0.38-0.41 while preserving exact greedy outputs. However, best speculative throughput was about 106 tokens/sec versus about 185 tokens/sec uncached greedy and 288 tokens/sec cached greedy on the cached-baseline rerun; estimated speedups stayed below 1.0.

## Boundaries and scale limits

Tested only GPT-2 small, Wikitext-2 slices, two seeds, 24 prompts per seed, 24 generated tokens per prompt, simple Hugging Face verifier implementation, and greedy exact decoding. Not a fused serving kernel or larger-model validation.

## Claim scope

On GPT-2 small with frozen base weights, Wikitext-2 early-head training, exact greedy verification, layers 4/8, draft lengths 2/4, and two fixed seeds, trained early-exit heads create a real acceptance signal but do not deliver end-to-end self-speculative speedup over greedy GPT-2 baselines.

## Why it stopped

Medium-tier direct validation with fixed seeds, ablations, exact greedy verification, and real baselines found useful mechanism support but falsified the end-to-end speedup threshold for this implementation.

## Recommended next action

Stop this run as a no-paper negative result; the next bounded test should train acceptance-aware or distillation-to-final-argmax heads and require cached-baseline speedup before further scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Acceptance-aware GPT-2-small early-exit heads for exact self-speculative decoding
- Success threshold: Layer 8 or earlier head with exact greedy preservation, mean accepted run length at least 1.5 for draft length 4, estimated speedup above 1.0, and measured wall-clock tokens/sec exceeding cached greedy baseline by at least 10% on the same prompts.
- Stop condition: Stop negative if trained acceptance-aware heads fail to exceed mean accepted run length 1.0 or fail to beat cached greedy baseline on two fixed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-gpt-2-small-self-speculative-decoding-with-trai-f29c835448`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

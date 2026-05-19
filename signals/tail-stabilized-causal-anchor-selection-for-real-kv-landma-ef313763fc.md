# Tail-Stabilized Causal Anchor Selection for Real-KV Landmark Pooling

Status: `useful_signal`
Project ID: `tail-stabilized-causal-anchor-selection-for-real-kv-landma-ef313763fc`
Run ID: `tail-stabilized-causal-anchor-selection-for-real-kv-landma-ef313763fc-20260517T025053301303+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Tail-Stabilized Causal Anchor Selection for Real-KV Landmark Pooling: internal_generated:tail-stabilized-causal-anchor-selection-for-real-kv-landma-ef313763fc

## What looked useful

Causal tail-attention mass is a strong real-KV landmark anchor signal, cutting mean relative attention-output error by about 85% versus uniform/random/norm controls. The stabilization component is not supported: tail_stable is consistently about 0.10% to 0.19% worse than tail_top across budgets in paired comparisons.

## Boundaries and scale limits

Validation covered GPT-2 small, WikiText-2, 768-token contexts, all 12 layers, 3 seeds, 64 contexts per seed, budgets 16/32/64, attention-output distortion, and mass preservation. It did not test end-to-end perplexity/generation, production decode latency, larger models, other datasets, or alternative stabilization formulas.

## Claim scope

On pretrained GPT-2 small real Q/K/V tensors from WikiText-2 test contexts, causal tail-attention anchor selection greatly reduces landmark-pooling attention-output distortion versus uniform, random, and K-norm controls, but the tested tail-stabilized scoring does not improve over a simpler raw tail-attention top-mass ablation.

## Why it stopped

Bounded direct validation produced a mixed useful signal but falsified the stabilizer-specific improvement against the required tail_top ablation; this is not paper-ready for the original claim.

## Recommended next action

Stop the tail-stabilized claim; if continuing, branch to an end-to-end small-LM test of the simpler causal tail_top landmark selector against uniform pooling and no-compression baselines.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: End-to-End Causal Tail-Mass Landmark Pooling Without Stabilization
- Success threshold: tail_top must reduce perplexity or next-token KL degradation by at least 20% versus uniform pooling at the same KV budget while preserving the attention-output error advantage observed here.
- Stop condition: Stop if tail_top does not beat uniform pooling on end-to-end next-token KL/perplexity at two KV budgets or if runtime overhead removes the practical memory benefit.

## Evidence references

- Artifact root: `<local-path>/projects/tail-stabilized-causal-anchor-selection-for-real-kv-landma-ef313763fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

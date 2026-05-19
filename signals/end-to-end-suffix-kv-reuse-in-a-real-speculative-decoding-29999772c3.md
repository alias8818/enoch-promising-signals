# End-to-End Suffix KV Reuse In A Real Speculative Decoding Loop

Status: `useful_signal`
Project ID: `end-to-end-suffix-kv-reuse-in-a-real-speculative-decoding-29999772c3`
Run ID: `end-to-end-suffix-kv-reuse-in-a-real-speculative-decoding-29999772c3-20260515T210723327192+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: End-to-End Suffix KV Reuse In A Real Speculative Decoding Loop: internal_generated:end-to-end-suffix-kv-reuse-in-a-real-speculative-decoding-29999772c3

## What looked useful

Exact intra-loop suffix KV reuse appears structurally unavailable in ordinary autoregressive speculative decoding because the committed prefix advances every verification. Token-suffix repeats exist, but ignoring prefix identity is not a valid KV reuse rule and showed material logit disagreement.

## Boundaries and scale limits

Tested distilgpt2 with sshleifer/tiny-gpt2 and a distilgpt2-as-draft control for 48 generated tokens per prompt, 3 fixed seeds, prompt variation, and gamma values 4 and 8. Did not test stochastic sampling, 7B+ models, long serving traces, or multi-request prefix-cache workloads.

## Claim scope

In a small-model greedy speculative decoding loop using real Hugging Face causal-LM KV caches, correctness-preserving target-side suffix KV reuse had zero exact prefix+suffix hits across both low-acceptance and high-acceptance controls; prefix-agnostic suffix reuse produced substantial logit drift.

## Why it stopped

Moderate local direct evidence falsified the correctness-preserving reuse opportunity in a real speculative loop: exact reuse was 0/1152 in the main run and 0/96 in the high-acceptance control, while prefix-agnostic suffix reuse showed unsafe logit drift.

## Recommended next action

Stop this intra-loop suffix-KV reuse line unless a new mechanism can preserve or reconstruct prefix-conditioned KVs; do not scale the current exact-suffix scheme.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-suffix-kv-reuse-in-a-real-speculative-decoding-29999772c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

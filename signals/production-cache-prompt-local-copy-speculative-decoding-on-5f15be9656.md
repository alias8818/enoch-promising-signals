# Production-cache prompt-local copy speculative decoding on broader extractive QA

Status: `useful_signal`
Project ID: `production-cache-prompt-local-copy-speculative-decoding-on-5f15be9656`
Run ID: `production-cache-prompt-local-copy-speculative-decoding-on-5f15be9656-20260518T185805143683+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Production-cache prompt-local copy speculative decoding on broader extractive QA: internal_generated:production-cache-prompt-local-copy-speculative-decoding-on-5f15be9656

## What looked useful

Prompt-local copy drafting did not materially accelerate exact speculative decoding in the validated setting. Lexical copy accepted roughly 0.5 tokens per example, reduced target calls by about 1.9%, and did not significantly beat random same-prompt copying. Even a gold-answer oracle span only reduced target calls by about 3.7%, suggesting weak copy alignment in the target LM continuation.

## Boundaries and scale limits

Only SQuAD was fully runnable from the local dataset cache; squad_v2, adversarial_qa, and hotpot_qa were not materialized and online dataset resolution hung. Larger/instruction-tuned causal targets were not validated; serving wall-clock speedup was not claimed.

## Claim scope

Exact speculative decoding on 100 fixed-seed SQuAD validation prompts with distilgpt2 as the target LM: a production-style lexical prompt-local copy draft preserves greedy output but yields only about 1.9% mean target decode-call reduction, barely above random and shuffled controls.

## Why it stopped

Bounded local validation on real SQuAD prompts directly tested exact speculative acceptance and target-call savings; the production-style copy draft failed to clear a practical acceleration threshold and the oracle upper bound was also weak.

## Recommended next action

Stop this branch as a useful negative/early falsification; any future retry should first require a cache-exact implementation for the intended target model family and locally materialized multi-dataset extractive QA evidence.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/production-cache-prompt-local-copy-speculative-decoding-on-5f15be9656`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

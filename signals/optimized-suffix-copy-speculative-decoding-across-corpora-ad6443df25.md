# Optimized suffix-copy speculative decoding across corpora and GPT-2 model sizes

Status: `useful_signal`
Project ID: `optimized-suffix-copy-speculative-decoding-across-corpora-ad6443df25`
Run ID: `optimized-suffix-copy-speculative-decoding-across-corpora-ad6443df25-20260516T141702916106+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Optimized suffix-copy speculative decoding across corpora and GPT-2 model sizes: internal_generated:optimized-suffix-copy-speculative-decoding-across-corpora-ad6443df25

## What looked useful

Suffix-copy proposals substantially outperformed prompt-unigram and prompt-mode baselines: best pooled target-forward speedups were 3.1093x for distilgpt2, 2.1041x for gpt2, and 1.8028x for bounded gpt2-medium, with all float32 rows exactly equivalent to greedy decoding.

## Boundaries and scale limits

This run measured target-forward-count speedup, not production KV-cache wall-clock serving speed. Corpora were small public text sources; generation was greedy only; gpt2-medium used fewer prompts/tokens than distilgpt2 and gpt2; no 7B-class or datacenter-scale validation was performed.

## Claim scope

On four modest public text corpora, a suffix-copy draft policy improved target-verified greedy speculative decoding forward-count efficiency for distilgpt2, gpt2, and a bounded gpt2-medium run, with exact float32 equivalence to greedy target output.

## Why it stopped

Direct local evidence supports the mechanism but falls short of Tier 4 paper-readiness because it lacks production serving latency/throughput, large benchmark coverage, and broader model-scale robustness.

## Recommended next action

Stop this follow-up at depth 4: preserve the useful mechanism evidence, but do not recommend another chained follow-up or paper writing without a separate production KV-cache wall-clock benchmark campaign.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/optimized-suffix-copy-speculative-decoding-across-corpora-ad6443df25`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

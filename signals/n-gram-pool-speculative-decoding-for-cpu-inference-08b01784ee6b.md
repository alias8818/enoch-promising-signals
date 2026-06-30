# N-gram Pool Speculative Decoding for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-pool-speculative-decoding-for-cpu-inference-08b01784ee6b`
Run ID: `n-gram-pool-speculative-decoding-for-cpu-inference-08b01784ee6b-20260604T134843096414+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/45c91285252e

## What looked useful

The mechanism is worth a bounded direct transformer test because accepted local n-gram continuations can substantially reduce verifier calls, but only if batched target verification is expensive enough to amortize draft overhead.

## Boundaries and scale limits

Proxy-only evidence: no real transformer, tokenizer, KV cache, quantization, sampling-quality control, or production CPU serving stack was tested. Runs were short, single-process NumPy experiments on 8 visible CPU cores.

## Claim scope

In a character-level Markov/NumPy CPU-cost proxy on Tiny Shakespeare, an n-gram-pool draft proposer reduced target verifier calls by 71%-86% and produced up to 4.09x wall-clock speedup when target calls had nontrivial simulated CPU cost; it was slower when target cost was zero.

## Why it stopped

Proxy-only useful signal, not full validation: the target model was synthetic/Markov and the zero-load control showed overhead can dominate when target calls are cheap.

## Recommended next action

Stop this run as no-paper proxy evidence; next concrete action is a bounded CPU transformer follow-up with KV-cache-aware verification and a >=1.25x end-to-end throughput success threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU Transformer Test of N-gram Pool Speculative Decoding
- Success threshold: At least 1.25x median tokens/s improvement over greedy decoding with byte-identical greedy output on the benchmark prompts and no more than 10% p95 latency regression.
- Stop condition: Stop as negative if accept rate is below 35%, target-call reduction is below 30%, or end-to-end throughput is <=1.05x after draft lookup optimization.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-pool-speculative-decoding-for-cpu-inference-08b01784ee6b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

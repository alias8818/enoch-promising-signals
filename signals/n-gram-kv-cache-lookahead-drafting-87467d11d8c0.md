# N-gram KV Cache Lookahead Drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-kv-cache-lookahead-drafting-87467d11d8c0`
Run ID: `n-gram-kv-cache-lookahead-drafting-87467d11d8c0-20260604T001513474828+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f1841f57fa90

## What looked useful

N-gram KV-cache lookahead drafting produced exact greedy outputs and measured speedups of 3.29x on distilgpt2 and 1.55x on gpt2, with forward-call reductions of 68.7% and 30.0% respectively. The gain depends on repetitive generated continuations and needs an adaptive fallback policy for broader use.

## Boundaries and scale limits

Tested only sshleifer/tiny-gpt2 smoke plus 8 prompts each for distilgpt2 and gpt2, 64 generated tokens per prompt, greedy decoding only, no production serving engine, no batching, no sampling, no long-context workload, and no 1B+/7B+ model validation.

## Claim scope

In a simple Transformers greedy-decoding loop on GB10, n-gram prompt/lookback drafting with KV-cache verification preserved exact greedy output and reduced forward calls for small GPT-2-family models on a small WikiText prompt sample.

## Why it stopped

Bounded local evidence supports the mechanism but is too small and too serving-unrealistic for a paper-positive claim.

## Recommended next action

Stop this worker run as a no-paper useful signal; next bounded work should compare this heuristic against prompt-lookup/speculative decoding baselines in an optimized serving stack on a larger prompt suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive N-gram Lookahead in a Serving Baseline
- Success threshold: Exact greedy output match on all prompts, at least 1.2x p50 latency improvement over greedy decoding, and no p90 latency regression larger than 5% versus the best baseline.
- Stop condition: Stop if exactness fails, if acceptance is below 25% after policy tuning, or if p50 speedup remains below 1.1x on two model/prompt configurations.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-kv-cache-lookahead-drafting-87467d11d8c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

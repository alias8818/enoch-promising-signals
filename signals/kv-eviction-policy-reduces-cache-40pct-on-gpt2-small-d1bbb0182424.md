# KV Eviction Policy Reduces Cache 40pct on GPT2 Small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-eviction-policy-reduces-cache-40pct-on-gpt2-small-d1bbb0182424`
Run ID: `kv-eviction-policy-reduces-cache-40pct-on-gpt2-small-d1bbb0182424-20260607T033338838596+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae5d5ea133b6

## What looked useful

Pure recent-window eviction reached the cache target but badly degraded perplexity (+1.264 NLL on 8 blocks). Adding 64 prefix/sink tokens within the same 614-token budget rescued quality on a 32-block confirmation (+0.027 NLL, +2.31% aggregate relative PPL) while preserving 39.98% peak KV reduction.

## Boundaries and scale limits

Single model (gpt2/GPT-2-small), single dataset stream (WikiText-2 test), 32 blocks, fp16 inference, batch size 1, max GPT-2 context length 1024, no generation-quality evaluation, no latency benchmark, no larger-model or long-context validation, and only a minimal policy grid.

## Claim scope

On GPT-2-small teacher-forced next-token evaluation over 32 WikiText-2 test blocks of 1024 tokens, a sink-plus-recent KV eviction policy retaining the first 64 tokens and latest 550 tokens achieved about 40% peak KV-cache token/element reduction with +0.027 mean NLL and +2.31% aggregate relative perplexity versus full KV cache.

## Why it stopped

This run produced a useful bounded signal but not publication-grade evidence; robustness, policy sensitivity, generation behavior, and broader baselines remain untested.

## Recommended next action

Run a bounded deepen follow-up that sweeps sink-token budgets and evaluates at least one additional corpus plus generation samples; stop paper consideration if +0.10 NLL or +10% relative PPL is exceeded at the 40% peak KV reduction target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sink-token sensitivity for 40% GPT-2 KV cache eviction
- Success threshold: At least one sink-plus-recent policy keeps peak KV reduction at about 40% with mean NLL delta <= 0.10 and relative PPL delta <= 10% on each corpus, without obvious generation regressions in sampled prompts.
- Stop condition: Stop if all sink budgets exceed +0.10 mean NLL or +10% relative PPL on any corpus at the 40% peak KV target, or if generation samples show severe coherence regressions despite acceptable likelihood.

## Evidence references

- Artifact root: `<local-path>/projects/kv-eviction-policy-reduces-cache-40pct-on-gpt2-small-d1bbb0182424`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

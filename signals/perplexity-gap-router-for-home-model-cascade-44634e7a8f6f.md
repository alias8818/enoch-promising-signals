# Perplexity-gap router for home model cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-gap-router-for-home-model-cascade-44634e7a8f6f`
Run ID: `perplexity-gap-router-for-home-model-cascade-44634e7a8f6f-20260522T154646401537+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bab4ca2ce6b9

## What looked useful

The prefix perplexity-gap score correlated with oracle target improvement at about 0.305 in the distilgpt2->gpt2 run and 0.309 in the tiny-gpt2->distilgpt2 ablation. At 50% routing it beat random by 0.0637 NLL in the primary run and 0.1023 NLL in the weak-to-strong ablation.

## Boundaries and scale limits

Tested only GPT-2-family causal LMs on one public text corpus with continuation NLL as the target metric. It does not validate instruction-answer quality, real user requests, latency/cost tradeoffs, calibrated production thresholds, larger home models, or broad multi-domain robustness.

## Claim scope

On a local Tiny Shakespeare continuation-likelihood proxy, routing by the prefix perplexity gap between a smaller and larger causal LM identifies higher-value fallback calls better than random routing and small-model prefix uncertainty at matched route fractions.

## Why it stopped

Proxy evidence supports the routing mechanism but is not direct or broad enough for a paper-positive claim.

## Recommended next action

Run a bounded deepen test on instruction-style prompts with answer-quality labels or judge scores, using a validation-calibrated threshold and reporting quality retained versus fallback-call rate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Instruction-quality validation for perplexity-gap home-model routing
- Success threshold: At matched fallback-call rates, the gap router retains at least 95% of all-fallback judged quality while reducing fallback calls by at least 30%, and beats both random and small-model uncertainty routing by at least 2 percentage points quality retained.
- Stop condition: Stop if the gap router fails to beat both baselines on held-out prompts at two or more route fractions, or if quality retained drops below 90% before reaching 30% fallback-call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-gap-router-for-home-model-cascade-44634e7a8f6f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

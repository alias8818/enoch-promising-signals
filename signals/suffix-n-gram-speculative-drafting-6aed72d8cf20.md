# Suffix N-Gram Speculative Drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-n-gram-speculative-drafting-6aed72d8cf20`
Run ID: `suffix-n-gram-speculative-drafting-6aed72d8cf20-20260529T083200938613+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5c0c56bfae25

## What looked useful

Prompt-local suffix lookup is the promising part of suffix n-gram speculative drafting: it averaged 27.0% target-call reduction and 1.37 tokens per target call, while unigram control gave 0% and corpus suffix tables barely helped. This supports a cheap follow-up focused on optimized latency and context stratification, not a paper now.

## Boundaries and scale limits

Only distilgpt2, WikiText-2, two random seeds, 32 prompts per seed, 32 generated tokens per prompt, and simple full-context block verification were tested. Wall-clock serving speed, KV-cache implementation overhead, sampling, larger models, longer contexts, and broader corpora were not validated.

## Claim scope

In a bounded local greedy-decoding experiment with distilgpt2 on WikiText-2, live prompt-suffix n-gram lookup reduced estimated target-model forward calls by 25.4-28.6% versus one-token greedy decoding over two 32-prompt seeds; static corpus suffix n-grams were weak at 2.0-5.6% in the same setup.

## Why it stopped

Evidence is bounded and partly proxy-like: target-call reduction was directly measured, but production latency and larger-model robustness were not.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should implement KV-cache prompt-suffix speculative verification and measure wall-clock latency on copy-heavy versus ordinary contexts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache latency validation for prompt-suffix speculative drafting
- Success threshold: At least 15% median wall-clock latency reduction on copy-heavy contexts, no more than 5% median latency regression on ordinary contexts, and positive target-call reduction in both prompt shards.
- Stop condition: Stop as negative if optimized verification overhead removes the target-call advantage or if copy-heavy latency gain is below 10%.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-n-gram-speculative-drafting-6aed72d8cf20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

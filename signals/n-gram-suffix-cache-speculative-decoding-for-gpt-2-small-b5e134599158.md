# N-gram suffix cache speculative decoding for GPT-2-small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-suffix-cache-speculative-decoding-for-gpt-2-small-b5e134599158`
Run ID: `n-gram-suffix-cache-speculative-decoding-for-gpt-2-small-b5e134599158-20260531T131941200993+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/eeb1ceb17c75

## What looked useful

The mechanism is supported locally: suffix-cache draft tokens were sometimes accepted by GPT-2-small greedy verification, producing exact-match output and fewer target forwards. Benefit is uneven across prompts and appears workload-dependent.

## Boundaries and scale limits

Single model, single dataset family, greedy decoding only, 32 prompts, 2,048 generated tokens, prototype PyTorch implementation without production KV-cache serving integration or comparisons to learned draft/prompt-lookup baselines.

## Claim scope

In a bounded GPT-2-small greedy-decoding test on Wikitext-2 validation prompts, a prompt-only n-gram suffix cache with exact speculative verification preserved greedy outputs exactly while reducing target model forward calls by 22.5% over 2,048 generated tokens.

## Why it stopped

Evidence is bounded and useful but not paper-ready because it is a small GPT-2-small/Wikitext-2 greedy-only prototype rather than robust production-serving or multi-domain validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should compare prompt-only suffix-cache speculation against KV-cache greedy generation and prompt-lookup baselines on multiple domains.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-only n-gram suffix-cache speculation with KV-cache serving baselines
- Success threshold: At least 15% aggregate target-forward reduction and no aggregate wall-clock regression versus optimized KV-cache greedy decoding, with exact output equivalence on all evaluated prompts.
- Stop condition: Stop as negative if target-forward reduction is below 10%, exactness fails, or KV-cache wall-clock runtime regresses by more than 5% on two or more domains.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-cache-speculative-decoding-for-gpt-2-small-b5e134599158`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Prompt-Suffix N-gram Speculative Decoding for GPT-2

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-suffix-n-gram-speculative-decoding-for-gpt-2-7f97ea8c0ed7`
Run ID: `prompt-suffix-n-gram-speculative-decoding-for-gpt-2-7f97ea8c0ed7-20260604T071314765174+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ede08e12091f

## What looked useful

Prompt/history suffix n-gram drafts can reduce target model calls and speed exact GPT-2-small greedy decoding when verification is KV-cache aware. The same idea is slower than greedy decoding if verification reprocesses the full context, so cache handling is central to viability.

## Boundaries and scale limits

Single small GPT-2 model, one dataset split, 16 prompts, greedy decoding only, local GB10 GPU, no batched serving, no sampling, no larger models, and no production kernel optimization.

## Claim scope

On 16 WikiText-2 prompts with 256-token prompts and 64-token greedy continuations, GPT-2 small on GB10 achieved exact greedy-equivalent output with a KV-cache prompt-suffix n-gram speculative verifier and improved aggregate throughput from 266.4 tokens/s to 492.7 tokens/s at draft_len=16, a 1.85x speedup.

## Why it stopped

The run produced a useful scoped mechanism signal but not publication-grade evidence; broader claims need multi-domain, multi-model, and serving-style robustness tests.

## Recommended next action

Stop this run as no-paper useful evidence; the concrete next local action is a bounded robustness benchmark across several corpora, prompt lengths, and GPT-2 sizes using the cached verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robustness benchmark for cached prompt-suffix n-gram decoding
- Success threshold: Across at least 4 domains, 3 prompt lengths, and GPT-2-small plus GPT-2-medium, median aggregate speedup is at least 1.3x with all outputs exactly matching greedy decoding.
- Stop condition: Stop if any model/domain/prompt-length group has exact-match failures, or if aggregate speedup is below 1.1x for two or more domains after tuning draft length over 2, 4, 8, and 16.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-suffix-n-gram-speculative-decoding-for-gpt-2-7f97ea8c0ed7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

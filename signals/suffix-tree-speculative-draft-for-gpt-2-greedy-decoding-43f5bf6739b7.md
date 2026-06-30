# Suffix-tree speculative draft for GPT-2 greedy decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-draft-for-gpt-2-greedy-decoding-43f5bf6739b7`
Run ID: `suffix-tree-speculative-draft-for-gpt-2-greedy-decoding-43f5bf6739b7-20260531T190731971637+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/262dd014414d

## What looked useful

Suffix-history drafting is mechanically valid and exact under verification. Natural-text acceptance was modest (0.300 mean draft-token acceptance, 1.14-1.19x wall-clock speedup), while synthetic repetition reached 1.000 acceptance and about 2.14x speedup. Correct implementations must avoid live-cache mutation during draft verification.

## Boundaries and scale limits

Tested 30 natural prompts and 30 synthetic repetition prompts at 96 prompt tokens and 64 generated tokens, plus 12-prompt draft-length ablations. Did not test larger corpora, long contexts, optimized non-copying cache forks, batch serving, or stronger learned/retrieval drafters.

## Claim scope

Local GPT-2 small greedy decoding experiments on WikiText-2 validation prompts show exact suffix-history speculative decoding can preserve baseline tokens and produce modest natural-text speedups, with strong speedups only on repetitive synthetic prompts.

## Why it stopped

The bounded direct GPT-2 evidence supports the mechanism but shows only modest, prompt-sensitive natural-text speedup and lacks the optimized implementation and larger controls needed for a paper claim.

## Recommended next action

Stop this run as no-paper useful signal; next, implement an optimized non-copying cache fork/crop path and benchmark at least 500 natural prompts with controls before reconsidering paper viability.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized cache-fork suffix-history drafting on larger GPT-2 prompt sets
- Success threshold: Exact token equality on all prompts, at least 1.25x wall-clock speedup overall or on a predeclared high-repetition stratum, and no more than 5% slowdown on the remaining natural prompts.
- Stop condition: Stop if optimized natural-text speedup remains below 1.15x overall and prompt strata cannot isolate a predeclared useful regime.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-draft-for-gpt-2-greedy-decoding-43f5bf6739b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

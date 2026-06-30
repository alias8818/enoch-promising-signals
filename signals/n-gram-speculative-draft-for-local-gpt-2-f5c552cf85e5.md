# N-gram Speculative Draft for Local GPT-2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-local-gpt-2-f5c552cf85e5`
Run ID: `n-gram-speculative-draft-for-local-gpt-2-f5c552cf85e5-20260528T133613267013+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/093bcd84ab6e

## What looked useful

N-gram prompt lookup is a plausible exact drafting mechanism when GPT-2 repeats context spans: full-context verification matched greedy output in all trials, averaged 5.115x speedup versus full-context greedy, reduced target forwards by 73.4%, and accepted 80.9% of drafted tokens. However, the cached implementation failed exactness, making this no-paper evidence until the cache path is fixed.

## Boundaries and scale limits

The validated path recomputes full context and is not a production cached-serving implementation. The manual KV-cache speculative path diverged from cached greedy on three of four prompts, so cached local serving acceleration is not established. Prompts were hand-written, short, greedy-only, and limited to GPT-2 small.

## Claim scope

On GPT-2 small running locally on CUDA, prompt-local n-gram drafting preserved exact greedy output and reduced target calls in a conservative full-context verifier across four hand-written 64-token prompt trials, with strongest gains on copy-like and code-pattern prompts.

## Why it stopped

Mechanism supported only in a conservative full-context proxy; the direct cached serving path failed exactness, so a production acceleration claim would be premature.

## Recommended next action

Stop this run as a useful no-paper signal; next, implement a cache-correct verifier and prove stepwise equivalence against cached greedy before measuring latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-correct n-gram speculative verifier for GPT-2 greedy decoding
- Success threshold: All cached speculative outputs exactly match cached greedy on at least the four current prompts and achieve at least 1.2x mean wall-clock speedup with at least 30% target-forward reduction on the repetitive prompt subset.
- Stop condition: Stop as negative if any prompt diverges from cached greedy after cache-position fixes and API-level generation/cache validation, or if exact cached speculation is slower than cached greedy on the repetitive subset.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-local-gpt-2-f5c552cf85e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

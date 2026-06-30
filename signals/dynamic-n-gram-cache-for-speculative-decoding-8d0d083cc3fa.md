# Dynamic n-gram cache for speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dynamic-n-gram-cache-for-speculative-decoding-8d0d083cc3fa`
Run ID: `dynamic-n-gram-cache-for-speculative-decoding-8d0d083cc3fa-20260608T223915352511+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0547e56fa3bc

## What looked useful

Dynamic n-gram caches consistently beat static warmup-only caches and random controls on repeated public text traces. Best aggregate dynamic configuration reached 1.0457x optimistic target-call reduction; best individual trace reached 1.0730x. The signal supports the mechanism but is too modest and too proxy-bound for a paper.

## Boundaries and scale limits

Trace-only proxy: no live LLM, no tokenizer/model distribution match, no wall-clock serving loop, no GPU/model verifier, and no comparison to neural speculative drafters.

## Claim scope

On three public text traces with word/punctuation tokenization, 10k warmup tokens, up to 20k eval tokens, draft length 8, and bounded dynamic n-gram caches, online cache updates improve exact-token speculative draft acceptance over static warmup-only caches, but only produce modest optimistic target-call reductions.

## Why it stopped

Closed as no-paper useful signal: the bounded trace proxy supports the mechanism but shows only modest optimistic verifier-call reductions and lacks direct LLM serving evidence.

## Recommended next action

Implement the dynamic cache as a prompt-lookup-style drafter inside a small LLM generation loop and require at least 1.10x measured tokens/sec over autoregressive decoding on repeated-prompt workloads before spending larger scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LLM serving test for dynamic n-gram speculative cache
- Success threshold: Mean measured throughput at least 1.10x over autoregressive decoding on repeated-prompt workloads, with no more than 5% slowdown on the low-repetition control.
- Stop condition: Stop if measured throughput is below 1.05x on repeated-prompt workloads or if drafter overhead erases the trace-level verifier-call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-n-gram-cache-for-speculative-decoding-8d0d083cc3fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

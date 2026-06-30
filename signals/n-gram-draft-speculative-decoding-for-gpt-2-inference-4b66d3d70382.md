# N-gram draft speculative decoding for GPT-2 inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-draft-speculative-decoding-for-gpt-2-inference-4b66d3d70382`
Run ID: `n-gram-draft-speculative-decoding-for-gpt-2-inference-4b66d3d70382-20260524T083503296929+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/868b1785ee47

## What looked useful

Exact target verification makes n-gram draft decoding output-equivalent to greedy GPT-2 while reducing target calls in repetition-prone continuations; acceptance and benefit degrade on the varied low-repeat control, especially for longer n-grams.

## Boundaries and scale limits

Short 64-token continuations, three hand-written prompt cases, greedy decoding only, GPT-2 small only, no production KV-cache verifier, no batched serving, no broad corpus benchmark, and no comparison against optimized prompt-lookup/speculative-decoding implementations.

## Claim scope

On a bounded GPT-2-small greedy-decoding probe with three short local prompts, n-gram/prompt-lookup drafts preserved exact greedy output and reduced target-model forward calls by 72.9% to 84.4% on average across tested configurations.

## Why it stopped

Bounded local evidence supports the mechanism but is not publication-grade because timing uses a simple full-context verifier and the prompt suite is too small.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded KV-cache implementation and benchmark on a real prompt corpus before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram draft verifier for GPT-2 prompt-lookup decoding
- Success threshold: Exact-match rate 100% for greedy decoding and at least 20% median end-to-end latency improvement over a KV-cache greedy baseline without worse p95 latency on the benchmark.
- Stop condition: Stop as negative if exactness fails, median latency improvement is below 10%, or p95 latency regresses by more than 10% after implementation-level tuning.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-for-gpt-2-inference-4b66d3d70382`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

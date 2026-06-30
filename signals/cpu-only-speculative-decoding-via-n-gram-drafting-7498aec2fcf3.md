# CPU-Only Speculative Decoding via N-Gram Drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-only-speculative-decoding-via-n-gram-drafting-7498aec2fcf3`
Run ID: `cpu-only-speculative-decoding-via-n-gram-drafting-7498aec2fcf3-20260605T092024021998+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/d8e1b158b562

## What looked useful

N-gram drafting produced exact-match speedups on CPU: distilgpt2 draft_len=8 improved mean token/s by 2.25x on a repeated prompt, 2.33x on a repeated code prompt, and 1.30x on a prose prompt, with 46.9-73.5% fewer forward calls. A cache-cropping repair was required for exactness with mutable DynamicCache.

## Boundaries and scale limits

Only two small Hugging Face decoder models were tested; prompts were three hand-written short prompts; generation lengths were 48-96 tokens; decoding was greedy only; no batching, sampling, long-context, production serving, or 7B+ model validation was performed.

## Claim scope

Exact greedy CPU decoding with n-gram drafts can reduce target-model forward calls and improve token/s on short repeated completions for sshleifer/tiny-gpt2 and distilgpt2, while preserving token-for-token equality with the baseline decoder.

## Why it stopped

No-paper useful signal: the local exact-decoding mechanism is supported, but evidence is short-run and repetition-heavy rather than publication-grade broad validation.

## Recommended next action

Run a bounded corpus-level CPU benchmark on distilgpt2 or GPT-2-small with natural/code prompts grouped by repetition density, and require exact greedy equality plus median token/s improvement before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-Level CPU N-Gram Drafting Benchmark by Repetition Density
- Success threshold: Median token/s speedup of at least 1.15x in the high-repetition bucket with exact equality and no more than 5% median slowdown in the low-repetition bucket.
- Stop condition: Stop if exact equality fails after cache repair, or if high-repetition median speedup is below 1.05x while low-repetition prompts show slowdown.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-only-speculative-decoding-via-n-gram-drafting-7498aec2fcf3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

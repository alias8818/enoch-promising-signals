# Lossless N-Gram Speculative Decoding on CPU for Small Transformers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lossless-n-gram-speculative-decoding-on-cpu-for-small-transformers-ece149137d3a`
Run ID: `lossless-n-gram-speculative-decoding-on-cpu-for-small-transformers-ece149137d3a-20260525T221521025183+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e67dcf88cc54

## What looked useful

Exact n-gram speculative decoding is viable as a narrow mechanism for repeated local spans: distilgpt2 reduced target decode calls from 256 to 129 with max draft 8 and preserved exact greedy outputs. Plain controls showed only about 1.04x mean speedup and no meaningful call reduction, limiting the generality.

## Boundaries and scale limits

Tested only sshleifer/tiny-gpt2 smoke and distilgpt2 on 8 hand-written prompts of 32 generated tokens, 4 CPU threads, greedy decoding, local cached models. Did not test larger models, sampling, natural corpora, chat workloads, server batching, or optimized cache slicing.

## Claim scope

On CPU greedy decoding for small HuggingFace GPT-2-family Transformers, prompt/history n-gram drafting can be lossless and reduce wall-clock latency when prompts contain repeated local spans; in this run distilgpt2 reached 1.51x overall speedup across a mixed 8-prompt suite and 2.26x mean speedup on repeated-span prompts with zero token mismatches.

## Why it stopped

Bounded direct evidence supports the mechanism but not a broad or paper-ready claim; controls show negligible benefit without repeated local spans.

## Recommended next action

Stop as no-paper useful signal; the next bounded test should use a natural document/code prompt suite to estimate how often repeated local spans create real CPU speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-suite lossless n-gram speculative decoding frequency test
- Success threshold: Zero token mismatches and at least 1.15x median wall-clock speedup with at least 20% target-call reduction on realistic repeated-span strata, without more than 5% slowdown on non-repetitive controls.
- Stop condition: Stop if natural prompts show median speedup below 1.05x or any exactness mismatch that cannot be traced to a bug.

## Evidence references

- Artifact root: `<local-path>/projects/lossless-n-gram-speculative-decoding-on-cpu-for-small-transformers-ece149137d3a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

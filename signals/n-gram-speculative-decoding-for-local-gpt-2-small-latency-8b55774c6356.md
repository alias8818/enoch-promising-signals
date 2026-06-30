# N-gram speculative decoding for local GPT-2-small latency

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-for-local-gpt-2-small-latency-8b55774c6356`
Run ID: `n-gram-speculative-decoding-for-local-gpt-2-small-latency-8b55774c6356-20260530T064352845811+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7f71c05face3

## What looked useful

The visible-context n-gram draft mechanism can reduce target forward calls on locally repetitive GPT-2-small generations: mean calls/token dropped from 1.016 to 0.434 and mean acceptance was 0.924 in exact float32. The same setup exposed an fp16 exactness hazard from batched-vs-sequential argmax drift.

## Boundaries and scale limits

Only GPT-2-small, greedy decoding, 64-token continuations, four hand-written prompt families, three repeats, one local GB10, Python implementation. fp16 did not preserve exact greedy equivalence on wiki/code prompts, and no larger corpus, sampling mode, serving concurrency, or optimized implementation was tested.

## Claim scope

On GB10 with GPT-2-small, exact float32 greedy decoding over four short prompt families, a Python n=3/max-draft=4 visible-context n-gram speculative decoder matched greedy outputs and improved mean throughput from 307.3 to 685.6 tokens/s.

## Why it stopped

No-paper useful signal: the exact float32 local benchmark supports the mechanism, but the prompt set is too small and fp16 exactness is mixed, so this is not publication-grade evidence.

## Recommended next action

Stop paper pursuit for this run; next useful action is a bounded corpus-level follow-up with dtype-specific exactness checks and an optimized cache-safe implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-level exactness and latency study for n-gram speculative GPT-2-small decoding
- Success threshold: Float32 exact-match failures are zero, median speedup is at least 1.2x over greedy, and the p10 speedup is at least 0.95x on the diverse prompt corpus.
- Stop condition: Stop if exact float32 failures occur after cache fixes, or if median speedup is below 1.0x with acceptance below 0.5 across the corpus.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-local-gpt-2-small-latency-8b55774c6356`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

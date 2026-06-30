# Suffix-Tree N-Gram Draft Speculative Decoding vs No-Spec Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-n-gram-draft-speculative-decoding-vs-no-spec-baseline-d35428b095ef`
Run ID: `suffix-tree-n-gram-draft-speculative-decoding-vs-no-spec-baseline-d35428b095ef-20260620T225532101454+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/330adaeef2cf

## What looked useful

Suffix/ngram drafting is promising for repetitive continuations: warmed repetition suite mean speedup 2.40x, median speedup 2.77x, target forwards reduced 86.6%, exact output match. Low-repetition control was net slower: mean speedup 0.93x, median 0.97x, despite 64.6% fewer target forwards, because draft chunks averaged only 2 tokens.

## Boundaries and scale limits

Small local benchmark only: distilgpt2, 8 prompts per suite, 96 generated tokens, greedy decoding, fp16 CUDA on GB10, simple rebuilt ngram index rather than optimized suffix tree, no sampling, no batched serving, no 1B+/7B+ model validation.

## Claim scope

On distilgpt2 greedy decoding on GB10, prompt-local suffix/ngram drafting produced exact greedy-equivalent output and accelerated repetition-friendly prompts, but did not broadly accelerate low-repetition prompts.

## Why it stopped

Mixed small-scale evidence: useful mechanism signal on repetitive prompts, but low-repetition controls were slightly slower and the validation is not broad or optimized enough for a paper.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded action is to test adaptive gating that only enables suffix/ngram verification when expected draft length is high enough to beat verification overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Gating for Suffix-NGram Speculative Decoding
- Success threshold: Median speedup >= 2.0x on the repetition suite and median speedup >= 1.0x on the low-repetition suite, with all outputs exactly matching greedy baseline.
- Stop condition: Stop if gated decoding still has median speedup < 1.0x on low-repetition prompts or loses more than 25% of the ungated repetition-suite median speedup.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-n-gram-draft-speculative-decoding-vs-no-spec-baseline-d35428b095ef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

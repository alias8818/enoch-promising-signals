# Suffix-Tree N-Gram Speculative Draft for CPU Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-n-gram-speculative-draft-for-cpu-decoding-46aeef09a797`
Run ID: `suffix-tree-n-gram-speculative-draft-for-cpu-decoding-46aeef09a797-20260531T200820882574+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e4cf71291266

## What looked useful

The suffix/variable-order mechanism works for exact continuation reuse, but its relative gain over a cheap fixed bigram baseline was only about 1% on Tiny Shakespeare and about 6% to 7% on WikiText-2 slices, so suffix-tree complexity needs direct latency evidence before it is worth pursuing.

## Boundaries and scale limits

This was a bounded CPU-only proxy using held-out token streams as the target oracle, not a real LLM tokenizer, target logits, rejection sampling loop, KV cache, or end-to-end CPU decoding latency measurement. Training was capped at 50k tokens per corpus after a 200k-token Python run proved too slow to checkpoint promptly.

## Claim scope

On three 20k-token held-out regex-tokenized text streams after 50k-token training slices, a variable-order max-16 suffix n-gram drafter reduced oracle target validation calls by 1.15x to 1.35x and consistently beat fixed-order n-gram baselines.

## Why it stopped

Bounded proxy evidence supports the mechanism but does not validate real CPU speculative decoding speed or justify paper writing.

## Recommended next action

Run a direct CPU LLM integration with tokenizer-matched tokens, a fixed bigram control, the variable-order suffix drafter, and end-to-end latency plus acceptance metrics; stop this run because current evidence is proxy-only and not paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU LLM latency test for suffix n-gram speculative drafting versus bigram drafting
- Success threshold: Variable-order suffix drafting must improve end-to-end tokens/second by at least 10% over both no-draft and fixed bigram baselines on a prompt set of at least 100 completions, without changing deterministic decoded outputs.
- Stop condition: Stop if fixed bigram matches or beats variable-order latency, if acceptance is too low to offset verification overhead, or if tokenizer/model semantics make exact n-gram drafting invalid for the chosen decoding mode.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-n-gram-speculative-draft-for-cpu-decoding-46aeef09a797`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

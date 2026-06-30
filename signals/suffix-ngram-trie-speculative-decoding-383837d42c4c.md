# Suffix-Ngram Trie Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-ngram-trie-speculative-decoding-383837d42c4c`
Run ID: `suffix-ngram-trie-speculative-decoding-383837d42c4c-20260527T225301007463+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1649e0e8edf2

## What looked useful

Suffix-copy achieved up to 1.858x verifier-call speedup, but majority n-gram achieved up to 1.990x and beat suffix-copy at every tested context and draft length. Trie build cost grew from 45.3 MB RSS at context 4 to 657.0 MB RSS at context 12 on the 200k-byte corpus.

## Boundaries and scale limits

Tested 200k corpus bytes, 170k train bytes, 20k evaluated held-out bytes per condition, byte tokens only, single corpus, CPU implementation, no real LLM target, tokenizer, KV-cache, batching, GPU latency, or serving integration.

## Claim scope

On a byte-level Tiny Shakespeare held-out proxy, suffix-context drafting reduces verifier calls versus no speculation, but suffix-copy drafting does not outperform a majority n-gram backoff control built from the same trie.

## Why it stopped

Bounded proxy evidence supports verifier-call reduction but early-falsifies suffix-copy trie as a better draft mechanism than a simpler majority n-gram control; this is not a full LLM validation.

## Recommended next action

Stop this run as a no-paper useful signal; only pursue a bounded follow-up if testing against a real small pretrained LM target with tokenizer-level speculative decoding and the same n-gram control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-level suffix trie speculative decoding against a small LM target
- Success threshold: Suffix-copy or a clearly specified suffix-trie variant must exceed majority n-gram by at least 10% wall-clock tokens per second and accepted tokens per verifier call, with less than 2x memory overhead on the same tokenizer-level corpus.
- Stop condition: Stop if suffix-trie variants fail to beat majority n-gram on either accepted tokens per verifier call or wall-clock tokens per second in the first tokenizer-level small-LM benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-ngram-trie-speculative-decoding-383837d42c4c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Suffix-Array Assisted Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-assisted-speculative-decoding-ddc23c4f5727`
Run ID: `suffix-array-assisted-speculative-decoding-ddc23c4f5727-20260602T162353423933+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e5c9324cda0f

## What looked useful

Exact-match backoff retrieval is a plausible draft source, but in this proxy the useful signal comes from short-context fallback rather than the suffix-array representation. For 8-byte drafts, suffix_array accepted 1.125 bytes/trial at 12.6k queries/s, while backoff_ngram_last accepted 1.173 bytes/trial at 138k queries/s.

## Boundaries and scale limits

No tokenizer, no target LLM, no GPU serving loop, no KV-cache or batching latency, one small natural-text corpus, Python implementation, and 240k-byte train / 80k-byte held-out split only.

## Claim scope

Byte-level proxy on Tiny Shakespeare shows suffix-array exact-context backoff can draft held-out continuations with non-trivial oracle acceptance, but does not outperform a simpler backoff n-gram control after the control is allowed the same context fallback.

## Why it stopped

Early byte-level proxy falsification of the suffix-array-specific advantage, not a full validation: the mechanism works, but a simpler backoff n-gram control matches or beats acceptance and is much faster in the bounded experiment.

## Recommended next action

Stop this as no-paper proxy evidence; if continuing, run a token-level serving-loop follow-up comparing suffix-array lookup against backoff hash/trie/FM-index controls with measured latency and accepted-token speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-level suffix-array prompt lookup versus backoff controls
- Success threshold: At least 10% net tokens/second improvement over no-draft decoding and a measurable memory or latency advantage over the strongest exact-match backoff control on the same prompts.
- Stop condition: Stop if suffix-array lookup fails to beat a hash/trie/FM-index exact-match control on either net tokens/second or memory-normalized accepted tokens after a small model-serving benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-assisted-speculative-decoding-ddc23c4f5727`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

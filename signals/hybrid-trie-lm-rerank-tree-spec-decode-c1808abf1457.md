# Hybrid Trie + LM-Rerank Tree Spec Decode

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hybrid-trie-lm-rerank-tree-spec-decode-c1808abf1457`
Run ID: `hybrid-trie-lm-rerank-tree-spec-decode-c1808abf1457-20260630T140103934102+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/98c91141a0ef

## What looked useful

Across 192 held-out prompts per configuration, trie top-1 achieved 1.496 tokens per modeled verifier batch in the main run, while trie+LM rerank achieved 1.414. Stronger reranker ablations also trailed trie top-1 with rerank/top ratios of 0.963 and 0.958. Reranking won only 6-14 prompts per 192 depending on configuration and usually tied or lost.

## Boundaries and scale limits

No transformer model, GPU serving latency, KV-cache effects, tokenizer effects, or real corpus distribution were tested. Results should not be read as a full large-model speculative decoding validation.

## Claim scope

CPU proxy benchmark with deterministic character n-gram target verifier, lower-order n-gram reranker, and trie proposal paths on generated structured text. Trie proposals improved modeled verifier-batch efficiency versus one-token target greedy, but LM reranking did not improve over trie top-1 selection.

## Why it stopped

Proxy evidence gives an early falsification of the LM-rerank component in this setup; it is not a full transformer-serving validation.

## Recommended next action

Run a bounded deepen follow-up with a real small transformer target/draft on a real text corpus, measuring target forward-pass latency and acceptance against trie-only and draft-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer trie rerank speculative decoding benchmark
- Success threshold: Trie+LM-rerank achieves at least 10% higher tokens per target forward pass than trie-only with no correctness regressions and with overhead low enough to improve measured end-to-end decode latency.
- Stop condition: Stop if trie+LM-rerank fails to beat trie-only on tokens per target forward pass or measured latency on two prompt shards, or if reranker overhead erases the verifier-batch savings.

## Evidence references

- Artifact root: `<local-path>/projects/hybrid-trie-lm-rerank-tree-spec-decode-c1808abf1457`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

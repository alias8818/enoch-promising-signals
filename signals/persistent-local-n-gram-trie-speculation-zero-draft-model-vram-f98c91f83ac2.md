# Persistent Local N-Gram Trie Speculation (Zero Draft-Model VRAM)

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `persistent-local-n-gram-trie-speculation-zero-draft-model-vram-f98c91f83ac2`
Run ID: `persistent-local-n-gram-trie-speculation-zero-draft-model-vram-f98c91f83ac2-20260613T042050170506+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f7f2ee05d5c7

## What looked useful

Online persistence is the useful signal: the persistent trie averaged 1.171 accepted tokens per target position versus 0.387 for a frozen prefix trie and 0.113 for an online unigram baseline, beating both controls on 80/80 streams.

## Boundaries and scale limits

CPU-only proxy; no real LLM tokenizer, no target-model verifier forward pass, no GPU serving benchmark, no batching/KV-cache overhead measurement, and no production compact trie implementation.

## Claim scope

On 80 local text/code streams with regex tokenization, a persistent online n-gram trie produced substantially more exact-match speculative tokens than a frozen prefix trie or online unigram baseline while using no draft-model VRAM.

## Why it stopped

No-paper closure: this run produced a reproducible proxy mechanism signal, but direct model-serving evidence is required before making a paper or deployment claim.

## Recommended next action

Run a bounded direct-serving follow-up with a small local model tokenizer and verifier to measure latency/throughput benefit versus greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model direct verifier benchmark for persistent local n-gram trie speculation
- Success threshold: Persistent trie improves end-to-end decoded tokens/sec or median latency by at least 10% over greedy decoding on repetitive strata without regression on non-repetitive strata and stays under a documented CPU memory cap.
- Stop condition: Stop if proposal overhead eliminates throughput gains, exact decoded outputs diverge from greedy under the same verifier policy, or gains appear only in the regex-token proxy and not with the real tokenizer.

## Evidence references

- Artifact root: `<local-path>/projects/persistent-local-n-gram-trie-speculation-zero-draft-model-vram-f98c91f83ac2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

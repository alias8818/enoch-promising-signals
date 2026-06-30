# End-to-end medium benchmark for persistent local n-gram trie speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `end-to-end-medium-benchmark-for-persistent-local-n-gram-tr-fc40f34bd8`
Run ID: `end-to-end-medium-benchmark-for-persistent-local-n-gram-tr-fc40f34bd8-20260613T050157920081+0000`

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

- Parent run decision: Small-model direct verifier benchmark for persistent local n-gram trie speculation: enoch://control-plane/projects/small-model-direct-verifier-benchmark-for-persistent-local-5f5c60d540/runs/small-model-direct-verifier-benchmark-for-persistent-local-5f5c60d540-20260613T044100243736+0000
- Parent run decision: Persistent Local N-Gram Trie Speculation (Zero Draft-Model VRAM): enoch://control-plane/projects/persistent-local-n-gram-trie-speculation-zero-draft-model-vram-f98c91f83ac2/runs/persistent-local-n-gram-trie-speculation-zero-draft-model-vram-f98c91f83ac2-20260613T042050170506+0000

## What looked useful

Persistent local n-gram trie speculation produced a reproducible medium-scale mechanism signal: 2.21x mean speedup and 51% fewer target forwards at the safe exact order4,k4 setting, outperforming static prompt-only and random/noise controls. This is useful no-paper evidence, not paper-positive validation.

## Boundaries and scale limits

Single small target LM, one dataset, 48 generated tokens per prompt, Python trie implementation, no KV-cache optimized serving baseline, no batched serving test, no larger-model robustness, and k=8 block validation showed a 98.96% exact-match limitation likely from CUDA/model numerical non-invariance.

## Claim scope

On 96 Wikitext-2 prompt-seed cases with distilgpt2 greedy decoding on NVIDIA GB10, a persistent local n-gram trie at order 4 and draft length 4 exactly matched sequential greedy output while reducing target forwards by 51.15% and improving mean end-to-end wall-clock speed by 2.21x versus a real greedy baseline.

## Why it stopped

Tier 2 direct benchmark supports the mechanism but is not publication-grade because it covers only distilgpt2/Wikitext-2 with a Python harness and exposes an exactness limitation for aggressive k=8 block validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to implement a KV-cache/block-validation benchmark with deterministic attention and test whether exact k=8 speedups survive on GPT-2-small-class targets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache deterministic validation for persistent n-gram trie speculation
- Success threshold: At least 1.5x mean wall-clock speedup versus KV-cache greedy baseline, 100% exact greedy-output match, and at least 30% target compute reduction on both distilgpt2 and GPT-2-small-class target runs; stop or downgrade if exactness falls below 100% for the claimed config.
- Stop condition: Stop if deterministic validation cannot reproduce sequential greedy outputs exactly for k=4, or if the KV-cache baseline reduces measured speedup below 1.2x despite at least 30% accepted draft tokens.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-medium-benchmark-for-persistent-local-n-gram-tr-fc40f34bd8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

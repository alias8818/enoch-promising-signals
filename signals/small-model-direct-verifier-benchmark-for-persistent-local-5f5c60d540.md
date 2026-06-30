# Small-model direct verifier benchmark for persistent local n-gram trie speculation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-model-direct-verifier-benchmark-for-persistent-local-5f5c60d540`
Run ID: `small-model-direct-verifier-benchmark-for-persistent-local-5f5c60d540-20260613T044100243736+0000`

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

- Parent run decision: Persistent Local N-Gram Trie Speculation (Zero Draft-Model VRAM): enoch://control-plane/projects/persistent-local-n-gram-trie-speculation-zero-draft-model-vram-f98c91f83ac2/runs/persistent-local-n-gram-trie-speculation-zero-draft-model-vram-f98c91f83ac2-20260613T042050170506+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f7f2ee05d5c7

## What looked useful

Across three sampled-position runs, the persistent local n-gram trie averaged 0.349 verifier-accepted draft tokens per evaluated position, range 0.292-0.380, and beat the local-unigram control by 7.0x-9.125x. All three runs met the predeclared Tier 1 threshold of at least 0.10 accepted tokens per position and at least 2x unigram control.

## Boundaries and scale limits

Single small verifier model, one dataset family, greedy verifier acceptance only, no exact speculative sampling correction, no integrated end-to-end decoding throughput measurement, and no larger-model or multi-domain robustness.

## Claim scope

Tier 1 direct benchmark: on Wikitext-2 test positions with distilgpt2 as a greedy verifier, a persistent local n-gram trie produced substantially more verifier-accepted draft tokens than local-unigram and random-local-token controls.

## Why it stopped

Tier 1 direct mechanism support was achieved, but the result remains no-paper because it lacks end-to-end speed, exact sampling, model-scale, and domain-robustness evidence.

## Recommended next action

Run a bounded medium confirmation with an integrated batched speculative decoding loop measuring real tokens/second and verifier acceptance on Wikitext-2 plus one non-Wikitext domain.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end medium benchmark for persistent local n-gram trie speculative decoding
- Success threshold: At least 1.25x end-to-end tokens/second over ordinary greedy decoding and at least 0.20 verifier-accepted trie draft tokens per position on both tested domains, with no more than 10% memory overhead from the trie.
- Stop condition: Stop as negative if end-to-end throughput is under 1.10x greedy decoding on either domain or if trie memory/lookup overhead erases verifier-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/small-model-direct-verifier-benchmark-for-persistent-local-5f5c60d540`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

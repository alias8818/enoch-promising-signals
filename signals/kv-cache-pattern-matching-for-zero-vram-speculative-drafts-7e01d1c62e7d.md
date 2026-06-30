# KV-Cache Pattern Matching for Zero-VRAM Speculative Drafts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-pattern-matching-for-zero-vram-speculative-drafts-7e01d1c62e7d`
Run ID: `kv-cache-pattern-matching-for-zero-vram-speculative-drafts-7e01d1c62e7d-20260529T080703306912+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6ae5e26a522b

## What looked useful

Last-layer key nearest-neighbor replay accepted 0.2897 draft tokens per position over 7270 positions with 768-token windows versus 0.2613 for same-token replay, 0.1689 for bigram replay, and 0.0144 for random prior replay. With 1024-token windows, key matching accepted 0.2872 tokens per position versus 0.2818 for same-token replay. Layer-0 keys were worse than same-token replay.

## Boundaries and scale limits

This was a bounded CPU evaluation, not an integrated speculative decoding runtime. It used DistilGPT2, Wikitext-2 validation text, exact in-window search, and at most 8192 source tokens per run with 1024-token windows. It does not validate larger LLMs, longer contexts, approximate nearest-neighbor lookup, or end-to-end tokens/sec speedup.

## Claim scope

On DistilGPT2 with Wikitext-2 validation text and within-context windows up to 1024 tokens, nearest-neighbor replay over actual cached key vectors produces non-random copied draft continuations but only marginally improves accepted draft tokens per position over a trivial recent same-token replay baseline.

## Why it stopped

No-paper mixed result: this proxy directly tested actual key-cache matching and found a real above-random mechanism, but the practical advantage over cheap token replay was too small and no end-to-end speculative decoding speedup was demonstrated.

## Recommended next action

Run one bounded deepen test with an online speculative verifier on GPT-2/DistilGPT2 and close unless it shows at least a 10% end-to-end tokens/sec speedup over greedy decoding and token-replay baselines after search overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online verifier for KV-nearest continuation replay
- Success threshold: At least 10% end-to-end tokens/sec improvement over greedy decoding and at least 5% over the best token-replay baseline, with matching/search overhead included.
- Stop condition: Stop as negative if key-nearest replay fails to beat the best token baseline on tokens/sec or if search overhead consumes the acceptance gain.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-pattern-matching-for-zero-vram-speculative-drafts-7e01d1c62e7d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

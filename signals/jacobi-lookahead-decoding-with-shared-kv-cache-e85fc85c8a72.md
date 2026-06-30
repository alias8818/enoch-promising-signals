# Jacobi lookahead decoding with shared KV cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `jacobi-lookahead-decoding-with-shared-kv-cache-e85fc85c8a72`
Run ID: `jacobi-lookahead-decoding-with-shared-kv-cache-e85fc85c8a72-20260601T045632044812+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e2ed0cb03f27

## What looked useful

Shared prefix KV is an exact and substantial memory-saving mechanism for candidate verification, with 70-96% modeled KV reduction in multi-candidate cases. However, latency gains appear only versus full-prefix recomputation; compared with replicated but already-prefilled cache, suffix-only shared-cache verification had median speedup 0.956x and was often slower.

## Boundaries and scale limits

Tested only a toy 4-layer 256-dim transformer on GB10 with prefix lengths 64/256/512, suffix lengths 4/8, and candidate counts 1/4/16/32. No pretrained LLM, real LookaheadDecoding integration, production attention kernel, paged KV layout, long context, or quality/acceptance benchmark was run.

## Claim scope

On a deterministic toy causal transformer, shared-prefix KV verification is numerically equivalent to full prefix-plus-suffix evaluation and reduces modeled KV storage for multi-candidate lookahead verification, but the naive PyTorch shared-view implementation does not improve suffix-only latency against a physically replicated prefilled-cache baseline.

## Why it stopped

Closed as no-paper useful signal: the proxy mechanism is exact and memory-saving, but the direct latency baseline is mixed/negative and the result lacks real-model and production-kernel evidence.

## Recommended next action

Run a bounded follow-up with a real small pretrained causal LM and a paged/shared-prefix attention layout; stop unless it preserves exact logits and reaches at least 1.05x suffix-verification speedup versus replicated-cache verification while retaining at least 50% KV memory reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Shared-prefix paged KV verifier for real lookahead decoding
- Success threshold: For prefix length >= 512 and candidate count >= 16 on a pretrained small causal LM, max logit difference <= 1e-4, KV memory reduction >= 50%, and median suffix-verification latency speedup >= 1.05x versus replicated-prefix-cache verification.
- Stop condition: Stop if exactness fails, memory reduction falls below 50%, or an optimized/paged shared-prefix implementation remains below 1.0x suffix-verification speedup versus replicated cache.

## Evidence references

- Artifact root: `<local-path>/projects/jacobi-lookahead-decoding-with-shared-kv-cache-e85fc85c8a72`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

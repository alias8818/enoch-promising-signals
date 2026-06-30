# Single-Model Tree Decoding with Shared KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `single-model-tree-decoding-with-shared-kv-cache-2378e661d2c8`
Run ID: `single-model-tree-decoding-with-shared-kv-cache-2378e661d2c8-20260526T094601055327+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ccd8285403a

## What looked useful

Shared KV cache is clearly useful for memory, and shared tree-node execution is conditionally useful for latency when branch suffixes overlap; without suffix overlap the indirection overhead can erase latency gains.

## Boundaries and scale limits

No real causal LM integration, no fused production tree-attention kernel, no real prompt/candidate distribution, and no generation-quality or acceptance-rate evaluation. The no-suffix-sharing case was slower despite memory savings.

## Claim scope

Synthetic CUDA microbenchmarks support shared KV cache and trie-node sharing for single-model candidate-tree decoding: direct KV allocation fell 16.5x-54.7x in tested layouts, and wall time improved up to 1.37x when suffix nodes were shared.

## Why it stopped

Bounded synthetic probe produced useful mechanism evidence but not direct full-model or production-kernel evidence; finalize as no-paper useful signal.

## Recommended next action

Implement exact-logit shared-tree decoding in a small Hugging Face causal LM and compare against naive branch decoding on real prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-logit shared-tree decoding in a small causal LM
- Success threshold: At least 1.2x memory-adjusted throughput improvement with exact logits on overlapping candidate trees, while no-overlap cases show no unacceptable regression beyond documented overhead.
- Stop condition: Stop if exact logits cannot be matched or if real-model throughput is not improved for overlapping trees after a straightforward batched implementation.

## Evidence references

- Artifact root: `<local-path>/projects/single-model-tree-decoding-with-shared-kv-cache-2378e661d2c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Anchor-KV: Exact-anchor-preserving int4 KV compression for long-context inference on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-kv-exact-anchor-preserving-int4-kv-compression-for-long-context-inference-on-gb10-e29a2dd43bb5`
Run ID: `anchor-kv-exact-anchor-preserving-int4-kv-compression-for-long-context-inference-on-gb10-e29a2dd43bb5-20260630T040021913243+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a0e36fb46c28

## What looked useful

Exact anchor preservation reduced synthetic attention relative L2 error from roughly 0.13-0.16 for all-int4 to about 1.6e-05-1.4e-04 at 3.125% anchors, while preserving 3.47x KV storage reduction. Runtime was negative: naive Anchor-KV ran only 0.03x-0.17x fp16 speed.

## Boundaries and scale limits

No real LLM, no perplexity/task metric, no fused int4 attention kernel, no multi-layer or serving-stack validation. The naive PyTorch materialize-then-attend path is slower than fp16 and is not a viable serving implementation.

## Claim scope

Synthetic GB10 single-token decode probe: exact preservation of salient fp16 anchor KV rows plus int4 non-anchor KV can greatly reduce attention-output error versus all-int4 while retaining about 3.2x-3.7x KV storage reduction for seq_len 8192 and about 3.47x at seq_len 512-16384.

## Why it stopped

Proxy synthetic evidence supports the anchor-preservation error mechanism but fails practical throughput in the naive implementation; this is not a full validation or paper-ready result.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded action is a fused GB10 CUDA/Triton dequantize-attend kernel that avoids full fp16 materialization and compares against fp16 plus all-int4 baselines on real model KV traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused GB10 Anchor-KV decode kernel without full KV materialization
- Success threshold: At seq_len 8192 and 16384, fused Anchor-KV has relative L2 output error below 1e-3, achieves at least 0.8x fp16 decode throughput, and retains at least 3x KV storage reduction.
- Stop condition: Stop if the fused path remains below 0.5x fp16 throughput after eliminating full materialization, or if real KV traces show relative L2 error above 1e-2 at 3x storage reduction.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-kv-exact-anchor-preserving-int4-kv-compression-for-long-context-inference-on-gb10-e29a2dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

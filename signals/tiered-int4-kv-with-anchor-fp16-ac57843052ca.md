# Tiered INT4 KV with Anchor FP16

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-int4-kv-with-anchor-fp16-ac57843052ca`
Run ID: `tiered-int4-kv-with-anchor-fp16-ac57843052ca-20260609T050341525961+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/df7ee48e93fd

## What looked useful

Sparse/default/dense anchor tiers reduced mean relative L2 attention-output error by 18.3%, 18.1%, and 21.4% versus all-INT4 with 2.9%, 10.2%, and 20.4% extra memory over all-INT4. A low-anchor-mass control with the same memory as default improved only 3.4%, indicating anchor usefulness depends on preserving attended tokens.

## Boundaries and scale limits

No pretrained model perplexity, generation-quality, long-context workload, or fused packed-INT4 serving kernel was tested. Timing is a dequantize-then-attend prototype proxy and not a production performance result.

## Claim scope

On synthetic single-step decode attention tensors up to seq_len=8192, heads=16, dim=64, tiered INT4 KV with selected FP16 anchors reduced attention-output error versus all-INT4 when anchors carried attention mass, while remaining about 27-32% of FP16 KV memory.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only; it supports the mechanism but does not validate real model quality or production kernel performance.

## Recommended next action

Run a bounded real-model follow-up by patching a GPT-2-small-class KV cache and measuring perplexity or next-token KL for FP16 KV, all-INT4 KV, and tiered-anchor KV at matched anchor densities.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model perplexity test for tiered INT4 KV with FP16 anchors
- Success threshold: Tiered-anchor KV should reduce all-INT4 next-token KL or perplexity degradation by at least 15% at no more than 33% of FP16 KV memory, and selected anchors should beat random anchors at matched memory.
- Stop condition: Stop if tiered-anchor KV fails to improve all-INT4 degradation by 10% or if selected anchors do not outperform random anchors at matched memory.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-int4-kv-with-anchor-fp16-ac57843052ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

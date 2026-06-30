# Quantized Anchor-Gated KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-anchor-gated-kv-cache-66156b1de1da`
Run ID: `quantized-anchor-gated-kv-cache-66156b1de1da-20260604T200816241281+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e92de2eb0aa4

## What looked useful

At an estimated 3.66x KV-cache compression ratio for seq_len=2048 int4 plus 16 restored anchors per head, gated anchors reduced stable-anchor relative L2 error from 0.11132 to 0.07826 while periodic and random same-budget anchors stayed near 0.111. Across seq_len 512/1024/2048, stable-anchor int4 error reductions were 50.7%, 42.8%, and 29.7%; weak-anchor reductions were only 12.2%, 6.4%, and 4.6%.

## Boundaries and scale limits

No pretrained transformer KV traces, no end-to-end perplexity or generation quality, no hardware dequantization kernel, and no serving latency measurement were tested. The result is CPU-only and synthetic with seq_len up to 2048, heads=4, dim=64, seeds=5.

## Claim scope

Synthetic NumPy attention traces show that preserving a small calibration-selected set of high-attention K/V anchor tokens can reduce attention-output reconstruction error versus all-token quantization and ungated same-budget anchor controls, especially when stable anchor tokens dominate attention.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy-only and does not validate real model quality or serving performance.

## Recommended next action

Run a bounded deepen follow-up on real pretrained transformer KV traces, measuring next-token loss/perplexity and latency overhead for int4 all-quantized, int4 random/periodic anchors, and int4 calibration-gated anchors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace validation for quantized anchor-gated cache
- Success threshold: At matched memory budget, gated-anchor int4 KV reduces loss degradation by at least 25% versus all-int4 and beats random/periodic anchor controls on most tested layers/prompts, with less than 10% decode-time overhead in a prototype implementation.
- Stop condition: Stop if real KV traces show less than 10% loss-degradation reduction versus all-int4, if random/periodic anchors match gated anchors, or if prototype decode overhead exceeds 25% at the same memory budget.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-anchor-gated-kv-cache-66156b1de1da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

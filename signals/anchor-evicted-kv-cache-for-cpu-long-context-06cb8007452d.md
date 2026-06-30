# Anchor-Evicted KV Cache for CPU Long-Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-evicted-kv-cache-for-cpu-long-context-06cb8007452d`
Run ID: `anchor-evicted-kv-cache-for-cpu-long-context-06cb8007452d-20260531T154341082884+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a71920fc2d04

## What looked useful

Mean block anchors retrieved 100% of old target blocks and matched full-attention output on coherent synthetic blocks, but retrieved only 27.37% of target blocks in single-needle traces; the oracle showed the same 16-block budget was sufficient when selection was correct.

## Boundaries and scale limits

No real transformer logits, perplexity, downstream task accuracy, optimized CPU serving path, GPU interaction, natural long-context corpus, or 7B+ model was tested. Timing is a NumPy CPU proxy, not production decode latency.

## Claim scope

Synthetic 16k-token KV-cache simulations show that block-anchor retrieval from an evicted prefix can nearly match full attention when old context is organized into coherent 64-token blocks, but naive mean/first block anchors are unreliable for needle-like old evidence.

## Why it stopped

Closed as no-paper useful signal: synthetic evidence supports the mechanism for coherent evicted blocks but early-falsifies naive single-anchor generality for needle-like old evidence.

## Recommended next action

Run a bounded deepen test with learned or multi-prototype evicted-block anchors inside a small real transformer decode loop, measuring perplexity/task accuracy and CPU throughput against recent-only, sink+recent, uniform retrieval, and oracle block selection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-prototype evicted-block anchors in a small transformer decode loop
- Success threshold: At matched active KV budget, multi-prototype anchors reduce old-reference error or improve task/perplexity metrics by at least 25% versus mean-anchor retrieval on needle/mixed cases while retaining at least 90% of coherent-block benefit and staying within 2x the CPU overhead of uniform retrieval.
- Stop condition: Stop if multi-prototype anchors fail to improve needle/mixed retrieval over mean anchors by at least 10% at matched budget, or if CPU overhead exceeds full-attention or oracle-selection cost on the bounded test.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-evicted-kv-cache-for-cpu-long-context-06cb8007452d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

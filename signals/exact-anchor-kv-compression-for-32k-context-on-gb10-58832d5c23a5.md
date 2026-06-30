# Exact-Anchor KV Compression for 32K Context on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-for-32k-context-on-gb10-58832d5c23a5`
Run ID: `exact-anchor-kv-compression-for-32k-context-on-gb10-58832d5c23a5-20260610T141305935231+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7baa2397cd09

## What looked useful

At 32K context, exact-anchor compression reduced fp16 KV from 256 MiB to 3-8 MiB per layer-equivalent case and improved median attention time from about 12.3 ms to 0.098-0.257 ms. Target-anchor probability remained 0.967-0.987 with exact anchors versus 0.002-0.008 for pooled-only compression. However, output relative L2 error versus full attention remained high at 0.71-0.78, so the mechanism is useful for anchor-dominated retrieval but not an exact full-attention approximation.

## Boundaries and scale limits

No real language model was patched; anchor selection was assumed correct; only one layer-equivalent decode attention computation was measured; synthetic K/V/query tensors do not validate downstream generation quality or robustness across natural long-context tasks.

## Claim scope

Synthetic single-layer fp16 decode-attention probe at 32K context on GB10: preserving designated anchor KV rows exactly while block-mean compressing non-anchor rows retains anchor-coded retrieval signals far better than pooled-only compression and reduces KV tokens/attention work substantially.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic and single-layer, with substantial output distortion despite strong anchor retrieval preservation.

## Recommended next action

Run a bounded real-model deepen test by patching a GPT-2-small-class decode loop with exact-anchor KV compression and measuring long-context retrieval exact match, generation quality, latency, and memory against full KV and pooled-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model exact-anchor KV compression for long-context retrieval decode
- Success threshold: At 16K-32K context, exact-anchor compression should retain at least 95% of full-KV retrieval exact match, outperform pooled-only compression by at least 20 percentage points, and reduce KV memory by at least 8x with no more than 10% median decode-latency overhead from compression bookkeeping.
- Stop condition: Stop if exact-anchor compression loses more than 10 percentage points of retrieval exact match versus full KV at 8x or lower compression, or if real decode bookkeeping removes the latency/memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-32k-context-on-gb10-58832d5c23a5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

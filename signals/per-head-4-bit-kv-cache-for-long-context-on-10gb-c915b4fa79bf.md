# Per-Head 4-Bit KV Cache for Long Context on 10GB

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-4-bit-kv-cache-for-long-context-on-10gb-c915b4fa79bf`
Run ID: `per-head-4-bit-kv-cache-for-long-context-on-10gb-c915b4fa79bf-20260527T124453271539+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/127bf6091a35

## What looked useful

Per-head 4-bit scales preserved 3.9998x packed KV compression and improved mean top-1 attention agreement from 0.4696 to 0.6862 versus global scaling, but mean relative L2 output error stayed high at 0.3882. A per-head plus 128-token-block control improved rel-L2 to 0.3397 with 3.9980x compression, indicating that per-head-only granularity is likely too coarse and block granularity is the better next direct test.

## Boundaries and scale limits

No real LLM perplexity, generation-quality, decoding-latency, packed-int4-kernel, or production-cache allocator validation was run. Sequence lengths were 512, 2048, and 8192 with 16 heads, head dim 64, and 16 query positions.

## Claim scope

Synthetic CUDA attention proxy on NVIDIA GB10: packed 4-bit KV cache byte accounting gives near-4x memory reduction, and per-head scales improve attention-output fidelity versus global scales, but one scale per head remains too lossy for a paper-ready per-head-only KV-cache claim.

## Why it stopped

Proxy early falsification: per-head-only 4-bit KV achieved the memory target but had high synthetic attention-output distortion, so it is not paper-ready without direct model evidence and likely needs finer scale granularity.

## Recommended next action

Stop this per-head-only run as a proxy useful signal; run a bounded direct GPT-2-small-class KV-cache experiment comparing fp16 KV, per-head q4 KV, and per-head-block q4 KV on perplexity and generation quality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-Decoder Test of Per-Head-Block 4-Bit KV Cache
- Success threshold: Per-head-block q4 KV keeps perplexity or NLL degradation within 5% of fp16 KV on the fixed validation slice, beats per-head-only q4 KV by at least 25% relative degradation reduction, and preserves at least 3.8x effective KV memory reduction.
- Stop condition: Stop if per-head-block q4 KV fails to materially improve over per-head-only q4 KV or if both q4 variants exceed 10% perplexity/NLL degradation versus fp16 KV on the fixed validation slice.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-4-bit-kv-cache-for-long-context-on-10gb-c915b4fa79bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

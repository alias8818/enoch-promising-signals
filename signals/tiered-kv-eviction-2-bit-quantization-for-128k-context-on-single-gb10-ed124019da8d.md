# Tiered KV Eviction + 2-bit Quantization for 128K Context on Single GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-kv-eviction-2-bit-quantization-for-128k-context-on-single-gb10-ed124019da8d`
Run ID: `tiered-kv-eviction-2-bit-quantization-for-128k-context-on-single-gb10-ed124019da8d-20260622T013022197676+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e0f2ec7e7459

## What looked useful

2-bit KV memory arithmetic is favorable, about 7.5x compression with fp16 per-vector scales, and all-old 2-bit KV preserved the synthetic old needle at 128K, but cosine versus fp16 was only about 0.887 with relative L2 about 0.528. Recent-only and random old-token eviction failed old-needle retrieval, while oracle old-token retention succeeded, indicating the eviction policy is the unresolved mechanism.

## Boundaries and scale limits

No full transformer, no packed 2-bit serving kernel, no autoregressive decoding throughput, no real long-context benchmark, and no deployable non-oracle eviction policy were validated. The 128K run was a single-layer synthetic attention proxy with 16 trials.

## Claim scope

Synthetic single-query CUDA attention probes on GB10 show that packed 2-bit old KV plus a recent fp16 tier can reduce effective KV memory and preserve old-needle top-1 retrieval in controlled 8K, 32K, and 128K contexts, but output vectors remain materially distorted versus full fp16 attention and eviction fails without an oracle importance signal.

## Why it stopped

Synthetic proxy evidence is useful but insufficient for a paper-ready 128K single-GB10 serving claim; eviction without an oracle importance signal failed the old-token retrieval stress case.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded action is a real-model 128K retrieval benchmark using a non-oracle heavy-hitter eviction signal and packed or simulated 2-bit KV against fp16/no-eviction controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model 128K KV compression test with non-oracle heavy-hitter eviction
- Success threshold: At 128K context, the compressed tiered policy uses at least 4x less KV memory than fp16 and stays within 5% relative quality degradation versus fp16/no-eviction while avoiding old-token retrieval failures in at least 95% of targeted retrieval cases.
- Stop condition: Stop if non-oracle eviction misses old retrieval targets in more than 10% of cases or if 2-bit KV causes more than 10% relative quality degradation even without eviction.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-eviction-2-bit-quantization-for-128k-context-on-single-gb10-ed124019da8d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

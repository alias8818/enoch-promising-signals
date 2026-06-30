# Exact-Anchor KV Compression with Recompute-on-Miss

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-with-recompute-on-miss-9748ebf8c50d`
Run ID: `exact-anchor-kv-compression-with-recompute-on-miss-9748ebf8c50d-20260630T041033891925+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/258725c218cc

## What looked useful

The mechanism is exact for selected tokens and saves roughly 43-47% of KV-cache memory in the tested settings, but latency rises sharply with misses: 1% misses caused 1.40x slowdown at seq=4096/d=1024 and 2.44x at seq=8192/d=2048 versus precomputed selected K/V.

## Boundaries and scale limits

No real decoder model, no learned or heuristic miss policy, no perplexity/logit-quality evaluation, no multi-layer serving integration, and no fused production kernel. Memory accounting assumes layer-input hidden states must be retained for evicted tokens, giving a theoretical best ratio near 0.5 before anchor overhead.

## Claim scope

Synthetic single-layer decoder KV-cache benchmark on NVIDIA GB10: exact-anchor plus hidden-state-backed recompute reproduces selected-token K/V attention within fp16 tolerance and reduces KV cache memory to about 0.535-0.569 of full KV for the tested anchor/recent settings.

## Why it stopped

Proxy synthetic benchmark supports exact recompute mechanics but shows substantial latency overhead at nonzero miss rates and lacks direct model-quality evidence, so it is not a publication-grade positive result.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate the mechanism into GPT-2-small-class inference with a non-oracle miss policy and compare logit/perplexity error plus decode latency against full KV and a quantized-KV baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model exact-anchor recompute with non-oracle miss policy
- Success threshold: At seq_len >= 2048, memory ratio <= 0.6, perplexity delta <= 1%, mean logit absolute error <= 0.02, and decode throughput >= 80% of full KV with observed non-oracle miss rate <= 1%.
- Stop condition: Stop as negative if non-oracle miss rate exceeds 1% while keeping quality within threshold, or if throughput falls below 80% of full KV at comparable quality and memory ratio.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-with-recompute-on-miss-9748ebf8c50d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

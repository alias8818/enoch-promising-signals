# Decode-time KV eviction quality and latency check

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `decode-time-kv-eviction-quality-and-latency-check-95559452c1`
Run ID: `decode-time-kv-eviction-quality-and-latency-check-95559452c1-20260608T233532920619+0000`

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

- Parent run decision: Tiered KV Cache Eviction via Attention-Score Histograms: enoch://control-plane/projects/tiered-kv-cache-eviction-via-attention-score-histograms-62993410e7a0/runs/tiered-kv-cache-eviction-via-attention-score-histograms-62993410e7a0-20260608T214407893081+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7b7a88ab66bb

## What looked useful

Recent plus heavy-hitter eviction was the best practical policy in local/sink and mixed regimes. At 50% retention it reached mean relative L2 0.147 in local_sink but 0.381 in mixed_retrieval and 0.981 in diffuse. Short-context latency was essentially unchanged, while a long-context sweep showed 2.40x speedup at 50% retention and 5.68x at 25% retention for 32768-token KV.

## Boundaries and scale limits

No full language model, real corpus, perplexity, generation quality, production fused kernel, or layerwise cache interaction was tested. Quality metric is direct for the attention primitive but only a proxy for end-to-end model quality.

## Claim scope

Controlled CUDA single-token attention benchmark with synthetic KV streams. KV eviction preserves attention outputs in favorable local/sink regimes at 50-75% retention and improves latency only at long contexts where attention length dominates overhead.

## Why it stopped

Tier 1 direct attention-primitive evidence is mixed and not paper-ready: the mechanism works under structured local/sink attention and long contexts but fails under diffuse/retrieval patterns and lacks end-to-end language-model validation.

## Recommended next action

Run a bounded real-model follow-up on GPT-2-small-class decoding with layerwise KV eviction, measuring perplexity/generation degradation and decode latency against full-cache and sliding-window baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model decode KV eviction quality and latency on GPT-2-small-class workloads
- Success threshold: At 50% KV retention and contexts where full-cache attention is latency-relevant, recent plus heavy-hitter eviction achieves at least 1.5x mean decode-attention or end-to-end decode speedup with less than 10% perplexity increase or mean next-token KL below 0.1 versus full cache, and beats recent-only on quality.
- Stop condition: Stop if recent plus heavy-hitter does not beat recent-only on quality at matched retention, or if 50% retention causes more than 10% perplexity increase / next-token KL above 0.1 before reaching 1.5x speedup.

## Evidence references

- Artifact root: `<local-path>/projects/decode-time-kv-eviction-quality-and-latency-check-95559452c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

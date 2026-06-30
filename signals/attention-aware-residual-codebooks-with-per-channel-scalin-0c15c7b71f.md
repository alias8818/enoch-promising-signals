# Attention-aware residual codebooks with per-channel scaling for sub-2-bit KV cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `attention-aware-residual-codebooks-with-per-channel-scalin-0c15c7b71f`
Run ID: `attention-aware-residual-codebooks-with-per-channel-scalin-0c15c7b71f-20260522T204150870196+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Sub-2-bit KV cache via residual codebook channels: enoch://control-plane/projects/sub-2-bit-kv-cache-via-residual-codebook-channels-f0e454110abe/runs/sub-2-bit-kv-cache-via-residual-codebook-channels-f0e454110abe-20260522T190047637252+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c268c71efb9e

## What looked useful

On 72 distilgpt2 sample-layer measurements, attention-aware residual variants at 1.25-1.75 payload bits/value achieved mean relative MSE around 0.77-0.78, about 23-24% of the simple 2-bit per-channel baseline's 3.32 and about 18-19% of the 1-bit baseline's 4.18. Norm-based residual allocation failed and random allocation was materially weaker, supporting attention-guided allocation as the useful mechanism.

## Boundaries and scale limits

Single small GPT-2-family model, 12 short text samples, 6 layers, local attention-output metric only. Payload bit counts exclude selector metadata. Attention-aware token selection uses exact attention from the evaluated query tail and is not yet a causal online cache policy. No end-to-end perplexity, generation, long-context, kernel, latency, or memory-bandwidth validation was run.

## Claim scope

Tier-1 local attention-output test on distilgpt2 Q/K/V tensors: oracle attention-aware 1-bit residual allocation with per-channel scaling at 1.25-1.75 payload bits/value reduced mean relative attention-output MSE versus simple 1-bit and 2-bit per-channel K/V quantization baselines.

## Why it stopped

The Tier-1 direct test supports the mechanism, but the strongest evidence is oracle-assisted and local; it is useful no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen test with a causal online selector, explicit metadata bit accounting, and end-to-end perplexity on a small corpus before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Causal attention-predicted residual KV allocation with metadata-inclusive bit budget
- Success threshold: At less than 2.0 total bits/value including metadata, the causal residual method should reduce perplexity degradation by at least 20% versus the strongest implemented 2-bit baseline while preserving a local attention-output error advantage on the same examples.
- Stop condition: Stop if metadata-inclusive bits/value reaches or exceeds 2.0, if the causal selector loses more than half of the oracle local-error benefit, or if perplexity degradation is not better than the strongest 2-bit baseline.

## Evidence references

- Artifact root: `<local-path>/projects/attention-aware-residual-codebooks-with-per-channel-scalin-0c15c7b71f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

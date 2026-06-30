# 2-bit Weight Quantization with Learned Residual Channel for CPU LLM Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-weight-quantization-with-learned-residual-channel-for-cpu-llm-inference-586e6b26653d`
Run ID: `2-bit-weight-quantization-with-learned-residual-channel-for-cpu-llm-inference-586e6b26653d-20260628T064022052766+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0d7c79acde9e

## What looked useful

Rank-1 residual channel reduced mean MSE by 0.79% at 2.56 bits/weight with 9.48% latency overhead over the dequantized 2-bit proxy. Rank 4 and 8 improved MSE by 2.66% and 4.80%, respectively, at 2.75 and 3.00 bits/weight. Mechanism exists but is too weak in this proxy for a paper-positive CPU LLM inference claim.

## Boundaries and scale limits

No real LLM weights, perplexity, downstream task quality, packed int2 kernel, cache-level CPU serving, or 7B+ validation was tested. Latency is dense dequantized NumPy proxy only.

## Claim scope

Synthetic GPT-2-small-shaped CPU NumPy proxy: learned low-rank residual channels monotonically reduce 2-bit quantized linear-layer output MSE, but rank-1 effect is less than 1% mean MSE reduction with latency and storage overhead.

## Why it stopped

Early proxy falsification of the strong practical claim: the residual channel improves synthetic output error monotonically, but the rank-1 effect is too small and not direct LLM evidence.

## Recommended next action

Run one bounded direct follow-up on real GPT-2-small weights measuring perplexity and CPU token throughput with a simple packed or semi-packed 2-bit implementation; stop if rank-1 residual does not improve perplexity at near-equal bits/weight without throughput loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real GPT-2-small perplexity and CPU throughput test for 2-bit residual channel quantization
- Success threshold: Rank-1 residual improves perplexity or layer-output error by at least 5% relative to 2-bit baseline while keeping storage under 2.7 bits/weight and throughput within 5% of the 2-bit implementation.
- Stop condition: Stop if real-model rank-1 residual improves perplexity or output error by less than 2% relative, exceeds 2.7 bits/weight, or costs more than 10% throughput.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-weight-quantization-with-learned-residual-channel-for-cpu-llm-inference-586e6b26653d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

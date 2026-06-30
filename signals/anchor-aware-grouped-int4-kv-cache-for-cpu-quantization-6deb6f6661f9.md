# Anchor-Aware Grouped INT4 KV Cache for CPU Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-aware-grouped-int4-kv-cache-for-cpu-quantization-6deb6f6661f9`
Run ID: `anchor-aware-grouped-int4-kv-cache-for-cpu-quantization-6deb6f6661f9-20260609T202132061404+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb42f9c0ae34

## What looked useful

Across 960 synthetic cases, nonzero-anchor variants reduced mean relative L2 attention-output error from 0.287612 to 0.175494 with 13.02% average overhead over ordinary INT4 and 3.56x average compression versus fp16 KV. Gains were large for spiky and mixed-scale distributions, modest for drift, and weak for Gaussian with five tiny one-anchor regressions.

## Boundaries and scale limits

No real LLM perplexity/task evaluation, no real KV trace replay, no packed INT4/SIMD CPU kernel, no production latency or throughput validation; maximum tested synthetic sequence length was 2048 and dimension was 128.

## Claim scope

Synthetic CPU decode-attention mechanism probe: preserving top key-norm anchors per token group before grouped INT4 quantization reduces fp32-attention output error versus ordinary grouped INT4, especially for spiky or mixed-scale KV distributions.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic mechanism evidence, not full CPU KV-cache validation.

## Recommended next action

Run a bounded direct follow-up on real small-model KV traces or perplexity with a packed anchor-aware INT4 CPU path and compare against ordinary grouped INT4 at matched memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace validation of anchor-aware grouped INT4 KV cache
- Success threshold: At matched memory within 15% overhead versus ordinary INT4, reduce attention-output error or perplexity degradation by at least 25% while keeping CPU decode latency overhead below 20%.
- Stop condition: Stop if real-trace accuracy gains are below 10% versus ordinary grouped INT4 or CPU decode overhead exceeds 30% at matched memory.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-aware-grouped-int4-kv-cache-for-cpu-quantization-6deb6f6661f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

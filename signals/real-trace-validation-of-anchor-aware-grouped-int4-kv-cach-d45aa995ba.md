# Real-trace validation of anchor-aware grouped INT4 KV cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-validation-of-anchor-aware-grouped-int4-kv-cach-d45aa995ba`
Run ID: `real-trace-validation-of-anchor-aware-grouped-int4-kv-cach-d45aa995ba-20260610T063451945268+0000`

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

- Parent run decision: Anchor-Aware Grouped INT4 KV Cache for CPU Quantization: enoch://control-plane/projects/anchor-aware-grouped-int4-kv-cache-for-cpu-quantization-6deb6f6661f9/runs/anchor-aware-grouped-int4-kv-cache-for-cpu-quantization-6deb6f6661f9-20260609T202132061404+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb42f9c0ae34

## What looked useful

Anchor-aware grouped INT4 KV cache cleared the predefined Tier 1 mechanism threshold for 4 prefix+sink anchors: mean all-INT4 relative RMSE was 0.26319, anchor-aware relative RMSE was 0.20296, and estimated anchor-aware KV memory was 31.28% of FP32. Nearby controls were informative: 4 prefix-only anchors improved RMSE by only 8.54%, 2 prefix+sink anchors by 8.07%, and 8 prefix+sink anchors improved by 33.62% but used 50.05% of FP32 KV memory.

## Boundaries and scale limits

Small model, 10 fixed prompts, sequence length <=96, dequantized replay instead of packed INT4 serving kernels, attention-output fidelity only; no end-to-end perplexity, generation-quality, latency, long-context, larger-model, or hardware-throughput validation.

## Claim scope

On a CPU-only Tier 1 direct replay using distilgpt2 KV activations from 10 natural-language prompts, preserving 4 prefix+sink anchor positions in FP32 while quantizing non-anchor KV values to grouped INT4 reduced final-token attention-output relative RMSE by 22.89% versus all-INT4, with estimated KV storage at 31.28% of FP32.

## Why it stopped

Tier 1 direct evidence supports the mechanism but remains too small and replay-only for publication readiness.

## Recommended next action

Run a bounded deepen follow-up that evaluates the 4-anchor prefix+sink policy on a held-out text benchmark with end-to-end perplexity/logit drift and longer contexts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out perplexity and logit-drift validation for 4-anchor prefix+sink INT4 KV cache
- Success threshold: At <=40% FP32 KV memory, 4-anchor prefix+sink must reduce logit drift or perplexity degradation by at least 10% versus all-INT4 without worse than 1% relative perplexity increase versus FP32 on the held-out evaluation.
- Stop condition: Stop if 4-anchor prefix+sink fails to beat all-INT4 by 10% on logit drift/perplexity degradation, exceeds 40% FP32 KV memory, or produces more than 1% relative perplexity increase versus FP32.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-validation-of-anchor-aware-grouped-int4-kv-cach-d45aa995ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# 2-Bit KV Cache with Residual Error Buffers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-residual-error-buffers-83a1c4712d97`
Run ID: `2-bit-kv-cache-with-residual-error-buffers-83a1c4712d97-20260603T204106352606+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/156664998da4

## What looked useful

Across 432 synthetic configurations, best high-error residual selection at >=3x compression gave median RMSE reductions of 3.1% on normal tensors, 25.8% on heavy-tailed tensors, and 99.7% on explicit outlier-token tensors. At 5% residual storage, recent/random policies improved median RMSE only about 2%, while top-error selection improved median RMSE about 25.8%.

## Boundaries and scale limits

Tested synthetic Q/K/V tensors only: batch 1, 8 heads, head dimension 64, 16 queries, sequence lengths up to 8192, three synthetic activation distributions, and three random seeds. No pretrained LM perplexity, generation, real prompt activations, decode-time cache integration, fused kernel, or long-context serving measurement was run.

## Claim scope

Synthetic single-attention benchmarks show that 2-bit groupwise KV cache quantization benefits materially from residual buffers only when residual storage is targeted to high quantization-error or outlier tokens; naive recent/random residual buffers provide little benefit.

## Why it stopped

Proxy-only synthetic attention evidence supports a narrow mechanism but does not validate end-to-end model quality or serving viability; close this run as no-paper useful signal rather than paper-positive.

## Recommended next action

Run a bounded pretrained GPT-2-small-class evaluation that patches decode-time KV cache quantization and compares fp16 KV, plain 2-bit KV, recent residual buffers, and quantization-error/outlier-targeted residual buffers on perplexity, generation drift, memory, and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained LM evaluation of targeted residual buffers for 2-bit KV cache
- Success threshold: At approximately 3x KV compression, targeted residual buffers reduce perplexity/NLL degradation by at least 25% versus plain 2-bit KV and outperform recent residual buffers, with no more than 15% decode latency overhead in the tested implementation.
- Stop condition: Stop if targeted residual buffers fail to improve real-model perplexity/NLL degradation by at least 10% over plain 2-bit KV at matched memory, or if selection overhead removes the practical memory/latency advantage.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-residual-error-buffers-83a1c4712d97`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

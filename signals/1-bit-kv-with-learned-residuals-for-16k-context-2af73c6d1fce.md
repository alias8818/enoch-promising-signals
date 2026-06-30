# 1-bit KV with Learned Residuals for 16k Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-kv-with-learned-residuals-for-16k-context-2af73c6d1fce`
Run ID: `1-bit-kv-with-learned-residuals-for-16k-context-2af73c6d1fce-20260523T105504383643+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aaff3ccd450d

## What looked useful

A learned low-rank residual over 1-bit sign KV is a plausible sub-2-bit mechanism: rank16 reduced attention-proxy relative RMSE from 1.0826 for sign-only to 0.5559 with mean cosine 0.8413, at 2.017 effective bits per element. However, raw K/V reconstruction remains materially worse than int4/int8, especially for V, so this is not paper-ready.

## Boundaries and scale limits

Single locally cached Qwen3-0.6B model; one repeated prompt-derived 16k token stream; layers 0, 14, and 27 only; two KV heads per layer; PCA residual basis fit on calibration prefix and evaluated on suffix; no patched model forward pass, perplexity, retrieval, generation, all-layer sweep, or packed-kernel latency measurement.

## Claim scope

On Qwen3-0.6B 16k-token KV activations for three selected layers and two KV heads per layer, sign bits plus learned PCA residual coefficients at 1.5-2.0 effective bits per element substantially improve sign-only and naive int2 KV compression, and rank16 improves a sampled attention-output proxy versus naive int4 on mean error. The result is proxy-only and not a model-quality validation.

## Why it stopped

Closed as no-paper useful signal because the current run used real 16k KV activations but only proxy attention-output metrics, not direct model quality or serving measurements.

## Recommended next action

Run one bounded direct-quality follow-up by patching Qwen3-0.6B attention to consume sign+rank16 residual KV and measuring perplexity plus a 16k needle/retrieval task against fp16 and int4 KV.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Qwen3-0.6B quality test for sign-plus-rank16 residual KV at 16k
- Success threshold: At 16k, sign-plus-rank16 residual KV should stay within 10% relative perplexity/loss degradation of fp16 KV and within 5 percentage points retrieval accuracy of fp16, while matching or beating int4 KV on at least one meaningful memory-quality tradeoff.
- Stop condition: Stop if patched sign-plus-rank16 residual KV causes more than 20% relative perplexity/loss degradation, more than 10 percentage points retrieval accuracy loss versus fp16, or materially worse quality than int4 KV at similar or higher effective memory cost.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-kv-with-learned-residuals-for-16k-context-2af73c6d1fce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

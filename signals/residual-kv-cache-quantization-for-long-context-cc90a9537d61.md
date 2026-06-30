# Residual KV-Cache Quantization for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-kv-cache-quantization-for-long-context-cc90a9537d61`
Run ID: `residual-kv-cache-quantization-for-long-context-cc90a9537d61-20260604T151142989271+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/52d33b61574f

## What looked useful

At 8192 tokens with int4 old-cache quantization, local-heavy queries improved from 0.14343 relative RMSE with no residual to 0.01739 with a 256-token residual at 0.2886x fp16 KV memory. Global and old-anchor cases improved only about 1.00x to 1.05x for int4, showing the mechanism depends on recent attention mass.

## Boundaries and scale limits

No real transformer model, perplexity, retrieval-task, decoding-quality, serving-latency, or kernel-overhead validation was run. Sequence length was capped at 8192 with synthetic KV/Q tensors and 128 query vectors per case.

## Claim scope

Synthetic GPU attention benchmark up to 8192 tokens shows that keeping a small recent fp16 residual KV window can substantially reduce quantization-induced attention-output error when attention mass is recent-local, but provides little benefit for global or old-anchor attention patterns.

## Why it stopped

Proxy/synthetic benchmark supports a conditional mechanism but is not direct model-quality evidence or publication-grade validation.

## Recommended next action

Stop this worker run as no-paper proxy evidence; the next bounded test should replay the same policy on real KV traces from a small decoder-only transformer and require both quality and memory metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model trace validation for residual KV-cache quantization
- Success threshold: At least 2x lower quality degradation than full-cache int4 quantization on high-recent-mass examples at comparable memory ratio, without regression on low-recent-mass examples beyond the full-cache int4 baseline.
- Stop condition: Stop if real-model traces show less than 10% of attention mass in practical residual windows or if residual windows fail to reduce quality degradation by at least 25% versus full-cache int4.

## Evidence references

- Artifact root: `<local-path>/projects/residual-kv-cache-quantization-for-long-context-cc90a9537d61`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

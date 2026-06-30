# KV-Cache Residual Channels for Long-Context Quantized Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-residual-channels-for-long-context-quantized-inference-6c142f3056ff`
Run ID: `kv-cache-residual-channels-for-long-context-quantized-inference-6c142f3056ff-20260531T183701465107+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b813c3cb1346

## What looked useful

Residual channels were correctly identified and helped only when extra cache budget was allowed. At the same 4.0-bit average cache budget, moving non-residual channels mostly to int3 caused 1.28x to 1.76x higher relative L2 attention-output error than uniform int4 across 1024-16384 token contexts.

## Boundaries and scale limits

No pretrained model perplexity, retrieval task accuracy, layer/head diversity, production KV-cache kernel, or decode throughput was tested. Activations were synthetic with injected persistent channel outliers.

## Claim scope

Synthetic single-head long-context attention probe with dim=128, 8 residual channels, 1024-16384 cache length, and 8 seeds per length. The exact 4.0 average bits-per-scalar residual-channel allocation did not reduce attention-output error versus uniform int4; an extra-budget 4.75-bit residual control did reduce error.

## Why it stopped

Proxy early falsification rather than full validation: exact-budget residual-channel KV quantization was worse than uniform int4 on the direct synthetic attention-output metric at every tested context length.

## Recommended next action

Stop this run as a proxy negative for the same-memory claim; a bounded follow-up should test whether learned per-layer residual allocation on real transformer activations can avoid the int3 remainder penalty.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Activation Residual KV Allocation for Int4-Budget Caches
- Success threshold: At the same 4.0 average bits per KV scalar, residual allocation must reduce mean attention-output relative L2 error by at least 10% versus uniform int4 and must not worsen perplexity/logit error on the tested model.
- Stop condition: Stop if exact-budget residual allocation is worse than uniform int4 in more than half of tested layers/heads or worsens perplexity/logit error at equal cache budget.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-residual-channels-for-long-context-quantized-inference-6c142f3056ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

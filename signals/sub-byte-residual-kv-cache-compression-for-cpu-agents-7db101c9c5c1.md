# Sub-byte Residual KV Cache Compression for CPU Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-byte-residual-kv-cache-compression-for-cpu-agents-7db101c9c5c1`
Run ID: `sub-byte-residual-kv-cache-compression-for-cpu-agents-7db101c9c5c1-20260523T151034605546+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/34cc41ba48dc

## What looked useful

Residual KV coding is promising only when KV deltas are strongly temporally correlated and anchors are frequent. Anchor-8 2b residual reduced attention rel-MSE by 247x, 522x, and 1770x versus absolute 2b on three high-correlation cases at about 4.1x compression vs fp16, but was worse than absolute 2b on the low-correlation control and exceeded the <3x slowdown target in high-correlation cases.

## Boundaries and scale limits

No real LLM KV traces, no end-to-end perplexity/logit/task validation, no packed sub-byte CPU kernel, and no layer/head diversity beyond synthetic correlation regimes. Timing is a Python/NumPy prototype and should not be interpreted as production serving latency.

## Claim scope

Synthetic CPU-only KV-cache probe: short-anchor residual affine quantization at 2-4 bits greatly reduces KV and attention-output error versus same-bit absolute quantization on high-temporal-correlation synthetic KV streams, but the same method is worse than absolute quantization on a low-correlation control and has substantial Python decode-plus-attention overhead.

## Why it stopped

Synthetic proxy produced a mixed useful signal, not full validation: high-correlation mechanism is supported, but robustness and CPU-serving viability are not established and the low-correlation control fails.

## Recommended next action

Run a bounded direct follow-up on real small-model KV traces with logit KL/perplexity and a packed CPU decode prototype; do not write a paper from this synthetic proxy alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace residual KV quantization with packed CPU decode
- Success threshold: Residual 2b or 3b must beat same-bit absolute quantization by at least 3x on logit KL or attention-output MSE on real traces, keep perplexity delta within an agreed small-model tolerance, retain at least 3.5x effective KV memory reduction vs fp16 including metadata, and add no more than 20% CPU token latency versus the strongest low-bit baseline.
- Stop condition: Stop if residual coding fails to beat absolute quantization on real-trace logit KL/attention error in most layers, if metadata/anchors reduce effective compression below 3.5x, or if packed decode cannot approach the latency threshold.

## Evidence references

- Artifact root: `<local-path>/projects/sub-byte-residual-kv-cache-compression-for-cpu-agents-7db101c9c5c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

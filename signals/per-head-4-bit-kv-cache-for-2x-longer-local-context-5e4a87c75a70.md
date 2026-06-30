# Per-head 4-bit KV cache for 2x longer local context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-4-bit-kv-cache-for-2x-longer-local-context-5e4a87c75a70`
Run ID: `per-head-4-bit-kv-cache-for-2x-longer-local-context-5e4a87c75a70-20260529T114133191177+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e8d22261cc54

## What looked useful

4-bit KV storage can fit 2x context under the FP16 KV-cache budget in the tested geometry. Per-token-head scaling preserved attention outputs better than static per-head scaling, while static per-head scaling was fragile under sparse outliers.

## Boundaries and scale limits

No production packed KV-cache kernel, no all-layer quantized autoregressive decoding, no perplexity or long-context task quality evaluation, and no latency validation at 2x serving context.

## Claim scope

Bounded attention-output and memory-accounting probe for static per-head and per-token-head 4-bit KV quantization on synthetic tensors plus distilgpt2 layer-0 Q/K/V tensors.

## Why it stopped

Closed as no-paper useful signal because the current result is a bounded attention-output probe, not full end-to-end validation of 2x longer local context quality.

## Recommended next action

Run a bounded full-decoding GPT-2-small-class evaluation of per-token-head 4-bit KV cache with perplexity, long-context retrieval accuracy, actual packed-cache memory, and decode latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full-decoding GPT-2-small per-token-head 4-bit KV cache validation
- Success threshold: At 2x context, packed 4-bit KV uses no more than 60% of FP16 baseline KV memory while perplexity degradation is no more than 5% and retrieval accuracy is no worse than 2 percentage points below FP16.
- Stop condition: Stop if all-layer 4-bit KV decoding exceeds 5% perplexity degradation, loses more than 2 percentage points retrieval accuracy, or the packed implementation fails to stay below 60% of FP16 baseline KV memory at 2x context.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-4-bit-kv-cache-for-2x-longer-local-context-5e4a87c75a70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Dynamic Precision Cascading for KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-precision-cascading-for-kv-cache-1617244cff61`
Run ID: `dynamic-precision-cascading-for-kv-cache-1617244cff61-20260526T083450909153+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12a892dcebd7

## What looked useful

At about 26.5% of fp16 KV memory, age-only cascading preserved recency-biased attention better than uniform int4 but failed retrieval and mixed regimes. Oracle importance allocation rescued retrieval at the same memory budget, suggesting importance tracking is the mechanism worth testing, not age alone.

## Boundaries and scale limits

No real LLM, perplexity, downstream task, autoregressive multi-step decode stability, serving latency, or quantized KV kernel overhead was measured. Oracle importance uses reference attention and is not directly deployable.

## Claim scope

Synthetic attention mechanism probe over 8-head, d=64 KV tensors at sequence lengths 512, 2048, and 4096. Age-only cascading was compared with uniform int4/int8 and an oracle importance cascade using attention-output error and modeled KV memory.

## Why it stopped

Closed as no-paper useful signal: bounded synthetic evidence is mixed and early-falsifies age-only cascading as a general KV cache policy, but it does not constitute full model or serving validation.

## Recommended next action

Run a bounded deepen test that replaces oracle importance with decayed attention-history importance in a small real transformer long-context decode benchmark; stop if it cannot beat uniform int4 on retrieval quality at matched modeled memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Attention-history precision cascading in a small transformer KV cache
- Success threshold: At no more than 30% of fp16 KV memory, the attention-history cascade must beat uniform int4 by at least 20% relative on retrieval error or retrieval accuracy loss without more than 10% decode latency overhead versus the closest quantized baseline.
- Stop condition: Stop if the practical tracker performs no better than uniform int4 on retrieval/mixed cases at matched memory, or if kernel/decode overhead eliminates the memory benefit.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-precision-cascading-for-kv-cache-1617244cff61`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

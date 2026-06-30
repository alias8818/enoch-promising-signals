# Grouped K/V projection sharing for local Transformer inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `grouped-k-v-projection-sharing-for-local-transformer-infer-6f021bef8d`
Run ID: `grouped-k-v-projection-sharing-for-local-transformer-infer-6f021bef8d-20260524T185201850068+0000`

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

- Parent run decision: Cross-layer KV projection sharing for local inference: enoch://control-plane/projects/cross-layer-kv-projection-sharing-for-local-inference-ad07fb680cf3/runs/cross-layer-kv-projection-sharing-for-local-inference-ad07fb680cf3-20260524T083003159818+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/868b1785ee47

## What looked useful

Across seeds 0-2, GQA 2-KV-head validation loss delta averaged +0.0016 vs MHA while halving fp16 KV cache; MQA 1-KV-head validation loss delta averaged +0.00001 while quartering fp16 KV cache. Unfused PyTorch local decode recompute timing was roughly neutral/slightly slower, so the speed claim remains unproven.

## Boundaries and scale limits

Synthetic task only; tiny model with d_model 96, 3 layers, 4 query heads, context 64, local window 32, 800 training steps, 3 seeds. No real-text language modeling, no GPT-2-small-class scale, no parameter-matched widened controls, and no fused incremental decode kernel.

## Claim scope

Tier 1 controlled small direct test: a tiny local causal Transformer on a synthetic local-copy autoregressive task preserved validation loss under 2-KV-head GQA and 1-KV-head MQA while reducing K/V cache footprint.

## Why it stopped

No-paper closure: Tier 1 mechanism support is useful but synthetic quality evidence and unfused timing are not publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on a small real-text local Transformer with parameter-matched controls and a cache-aware/fused decode benchmark before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small real-text local Transformer GQA/MQA quality and fused-decode check
- Success threshold: GQA validation loss within 1% of parameter-matched MHA and at least 1.2x cache-aware decode throughput or a clearly measured KV-cache bandwidth reduction at equal batch/context; MQA may pass only if its loss gap is also within 1%.
- Stop condition: Stop if GQA exceeds a 1% validation-loss gap after comparable training or if a cache-aware decode benchmark shows less than 5% practical memory/throughput benefit despite reduced KV-cache footprint.

## Evidence references

- Artifact root: `<local-path>/projects/grouped-k-v-projection-sharing-for-local-transformer-infer-6f021bef8d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

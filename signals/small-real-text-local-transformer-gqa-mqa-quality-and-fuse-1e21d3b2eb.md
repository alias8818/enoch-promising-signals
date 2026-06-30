# Small real-text local Transformer GQA/MQA quality and fused-decode check

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-real-text-local-transformer-gqa-mqa-quality-and-fuse-1e21d3b2eb`
Run ID: `small-real-text-local-transformer-gqa-mqa-quality-and-fuse-1e21d3b2eb-20260527T033213711586+0000`

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

- Parent run decision: Cross-layer KV projection sharing for local inference: enoch://control-plane/projects/cross-layer-kv-projection-sharing-for-local-inference-ad07fb680cf3/runs/cross-layer-kv-projection-sharing-for-local-inference-ad07fb680cf3-20260524T083003159818+0000
- Parent run decision: Grouped K/V projection sharing for local Transformer inference: enoch://control-plane/projects/grouped-k-v-projection-sharing-for-local-transformer-infer-6f021bef8d/runs/grouped-k-v-projection-sharing-for-local-transformer-infer-6f021bef8d-20260524T185201850068+0000

## What looked useful

GQA 2-KV reached mean validation loss 1.8405 versus full MHA 1.8365 (+0.0039) and parameter-matched MHA control 1.8548, while fused GQA decode was 2.51x geomean faster than materialized repeated KV over seq lengths 128/512/1024. MQA 1-KV was 2.99x faster but had +0.0163 loss versus full MHA.

## Boundaries and scale limits

Small byte-level model, 1000 training steps per seed, WikiText-2 only, short context, no GPT-2-small-class BPE tokenizer, no long-context evaluation, no end-to-end serving stack, and no large-model/datacenter validation.

## Claim scope

On a small CUDA-trained byte-level WikiText-2 Transformer with 4 layers, 8 query heads, context 128, and three fixed seeds, 2-KV GQA nearly matched full MHA validation loss while showing a fused decode speedup versus materialized KV repetition; 1-KV MQA was faster but had a larger quality penalty.

## Why it stopped

Tier-2 medium local evidence was completed; it supports a bounded mechanism signal but is not broad or long enough for publication-grade validation.

## Recommended next action

Run a deeper local GPT-2-small-class or BPE-tokenized follow-up with the same full MHA, parameter-matched MHA, GQA, and MQA matrix over longer training and longer context before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE GPT-2-small-class GQA/MQA quality and decode validation
- Success threshold: GQA 2-KV mean validation loss within +0.01 of full MHA and better than parameter-matched MHA control, with at least 2x geomean fused decode speedup over materialized repeated KV at seq lengths including 1024 or longer.
- Stop condition: Stop as negative if GQA exceeds full MHA by more than +0.02 validation loss across seeds or fails to beat the parameter-matched MHA control while decode speedup remains the only benefit.

## Evidence references

- Artifact root: `<local-path>/projects/small-real-text-local-transformer-gqa-mqa-quality-and-fuse-1e21d3b2eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

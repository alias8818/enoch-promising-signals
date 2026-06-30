# Grouped-Query Attention KV Pareto Frontier on GPT-2-class Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `grouped-query-attention-kv-pareto-frontier-on-gpt-2-class-models-9ad6d929f9d5`
Run ID: `grouped-query-attention-kv-pareto-frontier-on-gpt-2-class-models-9ad6d929f9d5-20260609T110640064108+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ca73369961ca

## What looked useful

KV-cache memory scales linearly with KV-head count as expected, but naive post-training GQA conversion sharply degrades GPT-2-small quality: 12-head baseline loss 3.611/PPL 37.0 versus 6 KV heads loss 6.282/PPL 535.1 and 1 KV head loss 7.175/PPL 1306.6. Decode throughput did not improve in this implementation.

## Boundaries and scale limits

No training or finetuning; no long-context serving; Python/Transformers attention implementation uses simple PyTorch operations rather than production fused GQA kernels; validation subset is small.

## Claim scope

Pretrained GPT-2-small converted post hoc to GQA/MQA by contiguous mean-pooling of K/V projection heads, evaluated without retraining on 32 WikiText-2 validation chunks and a short cached decode benchmark.

## Why it stopped

Early bounded post-training conversion test produced a useful negative signal: the cache reduction is real, but the no-retraining conversion is not quality-viable; this is not full validation of trained GQA.

## Recommended next action

Run a bounded finetuning recovery test for the 6-KV-head conversion and stop unless validation loss recovers to within 0.3 nats of the MHA baseline while retaining the 50% KV-cache reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Finetuning recovery for GPT-2-small 6-KV-head GQA conversion
- Success threshold: Post-finetuning 6-KV-head validation loss within 0.3 nats of the MHA baseline and analytical KV-cache ratio 0.5 or lower.
- Stop condition: Stop if loss remains more than 0.8 nats above baseline after the bounded finetuning budget or if training instability prevents comparable evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/grouped-query-attention-kv-pareto-frontier-on-gpt-2-class-models-9ad6d929f9d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

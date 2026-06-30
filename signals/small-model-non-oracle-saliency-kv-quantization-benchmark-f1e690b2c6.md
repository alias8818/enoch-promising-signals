# Small-model non-oracle saliency KV quantization benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-model-non-oracle-saliency-kv-quantization-benchmark-f1e690b2c6`
Run ID: `small-model-non-oracle-saliency-kv-quantization-benchmark-f1e690b2c6-20260607T003415955485+0000`

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

- Parent run decision: Mixed-Precision KV Cache with Graceful Quality Degradation for Long Context Inference: enoch://control-plane/projects/mixed-precision-kv-cache-with-graceful-quality-degradation-for-long-context-inference-b547c22437b0/runs/mixed-precision-kv-cache-with-graceful-quality-degradation-for-long-context-inference-b547c22437b0-20260607T001404757326+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/63bd8534a579

## What looked useful

Non-oracle prefix-attention saliency is real but weak: on 256 examples it beat random mixed keeping by 0.0666 NLL and uniform 2-bit by 0.1027 NLL, yet trailed uniform 3-bit by 0.3685 NLL at 2.984 average KV bits.

## Boundaries and scale limits

Single pretrained small model, WikiText-2 only, 128-token prefixes, 32-token scoring suffixes, dequantized tensors rather than fused low-bit cache kernels, and nominal KV bit accounting that ignores scale/mask metadata overhead.

## Claim scope

On distilgpt2 with WikiText-2 suffix NLL, prefix-attention-received saliency for preserving 9 of 128 KV positions in fp16 while quantizing the rest to 2-bit improves over random keeping and uniform 2-bit, but fails to approach uniform 3-bit at the same nominal average KV-bit budget.

## Why it stopped

Tier 1 direct small-model test falsified the stated competitiveness threshold; this is an early direct negative for the simple saliency rule, not full-scale validation.

## Recommended next action

Stop this simple prefix-attention saliency variant as no-paper evidence; if continuing locally, test a bounded alternative non-oracle score such as KV reconstruction-error or value-norm saliency in the same harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Value-norm or reconstruction-error non-oracle KV saliency in the same small-model harness
- Success threshold: At <=3.0 nominal average KV bits, the best alternative saliency-mixed scheme must beat random-mixed, beat uniform 2-bit, and reduce the saliency-minus-uniform-3-bit NLL gap from 0.3685 to <=0.184 on the same 256-example protocol.
- Stop condition: Stop if no alternative non-oracle saliency score reduces the uniform-3-bit NLL gap by at least 50% or if metadata-aware accounting exceeds the uniform 3-bit budget.

## Evidence references

- Artifact root: `<local-path>/projects/small-model-non-oracle-saliency-kv-quantization-benchmark-f1e690b2c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

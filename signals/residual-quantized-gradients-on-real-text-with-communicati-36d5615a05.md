# Residual Quantized Gradients on Real Text with Communication Timing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-quantized-gradients-on-real-text-with-communicati-36d5615a05`
Run ID: `residual-quantized-gradients-on-real-text-with-communicati-36d5615a05-20260604T085415809611+0000`

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

- Parent run decision: Residual Quantized Gradients in Local torch.distributed Language Modeling: enoch://control-plane/projects/residual-quantized-gradients-in-local-torch-distributed-la-75337261e7/runs/residual-quantized-gradients-in-local-torch-distributed-la-75337261e7-20260604T063233725728+0000
- Parent run decision: DistilRes: Residual-Quant Gradients for Home Distributed Training: enoch://control-plane/projects/distilres-residual-quant-gradients-for-home-distributed-training-1b1f9b46c2f3/runs/distilres-residual-quant-gradients-for-home-distributed-training-1b1f9b46c2f3-20260604T044842874650+0000

## What looked useful

Residuals reduced the 4-bit validation-loss penalty from +0.4415 to +0.1924 nats versus dense while preserving about 8x payload reduction, but missed the +0.10 nats threshold. Plain 8-bit quantization matched dense within +0.0048 nats and gave about 2.25x estimated communication speedup, outperforming 8-bit residual quantization.

## Boundaries and scale limits

Single GB10 process with virtual workers; communication timing includes measured GPU compression/aggregation plus estimated 25 Gbps wire time, not real multi-node all-reduce. Model, context length, and 300-step training horizon are small compared with GPT-2-small-class or datacenter-scale training.

## Claim scope

On a small byte-level Transformer trained on WikiText-2 with 4 virtual workers, 4-bit residual/error-feedback quantization improves over 4-bit no-residual quantization but remains meaningfully worse than dense FP32 gradients; 8-bit no-residual quantization matches dense loss while reducing estimated communication.

## Why it stopped

Tier 2 direct real-text evidence was mixed: residuals helped the aggressive 4-bit ablation but failed the quality-preservation threshold, and the strongest practical result was non-residual 8-bit quantization.

## Recommended next action

Stop this residual-global-scale claim as no-paper evidence; the only bounded next test worth running is layerwise or blockwise 4-bit residual quantization against the same dense and 8-bit baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layerwise 4-bit Residual Quantized Gradients on WikiText-2
- Success threshold: Layerwise q4 residual mean final validation loss within +0.10 nats of dense, at least 6x payload reduction versus dense, estimated communication speedup above 2x, and lower loss than all q4 no-residual/global-scale q4 residual controls.
- Stop condition: Stop if layerwise q4 residual remains more than +0.10 nats worse than dense or fails to beat q8 no-residual on the quality/communication tradeoff.

## Evidence references

- Artifact root: `<local-path>/projects/residual-quantized-gradients-on-real-text-with-communicati-36d5615a05`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

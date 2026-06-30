# Real-dataset small-model QAT/PTQ comparison with exported quantized inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-dataset-small-model-qat-ptq-comparison-with-exported-9630e8e6b5`
Run ID: `real-dataset-small-model-qat-ptq-comparison-with-exported-9630e8e6b5-20260613T063231210439+0000`

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

- Parent run decision: Quantization-Aware Training of Small Models at Home: enoch://control-plane/projects/quantization-aware-training-of-small-models-at-home-59d94931b8d9/runs/quantization-aware-training-of-small-models-at-home-59d94931b8d9-20260613T061128562010+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/62aab312ff43

## What looked useful

QAT-vs-PTQ mechanism survived a controlled small direct real-dataset test with exported quantized inference: mean QAT accuracy 0.9458 vs mean PTQ accuracy 0.9268 on 2,000 MNIST test images, and exported model reload max absolute difference was 0.0 for all repeated seeds.

## Boundaries and scale limits

Small MNIST-only validation; one CNN architecture; one ARM/QNNPACK backend; TorchScript export only; PyTorch eager torch.ao.quantization emitted deprecation warnings; no harder dataset, modern torchao/PT2E flow, ONNX/ExecuTorch runtime, or production serving validation.

## Claim scope

On a compact CNN trained on 8,000 real MNIST images and evaluated on 2,000 held-out images, eager QAT followed by TorchScript-exported QNNPACK quantized CPU inference consistently beat PTQ-exported inference by 1.5 to 2.45 percentage points across three seeds, with comparable throughput and successful reload checks.

## Why it stopped

Tier 1 direct validation produced a useful mechanism signal but remains too narrow and uses a deprecated eager quantization API, so it is no-paper evidence rather than paper-positive evidence.

## Recommended next action

Run a bounded deepen follow-up on Fashion-MNIST or CIFAR-10 with a modern torchao/PT2E exportable quantization path and require QAT to beat PTQ by at least 1 percentage point mean accuracy across 3 seeds without lower exported inference throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder-dataset QAT/PTQ exported inference comparison with modern quantization APIs
- Success threshold: Mean QAT exported accuracy exceeds mean PTQ exported accuracy by at least 0.01 absolute accuracy across three seeds, all exported models reload and run, and QAT throughput is no more than 5% slower than PTQ.
- Stop condition: Stop if QAT fails to exceed PTQ by 0.01 mean absolute accuracy, if modern export/reload cannot run locally after ordinary dependency fixes, or if exported QAT inference is more than 5% slower than PTQ.

## Evidence references

- Artifact root: `<local-path>/projects/real-dataset-small-model-qat-ptq-comparison-with-exported-9630e8e6b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

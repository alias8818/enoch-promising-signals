# 4-bit quantization-aware training for home GPU fine-tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-quantization-aware-training-for-home-gpu-fine-tuning-f4f56da13a54`
Run ID: `4-bit-quantization-aware-training-for-home-gpu-fine-tuning-f4f56da13a54-20260527T151714452225+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d359c38564ef

## What looked useful

Quantization noise was not an early stability blocker at toy/local scale, but naive fake-quant QAT does not deliver the memory benefit needed for home GPU fine-tuning; memory savings require packed/storage-aware weights or adapter-only trainable state.

## Boundaries and scale limits

Small randomly initialized model, short 500-step runs, byte-level language modeling, fake quantization with full-precision parameters and optimizer state, no pretrained 7B-class model, no adapter-only fine-tuning, and no packed int4 kernels or downstream task evaluation.

## Claim scope

On a small byte-level Tiny Shakespeare causal Transformer on NVIDIA GB10, 4-bit fake-quantized QAT for linear projections trained stably and matched dense validation loss within about 0.002 mean loss over three replicated 500-step runs, but provided no peak CUDA allocation reduction and ran about 13% slower.

## Why it stopped

Bounded local evidence supports QAT stability but not the practical home-GPU memory claim; this is a mechanism/proxy result rather than full-scale validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test adapter-based QAT against a QLoRA-style frozen 4-bit pretrained GPT-2-small-class baseline with real peak-memory and downstream-loss thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adapter-based 4-bit QAT versus QLoRA-style frozen 4-bit fine-tuning on GPT-2-small-class tasks
- Success threshold: Adapter-QAT reaches validation/downstream quality within 1% of dense or QLoRA control while reducing peak CUDA allocation by at least 25% versus dense fine-tuning and losing no more than 20% throughput versus the strongest 4-bit control.
- Stop condition: Stop if adapter-QAT is more than 3% worse in validation/downstream quality after matched budget, fails numerically, or shows less than 10% peak-memory reduction versus dense fine-tuning when using a storage-aware implementation.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-quantization-aware-training-for-home-gpu-fine-tuning-f4f56da13a54`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

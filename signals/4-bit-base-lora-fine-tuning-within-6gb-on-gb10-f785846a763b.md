# 4-bit base LoRA fine-tuning within 6GB on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `4-bit-base-lora-fine-tuning-within-6gb-on-gb10-f785846a763b`
Run ID: `4-bit-base-lora-fine-tuning-within-6gb-on-gb10-f785846a763b-20260604T081644005097+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/be144912c7ce

## What looked useful

The standard QLoRA stack works on GB10/CUDA 13 for a 1.1B-class model: the strongest run completed 6 steps at seq_len=2048 and rank=16 with peak CUDA allocated 4,142,742,528 bytes, peak CUDA reserved 5,630,853,120 bytes, max RSS 1,889,349,632 bytes, and no swap.

## Boundaries and scale limits

Evidence is limited to one 1.1B-class model, synthetic token batches, short runs of 6-12 optimizer steps, and PyTorch allocator/process telemetry because nvidia-smi reports GB10 memory as Not Supported. It does not validate real dataset convergence, adapter quality, checkpoint reload fidelity, dense/control baselines, 3B/7B models, or longer runs.

## Claim scope

On this GB10 host with torch 2.12.0+cu130, transformers 4.57.6, bitsandbytes 0.49.2, and peft 0.19.1, TinyLlama/TinyLlama-1.1B-Chat-v1.0 loaded as a 4-bit NF4 base with bf16 compute and LoRA adapters completed synthetic causal-LM update steps under a 6 GiB CUDA memory budget up to batch_size=1, seq_len=2048, LoRA rank=16.

## Why it stopped

Bounded synthetic GB10 evidence supports the mechanism but is not a full validation of real fine-tuning quality or broader model sizes.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded deepen test should use a small real dataset with checkpoint reload and a dense/bf16 LoRA control at the same 1.1B scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-dataset GB10 QLoRA envelope with dense LoRA control
- Success threshold: 4-bit run completes with validation loss improvement from the initial checkpoint, successful adapter reload, peak CUDA reserved under 6 GiB, and at least 25% lower peak CUDA reserved memory than the bf16 LoRA control.
- Stop condition: Stop if 4-bit training OOMs below seq_len=1024, adapter reload fails, validation loss cannot be measured reproducibly, or the bf16 control uses equal or less CUDA reserved memory.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-base-lora-fine-tuning-within-6gb-on-gb10-f785846a763b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

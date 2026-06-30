# Autograd Transformer Micro-Batch Checkpoint Benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `autograd-transformer-micro-batch-checkpoint-benchmark-3f61def4fe`
Run ID: `autograd-transformer-micro-batch-checkpoint-benchmark-3f61def4fe-20260607T121319396191+0000`

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

- Parent run decision: Micro-Batch Gradient Checkpoint Trainer: enoch://control-plane/projects/micro-batch-gradient-checkpoint-trainer-249e99be2001/runs/micro-batch-gradient-checkpoint-trainer-249e99be2001-20260607T065225314796+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/bde5126b6812

## What looked useful

Checkpointing saved about 6, 10, 21, 48, and 60 MB peak RSS at micro-batches 1, 2, 4, 8, and 16 respectively, while median throughput ratios versus no-checkpoint were 0.279, 0.221, 0.514, 0.641, and 0.842. The mechanism is visible but not paper-ready.

## Boundaries and scale limits

CPU-only, synthetic random-token workload, small model, short context, no CUDA peak-memory counters, no mixed precision, no distributed training, no OOM-boundary search, and only 5 measured steps per condition.

## Claim scope

On a CPU PyTorch 2.12 small transformer language-model workload with 2.59M parameters, sequence length 128, effective batch 16, and 5 measured optimizer steps per condition, layer-wise activation checkpointing reduces sampled peak RSS increasingly with larger micro-batches but reduces median throughput; micro-batch sizing without checkpointing is the stronger local memory/speed lever.

## Why it stopped

Tier 1 controlled small direct test completed; evidence is useful for mechanism triage but insufficient for publication readiness.

## Recommended next action

Run a bounded GPU/GB10 deepen test using CUDA peak-memory counters and an OOM-boundary batch-size search on a GPT-2-small-class or parameter-matched transformer before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPU OOM-boundary micro-batch checkpoint benchmark
- Success threshold: Checkpointing must enable at least 25% larger non-OOM micro-batch or sequence length, or at least 20% lower CUDA peak memory at no worse than 80% tokens/s, on a real GPU transformer training workload.
- Stop condition: Stop if checkpointing fails to improve the non-OOM boundary and remains below 80% of no-checkpoint throughput for all tested GPU configurations.

## Evidence references

- Artifact root: `<local-path>/projects/autograd-transformer-micro-batch-checkpoint-benchmark-3f61def4fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

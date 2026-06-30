# Multi-seed production-kernel validation of queue-depth adaptive batching

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-seed-production-kernel-validation-of-queue-depth-ada-a38c0bec52`
Run ID: `multi-seed-production-kernel-validation-of-queue-depth-ada-a38c0bec52-20260607T140712257679+0000`

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

- Parent run decision: Queue-depth adaptive batching for gpu_worker: enoch://control-plane/projects/queue-depth-adaptive-batching-for-gpu-worker-5858c26ea014/runs/queue-depth-adaptive-batching-for-gpu-worker-5858c26ea014-20260607T053339411880+0000
- Parent run decision: Trace replay validation of queue-depth adaptive batching in a real gpu_worker: enoch://control-plane/projects/trace-replay-validation-of-queue-depth-adaptive-batching-i-cc30b2a4d4/runs/trace-replay-validation-of-queue-depth-adaptive-batching-i-cc30b2a4d4-20260607T072258585829+0000

## What looked useful

Depth-aware batching appears useful, but wait-based accumulation is the wrong mechanism in this bounded test. adaptive_nowait was best on both throughput and p95 latency at all three offered loads; target adaptive improved p95 versus fixed8 by 8-17% but reduced throughput by 1-3%.

## Boundaries and scale limits

Not a full production serving stack: no real user traces, tokenizer/model server overhead, KV-cache growth, mixed prefill/decode scheduling, multi-GPU behavior, or long-duration utilization profiling. Model block is compact BF16 seq192 dim512 on one GB10.

## Claim scope

A bounded GB10/PyTorch CUDA kernel-level serving benchmark with fixed synthetic arrival traces, 5 seeds, 3 offered loads, and 6 batching policies. The tested wait-based queue-depth adaptive policy improves p95 latency versus fixed8 but loses throughput and is dominated by the adaptive_nowait ablation.

## Why it stopped

Tier 2 bounded production-kernel validation produced a mixed/no-paper result: the target policy is not a Pareto improvement over a simple fixed8 baseline and is dominated by its no-wait ablation.

## Recommended next action

Stop paper escalation for the wait-based adaptive policy; deepen only by testing adaptive_nowait against fixed batching inside a real continuous batching backend with mixed prefill/decode traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Serving-stack validation of no-wait queue-depth thresholds
- Success threshold: adaptive_nowait p95 latency improves by >=10% versus fixed/default batching with throughput no worse than -2% at every tested load and no correctness/token-count regression.
- Stop condition: Stop if adaptive_nowait loses more than 2% throughput at any load, fails to reduce p95 by 10%, or backend overhead makes the scheduler effect indistinguishable from noise.

## Evidence references

- Artifact root: `<local-path>/projects/multi-seed-production-kernel-validation-of-queue-depth-ada-a38c0bec52`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

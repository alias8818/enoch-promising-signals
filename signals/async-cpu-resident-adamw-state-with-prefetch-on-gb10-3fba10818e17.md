# Async CPU-resident AdamW state with prefetch on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `async-cpu-resident-adamw-state-with-prefetch-on-gb10-3fba10818e17`
Run ID: `async-cpu-resident-adamw-state-with-prefetch-on-gb10-3fba10818e17-20260621T135932197557+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/071c007f934b

## What looked useful

Pinned CPU-state async prefetch is a real but modest GB10 mechanism: it consistently beat synchronous CPU-state AdamW in pinned-memory tests, failed with pageable CPU memory, and remained materially slower than GPU-resident state. The idea is useful as a memory-capacity tradeoff candidate, not as a paper-ready speed result.

## Boundaries and scale limits

This run used synthetic tensors, not end-to-end model training. It did not test autograd overlap, real parameter layouts, loss convergence, distributed training, checkpointing, allocator fragmentation, or capacity-limited training where GPU-resident AdamW fails. The most stable sustained run covered 8 chunks of 4,194,304 fp32 elements for 50 optimizer steps.

## Claim scope

On a synthetic chunked fp32 AdamW optimizer-step benchmark on NVIDIA GB10, pinned CPU-resident first/second moment state with double-buffered CUDA-stream prefetch/writeback was numerically equivalent to synchronous CPU-state AdamW and improved CPU-state optimizer-step throughput by 6.8% to 17.7% versus synchronous CPU-state copies, while remaining about 1.8x to 2.1x slower than GPU-resident optimizer state in non-smoke pinned runs.

## Why it stopped

Closed as no-paper useful signal because current evidence is a synthetic optimizer-step proxy: it supports modest pinned-prefetch benefit but does not validate end-to-end training behavior or a publication-grade claim.

## Recommended next action

Run a bounded real training-loop follow-up that integrates async CPU-resident AdamW state into a GPT-2-small-class or parameter-matched model and measures step time, peak memory, and loss parity against GPU-resident and synchronous CPU-state baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real training-loop validation for async CPU-resident AdamW state on GB10
- Success threshold: Async CPU-state AdamW preserves loss parity over the bounded run, reduces peak device-resident optimizer state materially versus GPU-resident AdamW, and is at least 10% faster than synchronous CPU-state AdamW or enables a capacity setting that GPU-resident AdamW cannot run.
- Stop condition: Stop if async CPU-state AdamW is not faster than synchronous CPU-state AdamW in the real training loop, fails loss parity, or the memory saved does not enable any meaningful batch/model capacity improvement.

## Evidence references

- Artifact root: `<local-path>/projects/async-cpu-resident-adamw-state-with-prefetch-on-gb10-3fba10818e17`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

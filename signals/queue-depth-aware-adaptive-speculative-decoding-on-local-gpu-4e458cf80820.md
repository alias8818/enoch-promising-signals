# Queue-Depth-Aware Adaptive Speculative Decoding on Local GPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `queue-depth-aware-adaptive-speculative-decoding-on-local-gpu-4e458cf80820`
Run ID: `queue-depth-aware-adaptive-speculative-decoding-on-local-gpu-4e458cf80820-20260609T113715087505+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/153d62b5b21c

## What looked useful

Across the main 16 workload/rate cells, adaptive policies had 1 p95 win, 4 ties, and 11 losses versus the best fixed policy, with mean p95 latency 5.77% worse and throughput 0.93% lower. In 24 replicated lower-rate cells, adaptive policies had 2 wins, 7 ties, and 15 losses, with mean p95 latency 3.95% worse and throughput 0.19% lower.

## Boundaries and scale limits

This run used a simulator with CUDA cost-ratio calibration, not real transformer serving. It did not test KV-cache pressure, batching, real prompt acceptance, scheduler overhead, or production traces.

## Claim scope

In a bounded single-GPU FIFO queue simulator calibrated with local GB10 CUDA target/draft proxy costs, queue-depth-only speculative draft-length adaptation did not consistently beat the best fixed draft length on p95 latency or throughput.

## Why it stopped

Proxy/early falsification: the directly tested simulator did not support queue depth alone as a robust adaptive speculative decoding signal, though real serving evidence could overturn this.

## Recommended next action

Stop queue-depth-only testing as an early proxy falsification; the next bounded test should add request-level acceptance/confidence estimation and compare it against fixed draft lengths and queue-only thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Acceptance-Aware Adaptive Speculative Draft Length Under Queueing
- Success threshold: Confidence-plus-queue adaptation improves p95 latency by at least 5% versus the best fixed draft length while keeping throughput within 2%, across at least three seeds or traces.
- Stop condition: Stop if confidence-plus-queue adaptation fails to beat the best fixed draft length by at least 2% p95 latency on two consecutive bounded traces or if implementation cannot produce real acceptance diagnostics.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-aware-adaptive-speculative-decoding-on-local-gpu-4e458cf80820`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

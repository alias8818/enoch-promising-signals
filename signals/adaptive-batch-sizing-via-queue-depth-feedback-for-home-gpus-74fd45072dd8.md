# Adaptive batch sizing via queue depth feedback for home GPUs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `adaptive-batch-sizing-via-queue-depth-feedback-for-home-gpus-74fd45072dd8`
Run ID: `adaptive-batch-sizing-via-queue-depth-feedback-for-home-gpus-74fd45072dd8-20260608T014753284590+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e4978c02a2ea

## What looked useful

The no-wait fixed_max_64 baseline had the best p95 latency in all four scenarios. Adaptive threshold was 0.1% to 47.6% worse on p95, and adaptive AIMD was 2.4% to 100.1% worse, with no throughput gain. Queue-depth feedback alone mainly underbatched relative to a work-conserving max-batch baseline.

## Boundaries and scale limits

Not a full LLM-serving validation. Service times use a small FP16 matmul+GELU proxy with relative batch efficiency measured on GB10 and absolute service times scaled to a 1200 requests/s replay target. Traffic is synthetic, and memory pressure, decode/prefill differences, real traces, and timeout-based batch filling are not covered.

## Claim scope

On a GB10 toy CUDA batch-service proxy with synthetic arrival traces, queue-depth adaptive batch sizing did not outperform a work-conserving fixed maximum batch policy that dispatches immediately with up to 64 queued requests.

## Why it stopped

Bounded proxy evidence falsified the simple queue-depth-feedback claim against the strongest local baseline tested; this is not full LLM-serving validation.

## Recommended next action

Stop this no-paper proxy result; the next bounded test should use a real home-GPU LLM serving harness with timeout-based fixed batching and SLO-aware adaptive batching if further evidence is desired.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SLO-aware adaptive batching against timeout fixed batching on a real home-GPU LLM server
- Success threshold: Adaptive SLO-aware batching reduces p95 latency by at least 10% versus timeout fixed batching while matching throughput within 3% and avoiding memory regressions.
- Stop condition: Stop if no-wait max-batch or timeout fixed-batch matches or beats adaptive p95 at matched throughput across at least three bursty traces.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-batch-sizing-via-queue-depth-feedback-for-home-gpus-74fd45072dd8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

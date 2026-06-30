# Real Trace Replay for Tight Bounded Volunteer GPU Queue

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-trace-replay-for-tight-bounded-volunteer-gpu-queue-5c77d74d90`
Run ID: `real-trace-replay-for-tight-bounded-volunteer-gpu-queue-5c77d74d90-20260614T040712753091+0000`

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

- Parent run decision: Trace-Replay Bounded Queue Depth Test for Volunteer GPU Worker: enoch://control-plane/projects/trace-replay-bounded-queue-depth-test-for-volunteer-gpu-wo-813a8ff492/runs/trace-replay-bounded-queue-depth-test-for-volunteer-gpu-wo-813a8ff492-20260614T032601557430+0000
- Parent run decision: Bounded Queue Depth Test for Volunteer GPU Worker: enoch://control-plane/projects/bounded-queue-depth-test-for-volunteer-gpu-worker-d24b0bf2aa37/runs/bounded-queue-depth-test-for-volunteer-gpu-worker-d24b0bf2aa37-20260614T030621938367+0000

## What looked useful

Real-trace replay supports a bounded-admission mechanism only as an overload-control tool: it can make waits predictable and outperform random shedding, but the useful region is narrow and not paper-ready because small pools shed too much work and large pools do not need the mechanism.

## Boundaries and scale limits

Replay uses fixed aggregate volunteer capacity, known trace runtimes, and nonpreemptive jobs. It does not model volunteer churn, heterogeneous devices, network locality, prediction error, fallback completion/cost, or production admission overhead. At 64-256 GPUs the mechanism rejects 55.7-87.1% of GPU-hours; at 1024 GPUs FIFO already satisfies the bound.

## Claim scope

On the public Microsoft Philly DNN GPU trace, a simple bounded admission FIFO replay can enforce 6h/24h wait bounds at fixed volunteer capacities, but only with a capacity-dependent rejected-work tradeoff. The strongest full-trace useful point is 512 GPUs with 64.1% accepted jobs, 23.4% rejected GPU-hours, zero 6h SLA misses, and better rejected-GPU-hour/utilization tradeoff than random shedding at the same acceptance rate.

## Why it stopped

Medium real-trace validation produced mixed evidence: mechanism support exists at 512 GPUs, but the result is not robust or novel enough for paper escalation because lower capacities reject most work and higher capacities are matched by FIFO.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should replace FIFO admission with deadline-aware backfill/prediction and require at least 80% accepted jobs, no more than 20% rejected GPU-hours, and under 1% 6h SLA misses at 512 GPUs on the full Philly trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deadline-Aware Backfill Admission for Bounded Volunteer GPU Replay
- Success threshold: At 512 GPUs on the full retained Philly trace: accepted jobs >= 80%, rejected GPU-hours <= 20%, 6h SLA miss rate <= 1%, p95 wait <= 6h, and rejected GPU-hour rate at least 10 percentage points lower than matched random shedding.
- Stop condition: Stop negative if the policy cannot reach accepted jobs >= 70% and rejected GPU-hours <= 30% while keeping 6h SLA miss rate <= 1% on the full trace, or if gains disappear under moderate runtime prediction error.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-replay-for-tight-bounded-volunteer-gpu-queue-5c77d74d90`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

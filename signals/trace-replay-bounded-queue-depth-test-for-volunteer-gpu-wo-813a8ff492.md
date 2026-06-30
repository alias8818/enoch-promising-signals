# Trace-Replay Bounded Queue Depth Test for Volunteer GPU Worker

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-replay-bounded-queue-depth-test-for-volunteer-gpu-wo-813a8ff492`
Run ID: `trace-replay-bounded-queue-depth-test-for-volunteer-gpu-wo-813a8ff492-20260614T032601557430+0000`

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

- Parent run decision: Bounded Queue Depth Test for Volunteer GPU Worker: enoch://control-plane/projects/bounded-queue-depth-test-for-volunteer-gpu-worker-d24b0bf2aa37/runs/bounded-queue-depth-test-for-volunteer-gpu-worker-d24b0bf2aa37-20260614T030621938367+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b55635fe84fe

## What looked useful

A very small bounded ingress queue can provide backpressure that prevents burst backlog and pending payload growth in this direct GB10 trace-replay worker without reducing completed-job throughput.

## Boundaries and scale limits

Synthetic trace and payloads only; single worker process; no real volunteer fleet trace, network ingress, production model kernels, retry/cancellation behavior, or multi-worker scheduling. Not publication-grade evidence.

## Claim scope

On a single controlled 240-request synthetic burst trace replayed through one actual CUDA-backed GB10 worker, queue cap 1 bounded admitted depth to 1, reduced max pending payload from 84 MiB to 36 MiB, preserved approximately 100% of unbounded throughput, and reduced p95 wait.

## Why it stopped

Tier 1 controlled direct test met the local mechanism threshold for cap 1, but the evidence is synthetic single-worker evidence and is not sufficient for a paper.

## Recommended next action

Run a bounded deepen test using real or recorded volunteer-worker traces and production-like payload staging, requiring cap <= 2 to preserve at least 90% throughput while reducing max pending payload by at least 50%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Replay for Tight Bounded Volunteer GPU Queue
- Success threshold: A cap <= 2 keeps admitted queue depth at or below the cap, reduces max pending payload residency by >=50% versus unbounded, and preserves >=90% completed-job throughput across the tested real trace windows.
- Stop condition: Stop if caps <= 2 fall below 90% throughput, fail to reduce max pending payload by 50%, or if no real/production-derived trace can be obtained for direct replay.

## Evidence references

- Artifact root: `<local-path>/projects/trace-replay-bounded-queue-depth-test-for-volunteer-gpu-wo-813a8ff492`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Evidence Ledger Pressure Test: Queue Depth 21 vs 25 on GPU Worker Reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-pressure-test-queue-depth-21-vs-25-on-gpu-worker-reliability-67024a372029`
Run ID: `evidence-ledger-pressure-test-queue-depth-21-vs-25-on-gpu-worker-reliability-67024a372029-20260608T095913460314+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/51028fbb9717

## What looked useful

Depth 25 was reliable in the bounded local test but gave no operational win over depth 21: 75/75 tasks succeeded at depth 25 and 63/63 at depth 21, while depth 25 per-task iteration rate was about 82.5% of depth 21 and aggregate throughput was slightly lower in each repeat.

## Boundaries and scale limits

Single-worker, short-duration synthetic workload only: 3 repeats per depth, 20 seconds per task, depths 21 and 25, 768 MiB scratch per task. This does not validate production Enoch controller behavior, multi-worker scheduling, long-running training jobs, or datacenter-scale reliability.

## Claim scope

On one local GB10 GPU worker running synthetic concurrent PyTorch CUDA matmul pressure, queue depths 21 and 25 both completed all planned tasks without failures; depth 25 did not improve aggregate throughput and reduced per-task iteration rate relative to depth 21.

## Why it stopped

Bounded local pressure test completed and produced a useful no-paper result: no reliability regression at depth 25, but no throughput advantage over depth 21; this is not full production validation.

## Recommended next action

Keep queue depth 21 as the conservative default unless a production-shaped Enoch controller run shows depth 25 improves end-to-end throughput without increasing failures.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-shaped Enoch queue-depth alternation test for depths 21 and 25
- Success threshold: Depth 25 must improve completed tasks per hour by at least 5% over depth 21 with no increase in task failures, retries, or p95 callback latency.
- Stop condition: Stop early if either depth records two worker/process failures, MemAvailable falls below the local safety threshold, or depth 25 shows less than 5% throughput improvement after two balanced windows.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-pressure-test-queue-depth-21-vs-25-on-gpu-worker-reliability-67024a372029`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

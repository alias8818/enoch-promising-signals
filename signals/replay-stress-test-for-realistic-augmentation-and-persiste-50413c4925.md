# Replay stress test for realistic augmentation and persistent worker pipelines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `replay-stress-test-for-realistic-augmentation-and-persiste-50413c4925`
Run ID: `replay-stress-test-for-realistic-augmentation-and-persiste-50413c4925-20260610T182839763610+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Deterministic CPU replay across process restarts with DataLoader workers and threaded kernels: enoch://control-plane/projects/deterministic-cpu-replay-across-process-restarts-with-data-5c2ec58fee/runs/deterministic-cpu-replay-across-process-restarts-with-data-5c2ec58fee-20260610T174352036934+0000
- Parent run decision: Framework-level deterministic CPU gradient replay with process restarts: enoch://control-plane/projects/framework-level-deterministic-cpu-gradient-replay-with-pro-ae63f60887/runs/framework-level-deterministic-cpu-gradient-replay-with-pro-ae63f60887-20260610T152729884910+0000

## What looked useful

Persistent replay preserved 269,009/269,009 expected outputs with zero missing, duplicate, unexpected, or hash-mismatched outputs under repeated mid-claim crashes, while the volatile in-memory baseline missed 267,169 outputs under the same crash schedule and both designs were correct in the matched no-crash control.

## Boundaries and scale limits

Synthetic 1 KiB hash-based augmentation payloads only; single worker subprocess at a time; local SQLite WAL persistence; no real augmentation library, object store, distributed queue, multi-worker contention, Kubernetes eviction, or 24-hour soak.

## Claim scope

A single-worker SQLite-backed persistent augmentation queue with deterministic replay and idempotent output keys recovered complete, duplicate-free, hash-stable outputs after 435 injected mid-claim process crashes across three fixed seeds and 269,009 expected synthetic augmentation outputs.

## Why it stopped

The local stress result supports the replay/persistence mechanism but remains synthetic and single-worker, so it is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Run one bounded depth-4 deepen test with concurrent workers and a real augmentation backend; stop if any missing, duplicate, unexpected, or hash-mismatched output appears.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent real-augmentation replay stress for persistent workers
- Success threshold: Persistent pipeline produces 100% of expected outputs with zero duplicate IDs and zero content mismatches across all seeds while the crash baseline fails or a non-crash control verifies ordinary augmentation correctness.
- Stop condition: Stop as negative/no-paper if any persistent run has missing outputs, duplicate output IDs, content mismatches, unrecovered stale claims, or requires resource scale beyond the local bounded deployment.

## Evidence references

- Artifact root: `<local-path>/projects/replay-stress-test-for-realistic-augmentation-and-persiste-50413c4925`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

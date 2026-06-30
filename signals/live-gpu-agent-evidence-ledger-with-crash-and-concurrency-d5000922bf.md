# Live GPU-Agent Evidence Ledger With Crash and Concurrency Checks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-gpu-agent-evidence-ledger-with-crash-and-concurrency-d5000922bf`
Run ID: `live-gpu-agent-evidence-ledger-with-crash-and-concurrency-d5000922bf-20260630T015832198802+0000`

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

- Parent run decision: Evidence Ledger for Local GPU Agents: enoch://control-plane/projects/evidence-ledger-for-local-gpu-agents-1e0531e52f47/runs/evidence-ledger-for-local-gpu-agents-1e0531e52f47-20260629T224531940425+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f57ede06da9f

## What looked useful

Crash stress completed 36/36 CUDA tasks with 13 recovered claims, 7 crash-after-claim exits, 6 crash-after-GPU exits, intact hash chain, no duplicate done events, no orphan done events, and no lost ownership. A short-lease negative control with 50 ms stale timeout produced 2 lost-ownership events despite clean terminal accounting, showing lease calibration is necessary.

## Boundaries and scale limits

Tested only on one GB10 host, one SQLite database, four concurrent worker processes, 36 small CUDA tasks, and synthetic matrix-work evidence payloads. Not tested for long-running LLM agents, high memory pressure, multi-GPU, multi-node, network filesystems, or adversarial online tampering.

## Claim scope

A local SQLite WAL evidence ledger with hash-chained events can recover crashed small CUDA worker claims without duplicate or orphan completions when the stale-claim lease is calibrated above observed GPU task latency.

## Why it stopped

No-paper useful signal: bounded local crash/concurrency evidence supports the calibrated-lease mechanism, but the short-lease negative control shows the simple fixed-lease design is not robust enough for publication-grade claims.

## Recommended next action

Run a bounded deepen test implementing heartbeat-based lease renewal and compare it against fixed stale leases under variable GPU task latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Heartbeat-Renewed GPU Evidence Ledger Lease Robustness
- Success threshold: Across at least 200 local CUDA tasks with four or more concurrent workers, injected crash-after-claim and crash-after-GPU probabilities of at least 10% each, and variable task durations spanning at least 20x, heartbeat renewal has zero lost-ownership, duplicate-done, orphan-done, pending, claimed, or failed tasks with less than 10% wall-clock overhead versus a calibrated fixed lease.
- Stop condition: Stop if heartbeat renewal still produces any lost ownership or duplicate completion in two consecutive runs, or if overhead exceeds 25% on the local GB10 workload.

## Evidence references

- Artifact root: `<local-path>/projects/live-gpu-agent-evidence-ledger-with-crash-and-concurrency-d5000922bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

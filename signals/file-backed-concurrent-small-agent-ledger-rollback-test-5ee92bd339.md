# File-Backed Concurrent Small-Agent Ledger Rollback Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `file-backed-concurrent-small-agent-ledger-rollback-test-5ee92bd339`
Run ID: `file-backed-concurrent-small-agent-ledger-rollback-test-5ee92bd339-20260522T154144494293+0000`

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

- Parent run decision: Small-Agent Evidence Ledger with Rollback: enoch://control-plane/projects/small-agent-evidence-ledger-with-rollback-1ce70bd75f24/runs/small-agent-evidence-ledger-with-rollback-1ce70bd75f24-20260522T142314527859+0000
- Parent run decision: Real Small-Agent Evidence Ledger Rollback Harness: enoch://control-plane/projects/real-small-agent-evidence-ledger-rollback-harness-644b4e665f/runs/real-small-agent-evidence-ledger-rollback-harness-644b4e665f-20260522T145924343297+0000

## What looked useful

The mechanism signal is positive: append-only commit/abort records are enough to prevent failed transaction leakage under the tested concurrent small-agent workload. The lock-only ablation failed exact recovery on every seed, isolating rollback records as the useful mechanism. This is not paper-ready because SQLite WAL is a stronger practical baseline and the durability campaign is narrow.

## Boundaries and scale limits

Not tested on real LLM agents, multi-host filesystems, disk-full/fsync failure, arbitrary kill points around every append boundary, ledger compaction, long-running log growth, or non-balance external side effects. SQLite WAL was about 2.3x faster than the file ledger in this local workload.

## Claim scope

In a local deterministic multiprocessing benchmark with 8 small agents, 64-account transfer state, 5 fixed seeds, 800 attempted operations per run, and 5% pre-commit failure injection, an append-only JSONL file ledger with exclusive append locking recovered exactly the committed operation state on 5/5 runs, matching SQLite WAL correctness and outperforming naive and lock-only file controls on rollback correctness.

## Why it stopped

Tier 2 local validation produced useful mechanism support but not publication-grade novelty or robustness; SQLite WAL matched correctness with higher throughput.

## Recommended next action

Run a bounded kill-point durability follow-up with process termination around each ledger append/fsync boundary plus snapshot compaction before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Kill-Point Durability and Compaction Test for File-Backed Agent Ledger
- Success threshold: File ledger and SQLite WAL both achieve 100% exact recovery across all fixed seeds and kill points; file ledger has zero parse errors, zero committed-operation mismatches, and recovered state equal to committed replay before and after compaction.
- Stop condition: Stop as unsupported if any committed transaction is lost, any aborted transaction is applied, any ledger parse error prevents recovery, or compaction changes recovered state on a reproducible seed.

## Evidence references

- Artifact root: `<local-path>/projects/file-backed-concurrent-small-agent-ledger-rollback-test-5ee92bd339`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

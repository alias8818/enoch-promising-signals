# Hash-Chained Evidence Ledger for Local Agent Task Boundaries

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chained-evidence-ledger-for-local-agent-task-boundaries-4e305cdb85d2`
Run ID: `hash-chained-evidence-ledger-for-local-agent-task-boundaries-4e305cdb85d2-20260630T035022658197+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/10b86387d25e

## What looked useful

Anchored verification detected all six injected mutation classes in 10/10 cases while sustaining at least 130,584 ledger events/s and 215,545 verification events/s. Without an external anchor, truncation and full recomputation were detected in 0/10 cases, establishing that hash chaining alone is insufficient for local task-boundary evidence.

## Boundaries and scale limits

Tested only in a deterministic Python harness with 550,000 clean synthetic events plus mutation variants across 10 cases. Not integrated into a live agent runtime, not tested against logging suppression, compromised supervisors, concurrent writers, crash recovery, or real external anchor services.

## Claim scope

Synthetic local-agent JSONL event streams show that a canonical SHA-256 hash-chained ledger can verify clean task-boundary evidence and detect modification, deletion, reorder, boundary escape, truncation, and full recomputation mutations when the verifier has a trusted external final hash anchor.

## Why it stopped

No-paper useful signal: the synthetic result supports the mechanism and exposes the anchor requirement, but direct live-agent evidence is still missing.

## Recommended next action

Run a live local-agent supervisor integration with periodic external anchor checkpoints and adversarial task-boundary fault injection before considering a bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live supervisor hash-chain ledger with external anchor checkpoints
- Success threshold: Detect 100% of injected ledger tampering and boundary-escape faults across at least 30 live-agent task runs while keeping p95 event-recording overhead below 10 ms and demonstrating recovery from an interrupted run.
- Stop condition: Stop as negative if live integration misses any anchored tamper class, cannot reliably anchor checkpoints outside the mutable ledger, or adds overhead that materially disrupts local-agent task execution.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-evidence-ledger-for-local-agent-task-boundaries-4e305cdb85d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

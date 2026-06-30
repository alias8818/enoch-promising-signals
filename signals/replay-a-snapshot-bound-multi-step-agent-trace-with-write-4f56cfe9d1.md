# Replay a snapshot-bound multi-step agent trace with write operations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-a-snapshot-bound-multi-step-agent-trace-with-write-4f56cfe9d1`
Run ID: `replay-a-snapshot-bound-multi-step-agent-trace-with-write-4f56cfe9d1-20260529T164113306347+0000`

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

- Parent run decision: Replay Real Agent Workspace Traces Through a Checksum Ledger: enoch://control-plane/projects/replay-real-agent-workspace-traces-through-a-checksum-ledg-92bd44098e/runs/replay-real-agent-workspace-traces-through-a-checksum-ledg-92bd44098e-20260529T061647418654+0000
- Parent run decision: Local Checksum Ledger for CPU Agent Reliability: enoch://control-plane/projects/local-checksum-ledger-for-cpu-agent-reliability-9e0b3745af8e/runs/local-checksum-ledger-for-cpu-agent-reliability-9e0b3745af8e-20260529T015143383309+0000

## What looked useful

Snapshot binding and per-step integrity checks appear to solve different replay requirements: snapshot binding enables deterministic reproduction after environment drift, while per-step checks catch invalidating writes. Removing either component fails one of those target metrics.

## Boundaries and scale limits

Synthetic text-file traces only; single process; no real LLM/tool traces, concurrent writes, large repositories, binary files, symlinks, permissions, OS metadata, network tools, or production LangGraph persistence semantics were tested.

## Claim scope

On 200 fixed-seed synthetic filesystem traces with 24 real file-write steps each, snapshot-bound replay reproduced valid final workspace states after adversarial pre-replay drift, while live unbound replay did not; per-step hash checks detected injected mid-run invalidating writes.

## Why it stopped

Medium synthetic filesystem-backed evidence supports the mechanism but is not direct real-agent evidence and is not paper-positive.

## Recommended next action

Run a deepen follow-up on captured real multi-step agent traces over repository-scale snapshots before considering any paper gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay real captured agent traces with repository-scale snapshot binding
- Success threshold: Snapshot-bound replay reaches >=95% valid final-match rate and >=95% invalid-write detection, with <=5% false rejection on valid traces and >=50 percentage point final-match improvement over live unbound replay.
- Stop condition: Stop if real captured traces cannot be obtained locally, if snapshot-bound replay falls below 80% valid final-match rate, or if failures are dominated by unmodeled external side effects that the snapshot manifest cannot represent.

## Evidence references

- Artifact root: `<local-path>/projects/replay-a-snapshot-bound-multi-step-agent-trace-with-write-4f56cfe9d1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

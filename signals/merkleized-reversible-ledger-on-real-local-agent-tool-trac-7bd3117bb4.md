# Merkleized reversible ledger on real local-agent tool traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `merkleized-reversible-ledger-on-real-local-agent-tool-trac-7bd3117bb4`
Run ID: `merkleized-reversible-ledger-on-real-local-agent-tool-trac-7bd3117bb4-20260528T014530988576+0000`

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

- Parent run decision: Reversible tool-call ledger for home CPU agents: enoch://control-plane/projects/reversible-tool-call-ledger-for-home-cpu-agents-c9003b79fdcc/runs/reversible-tool-call-ledger-for-home-cpu-agents-c9003b79fdcc-20260527T201030942256+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0b5705bd13e5

## What looked useful

Mechanism support: real local-agent events can be canonicalized into a verifiable Merkleized append-only ledger, and exact reversal is feasible when tool-effect records capture before/after state. This is useful engineering evidence but not paper-positive.

## Boundaries and scale limits

Small single-run trace only; reversibility was demonstrated for controlled local file mutations, not arbitrary real shell commands, process effects, network effects, databases, concurrency, large files, permissions, symlinks, or long-running crash recovery.

## Claim scope

Tier-1 local test: a Merkleized hash-chain ledger over a frozen real Codex/Enoch JSONL trace verified 35 actual local-agent events and detected payload tampering; a controlled four-event local file-effect trace with captured before/after state rolled back and replayed exactly.

## Why it stopped

Tier-1 mechanism test passed, but the evidence is no-paper useful signal because arbitrary real tool calls were not reversibly instrumented.

## Recommended next action

Run a deepen follow-up with a real local-agent file-tool wrapper that captures side-effect deltas for actual agent actions, then require exact rollback/replay and tamper detection on a mixed success/failure trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Runtime-instrumented reversible ledger for real local-agent file tool calls
- Success threshold: Pass if 25 or more real wrapped tool operations verify under the Merkleized ledger, rollback and replay match byte-for-byte filesystem snapshots, and payload/order/delta tampering are all detected with under 2x runtime overhead on the small trace.
- Stop condition: Stop negative if any committed wrapped operation cannot be rolled back byte-for-byte, if any tamper class is not detected, or if required side-effect capture is impractical for ordinary file-tool operations.

## Evidence references

- Artifact root: `<local-path>/projects/merkleized-reversible-ledger-on-real-local-agent-tool-trac-7bd3117bb4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

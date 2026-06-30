# Small Agent Evidence Ledger with Reversible Action Log

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-agent-evidence-ledger-with-reversible-action-log-f44f20551a3b`
Run ID: `small-agent-evidence-ledger-with-reversible-action-log-f44f20551a3b-20260527T102755187669+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9e30e000efb9

## What looked useful

Inverse-delta evidence ledgers are practical for small sparse action traces and can be much smaller than snapshots, but naive full-state verification is the main scaling bottleneck.

## Boundaries and scale limits

Synthetic single-process CPU-only tests; no real agent traces, concurrent writers, crash recovery, durable storage backend, or large adversarial evaluation. Verification re-hashes replayed state and scales poorly with live-state size.

## Claim scope

Local Python prototype on synthetic sparse key-value agent-action workloads up to 5,000 actions showed reversible inverse-delta rollback, deterministic replay, hash-bound evidence records, and simple tamper detection, with lower serialized storage than full-state snapshots when state is sparse/growing.

## Why it stopped

No-paper useful signal: bounded synthetic evidence supports the mechanism but does not provide direct real-agent or scalable verification evidence.

## Recommended next action

Run a bounded deepen experiment with a Merkleized state digest plus serialized crash/recovery replay on recorded agent tool traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Merkleized Evidence Ledger on Recorded Agent Tool Traces
- Success threshold: On at least 10,000 recorded or realistic actions, Merkleized verification remains correct and reduces verify time per action by at least 5x versus full-state hashing while keeping serialized ledger size within 2x of the current inverse-delta format.
- Stop condition: Stop if Merkleized verification fails replay/rollback correctness, fails to detect tampering, or does not improve verify time by at least 2x on the 10,000-action trace.

## Evidence references

- Artifact root: `<local-path>/projects/small-agent-evidence-ledger-with-reversible-action-log-f44f20551a3b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

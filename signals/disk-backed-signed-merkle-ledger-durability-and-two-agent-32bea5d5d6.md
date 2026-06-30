# Disk-backed signed Merkle ledger durability and two-agent synchronization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `disk-backed-signed-merkle-ledger-durability-and-two-agent-32bea5d5d6`
Run ID: `disk-backed-signed-merkle-ledger-durability-and-two-agent-32bea5d5d6-20260609T020905041154+0000`

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

- Parent run decision: Merkle Evidence Ledger for Small Agents: enoch://control-plane/projects/merkle-evidence-ledger-for-small-agents-21af43a5630b/runs/merkle-evidence-ledger-for-small-agents-21af43a5630b-20260608T234540882146+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48099f486882

## What looked useful

Tier 1 direct test supports the mechanism: 256 records appended and synced, roots matched, 94-byte partial tail was truncated back to 132900 committed bytes and 256 lines, root was preserved, and tampering was detected by verification.

## Boundaries and scale limits

Single local host, deterministic harness, HMAC signatures, one writer, one syncing follower, 256 records, simulated torn tail only; no multi-host network, public-key signatures, concurrent writers, real process-kill/power-loss fault injection, key rotation, or long-duration/large-ledger validation.

## Claim scope

A small single-process local-disk Python ledger can durably append 256 signed Merkle-chain records, synchronize a second agent from zero to the same root, recover by truncating an unterminated crash tail without losing committed records, and detect tampering in persisted records.

## Why it stopped

Tier 1 direct mechanism support was achieved, but the evidence is local and bounded rather than publication-grade durability or synchronization validation.

## Recommended next action

Run a bounded deepen test with process-kill fault injection around append/fsync boundaries and asymmetric signing before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Process-kill durability and asymmetric-signature sync test for disk-backed Merkle ledger
- Success threshold: Zero accepted corrupt records, zero root divergences after recovery plus resync, and all recoveries truncate only incomplete trailing records across at least 100 randomized fault-injection trials.
- Stop condition: Stop on any accepted tampered record, unrecoverable committed-prefix corruption, or reproducible root divergence after resync.

## Evidence references

- Artifact root: `<local-path>/projects/disk-backed-signed-merkle-ledger-durability-and-two-agent-32bea5d5d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

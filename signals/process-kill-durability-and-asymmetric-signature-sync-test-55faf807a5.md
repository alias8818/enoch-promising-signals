# Process-kill durability and asymmetric-signature sync test for disk-backed Merkle ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `process-kill-durability-and-asymmetric-signature-sync-test-55faf807a5`
Run ID: `process-kill-durability-and-asymmetric-signature-sync-test-55faf807a5-20260609T151845286522+0000`

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

- Parent run decision: Disk-backed signed Merkle ledger durability and two-agent synchronization: enoch://control-plane/projects/disk-backed-signed-merkle-ledger-durability-and-two-agent-32bea5d5d6/runs/disk-backed-signed-merkle-ledger-durability-and-two-agent-32bea5d5d6-20260609T020905041154+0000
- Parent run decision: Merkle Evidence Ledger for Small Agents: enoch://control-plane/projects/merkle-evidence-ledger-for-small-agents-21af43a5630b/runs/merkle-evidence-ledger-for-small-agents-21af43a5630b-20260608T234540882146+0000

## What looked useful

The direct tests support the mechanism: durable JSONL and SQLite recovered 2468/2468 ACKed records with zero invalid records, while the unsafe ACK-before-write control lost 30 ACKed records across 30/30 trials. Asymmetric sync accepted 100% of legitimate records and 0% of receiver-forged records; unsigned and HMAC baselines accepted 100% of forged records under receiver compromise.

## Boundaries and scale limits

Validated on small local ledgers only: 90 process-kill trials total, 30 per durability backend, and 10 sync trials per signature mode. This does not cover production implementation behavior, sudden power loss, filesystem/storage-controller failure modes, distributed sync races, or signer private-key compromise.

## Claim scope

In a self-contained Python disk-backed Merkle ledger harness, ACK-after-fsync JSONL and SQLite WAL synchronous=FULL recovered all ACKed records after deterministic SIGKILL trials, and RSA-PSS public-key sync rejected receiver-forged records that unsigned and shared-secret HMAC baselines accepted.

## Why it stopped

Mechanism supported in a controlled local harness with fixed seeds, ablations, and SQLite baseline, but evidence is not production-grade or paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up on the target ledger implementation with filesystem or power-loss fault injection and the same receiver-compromise sync test.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Target-ledger crash and receiver-compromise validation with filesystem fault injection
- Success threshold: At least 100 process-kill/fault-injection trials with zero ACKed-record loss, zero accepted invalid Merkle roots/signatures, and zero receiver-forged records accepted by asymmetric sync, while unsafe or symmetric controls show the expected failure mode.
- Stop condition: Stop negative if the target ledger loses any ACKed record, accepts any invalid root/signature, or accepts any receiver-forged asymmetric-sync record under the fixed-seed test protocol.

## Evidence references

- Artifact root: `<local-path>/projects/process-kill-durability-and-asymmetric-signature-sync-test-55faf807a5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

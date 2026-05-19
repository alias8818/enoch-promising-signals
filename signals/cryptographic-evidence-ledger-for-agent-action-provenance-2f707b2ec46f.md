# Cryptographic Evidence Ledger for Agent Action Provenance

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cryptographic-evidence-ledger-for-agent-action-provenance-2f707b2ec46f`
Run ID: `cryptographic-evidence-ledger-for-agent-action-provenance-2f707b2ec46f-20260516T021034528032+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/40feb6f09d0c

## What looked useful

The prototype shows that signed hash-chain provenance for agent actions is technically viable at small-to-medium local scale with all tested tamper cases detected and with measurable but practical overhead versus unsigned JSONL logging.

## Boundaries and scale limits

Evidence is limited to synthetic single-process traces on one machine. It does not validate live agent runtime integration, concurrent writers, remote transparency anchoring, timestamp authority use, key compromise or rotation, crash recovery, privacy redaction, or comparison against existing production audit/provenance systems.

## Claim scope

A local prototype using SHA-256 hash chaining, Ed25519 per-entry signatures, periodic Merkle checkpoints, and a final signed anchor made deterministic synthetic agent action traces up to 100,000 events tamper-evident against payload mutation, deletion, adjacent reorder, tail truncation, and unsigned payload-hash forgery while sustaining about 46.8k ledger writes/s and 22.0k verifies/s on this host.

## Why it stopped

This run provides synthetic/proxy evidence only, so it supports the mechanism but does not provide direct deployment evidence needed for a publication-grade claim.

## Recommended next action

Stop this run as a no-paper useful signal; next, instrument a real agent runtime with the same ledger and compare it against plain JSONL plus one existing signed audit-log baseline under concurrent tool execution and crash/restart tests.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-runtime signed provenance ledger evaluation for agent actions
- Success threshold: All pre-registered tamper cases are detected, p95 logging overhead is below 10 ms/action, storage is below 2 KB/action, crash/restart preserves verifiability, and the ledger outperforms or matches the selected signed audit baseline on detection coverage with acceptable overhead.
- Stop condition: Stop if integration cannot preserve total ordering or verifiable anchors across crash/restart, if any pre-registered tamper case is undetected, or if p95 logging overhead exceeds 10 ms/action in the 10,000-event runtime test.

## Evidence references

- Artifact root: `<local-path>/projects/cryptographic-evidence-ledger-for-agent-action-provenance-2f707b2ec46f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

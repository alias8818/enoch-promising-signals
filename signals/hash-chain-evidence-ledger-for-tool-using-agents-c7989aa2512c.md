# Hash-Chain Evidence Ledger for Tool-Using Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chain-evidence-ledger-for-tool-using-agents-c7989aa2512c`
Run ID: `hash-chain-evidence-ledger-for-tool-using-agents-c7989aa2512c-20260525T025731445356+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/746db4ff038f

## What looked useful

The practical signal is that a hash-chain ledger for tool-using agents needs an external commitment. Public hashes alone are insufficient: an unanchored chain missed tail truncation, and recomputed row digests detected none of the tested storage-rewrite attacks. Signed checkpoints or final head commitments closed the tested gap with low local overhead.

## Boundaries and scale limits

Synthetic traces only; no live agent runtime integration, no concurrent writer validation, no cross-language canonicalization test, no production storage backend, and no key-compromise or crash-recovery evaluation.

## Claim scope

In a dependency-free Python prototype over 100k synthetic tool-call events, deterministic positional SHA-256 chaining with an externally committed final head/length or verifier-held HMAC checkpoints detected all five tested tamper classes, while plain logs, row digests, and unanchored chains missed important attacks.

## Why it stopped

The result is a synthetic/local useful signal, not full validation or a novel paper-ready contribution; prior art already contains hash-chained AI/audit ledger systems.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should integrate checkpointed receipts into a real agent/tool runtime and replay real traces with the same tamper matrix.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Runtime Checkpointed Evidence Ledger
- Success threshold: Detect 100 percent of the five tested tamper classes after public-hash recomputation, with median runtime overhead below 5 percent and storage overhead reported per event.
- Stop condition: Stop if integration cannot emit deterministic receipts, if any tested tamper class passes with committed checkpoints, or if median runtime overhead exceeds 15 percent on representative workflows.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chain-evidence-ledger-for-tool-using-agents-c7989aa2512c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

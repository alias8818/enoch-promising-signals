# Multi-Trace External-Witness Validation for Anchored Merkleized Agent Ledgers

Status: `useful_signal`
Project ID: `multi-trace-external-witness-validation-for-anchored-merkl-600a7b18f0`
Run ID: `multi-trace-external-witness-validation-for-anchored-merkl-600a7b18f0-20260519T172758327087+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Multi-Trace External-Witness Validation for Anchored Merkleized Agent Ledgers: internal_generated:multi-trace-external-witness-validation-for-anchored-merkl-600a7b18f0

## What looked useful

Medium fixed-seed simulation found 83.33% overall attack detection for two-witness validators versus 16.67% for local-only Merkle validation and 50.00% for single-witness validation, with 0% clean false positives across all schemes. Two-witness validation caught cross-witness equivocation and single-witness compromise, while all schemes failed when both witnesses were compromised.

## Boundaries and scale limits

Synthetic in-process model only; no independently administered witness services, no persisted authenticated transparency log, no real agent traces, no network adversary, no witness key management, and no protection when both witnesses are compromised to agree on the forged history.

## Claim scope

In a deterministic synthetic Python harness with 64 traces, 256 events per trace, 20 fixed seeds, and modeled external witnesses, multi-witness anchoring improved detection of rehashed local tampering, omitted trace epochs, cross-witness equivocation, and single-witness compromise versus local-only Merkle validation and single-witness ablations.

## Why it stopped

Tier 2 synthetic evidence supports the mechanism but is not direct production-grade external witness evidence, and the run found a clear colluding-witness limitation.

## Recommended next action

Stop paper escalation for this run; next, implement the same attack matrix against a small persisted multi-process witness service with authenticated append-only logs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persisted Multi-Process Witness Validation for Anchored Agent Ledgers
- Success threshold: Across at least 20 fixed seeds and replayable multi-agent traces, two-witness validation detects 100% of rehashed local tampering, omitted trace epochs, cross-witness equivocation, and single-witness compromise attacks with 0% clean false positives, and documents the expected failure under full witness collusion.
- Stop condition: Stop if persisted witness replay introduces clean false positives above 1%, if single-witness compromise is not reliably detected by the two-witness validator, or if restart/persistence checks allow forged history to be accepted.

## Evidence references

- Artifact root: `<local-path>/projects/multi-trace-external-witness-validation-for-anchored-merkl-600a7b18f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

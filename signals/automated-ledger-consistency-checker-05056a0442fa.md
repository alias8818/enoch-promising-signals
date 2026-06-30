# Automated Ledger Consistency Checker

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `automated-ledger-consistency-checker-05056a0442fa`
Run ID: `automated-ledger-consistency-checker-05056a0442fa-20260629T230111612989+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fa338371aaca

## What looked useful

The local benchmark shows that balance-only ledger controls miss non-balance inconsistencies, while explicit rules for period status, account validity, duplicate journal IDs, currency consistency, and line completeness can catch those classes in a reproducible harness.

## Boundaries and scale limits

Evidence is synthetic only; no real ERP exports, anonymized production ledgers, human-labeled accounting exceptions, multi-entity consolidation cases, or policy-specific accounting edge cases were tested.

## Claim scope

On a deterministic synthetic double-entry ledger benchmark with six injected inconsistency classes, a rule-based checker detected all labeled faults and outperformed a balance-only baseline.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct real-ledger validation and therefore is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; deepen with an anonymized real or semi-real ledger export and independent labels for the same fault classes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-ledger validation of deterministic consistency checks
- Success threshold: Rule checker recall improves by at least 30 percentage points over balance-only baseline with precision >= 0.95 on independently labeled real or semi-real data.
- Stop condition: Stop if precision falls below 0.90 after rule tuning on documented edge cases, or if no independently labeled or realistically seeded ledger data can be obtained.

## Evidence references

- Artifact root: `<local-path>/projects/automated-ledger-consistency-checker-05056a0442fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

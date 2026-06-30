# Real-ledger validation of deterministic consistency checks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-ledger-validation-of-deterministic-consistency-checks-a70e6f80ba`
Run ID: `real-ledger-validation-of-deterministic-consistency-checks-a70e6f80ba-20260630T004722216758+0000`

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

- Parent run decision: Automated Ledger Consistency Checker: enoch://control-plane/projects/automated-ledger-consistency-checker-05056a0442fa/runs/automated-ledger-consistency-checker-05056a0442fa-20260629T230111612989+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fa338371aaca

## What looked useful

Deterministic ledger checks materially expanded corruption coverage over trial-balance-only validation in the bounded harness: 160/160 detected by the full suite versus 20/160 by trial balance, with 0 clean-ledger false positives.

## Boundaries and scale limits

Synthetic production-style ledger only; no private production ledger, public audited ledger, messy import formats, multi-currency edge cases, reconciliations, closing periods, or adversarial multi-fault corruptions were tested.

## Claim scope

On a deterministic synthetic double-entry ledger with 2000 transactions and 160 single-fault injected corruptions, a full deterministic consistency suite detected all tested corruptions while trial-balance-only validation detected only the single-sided amount drift class.

## Why it stopped

Useful bounded synthetic evidence was produced, but the mission's real-ledger validation claim is not closed without direct real-ledger evidence.

## Recommended next action

Run the same deterministic check suite on a real public accounting export or private audited ledger with labeled incidents/injected corruptions before making any real-ledger validation claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-ledger deterministic consistency validation on labeled accounting exports
- Success threshold: Full suite detects at least 90% of labeled corruptions and at least twice as many corruption classes as trial-balance-only validation, with no more than 1% false positives on clean periods.
- Stop condition: Stop if no analyzable real ledger with labels or auditable injected corruptions can be obtained, or if false positives exceed 5% on clean periods after one bounded tuning pass.

## Evidence references

- Artifact root: `<local-path>/projects/real-ledger-validation-of-deterministic-consistency-checks-a70e6f80ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

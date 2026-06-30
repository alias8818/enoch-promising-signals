# Committed Shuffle Order for Volunteer Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `committed-shuffle-order-for-volunteer-validation-89a98d4e50df`
Run ID: `committed-shuffle-order-for-volunteer-validation-89a98d4e50df-20260628T161140914490+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/afca895b5ac5

## What looked useful

Seed-only commitment is insufficient because a shortened manifest plus shortened recomputed order can verify. Binding the canonical manifest into the commitment fixed this failure in local tests; swapped order, wrong seed, removed task, and added task attempts were rejected, and the HMAC sort-key shuffle showed no obvious positional bias in the bounded synthetic run.

## Boundaries and scale limits

Tested only with synthetic task IDs, 12-item manifests, and 100000 seed trials on one local CPU process. Did not test live volunteers, UI audit logs, public append-only publication, key custody, collusion resistance, or deployed review workflows.

## Claim scope

A local deterministic protocol probe shows that committed volunteer validation shuffle order is reproducible and tamper-evident for synthetic task IDs when the public commitment binds both a secret seed and the canonical task manifest, and the revealed seed is later used to recompute HMAC-SHA256 sort keys.

## Why it stopped

Bounded local protocol evidence supports a mechanism and rules out a weaker seed-only design, but this is not direct or full validation of volunteer behavior or a deployed integrity workflow.

## Recommended next action

Stop this run as no-paper useful signal; if pursued, implement the seed-plus-manifest protocol in a small real validation workflow with append-only commitment publication and independent verifier logs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pilot committed shuffle verification in a live volunteer validation workflow
- Success threshold: In a pilot with at least 30 tasks and 5 volunteers, 100% of independent verifiers reproduce the published order, all injected manifest/order tamper cases are detected, and completion/error rates are not worse than control by more than 10%.
- Stop condition: Stop if independent verifiers cannot reproduce the order from published artifacts, if any injected tamper case is missed, or if the workflow increases volunteer error/dropout by more than 10% versus control.

## Evidence references

- Artifact root: `<local-path>/projects/committed-shuffle-order-for-volunteer-validation-89a98d4e50df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

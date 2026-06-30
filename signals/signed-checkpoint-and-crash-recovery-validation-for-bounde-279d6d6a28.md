# Signed checkpoint and crash-recovery validation for bounded evidence ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `signed-checkpoint-and-crash-recovery-validation-for-bounde-279d6d6a28`
Run ID: `signed-checkpoint-and-crash-recovery-validation-for-bounde-279d6d6a28-20260608T161711454097+0000`

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

- Parent run decision: Bounded Evidence Ledger Local Validation: enoch://control-plane/projects/bounded-evidence-ledger-local-validation-637fc81ef17a/runs/bounded-evidence-ledger-local-validation-637fc81ef17a-20260608T134524472009+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/9a735872710e

## What looked useful

All 9 scenarios passed. Recovery preserved expected state and hash-chain head, rejected incomplete or tampered checkpoints, recovered signed checkpoints even before manifest update by scanning verified candidates, and retained entry files stayed within the crash-state bound of 22 with completed compaction returning to 12.

## Boundaries and scale limits

Tier 1 controlled small direct test only: 40 entries, checkpoint interval 10, retained tail 12, single-process Python model, no real process kill, no power-loss storage testing, no concurrency, and no production implementation integration.

## Claim scope

A minimal bounded evidence ledger model using Ed25519-signed checkpoints, hash-chained entry files, scan-and-verify recovery, and tail compaction recovered correctly across seven controlled checkpoint-publication crash states and rejected two tampered latest-checkpoint cases.

## Why it stopped

The Tier 1 direct model supports the mechanism but is not publication-grade validation because real process death, power-loss behavior, concurrency, and production-scale traces were not tested.

## Recommended next action

Stop this run as no-paper useful mechanism evidence; next deepen with process-level kill/fault injection on the target filesystem before considering broader claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Process-level crash fault injection for signed bounded evidence ledger recovery
- Success threshold: Zero incorrect recoveries or accepted tampered checkpoints across at least 100 seeded process-kill trials, with retained entries never exceeding checkpoint_interval + retained_tail after crash recovery.
- Stop condition: Stop on the first reproducible incorrect recovery, accepted tampered checkpoint, hash-chain break, or retention bound violation; otherwise stop after the seeded trial target and report aggregate metrics.

## Evidence references

- Artifact root: `<local-path>/projects/signed-checkpoint-and-crash-recovery-validation-for-bounde-279d6d6a28`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

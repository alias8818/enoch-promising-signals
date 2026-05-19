# Process-kill rollback ledger validation with external service emulator

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `88`
Project ID: `process-kill-rollback-ledger-validation-with-external-serv-9a2fc1f56f`
Run ID: `process-kill-rollback-ledger-validation-with-external-serv-9a2fc1f56f-20260515T190923350866+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `88`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Process-kill rollback ledger validation with external service emulator: internal_generated:process-kill-rollback-ledger-validation-with-external-serv-9a2fc1f56f

## What looked useful

No-ledger baseline had 1,262/5,000 invariant violations; ledger without recovery had 914/5,000; naive ledger recovery had 12/5,000 due to a local job versus ledger marker atomicity gap; atomic local+ledger recovery had 0/5,000 violations with 4.187 ms p95 recovery latency.

## Boundaries and scale limits

Bounded emulator validation only: 20,000 total process-kill trials on one host, one external service emulator, no real third-party API, no host reboot or fsync fault injection, no multi-node recovery ownership, and no concurrent multi-operation contention.

## Claim scope

In a local SQLite-backed app plus SQLite-backed HTTP external-service emulator, process-kill rollback recovery sharply reduces local/external consistency violations, but only the variant that atomically commits the local state transition and ledger progress marker reached zero violations in the tested fixed-seed 5,000-trial arm.

## Why it stopped

The direct bounded emulator test found a useful mechanism and a concrete flaw in naive rollback ledgers, but the evidence is not broad enough for publication-grade claims over real external services or concurrent distributed recovery.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded action is a concurrent recovery-owner and external-failure injection validation of the atomic ledger variant.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent atomic rollback ledger recovery under external latency and error injection
- Success threshold: Zero invariant violations for the atomic recovery plus owner-lease variant across at least 20,000 process-kill trials and at least two external failure modes, while controls reproduce nonzero violation rates.
- Stop condition: Stop early if the atomic recovery plus owner-lease variant produces any durable invariant violation that is reproducible under the same seed, or if controls do not reproduce any failure under the injected workload.

## Evidence references

- Artifact root: `<local-path>/projects/process-kill-rollback-ledger-validation-with-external-serv-9a2fc1f56f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

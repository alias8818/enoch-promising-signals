# Process-level crash fault injection for signed bounded evidence ledger recovery

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `process-level-crash-fault-injection-for-signed-bounded-evi-d99ec6529b`
Run ID: `process-level-crash-fault-injection-for-signed-bounded-evi-d99ec6529b-20260608T184505231735+0000`

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

- Parent run decision: Bounded Evidence Ledger Local Validation: enoch://control-plane/projects/bounded-evidence-ledger-local-validation-637fc81ef17a/runs/bounded-evidence-ledger-local-validation-637fc81ef17a-20260608T134524472009+0000
- Parent run decision: Signed checkpoint and crash-recovery validation for bounded evidence ledgers: enoch://control-plane/projects/signed-checkpoint-and-crash-recovery-validation-for-bounde-279d6d6a28/runs/signed-checkpoint-and-crash-recovery-validation-for-bounde-279d6d6a28-20260608T161711454097+0000

## What looked useful

Bounded signed recovery worked under process crashes and was 1.378x the SQLite WAL FULL baseline in recovered-records-per-second, but SQLite WAL FULL also lost zero acknowledged records and unsafe JSONL still recovered a prefix despite malformed tails in 12/60 trials. The mechanism is useful but not a paper-ready advantage.

## Boundaries and scale limits

The run tested process-level crashes only, not power loss, kernel panic, storage write reordering, concurrent writers, production filesystems, or large traces. Because process crashes do not drop dirty kernel page cache, the no-fsync ablation also passed and this evidence cannot support durability claims beyond process failure.

## Claim scope

In a local Python harness with real SIGKILL writer-process crashes, a single-writer Ed25519-signed hash-chain ledger with bounded commit frames recovered a valid committed prefix in 60/60 fixed-seed trials, lost zero acknowledged records, and verified all recovered signatures/hash links.

## Why it stopped

Tier 2 process-crash evidence supports the recovery mechanism but does not establish a novel or paper-positive advantage over SQLite WAL FULL or process-crash-only ablations.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should inject block-device or power-failure style faults to determine whether fsync plus commit frames separate from the no-fsync ablation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-device fault injection for signed bounded ledger durability
- Success threshold: bounded_signed has zero lost acknowledged records and zero invalid recovered signatures/hash links in at least 50 injected storage-fault trials, while bounded_no_fsync loses acknowledged records or fails recovery in at least 10% of comparable trials.
- Stop condition: Stop if storage-fault injection cannot be run locally, or if bounded_signed loses acknowledged records or accepts invalid signed/hash-chain records in any reproducible trial.

## Evidence references

- Artifact root: `<local-path>/projects/process-level-crash-fault-injection-for-signed-bounded-evi-d99ec6529b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

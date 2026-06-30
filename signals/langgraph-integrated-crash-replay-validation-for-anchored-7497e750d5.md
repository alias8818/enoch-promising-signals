# LangGraph-integrated crash/replay validation for anchored tool-call ledgers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `langgraph-integrated-crash-replay-validation-for-anchored-7497e750d5`
Run ID: `langgraph-integrated-crash-replay-validation-for-anchored-7497e750d5-20260527T022854256924+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-runtime anchored tool-call ledger with crash and concurrency faults: enoch://control-plane/projects/real-runtime-anchored-tool-call-ledger-with-crash-and-conc-3e6adf255a/runs/real-runtime-anchored-tool-call-ledger-with-crash-and-conc-3e6adf255a-20260526T195531317700+0000
- Parent run decision: Runtime-integrated anchored tool-call ledger: enoch://control-plane/projects/runtime-integrated-anchored-tool-call-ledger-6e04a98f51/runs/runtime-integrated-anchored-tool-call-ledger-6e04a98f51-20260526T130857146414+0000

## What looked useful

Across 1,000 one-crash trials and 500 three-crash trials, anchored deterministic ledger keys achieved exactly_once_rate=1.0 and mean_effects=1, while no-ledger and replay-unstable-key baselines achieved exactly_once_rate=0.0 and duplicated effects. A 500-trial adversarial cutpoint where the external effect committed before the ledger anchor also failed for anchored ledgers with exactly_once_rate=0.0, showing the mechanism requires atomic anchoring or external idempotency.

## Boundaries and scale limits

Local deterministic SQLite stand-in; small graph topology; no real remote tool/API, distributed transaction, LLM nondeterminism, concurrent threads, or long-running production workload. The adversarial non-atomic cutpoint fails.

## Claim scope

LangGraph SQLite-checkpointed crash/replay harness with deterministic single-tool workflows and a SQLite-modeled external effect. Anchored ledgers preserve exactly-once effects when the side effect and ledger anchor commit atomically, or equivalently when the external system honors the same idempotency anchor.

## Why it stopped

Mixed direct validation: the scoped atomic/idempotent-anchor mechanism is supported, but the broader crash/replay claim is falsified by the non-atomic external-effect-before-ledger cutpoint.

## Recommended next action

Stop this branch as no-paper useful evidence; the next bounded deepen test should use a real idempotent external tool API or service-backed transactional outbox to verify the same cutpoints outside the SQLite stand-in.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-service idempotency validation for LangGraph anchored tool ledgers
- Success threshold: Anchored service-level idempotency reaches exactly_once_rate >= 0.999 with zero duplicate committed effects across all crash cutpoints, while both baselines duplicate in the post-commit/pre-return cutpoint.
- Stop condition: Stop as negative if any anchored service-level idempotency cutpoint produces a duplicate committed effect, an unresolvable false conflict, or more than 5% failed recovery at 500 fixed-seed trials.

## Evidence references

- Artifact root: `<local-path>/projects/langgraph-integrated-crash-replay-validation-for-anchored-7497e750d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

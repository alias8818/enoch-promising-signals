# Online Independent Replay Verification for Real Multi-Tool Agent Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `online-independent-replay-verification-for-real-multi-tool-edb920ac25`
Run ID: `online-independent-replay-verification-for-real-multi-tool-edb920ac25-20260524T020315495607+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Replay Validation on Real Agent Workflow Ledgers: enoch://control-plane/projects/replay-validation-on-real-agent-workflow-ledgers-71a9e6e4a8/runs/replay-validation-on-real-agent-workflow-ledgers-71a9e6e4a8-20260524T014811214190+0000
- Parent run decision: Trace Replay Validation for Agent Evidence Ledgers: enoch://control-plane/projects/trace-replay-validation-for-agent-evidence-ledgers-df1f7a6569/runs/trace-replay-validation-for-agent-evidence-ledgers-df1f7a6569-20260524T013758531131+0000

## What looked useful

Independent replay materially outperformed self-consistent hash-chain checking: replay reached 0.0 clean false-positive rate and 1.0 tamper detection over 150 corrected tampered ledgers, while schema/hash-only checking detected only stale-hash edits for a 0.2 tamper detection rate.

## Boundaries and scale limits

Evidence is from a local deterministic harness, not production LLM agent traces or external tool APIs. Nondeterministic tools, adversarial equivalent-output input changes, distributed verifier trust, signing, concurrent verification, and long production ledgers were not validated.

## Claim scope

For deterministic, replayable local multi-tool ledgers with file, SQLite, calculator, JSON transform, and controlled local HTTP tools, an independent online replay verifier detected all tested output, input, omission, reorder, and stale-hash tamper controls across 30 fixed-seed 200-event ledgers with zero clean false positives.

## Why it stopped

Bounded local validation supports the mechanism but does not provide publication-grade evidence over real production multi-tool agent ledgers.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded deepening should validate adapters on real framework trace formats before making a production-agent-ledger claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Verification on Real Agent Framework Trace Formats
- Success threshold: Across at least 100 clean and 500 tampered real-framework ledgers, achieve <=1% clean false-positive rate, >=95% tamper detection overall, >=90% detection in each tamper class, and median replay overhead below 5 ms per event.
- Stop condition: Stop if real traces cannot be independently replayed or snapshotted without private credentials, or if clean false positives exceed 5% after deterministic tool normalization.

## Evidence references

- Artifact root: `<local-path>/projects/online-independent-replay-verification-for-real-multi-tool-edb920ac25`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

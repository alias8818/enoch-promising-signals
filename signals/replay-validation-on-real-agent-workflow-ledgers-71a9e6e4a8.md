# Replay Validation on Real Agent Workflow Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-validation-on-real-agent-workflow-ledgers-71a9e6e4a8`
Run ID: `replay-validation-on-real-agent-workflow-ledgers-71a9e6e4a8-20260524T014811214190+0000`

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

- Parent run decision: Agent Evidence Ledger for Tool-Use Reliability: enoch://control-plane/projects/agent-evidence-ledger-for-tool-use-reliability-f699e49cb406/runs/agent-evidence-ledger-for-tool-use-reliability-f699e49cb406-20260524T011853968704+0000
- Parent run decision: Trace Replay Validation for Agent Evidence Ledgers: enoch://control-plane/projects/trace-replay-validation-for-agent-evidence-ledgers-df1f7a6569/runs/trace-replay-validation-for-agent-evidence-ledgers-df1f7a6569-20260524T013758531131+0000

## What looked useful

Tier 2 medium confirmation passed: hash_chain_with_manifest achieved 1.000 accuracy with 0/900 false accepts on tamper and 0/150 false rejects on clean real-ledger cases. Unsigned structured and transcript baselines accepted 900/900 tampered cases. The no-manifest ablation accepted 150/150 tail truncations, showing the final manifest is necessary.

## Boundaries and scale limits

Local post-hoc replay only; command_execution workflow rows only; one Python implementation; deterministic local mutations; no online recorder, independent verifier, public-key signing, concurrent writers, streaming partial records, non-command tool families, public corpus, or hostile storage/transfer test.

## Claim scope

On 30 real local Codex/Enoch JSONL workflow traces containing 1,015 completed command_execution rows, manifest-bound hash-chain replay validation accepted all clean replay cases and rejected all deterministic tamper cases across fixed seeds, outperforming count-only, unsigned structured, and transcript-regex baselines.

## Why it stopped

The bounded Tier 2 real-ledger replay test supports the mechanism, but the evidence is local, post-hoc, single-implementation, and command-workflow scoped, so it is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded online-recorder follow-up that writes and independently verifies manifest-bound workflow ledgers during active multi-tool agent sessions, including streaming/restart and non-command tool events.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online Independent Replay Verification for Real Multi-Tool Agent Ledgers
- Success threshold: Manifest-bound online replay has 0 clean false rejects and 0 tamper false accepts across the fixed matrix, while at least one real baseline has tamper false accept rate >= 0.75 and the no-manifest ablation accepts tail truncation.
- Stop condition: Stop if online recording cannot produce at least 20 complete multi-tool sessions within the local budget, if independent verification disagrees on clean ledgers, or if manifest-bound replay has any deterministic tamper false accept in the fixed matrix.

## Evidence references

- Artifact root: `<local-path>/projects/replay-validation-on-real-agent-workflow-ledgers-71a9e6e4a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

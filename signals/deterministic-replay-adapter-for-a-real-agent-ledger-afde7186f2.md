# Deterministic Replay Adapter for a Real Agent Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-replay-adapter-for-a-real-agent-ledger-afde7186f2`
Run ID: `deterministic-replay-adapter-for-a-real-agent-ledger-afde7186f2-20260522T092004428790+0000`

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

- Parent run decision: Deterministic Harness for Agent Ledger Consistency: enoch://control-plane/projects/deterministic-harness-for-agent-ledger-consistency-6a6e7ba6f5c8/runs/deterministic-harness-for-agent-ledger-consistency-6a6e7ba6f5c8-20260522T073734083060+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8b8a45c3f053

## What looked useful

The adapter replayed the real ledger snapshot twice to the same digest e7fc72c1142e316716226ac534a5cf1700221ec02bfe318f1a9311486c4d3fc0 and detected drop_last, swap_first_two, and edit_text mutations.

## Boundaries and scale limits

Tested on one short ledger snapshot from this project only; not validated on long multi-session ledgers, concurrent lifecycle anomalies, schema drift, external agent frameworks, or runtime side-effect replay.

## Claim scope

A dependency-free deterministic replay adapter can canonicalize and replay one real 26-event Codex/Enoch JSONL agent ledger snapshot with stable final digest and controlled perturbation detection.

## Why it stopped

Tier 1 direct mechanism test passed, but the evidence is too narrow for publication readiness.

## Recommended next action

Run the same adapter against a heterogeneous corpus of at least 100 real Codex/Enoch ledgers with interrupted commands and multi-turn sessions before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Heterogeneous Real-Ledger Deterministic Replay Corpus Test
- Success threshold: At least 99% of valid ledgers replay deterministically on repeated runs and 100% of eligible controlled perturbations are detected, with all failures classified by schema/lifecycle cause.
- Stop condition: Stop if more than 5% of valid ledgers require manual schema-specific patches or if any common event type cannot be represented without losing semantic replay state.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-replay-adapter-for-a-real-agent-ledger-afde7186f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

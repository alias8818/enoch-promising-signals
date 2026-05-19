# Live Agent Integration Replay Test For Signed Tool-Path Recorder

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `live-agent-integration-replay-test-for-signed-tool-path-re-428259d2c6`
Run ID: `live-agent-integration-replay-test-for-signed-tool-path-re-428259d2c6-20260518T123004631736+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Live Agent Integration Replay Test For Signed Tool-Path Recorder: internal_generated:live-agent-integration-replay-test-for-signed-tool-path-re-428259d2c6

## What looked useful

Signed event hashes plus a signed final manifest produced 100% exact replay and 100% tamper detection in the local test; the no-manifest ablation missed all tail truncations, and unsigned JSONL detected none of the structural tamper cases.

## Boundaries and scale limits

The run used a deterministic local workload rather than production LLM agent frameworks, remote tool buses, public-key signing, concurrent or streaming traces, binary payloads, redaction, key rotation, or independent verifier implementations.

## Claim scope

A dependency-light local Python prototype of a signed, hash-chained tool-path recorder with a signed final manifest achieved exact replay and tamper evidence for deterministic sequential tool-call traces across 500 fixed-seed sessions and 3,000 injected tamper trials.

## Why it stopped

No-paper useful signal: the mechanism is supported locally, but Tier 4 paper-readiness is not met because the evidence is bounded/proxy integration rather than robust live-agent replication.

## Recommended next action

Stop this follow-up campaign at depth 4; preserve the useful local mechanism evidence, but do not claim paper readiness without real multi-framework live-agent integration and public-key verifier replication.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/live-agent-integration-replay-test-for-signed-tool-path-re-428259d2c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

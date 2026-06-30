# Replay Real Enoch Worker Traces Through a Signed Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-real-enoch-worker-traces-through-a-signed-evidence-2958f654f7`
Run ID: `replay-real-enoch-worker-traces-through-a-signed-evidence-2958f654f7-20260608T022725821238+0000`

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

- Parent run decision: Evidence Ledger for CPU Worker Reliability Verification: enoch://control-plane/projects/evidence-ledger-for-cpu-worker-reliability-verification-e68b049454b5/runs/evidence-ledger-for-cpu-worker-reliability-verification-e68b049454b5-20260607T213045242796+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/bf7bbd7d1a18

## What looked useful

The direct Tier 1 test supports the signed-ledger mechanism on real Enoch trace data and surfaced an important design requirement: snapshot the live Codex JSONL before signing because the live log grows while commands execute.

## Boundaries and scale limits

Only one 41-event real trace snapshot was tested. The run did not test a corpus of completed workers, restart/resume traces, stdout/stderr sidecars, decision artifact inclusion, key rotation, storage integration, or broad adversarial tamper cases.

## Claim scope

A single immutable snapshot of one real Enoch Codex JSONL worker trace can be replayed into a canonical hash-chained evidence ledger, signed with an Ed25519 manifest, verified from source, and reject a post-signing event tamper control.

## Why it stopped

Tier 1 direct validation succeeded on one real trace snapshot, but evidence remains no-paper because breadth, production snapshot integration, and adversarial robustness were not tested.

## Recommended next action

Run a bounded deepen test on a small corpus of closed Enoch worker runs, including resumed and failed runs, and require all replay/signature checks plus deletion, reordering, mutation, and sidecar mismatch controls to pass.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay a Corpus of Closed Enoch Worker Runs Through the Signed Evidence Ledger
- Success threshold: All baseline verifications pass for at least 10 closed real runs, and every tamper class is detected in every tested run with no false clean verification.
- Stop condition: Stop as negative if any untampered closed run cannot be replayed deterministically or if any tamper class verifies cleanly after signing.

## Evidence references

- Artifact root: `<local-path>/projects/replay-real-enoch-worker-traces-through-a-signed-evidence-2958f654f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

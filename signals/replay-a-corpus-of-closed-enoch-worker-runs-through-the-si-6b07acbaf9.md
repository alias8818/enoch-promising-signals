# Replay a Corpus of Closed Enoch Worker Runs Through the Signed Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-a-corpus-of-closed-enoch-worker-runs-through-the-si-6b07acbaf9`
Run ID: `replay-a-corpus-of-closed-enoch-worker-runs-through-the-si-6b07acbaf9-20260608T080550407639+0000`

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
- Parent run decision: Replay Real Enoch Worker Traces Through a Signed Evidence Ledger: enoch://control-plane/projects/replay-real-enoch-worker-traces-through-a-signed-evidence-2958f654f7/runs/replay-real-enoch-worker-traces-through-a-signed-evidence-2958f654f7-20260608T022725821238+0000

## What looked useful

On 5 fixed seeds and 100 trials per attack, signed_external_head detected 400/400 attack trials with 0/100 clean false rejects. Presence-only detected 0/400, unsigned-manifest detected 100/400, and signed-without-witness detected 300/400, isolating the importance of both signatures and an external witness head.

## Boundaries and scale limits

The witness head, signing key, and ledger service are simulated locally; this does not validate production key custody, a real transparency log, controller callback integration, multi-host replication, crash recovery, or the full historical corpus.

## Claim scope

Tier 2 local replay over 128 real closed sibling Enoch worker-run artifact directories shows that a signed manifest ledger with an independently checked witness head detects seeded artifact tamper, local ledger forgery, rollback/prefix replay, and decision-swap forgery with zero clean false rejects.

## Why it stopped

Closed as useful no-paper evidence: Tier 2 local corpus replay supports the mechanism, but production external anchoring and controller integration were not directly tested.

## Recommended next action

Run a bounded production-integration replay that writes real Enoch controller callback payloads into the signed ledger and verifies them against an actual append-only witness service.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production Callback Replay Through Real Signed Enoch Evidence Ledger
- Success threshold: signed production ledger detects at least 99% of seeded attacks with 0 clean false rejects across fixed seeds, and both baselines fail on their expected ablation classes
- Stop condition: Stop if production integration cannot expose callback payloads and external witness heads locally, or if signed production verification has any reproducible clean false reject or misses rollback/tamper attacks.

## Evidence references

- Artifact root: `<local-path>/projects/replay-a-corpus-of-closed-enoch-worker-runs-through-the-si-6b07acbaf9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

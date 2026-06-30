# Signed External Anchor Evidence Ledger Replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `signed-external-anchor-evidence-ledger-replay-dcd1bf37ca`
Run ID: `signed-external-anchor-evidence-ledger-replay-dcd1bf37ca-20260524T230201532570+0000`

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

- Parent run decision: Evidence-Ledger Agent Integrity: enoch://control-plane/projects/evidence-ledger-agent-integrity-556a687c49dd/runs/evidence-ledger-agent-integrity-556a687c49dd-20260524T220110997952+0000
- Parent run decision: Real-Agent Evidence Ledger Integrity Replay: enoch://control-plane/projects/real-agent-evidence-ledger-integrity-replay-36e6aa972e/runs/real-agent-evidence-ledger-integrity-replay-36e6aa972e-20260524T222131443358+0000

## What looked useful

Signed external anchors plus external witness-head verification achieved 500/500 attack detections with 0 clean false rejects. The hash-chain baseline detected only 125/500 attacks, signed anchors without a witness head detected 250/500, and unsigned anchors detected 375/500, showing both signing and independent latest-head knowledge are necessary for the tested replay-resistance mechanism.

## Boundaries and scale limits

Synthetic single-process simulation only; no real transparency service, public timestamping, KMS/HSM custody, distributed clocks, network faults, storage engine, legal evidence workflow, or operational adversary was tested.

## Claim scope

In a deterministic synthetic evidence-ledger benchmark with 50,000 events, fixed seeds, a standard hash-chain baseline, and anchor ablations, signed external anchors verified against an independently known witness head detected all tested replay, rollback, truncation, and tamper attacks.

## Why it stopped

Tier 2 synthetic evidence supports the mechanism but is not paper-positive direct systems evidence.

## Recommended next action

Stop as no-paper useful signal; next concrete deepen test should replace the simulated witness head with a real append-only transparency log or timestamping service and replay captured ledger snapshots through the same verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transparency-Log Replay Test for Signed Evidence Ledgers
- Success threshold: At least 99% detection of rollback, truncation, and internally rehashed tamper attempts with 0 clean false rejects across no fewer than 1,000 replay cases, while preserving median verification overhead below 10% over the hash-chain baseline excluding external publication latency.
- Stop condition: Stop if the real witness integration introduces clean false rejects, cannot reliably establish a latest external head, or fails to detect any rollback/truncation class that the synthetic signed-anchor verifier detected.

## Evidence references

- Artifact root: `<local-path>/projects/signed-external-anchor-evidence-ledger-replay-dcd1bf37ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

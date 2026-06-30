# LMS-backed timestamp-anchor validation for volunteer training provenance chains

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lms-backed-timestamp-anchor-validation-for-volunteer-train-6befc936e6`
Run ID: `lms-backed-timestamp-anchor-validation-for-volunteer-train-6befc936e6-20260608T070725181486+0000`

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

- Parent run decision: Time-stamped provenance chains for volunteer training validation: enoch://control-plane/projects/time-stamped-provenance-chains-for-volunteer-training-validation-e77cb95075c0/runs/time-stamped-provenance-chains-for-volunteer-training-validation-e77cb95075c0-20260608T022726699548+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e4978c02a2ea

## What looked useful

Signed LMS timestamp anchors materially improved tamper detection over hash-only and unsigned-anchor controls: signed anchors detected 4/4 attack cases while hash-only detected 0/4 and unsigned anchors detected 1/4, with the clean corpus accepted by all validators.

## Boundaries and scale limits

Synthetic LMS authority and simplified event schema only; no real LMS export/API, clock synchronization behavior, key-rotation audit trail, volunteer identity binding, deployment latency, operator workflow, or broader adversary study was validated.

## Claim scope

In a deterministic controlled 1,000-record synthetic volunteer training corpus, Ed25519-signed LMS timestamp anchors plus a 15 minute completion/anchor skew policy rejected four post-hoc tamper classes that plain hash-chain and unsigned-anchor controls mostly accepted.

## Why it stopped

Tier 1 controlled synthetic evidence supports the mechanism but is not real-world or robust enough for publication readiness.

## Recommended next action

Run a bounded deepen follow-up against an actual LMS sandbox export or xAPI/SCORM event feed with real key rotation metadata and clock skew observations before considering paper-level claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sandbox LMS export validation for signed timestamp-anchor provenance chains
- Success threshold: On a real LMS sandbox/export corpus of at least 100 completion events, accept 100% of clean chains and reject all tested no-key tampering cases plus excessive backdating beyond an empirically justified skew threshold.
- Stop condition: Stop if the LMS export cannot provide a verifiable timestamp authority or stable event identity sufficient to bind receipts to event hashes, or if clean export acceptance falls below 99% after documented schema mapping fixes.

## Evidence references

- Artifact root: `<local-path>/projects/lms-backed-timestamp-anchor-validation-for-volunteer-train-6befc936e6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

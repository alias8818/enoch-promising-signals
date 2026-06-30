# Real LMS fixture validation for signed timestamp-anchor export provenance

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-lms-fixture-validation-for-signed-timestamp-anchor-ex-5b2a7b6ae7`
Run ID: `real-lms-fixture-validation-for-signed-timestamp-anchor-ex-5b2a7b6ae7-20260608T150114317444+0000`

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

- Parent run decision: Sandbox LMS export validation for signed timestamp-anchor provenance chains: enoch://control-plane/projects/sandbox-lms-export-validation-for-signed-timestamp-anchor-c2af5734cf/runs/sandbox-lms-export-validation-for-signed-timestamp-anchor-c2af5734cf-20260608T105914751363+0000
- Parent run decision: LMS-backed timestamp-anchor validation for volunteer training provenance chains: enoch://control-plane/projects/lms-backed-timestamp-anchor-validation-for-volunteer-train-6befc936e6/runs/lms-backed-timestamp-anchor-validation-for-volunteer-train-6befc936e6-20260608T070725181486+0000

## What looked useful

Both real Moodle fixtures verified successfully with source checks intact. CAPES: 514 archive members, 422 XML members, 4.307 s, 9.22 MiB/s, 6/6 tamper controls detected. Zenodo: 227 archive members, 180 XML members, 1.513 s, 43.60 MiB/s, 6/6 tamper controls detected. Hash-only baseline lacks exporter signature and signed timestamp-anchor provenance.

## Boundaries and scale limits

Tested two public Moodle backup fixtures only: 41.7 MB CAPES and 69.2 MB Zenodo archives. No live LMS export workflow, no Canvas/Brightspace/Blackboard matrix, no external RFC3161/OpenTimestamps authority, no institutional audit logs, and no end-user restore-path validation.

## Claim scope

Real archived Moodle .mbz fixtures can be canonicalized into export manifests, signed with Ed25519, linked to a local signed timestamp-anchor chain, and verified against archive payload, manifest, signature, timestamp-backdating, and anchor-chain tampering.

## Why it stopped

No-paper useful signal: the mechanism passed real archived LMS fixture validation, but publication-grade evidence requires live LMS export integration and independent timestamp anchoring.

## Recommended next action

Run a depth-4 bounded live-Moodle validation: generate backups from a local Moodle instance via CLI, sign/export through the harness, and add third-party timestamp-token validation before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Moodle export validation with independent timestamp authority
- Success threshold: At least three live-generated Moodle backups across two fixed seeds verify successfully; all tamper controls are detected; timestamp-token verification works offline; hash-only baseline remains unable to provide signed exporter and independent timestamp provenance.
- Stop condition: Stop if Moodle backup generation cannot be automated locally within 4 hours, if third-party timestamp verification cannot be reproduced offline, or if any tamper class is not detected after one harness fix.

## Evidence references

- Artifact root: `<local-path>/projects/real-lms-fixture-validation-for-signed-timestamp-anchor-ex-5b2a7b6ae7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

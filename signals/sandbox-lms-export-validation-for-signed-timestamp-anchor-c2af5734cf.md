# Sandbox LMS export validation for signed timestamp-anchor provenance chains

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sandbox-lms-export-validation-for-signed-timestamp-anchor-c2af5734cf`
Run ID: `sandbox-lms-export-validation-for-signed-timestamp-anchor-c2af5734cf-20260608T105914751363+0000`

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

- Parent run decision: LMS-backed timestamp-anchor validation for volunteer training provenance chains: enoch://control-plane/projects/lms-backed-timestamp-anchor-validation-for-volunteer-train-6befc936e6/runs/lms-backed-timestamp-anchor-validation-for-volunteer-train-6befc936e6-20260608T070725181486+0000
- Parent run decision: Time-stamped provenance chains for volunteer training validation: enoch://control-plane/projects/time-stamped-provenance-chains-for-volunteer-training-validation-e77cb95075c0/runs/time-stamped-provenance-chains-for-volunteer-training-validation-e77cb95075c0-20260608T022726699548+0000

## What looked useful

Across 6,965 attack trials per validator and 995 clean trials per validator, the full signed timestamp-anchor chain accepted all clean exports and detected all modeled attacks, while hash-manifest and signed-manifest baselines detected 14.3% and 57.1% of attack trials respectively. Targeted ablations each missed the attack class they were expected to miss.

## Boundaries and scale limits

No real LMS exports, no external RFC 3161 timestamp authority, no institutional key-management integration, and no adversarial corpus from production LMS workflows were tested.

## Claim scope

In a synthetic LMS-like export harness with fixed seeds, signed timestamp-anchor chains detected modeled content tamper, manifest rewrite, replay, stale-anchor, backdating, unsigned-anchor forgery, and chain-splice attacks that conventional zip/hash/signed-manifest baselines or targeted ablations missed.

## Why it stopped

Tier 2 synthetic medium confirmation produced a useful mechanism signal but not real-LMS or publication-grade evidence.

## Recommended next action

Run a bounded deepen validation using real Canvas/Moodle/Common Cartridge export fixtures and an external RFC 3161-compatible timestamp authority, with the same replay/backdating/manifest-rewrite attack matrix.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LMS fixture validation for signed timestamp-anchor export provenance
- Success threshold: On real LMS fixture families, full chain clean acceptance >= 99%, attack detection >= 99% for every modeled provenance attack class, false rejection <= 1%, and p95 validation latency below 250 ms per export on CPU.
- Stop condition: Stop if real export formats cannot be canonicalized without lossy rewriting, if clean acceptance drops below 95%, or if any core provenance attack class remains undetected by the full chain under a valid threat model.

## Evidence references

- Artifact root: `<local-path>/projects/sandbox-lms-export-validation-for-signed-timestamp-anchor-c2af5734cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

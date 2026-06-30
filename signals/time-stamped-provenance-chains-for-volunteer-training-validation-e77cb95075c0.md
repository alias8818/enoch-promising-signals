# Time-stamped provenance chains for volunteer training validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `time-stamped-provenance-chains-for-volunteer-training-validation-e77cb95075c0`
Run ID: `time-stamped-provenance-chains-for-volunteer-training-validation-e77cb95075c0-20260608T022726699548+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e4978c02a2ea

## What looked useful

Anchored signed provenance chains provide a concrete tamper-evidence advantage over independent signed certificates for omission attacks: unanchored chains caught middle deletion but not tail truncation, while anchored chains caught both at 100% in the synthetic attack suite.

## Boundaries and scale limits

Synthetic records only; no real LMS integration, trusted timestamp authority, transparency log, volunteer identity proofing, issuer key compromise test, privacy review, or operational deployment evidence. The benchmark was CPU-only and bounded to 2,000 records with 20 trials per attack.

## Claim scope

In a deterministic 2,000-record synthetic volunteer-training ledger, per-volunteer signed hash chains detect middle-record deletion that independent signed certificates miss, and a published per-volunteer head anchor is required to detect tail truncation. The added chain/anchor verification cost was negligible relative to Ed25519 signature verification.

## Why it stopped

No-paper useful signal: evidence is a synthetic proxy mechanism validation, not direct real-world volunteer training validation.

## Recommended next action

Run a bounded LMS-style integration follow-up with externally published timestamp/head anchors, revocation handling, and realistic append/delete/export workflows before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LMS-backed timestamp-anchor validation for volunteer training provenance chains
- Success threshold: Anchored-chain verifier detects at least 95% of omission/truncation/replay attacks that pass the signed-only baseline, accepts clean exported histories, and verifies 10,000 records in under 250 ms on a commodity CPU.
- Stop condition: Stop if realistic correction/revocation workflows cannot be represented without external human/private policy decisions, or if anchored-chain verification fails clean-history acceptance or misses tail truncation under a published-anchor model.

## Evidence references

- Artifact root: `<local-path>/projects/time-stamped-provenance-chains-for-volunteer-training-validation-e77cb95075c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

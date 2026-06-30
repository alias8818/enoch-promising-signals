# Adversarial Ledger Injection Stress Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adversarial-ledger-injection-stress-test-c01ccd3cde03`
Run ID: `adversarial-ledger-injection-stress-test-c01ccd3cde03-20260525T024721117707+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/746db4ff038f

## What looked useful

Raw line hash-chain audit views showed 10,500 rows for 10,000 committed records, unsafe interpolated NDJSON showed 10,335 audit-view rows and 2,085 parse errors, and length-framed canonical JSON HMAC showed exactly 10,000 rows, zero parse errors, and 500/500 random tamper detections.

## Boundaries and scale limits

Synthetic encodings only; no named production ledger, multi-writer append path, network transport, UI workflow, key management, cross-language canonicalization, or long-running deployment was tested.

## Claim scope

In a synthetic 10,000-record local stress test, adversarial payloads injected or corrupted displayed records in delimiter-oriented ledger encodings, while canonical length-framed JSON records with per-record HMAC preserved record count and chain validity under the same payload corpus.

## Why it stopped

Synthetic local evidence supports the encoding-level mechanism but is not direct production evidence or publication-grade validation.

## Recommended next action

Stop as no-paper useful signal; the concrete next bounded test is to run the same payload corpus against real ledger libraries or production-like exported audit formats with UI/auditor rendering included.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Ledger Parser and Viewer Injection Confirmation
- Success threshold: A bounded follow-up is successful if any real parser/viewer shows rendered row count different from committed count or accepts a forged marker as an independent record, while the hardened control preserves exact committed count and rejects tampering.
- Stop condition: Stop if two representative real systems both preserve exact committed counts, reject all tampering, and render payload markers unambiguously as payload text rather than ledger structure.

## Evidence references

- Artifact root: `<local-path>/projects/adversarial-ledger-injection-stress-test-c01ccd3cde03`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

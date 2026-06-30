# Attestation-based volunteer identity for distributed training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `attestation-based-volunteer-identity-for-distributed-training-ac7ae0775f22`
Run ID: `attestation-based-volunteer-identity-for-distributed-training-ac7ae0775f22-20260607T181738742684+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aa85fc0bcc9a

## What looked useful

Attestation is useful as an admission-control proof of approved code and fresh session keys. It is not sufficient as privacy-preserving volunteer identity: anonymous attestation admits duplicate Sybil registrations, while linkable unique hardware identity blocks duplicates but creates privacy/vendor-policy tradeoffs.

## Boundaries and scale limits

No real Intel/AMD/NVIDIA/TPM quote parsing, no volunteer hardware coverage survey, no distributed training run, and no side-channel or vendor-service robustness testing. Results are mechanism-level and source-backed, not deployment-grade.

## Claim scope

Bounded local mechanism probe: synthetic quote-like attestations can bind freshness, workload measurement, and session keys cheaply, but Sybil-resistant volunteer identity requires verifier-visible stable hardware identifiers or an external scarcity/reputation mechanism.

## Why it stopped

Bounded synthetic evidence supports code/freshness binding but early-falsifies attestation-only privacy-preserving Sybil-resistant identity; this is a proxy/mechanism result rather than full validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should parse real public/vendor quote examples and measure which stable identifiers are available under linkable versus privacy-preserving attestation modes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real quote identifier audit for volunteer attestation identity
- Success threshold: At least two attestation families have parsed evidence showing whether stable device identity is exposed; verifier latency remains under 10 ms median for cached-policy repeated verification; the audit can classify each family as anonymous, pseudonymous-linkable, or directly linkable.
- Stop condition: Stop if real quote examples or documentation do not expose enough identifier fields to classify at least two attestation families, or if parsing requires private vendor credentials unavailable to researchers.

## Evidence references

- Artifact root: `<local-path>/projects/attestation-based-volunteer-identity-for-distributed-training-ac7ae0775f22`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

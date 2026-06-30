# Falsifiable Evidence Ledger with Tiered Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `falsifiable-evidence-ledger-with-tiered-validation-421bc729f683`
Run ID: `falsifiable-evidence-ledger-with-tiered-validation-421bc729f683-20260612T052130669313+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/998410ae075f

## What looked useful

Across 700 deterministic trials, the naive append-only ledger accepted 600/600 invalid ledgers while the tiered validator accepted 0/600 invalid ledgers and rejected 0/100 valid ledgers; median tiered validation latency was 0.0691925 ms.

## Boundaries and scale limits

Synthetic JSON fixtures only; no real research corpus, human review workflow, external trust anchors, collusion model, long-lived ledger operation, or production artifact store was tested.

## Claim scope

In a local synthetic adversarial fixture set, explicit tier validation for artifacts, hashes, metric thresholds, validator independence, tier ordering, and falsifier thresholds rejects unsupported evidence promotions that a naive append-only ledger accepts.

## Why it stopped

No-paper useful signal: the mechanism passed a bounded synthetic adversarial test, but the evidence is not direct enough for broad or publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up on a small real or semi-real claim/evidence corpus with independent annotators and explicit false-accept/false-reject thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus False Accept and False Reject Test for Tiered Evidence Ledgers
- Success threshold: Tiered validator false-accept rate at least 80% lower than naive baseline and false-reject rate below 10% on labeled bundles.
- Stop condition: Stop if labeled corpus construction cannot distinguish validator independence, artifact integrity, metric thresholds, and falsifier states, or if tiered false rejects exceed 25% in the first 20 labeled bundles.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-evidence-ledger-with-tiered-validation-421bc729f683`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

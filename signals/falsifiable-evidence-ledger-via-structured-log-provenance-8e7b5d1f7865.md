# Falsifiable Evidence Ledger via Structured Log Provenance

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `falsifiable-evidence-ledger-via-structured-log-provenance-8e7b5d1f7865`
Run ID: `falsifiable-evidence-ledger-via-structured-log-provenance-8e7b5d1f7865-20260525T072140990464+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/111b44975757

## What looked useful

A falsifiable evidence ledger needs both structured provenance checks and an anchored terminal checkpoint; under that condition the prototype detected 8000/8000 synthetic tampering cases while unstructured text logs detected 0/8000.

## Boundaries and scale limits

Synthetic single-process ledgers only; no real CI/lab/audit logs, no multi-writer concurrency, no checkpoint-compromise model, no usability or authoring-overhead study, and only a minimal unstructured text-log baseline.

## Claim scope

In deterministic synthetic ledgers, canonical structured events with hash-chain provenance, typed references, content hashes, and an externally anchored terminal checkpoint detected all tested payload edits, claim edits, deletions, reorders, broken references, chain rewrites, and unsupported conclusion appends.

## Why it stopped

The result is synthetic mechanism evidence, not direct real-world or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded real-log replay against stronger signed-log or manifest baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-log replay for anchored structured evidence ledgers
- Success threshold: Detect at least 99% of injected tampering cases with zero false positives on unmodified logs and no more than 20% log-size overhead versus the strongest baseline.
- Stop condition: Stop if converted real logs produce false positives above 1%, if a stronger baseline matches detection with lower overhead, or if checkpoint management dominates the design.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-evidence-ledger-via-structured-log-provenance-8e7b5d1f7865`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

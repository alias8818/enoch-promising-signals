# Held-out realistic ledger mutation benchmark for semantic notary fingerprints

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `held-out-realistic-ledger-mutation-benchmark-for-semantic-66ffaff727`
Run ID: `held-out-realistic-ledger-mutation-benchmark-for-semantic-66ffaff727-20260522T003742717609+0000`

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

- Parent run decision: Semantic Ledger Notary: enoch://control-plane/projects/semantic-ledger-notary-6ed8c4237097/runs/semantic-ledger-notary-6ed8c4237097-20260521T223326136473+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2eeb37ddb77e

## What looked useful

Semantic posting hashes reached 1.00 semantic mutation detection and 1.00 benign invariance over 9,000 scored cases; raw and canonical JSON hashes detected semantic changes but had 0.00 benign invariance.

## Boundaries and scale limits

Generated realistic-template ledgers only; no private audited ledgers, no live accounting-system exports, no adversarial collision search, no multi-currency/subledger/OCR-import edge cases.

## Claim scope

In a deterministic Tier 1 benchmark of 200 generated balanced double-entry ledgers from held-out payroll and import-distribution scenarios, a posting-normalized semantic fingerprint detected all held-out semantic ledger mutations while ignoring all held-out benign metadata and description-noise changes.

## Why it stopped

Tier 1 generated-ledger evidence supports the mechanism but is not direct real-ledger publication evidence.

## Recommended next action

Run the same scoring contract on anonymized real ledger exports from at least two accounting systems before considering a bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-export ledger mutation replay for semantic notary fingerprints
- Success threshold: semantic_posting_sha256 >= 0.95 semantic detection and >= 0.95 benign invariance on real-export held-out cases, with raw/canonical baselines reported for comparison.
- Stop condition: Stop if real exports cannot be obtained without private/human evidence, or if semantic posting invariance falls below 0.90 on benign real export noise after only deterministic normalization.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-realistic-ledger-mutation-benchmark-for-semantic-66ffaff727`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

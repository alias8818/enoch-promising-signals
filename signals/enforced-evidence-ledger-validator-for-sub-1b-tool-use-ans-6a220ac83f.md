# Enforced Evidence Ledger Validator for Sub-1B Tool-Use Answers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `enforced-evidence-ledger-validator-for-sub-1b-tool-use-ans-6a220ac83f`
Run ID: `enforced-evidence-ledger-validator-for-sub-1b-tool-use-ans-6a220ac83f-20260516T095222794897+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/26a54cf52b91

## What looked useful

The validator reached 1.00 unsupported recall and 1.00 supported pass rate on the controlled benchmark, while citation-only recall was 0.10 and lexical-overlap recall was 0.40. This supports the mechanism that enforced ledger checks catch unsupported tool-use answer claims that citation presence alone misses.

## Boundaries and scale limits

Small controlled synthetic dataset; no live sub-1B model generations, no human adversarial labeling, no large public benchmark, and no decoding or training-loop integration.

## Claim scope

On 18 controlled tool-use answer cases with 29 labeled claims, a deterministic evidence-ledger validator detected unsupported claims and preserved supported claims better than citation-only and lexical-overlap baselines.

## Why it stopped

Tier 1 controlled direct test passed the local threshold, but the evidence remains too small and synthetic for publication readiness.

## Recommended next action

Run a held-out direct test on real sub-1B model outputs with independent claim labels before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out sub-1B generation test for evidence-ledger validation
- Success threshold: Unsupported-claim recall >= 0.85 and supported-claim pass rate >= 0.90 on independently labeled held-out sub-1B model outputs, with both metrics exceeding citation-only and lexical-overlap baselines.
- Stop condition: Stop if unsupported recall is below 0.70 or supported pass rate is below 0.80 on the first 100 independently labeled generated claims, because that would falsify practical validator viability at this tier.

## Evidence references

- Artifact root: `<local-path>/projects/enforced-evidence-ledger-validator-for-sub-1b-tool-use-ans-6a220ac83f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

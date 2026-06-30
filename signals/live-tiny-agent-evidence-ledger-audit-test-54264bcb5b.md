# Live Tiny-Agent Evidence Ledger Audit Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-tiny-agent-evidence-ledger-audit-test-54264bcb5b`
Run ID: `live-tiny-agent-evidence-ledger-audit-test-54264bcb5b-20260605T073504909861+0000`

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

- Parent run decision: Tiny Agent Evidence Ledger: enoch://control-plane/projects/tiny-agent-evidence-ledger-6535aa02b1ec/runs/tiny-agent-evidence-ledger-6535aa02b1ec-20260605T033943945711+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/28b2f05902ed

## What looked useful

The Tier 1 controlled test met its threshold with 200/200 supported claims accepted, 800/800 unsupported claims rejected, 0 false positives, and 0 false negatives. This supports the ledger-audit mechanism in a narrow setting but is not paper-ready.

## Boundaries and scale limits

Synthetic exact-match corpus only; no real LLM natural-language generation, noisy external evidence, semantic entailment, multi-hop provenance, live tool/API traces, or adversarial paraphrase was tested.

## Claim scope

In a deterministic controlled corpus of 1,000 tiny-agent claims, a claim-level evidence ledger with artifact hashes and exact subject/predicate/value checks accepted all supported claims and rejected all tested unsupported claims from missing citations, wrong citations, tampered hashes, and contradicted values.

## Why it stopped

Tier 1 controlled direct test completed and produced useful no-paper evidence; paper readiness requires broader live-agent and semantic-evidence validation.

## Recommended next action

Run a bounded deepen follow-up on live small-agent natural-language traces where claims are ledger-cited and independently judged for semantic support.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Small-Agent Natural-Language Evidence Ledger Audit
- Success threshold: Ledger-required mode has at least 80% lower accepted unsupported-claim rate than baseline and no more than 10% supported-claim false rejection on at least 30 tasks.
- Stop condition: Stop if ledger-required mode fails to reduce accepted unsupported claims by at least 50% or if supported-claim false rejection exceeds 20%, because the mechanism would not be robust enough for the next validation tier.

## Evidence references

- Artifact root: `<local-path>/projects/live-tiny-agent-evidence-ledger-audit-test-54264bcb5b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

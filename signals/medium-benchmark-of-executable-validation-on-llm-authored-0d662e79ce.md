# Medium benchmark of executable validation on LLM-authored public-data evidence ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-benchmark-of-executable-validation-on-llm-authored-0d662e79ce`
Run ID: `medium-benchmark-of-executable-validation-on-llm-authored-0d662e79ce-20260518T144253452393+0000`

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

- Internal Enoch project: Medium benchmark of executable validation on LLM-authored public-data evidence ledgers: internal_generated:medium-benchmark-of-executable-validation-on-llm-authored-0d662e79ce

## What looked useful

Across 1,890 ledgers from three fixed seeds, full executable validation reached 1.000 invalid-ledger recall and 1.000 specificity, versus 0.1667 recall for provenance/schema, 0.5000 for evidence-only, and 0.6667 for query-execute-only. The key mechanism was catching wrong-filter and wrong-group ledgers that were internally consistent with the author query but inconsistent with the claim spec.

## Boundaries and scale limits

The ledgers were synthetically mutated rather than sampled from live LLM outputs; the full validator assumes trusted machine-readable claim specs; only three public tabular datasets and scalar aggregate claims were tested.

## Claim scope

In a controlled medium benchmark of structured public-data evidence ledgers with deterministic LLM-like injected errors, full executable validation detected invalid ledgers substantially better than provenance-only, evidence-only, and query-execute-only baselines.

## Why it stopped

Medium controlled evidence supports the mechanism, but actual LLM-authored ledger evidence is missing and the validator depends on machine-readable claim specs, so this is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up with organic LLM-authored public-data ledgers from multiple models before making any publication claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Organic LLM-authored public-data evidence ledger validation benchmark
- Success threshold: Full executable validation improves invalid-ledger recall by at least 20 percentage points over the best baseline while keeping valid-ledger false positive rate at or below 5%.
- Stop condition: Stop if full executable validation improves recall by less than 10 percentage points over the best baseline or if organic ledgers cannot be labeled reliably enough to separate claim/spec ambiguity from data errors.

## Evidence references

- Artifact root: `<local-path>/projects/medium-benchmark-of-executable-validation-on-llm-authored-0d662e79ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

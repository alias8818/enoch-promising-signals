# Organic LLM-authored public-data evidence ledger validation benchmark

Status: `useful_signal`
Project ID: `organic-llm-authored-public-data-evidence-ledger-validatio-bc531a9fd7`
Run ID: `organic-llm-authored-public-data-evidence-ledger-validatio-bc531a9fd7-20260518T145304824363+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Organic LLM-authored public-data evidence ledger validation benchmark: internal_generated:organic-llm-authored-public-data-evidence-ledger-validatio-bc531a9fd7

## What looked useful

A reproducible benchmark harness shows that digest verification and citation binding are necessary controls for public-data evidence ledgers: removing digest checks creates 7,480 false positives on tampered rows, and removing citation binding creates 14,960 false positives on citation-mismatch plus tampered rows.

## Boundaries and scale limits

37,400 templated ledger rows across five fixed seeds, one structured public API, six fields, generated corruptions, and validators that consume structured claim slots. This does not validate arbitrary organic LLM prose, broad public-data sources, open web retrieval, or human-labeled evidence ledgers.

## Claim scope

In a deterministic public-data evidence-ledger benchmark over REST Countries records, schema-aware validation with evidence-digest checking and citation-to-entity binding cleanly detects generated unsupported ledger rows and outperforms citation-only, text-containment, no-digest, and no-citation-binding controls.

## Why it stopped

The run supports the validation mechanism on a generated structured benchmark, but the original title-level claim needs organic LLM-authored rows and broader public-data sources before paper readiness.

## Recommended next action

Stop this run as no-paper useful evidence; the concrete next bounded deepen is to replace templated claims with real LLM-authored ledgers over several public APIs and require the same validator/ablation pattern to hold on audited labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Organic LLM-authored multi-source evidence-ledger validation
- Success threshold: Schema-bound validation reaches at least 0.95 overall accuracy and at least 0.90 specificity on each corruption class, while both no-digest and no-citation-binding ablations show statistically meaningful false-positive degradation.
- Stop condition: Stop negative if organic LLM-authored rows collapse schema-bound validation below 0.90 accuracy or if text-containment matches schema-bound performance without digest or citation-binding controls across audited slices.

## Evidence references

- Artifact root: `<local-path>/projects/organic-llm-authored-public-data-evidence-ledger-validatio-bc531a9fd7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Evidence-Ledger for Small Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-local-agents-3a409640f5d2`
Run ID: `evidence-ledger-for-small-local-agents-3a409640f5d2-20260608T221915772736+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8f715af5ee7e

## What looked useful

The ledger mechanism worked as a provenance gate: mean unsupported emitted claim rate fell from 0.1811851851851852 to 0.0, emitted-claim support rose from 0.8188148148148149 to 1.0, mean accuracy changed from 0.6742962962962963 to 0.6712814814814814, and mean completeness fell to 0.8518518518518517.

## Boundaries and scale limits

Synthetic controlled tasks only; no real local LLM, no natural documents, no human evidence labels, no multi-step production agent traces, and no broad external validation.

## Claim scope

In a deterministic synthetic small-agent harness with structured field/value claims, a hash-linked evidence ledger plus support-checking compiler eliminated unsupported emitted claims across 45,000 task pairs while preserving near-baseline accuracy at lower completeness.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only; it supports the mechanism but not a publication-grade claim about real small local agents.

## Recommended next action

Run a direct local-LLM follow-up on natural short-document QA with the same ledger protocol and compare unsupported-claim rate, task accuracy, completeness, and latency against a citation-only baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Local-LLM Evidence-Ledger QA Evaluation
- Success threshold: Ledger condition reduces unsupported emitted claims by at least 50% relative to citation-only baseline while keeping relative task-accuracy loss below 20% and adding no more than 2x finalization latency on CPU.
- Stop condition: Stop if unsupported-claim reduction is below 25%, if task-accuracy loss exceeds 30%, or if local CPU latency makes the ledger path more than 5x slower than citation-only finalization on the bounded dataset.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-local-agents-3a409640f5d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

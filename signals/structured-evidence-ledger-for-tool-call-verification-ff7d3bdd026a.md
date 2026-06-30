# Structured Evidence Ledger for Tool-Call Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structured-evidence-ledger-for-tool-call-verification-ff7d3bdd026a`
Run ID: `structured-evidence-ledger-for-tool-call-verification-ff7d3bdd026a-20260525T135741103565+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aea5c8197654

## What looked useful

Structured call IDs, status, tool names, and parsed result fields remove parser brittleness and missing status/provenance checks in a small reproducible verification benchmark.

## Boundaries and scale limits

Synthetic generated traces only; no real LLM transcripts, production agent logs, adversarial ledger writer, cryptographic tamper model, or LLM-assisted transcript verifier baseline. Local CPU run only: 25,000 examples per condition across clean and noisy transcript variants.

## Claim scope

In a deterministic synthetic benchmark of tool-call traces and claim faults, a canonical structured evidence ledger verified claims perfectly while transcript-only regex baselines lost recall under heterogeneous formatting or accepted failed-call evidence when status was not bound to the result.

## Why it stopped

The result is a bounded synthetic mechanism demonstration, not full validation or publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; next direct evidence should evaluate the ledger on real agent traces with gold claim labels and stronger transcript baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Evaluation of Structured Tool-Call Evidence Ledgers
- Success threshold: Ledger verifier improves invalid-claim recall by at least 10 percentage points over the strongest transcript baseline while keeping valid-claim recall at or above 98% and adding less than 5% runtime overhead on the evaluated harness.
- Stop condition: Stop if the strongest transcript baseline matches ledger invalid-claim recall within 2 percentage points, if valid-claim recall drops below 98%, or if instrumentation overhead exceeds 5% without a clear optimization path.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-for-tool-call-verification-ff7d3bdd026a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

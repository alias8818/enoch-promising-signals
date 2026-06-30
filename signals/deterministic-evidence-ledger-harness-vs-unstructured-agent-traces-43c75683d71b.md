# Deterministic Evidence-Ledger Harness vs Unstructured Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-evidence-ledger-harness-vs-unstructured-agent-traces-43c75683d71b`
Run ID: `deterministic-evidence-ledger-harness-vs-unstructured-agent-traces-43c75683d71b-20260619T105742114109+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5b7f316d89e1

## What looked useful

Ledger verifier: TP 48, TN 72, FP 0, FN 0. Unstructured trace proxy: TP 48, TN 24, FP 48, FN 0. The signal is useful for future harness design but not paper-ready.

## Boundaries and scale limits

120 synthetic cases only; no real LLM agents, no production traces, no multi-hop evidence chains, and no strong semantic unstructured-trace auditor baseline.

## Claim scope

Synthetic deterministic single-observation trap cases show that explicit evidence-reference/value checks reject planted missing-reference and mismatch failures that a final-verdict unstructured trace proxy falsely accepts.

## Why it stopped

Local evidence is a synthetic proxy demonstration, not direct/full validation on real agent traces.

## Recommended next action

Stop this run as no-paper useful signal; if continued, run a bounded deepen test on real or LLM-generated tool traces with a stronger semantic trace-auditor baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger harness on real tool-use traces with semantic trace-auditor control
- Success threshold: At least 100 paired trace tasks with ledger false accept rate <= 0.05 and at least 50% relative false-accept reduction versus the semantic unstructured auditor, with false reject rate <= 0.10.
- Stop condition: Stop if the ledger false accept rate exceeds 0.10, if false rejects exceed 0.20, or if the paired trace corpus cannot be generated reproducibly inside the available local budget.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-evidence-ledger-harness-vs-unstructured-agent-traces-43c75683d71b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

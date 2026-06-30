# Multi-dataset generative QA replication for evidence-ledger gates

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `33`
Project ID: `multi-dataset-generative-qa-replication-for-evidence-ledge-174674211a`
Run ID: `multi-dataset-generative-qa-replication-for-evidence-ledge-174674211a-20260604T031223764480+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `33`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-context benchmark ablation for evidence-ledger gates on small factual QA agents: enoch://control-plane/projects/real-context-benchmark-ablation-for-evidence-ledger-gates-6c04e7de89/runs/real-context-benchmark-ablation-for-evidence-ledger-gates-6c04e7de89-20260604T013413754858+0000
- Parent run decision: Evidence ledger gate on small-model factual QA agents: enoch://control-plane/projects/evidence-ledger-gate-on-small-model-factual-qa-agents-06c47df5ff/runs/evidence-ledger-gate-on-small-model-factual-qa-agents-06c47df5ff-20260603T232431027075+0000

## What looked useful

The gate improved accepted precision only on SQuAD but with 10% coverage; it failed on Qasper with 2% coverage and zero exact accepted answers, and arithmetic consistency gating on GSM8K did not materially beat the weak baseline. Ungated ledger prompting reduced overall exact match.

## Boundaries and scale limits

Bounded local validation only: one 0.5B model, greedy decoding, 400 QA items in the extended run, Qasper contexts truncated to 2500 characters, and ToolQA/GSM8K limited to the 100 available local easy questions.

## Claim scope

For Qwen/Qwen2.5-0.5B-Instruct on SQuAD validation, Qasper/Scrolls validation, and local ToolQA/GSM8K easy questions, simple ledger-format prompting plus deterministic quote/equation gates did not meet the registered multi-dataset precision and coverage threshold.

## Why it stopped

Direct bounded multi-dataset validation falsified the registered threshold: macro gated precision gain was only +0.0204 at 0.1433 coverage, below the required +0.10 gain and 0.25 coverage.

## Recommended next action

Stop this line as no-paper evidence unless a future project replaces brittle lexical/equation gates with stronger evidence extraction and verifies the same precision/coverage threshold before scaling.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/multi-dataset-generative-qa-replication-for-evidence-ledge-174674211a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

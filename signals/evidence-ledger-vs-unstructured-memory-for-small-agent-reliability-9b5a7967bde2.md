# Evidence Ledger vs Unstructured Memory for Small Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-vs-unstructured-memory-for-small-agent-reliability-9b5a7967bde2`
Run ID: `evidence-ledger-vs-unstructured-memory-for-small-agent-reliability-9b5a7967bde2-20260525T174110999471+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/12cd6f3c96f9

## What looked useful

Ledger accuracy stayed at 0.9313 across token budgets 120-720 while unstructured memory rose from 0.1756 to 0.8288 as capacity increased; paired accuracy deltas remained positive with 95% CIs excluding zero. A high-budget control narrowed value accuracy delta to 0.0301 but preserved better evidence citation for the ledger, 0.9115 vs 0.8178.

## Boundaries and scale limits

No real LLM agents were evaluated. The run used 100 medium episodes per seed across five seeds and synthetic retrieval/noise models; it does not validate prompt-level behavior, real context-window effects, tool-use failures, or deployment-scale agent reliability.

## Claim scope

Synthetic proxy only: in a timestamped conflicting-evidence memory task with noisy parsing and bounded text buffers, a structured evidence ledger improves current-value accuracy and evidence-citation reliability versus unstructured memory, especially under tight memory budgets.

## Why it stopped

Proxy-only synthetic mechanism evidence is insufficient for a paper-ready claim about small agent reliability.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test the same task family with real small LLM agents using matched ledger and unstructured-memory prompts/tools.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-LLM Evidence Ledger vs Unstructured Memory Reliability Probe
- Success threshold: Ledger improves paired answer accuracy by at least 5 percentage points at constrained context budgets and improves evidence-citation accuracy by at least 5 percentage points in the high-budget control, with confidence intervals excluding zero.
- Stop condition: Stop as unsupported if real LLM-agent paired deltas are below 2 percentage points or confidence intervals include zero across constrained and high-budget settings.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-vs-unstructured-memory-for-small-agent-reliability-9b5a7967bde2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

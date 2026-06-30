# Direct Token-Budgeted LLM Agent Test of a Bounded Evidence Ledger

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `direct-token-budgeted-llm-agent-test-of-a-bounded-evidence-fc2931fa8e`
Run ID: `direct-token-budgeted-llm-agent-test-of-a-bounded-evidence-fc2931fa8e-20260529T053420108188+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Bounded Sliding-Window Evidence Ledger for Context-Constrained Agents: enoch://control-plane/projects/bounded-sliding-window-evidence-ledger-for-context-constrained-agents-42c74885e9bf/runs/bounded-sliding-window-evidence-ledger-for-context-constrained-agents-42c74885e9bf-20260529T030103328370+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/87997efde574

## What looked useful

The ledger agent missed the predeclared threshold: 20.83% accuracy versus 25.00% for the plain truncated baseline, -4.17 percentage-point delta versus the required +20 points, and 6.57x latency versus the allowed 4x. It did avoid fabricated evidence ids, but diagnostics showed 0/24 strict relevance-retention success and mostly REFUTED-biased final decisions.

## Boundaries and scale limits

Synthetic controlled cases only; one 0.5B instruction model; one prompt family; no natural retrieval traces, larger local models, API frontier models, or publication-grade robustness ablations.

## Claim scope

A small direct local LLM-agent test using Qwen/Qwen2.5-0.5B-Instruct on 24 controlled evidence-classification cases did not show that a bounded evidence ledger improves token-budgeted support/refute/mixed/insufficient decisions over a truncated-context baseline.

## Why it stopped

The direct small test falsified the predeclared success threshold for the tested bounded evidence-ledger agent, rather than providing full validation of the broader idea.

## Recommended next action

Stop this run as a no-paper useful negative signal; the next bounded deepen test should repeat the same harness with a stronger local model and stricter structured ledger output before any paper consideration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stronger Structured Ledger Agent on Controlled Token-Budgeted Evidence Cases
- Success threshold: Ledger accuracy at least 20 percentage points above plain truncated-context baseline, citation validity at least 90%, no more than 1 fabricated id per 48 cases, strict relevance retention at least 75%, and mean latency no more than 4x baseline.
- Stop condition: Stop as negative if the stronger structured ledger still fails to beat baseline accuracy by 10 percentage points or if strict relevance retention remains below 50%.

## Evidence references

- Artifact root: `<local-path>/projects/direct-token-budgeted-llm-agent-test-of-a-bounded-evidence-fc2931fa8e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

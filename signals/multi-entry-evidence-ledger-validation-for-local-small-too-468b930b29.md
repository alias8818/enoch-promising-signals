# Multi-entry evidence-ledger validation for local small tool agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-entry-evidence-ledger-validation-for-local-small-too-468b930b29`
Run ID: `multi-entry-evidence-ledger-validation-for-local-small-too-468b930b29-20260609T070307330643+0000`

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

- Parent run decision: Evidence-ledger wrapper for local small LLM tool agents: enoch://control-plane/projects/evidence-ledger-wrapper-for-local-small-llm-tool-agents-3113ecb421/runs/evidence-ledger-wrapper-for-local-small-llm-tool-agents-3113ecb421-20260609T033216769015+0000
- Parent run decision: Evidence Ledger for Tool-Calling Safety in Small Agents: enoch://control-plane/projects/evidence-ledger-for-tool-calling-safety-in-small-agents-99d51ddfc303/runs/evidence-ledger-for-tool-calling-safety-in-small-agents-99d51ddfc303-20260609T012635202719+0000

## What looked useful

Across 1,500 tasks per arm with fixed seeds, multi-entry validation reached 0.9593 accuracy versus 0.3193 for the no-ledger baseline, reduced unsupported claims from 1.0000 to 0.0000, and used 4.0x baseline tool calls. The repeat run had zero non-timing mismatches across 6,000 records.

## Boundaries and scale limits

Results use generated local evidence tasks and deterministic tool-agent policies, not real LLM agents, public tool-use benchmarks, or field deployments. The evidence supports the mechanism but does not establish publication-grade external validity.

## Claim scope

In a seeded synthetic local evidence-lookup benchmark for small tool-agent policies, multi-entry evidence-ledger validation improves exact-answer accuracy and eliminates unsupported claims versus a no-ledger baseline and single-entry or unvalidated ledger ablations.

## Why it stopped

Tier 2 controlled validation succeeded as a useful mechanism signal, but the result is synthetic/local and not direct publication-grade evidence with real LLM tool agents.

## Recommended next action

Run the same ledger protocol with actual local 1B-3B LLM tool agents on a public evidence-grounded tool-use task suite before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-LLM tool-agent validation of multi-entry evidence ledgers
- Success threshold: Multi-entry validation improves exact-answer accuracy by at least 0.10 over the best baseline and reduces unsupported claims by at least 40 percent with no more than 5x baseline tool calls.
- Stop condition: Stop if multi-entry validation fails to beat the best baseline by at least 0.05 accuracy or does not reduce unsupported claims by at least 20 percent on the first completed public-task/model pair.

## Evidence references

- Artifact root: `<local-path>/projects/multi-entry-evidence-ledger-validation-for-local-small-too-468b930b29`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

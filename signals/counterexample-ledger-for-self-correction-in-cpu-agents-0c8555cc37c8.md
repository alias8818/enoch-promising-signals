# Counterexample Ledger for Self-Correction in CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-ledger-for-self-correction-in-cpu-agents-0c8555cc37c8`
Run ID: `counterexample-ledger-for-self-correction-in-cpu-agents-0c8555cc37c8-20260528T193631124988+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57b4ce2850fe

## What looked useful

Structured family-scoped counterexample records reached 0.990 tight-budget success versus 0.984 for unstructured notes, 0.779 for shuffled-ledger control, and 0.000 for no-memory under a 3-attempt budget; with a 4-attempt budget all policies solved but the ledger reduced mean attempts to 1.03 versus 1.27 for unstructured notes and 4.00 for no-memory, with zero repeated failure rate.

## Boundaries and scale limits

Evidence is synthetic and mechanism-level only: five task families, hand-written candidate strategies, deterministic hidden tests, and no real LLM/code-agent trace extraction or repository-scale tasks.

## Claim scope

In a synthetic CPU-only iterative task harness with recurring deterministic task families, a correctly keyed structured counterexample ledger reduced repeated failures and attempts compared with retry-only, unstructured notes, shuffled-ledger, and noisy-ledger controls.

## Why it stopped

No-paper closure: the local result is a useful synthetic mechanism signal, but it is not direct evidence for real LLM or coding-agent self-correction.

## Recommended next action

Run a bounded real CPU coding-agent harness that extracts ledger entries from actual failed tests/traces and compares against transcript memory and retrieved-note baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Counterexample Ledger in a Real CPU Coding-Agent Harness
- Success threshold: Across at least 30 seeds or task orderings, the structured ledger should reduce repeated error modes by at least 30% and reduce attempts/tool calls by at least 15% versus the strongest non-structured memory baseline without lowering solve rate by more than 2 percentage points.
- Stop condition: Stop if real-trace extraction cannot produce reliable family/error signatures, or if the structured ledger fails to beat unstructured retrieved notes on repeated-error rate and attempts in a CPU-bounded pilot.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-ledger-for-self-correction-in-cpu-agents-0c8555cc37c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

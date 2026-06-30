# Evidence Ledger for Small Tool-Calling Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-tool-calling-agents-ffe2a6c85e6f`
Run ID: `evidence-ledger-for-small-tool-calling-agents-ffe2a6c85e6f-20260525T205411106069+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c88017cb2969

## What looked useful

Across 500 main tasks, ledger_context_900 achieved 1.000 exact accuracy and 0.000 unsupported rate while raw_context_900 achieved 0.000 exact accuracy and 1.000 unsupported rate; raw_context_20000 also achieved 1.000, indicating failures came from evidence retention rather than unsolvable tasks. A 12-setting sweep showed the ledger retained all required keys in every setting while raw small-context accuracy degraded as noise exceeded budget.

## Boundaries and scale limits

Synthetic rule-based tasks only; no real LLM tool-call planning, no naturalistic tool outputs, no human evaluation, and no large-scale deployment traces. Character budgets proxy model context limits.

## Claim scope

In a deterministic synthetic tool-calling harness where required verified facts are present in noisy tool outputs, a structured evidence ledger preserves evidence under small rolling-context budgets and eliminates unsupported answers compared with a raw transcript of the same final size.

## Why it stopped

Closed as no-paper useful signal because the positive result is synthetic/proxy evidence for the retention mechanism, not direct validation on real small tool-calling agents.

## Recommended next action

Run a bounded deepen follow-up using a real small local LLM or API model on naturalistic tool traces, with the same planner and token budget for raw-transcript and evidence-ledger conditions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger on Real Small Tool-Calling Traces
- Success threshold: Ledger condition improves exact accuracy by at least 10 percentage points and reduces unsupported claims by at least 30% relative to raw transcript at the same token budget, with no more than 20% extra tool calls.
- Stop condition: Stop if the ledger gain is below 5 percentage points in exact accuracy or unsupported-claim reduction is below 10% on the first 100 naturalistic tasks.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-tool-calling-agents-ffe2a6c85e6f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

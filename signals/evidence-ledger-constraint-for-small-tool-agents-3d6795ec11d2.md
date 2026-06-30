# Evidence-Ledger Constraint for Small Tool Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-constraint-for-small-tool-agents-3d6795ec11d2`
Run ID: `evidence-ledger-constraint-for-small-tool-agents-3d6795ec11d2-20260604T102629225546+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7c5b6c075e7f

## What looked useful

Ledger constraints act as a precision and provenance control: they block unsupported guesses after incomplete tool use, but they do not recover missing evidence and can expose a substantial coverage/utility tradeoff.

## Boundaries and scale limits

Simulator-only evidence with 3,000 episodes per setting across four synthetic settings; no real LLMs, no prompt-compliance measurement, no real tool APIs, and no human utility evaluation.

## Claim scope

In a synthetic paired simulation of budget-limited tool QA agents, a final-answer evidence-ledger constraint eliminated unsupported claims and reduced wrong emitted claims versus an unconstrained guessing baseline, while reducing coverage and complete-answer accuracy under subtask tool budgets.

## Why it stopped

No-paper useful signal: the local simulator supports the mechanism, but real LLM/tool-agent evidence is required before any paper claim.

## Recommended next action

Run a bounded direct follow-up with small LLM tool agents on deterministic QA tasks, comparing unconstrained final answers against ledger-enforced answers under equal tool budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger constraint on real small LLM tool agents
- Success threshold: At least 50% relative reduction in unsupported claim rate with at least 80% retention of baseline correct supported claims across two small-agent configurations.
- Stop condition: Stop if ledger prompting fails to reduce unsupported claims by 25% in the first 100 paired tasks or if citation compliance cannot be reliably parsed/audited.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constraint-for-small-tool-agents-3d6795ec11d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

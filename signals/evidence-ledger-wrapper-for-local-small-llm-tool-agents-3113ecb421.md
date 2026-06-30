# Evidence-ledger wrapper for local small LLM tool agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-wrapper-for-local-small-llm-tool-agents-3113ecb421`
Run ID: `evidence-ledger-wrapper-for-local-small-llm-tool-agents-3113ecb421-20260609T033216769015+0000`

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

- Parent run decision: Evidence Ledger for Tool-Calling Safety in Small Agents: enoch://control-plane/projects/evidence-ledger-for-tool-calling-safety-in-small-agents-99d51ddfc303/runs/evidence-ledger-for-tool-calling-safety-in-small-agents-99d51ddfc303-20260609T012635202719+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6efc1435e55d

## What looked useful

The wrapper produced a bounded mechanism signal: ledger-constrained finalization with explicit evidence-id resolution reduced distractor uptake and improved accuracy in a small local direct test, but failures remained and the setup is not publication-grade.

## Boundaries and scale limits

Single small model, synthetic simple fact/calculation tasks, precomputed tool observations, mostly one relevant ledger entry per task, one prompt family, no live planner/tool-selection loop, no multi-model or statistical robustness study.

## Claim scope

In a 30-task controlled local test using google/flan-t5-small as a tool-agent finalizer, a narrow evidence-ledger prompt plus evidence-id resolution improved exact-answer accuracy from 18/30 to 22/30 and reduced unverified-memory distractor inclusion from 8/30 to 3/30 versus the same model with raw tool observations.

## Why it stopped

Tier 1 controlled direct test completed with useful mechanism support, but evidence is limited to a small synthetic local setting and is not paper-ready.

## Recommended next action

Run a bounded deepen follow-up with at least 60 tasks containing multiple competing ledger entries, a second local small model, and live tool-agent traces; require accuracy to be non-decreasing and distractor inclusion to fall by at least 30% relative.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-entry evidence-ledger validation for local small tool agents
- Success threshold: Ledger wrapper has non-decreasing exact-answer accuracy and at least 30% relative reduction in distractor or unsupported-claim rate on both models.
- Stop condition: Stop if either model shows lower exact-answer accuracy with the ledger wrapper or less than 10% relative reduction in distractor/unsupported-claim rate after 60 tasks.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-wrapper-for-local-small-llm-tool-agents-3113ecb421`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
